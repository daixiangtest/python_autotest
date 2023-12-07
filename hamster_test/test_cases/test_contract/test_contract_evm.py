import allure
import time
import pytest
from selenium.webdriver.common.by import By
from hamster_test.comms.constants import DATA_EVM, INFO_FILE, ERROR_FILE
from hamster_test.comms.log_utils import get_logger
from hamster_test.comms.yaml_utils import get_yaml_data, get_picture, get_ini_data
from hamster_test.web.selenium.page.create_project import CreateProject
from hamster_test.web.selenium.elenium import elenium as em

logger = get_logger()


@allure.epic('hamster系统')
@allure.feature("EVM项目合约")
@allure.parent_suite('EVM项目合约')
class TestEvm:
    cases = get_yaml_data(DATA_EVM)  # 读取yaml文件中的测试数据
    ids = ['测试{}'.format(case['case_title'][0]) for case in cases]

    @allure.suite('EVM生态创建合约')
    @allure.description("EVM生态创建合约")
    @pytest.mark.parametrize('case', cases, ids=ids)
    def test_create(self, case, connect_db1):
        allure.dynamic.title(case['case_title'][0])
        allure.attach(body=get_ini_data('url', 'get_url'), name='请求路径')
        cp = CreateProject(connect_db1)
        cp.geturl(get_ini_data('url', 'get_url'))  # 输入项目地址
        # 判断项目是否需要登录
        cp.login_pass()
        # 点击跳转至切换页面
        if cp.iselement(10, *em.create_project):
            cp.click(5, *em.create_project)
        # 打开evm的项目页面
        cp.open_evm()
        # 点击项目名称
        time.sleep(3)
        cp.find_elements(10, *em.contract_nfts)[case['case_id'] - 1].click()
        time.sleep(5)
        # 点击创建项目
        cp.create_by_template(case['case_data'])
        cp.click(60, *em.back_to_project)
        url = connect_db1.current_url
        text = cp.find_elements(10, *em.project_contract_names)[0].text

        try:
            assert get_ini_data('url', 'new_url') in url  # 断言URL地址与预期一致
            assert case["case_data"] in text  # 断言文本信息是都存在
            # 断言是否有创建项目的按钮

            logger.info("测试编号:{},测试标题:{},执行成功！".format(case['case_id'], case['case_title'][0]))
            allure.attach.file(INFO_FILE, name='longing info', attachment_type=allure.attachment_type.TEXT)
        except AssertionError as e:
            get_picture(connect_db1, case['case_title'][0])  # 失败截图
            logger.error(
                "测试编号:{},测试标题:{},执行失败!实际结果:{}".format(case['case_id'], case['case_title'][0], e))
            allure.attach.file(ERROR_FILE, name='longing error', attachment_type=allure.attachment_type.TEXT)
            logger.exception(e)
            raise e

    ids1 = ['测试{}'.format(case['case_title'][1]) for case in cases]

    @pytest.mark.skip("暂不测试")
    @allure.suite('EVM生态合约检查')
    @allure.description("EVM生态合约检查")
    @pytest.mark.parametrize('case', cases, ids=ids1)
    def test_check(self, case, connect_db1):
        allure.dynamic.title(case['case_title'][1])
        allure.attach(body=get_ini_data('url', 'get_url'), name='请求路径')
        cp = CreateProject(connect_db1)
        cp.geturl(get_ini_data('url', 'get_url'))  # 输入项目地址
        cp.login_pass()
        lens = len(get_yaml_data(DATA_EVM))
        # 点击所选的项目名称进入项目详情页
        cp.contract_projects(case['case_data'], lens)
        # 点击check按钮
        cp.click(10, *em.projects_check)
        # 选择需要的检查工具
        cp.run_metatrust_evm('sa1')
        time.sleep(5)
        connect_db1.refresh()
        # 判断代码是否检查成功
        cp.wait_recent(300, *em.projects_recent_check)
        # 点击检查的详情页面
        cp.clicks(10, *em.projects_view_check)
        time.sleep(3)
        ast = cp.run_metatrust_evm_reports('sa1')
        # 获取页面的文本信息
        new_url = connect_db1.current_url
        tx = cp.text(10, *em.check_result)
        print(tx)
        try:
            assert False not in ast
            assert get_ini_data('url', 'new_url') in new_url
            assert case['text']['tx1'] in tx
            logger.info("测试编号:{},测试标题:{},执行成功！".format(case['case_id'], case['case_title'][1]))
        except AssertionError as e:
            get_picture(connect_db1, case['case_title'][1])  # 失败截图
            logger.error(
                "测试编号:{},测试标题:{},执行失败!实际结果:{}".format(case['case_id'], case['case_title'][1], e))
            logger.exception(e)
            raise e

    ids2 = ['测试{}'.format(case['case_title'][2]) for case in cases]

    @allure.suite('EVM生态合约编译')
    @allure.description("EVM生态合约编译")
    @pytest.mark.parametrize('case', cases, ids=ids2)
    def test_build(self, case, connect_db1):
        allure.dynamic.title(case['case_title'][2])
        allure.attach(body=get_ini_data('url', 'get_url'), name='请求路径')
        cp = CreateProject(connect_db1)
        cp.geturl(get_ini_data('url', 'get_url'))
        cp.login_pass()
        # 点击编译按钮
        lens = len(get_yaml_data(DATA_EVM))
        # 点击对应的项目的名称进入项目详情页面
        cp.contract_projects(case['case_data'], lens)
        # 点击build按钮
        cp.click(10, *em.projects_build)
        # 等待build运行成功
        cp.wait_recent(300, *em.projects_recent_build)
        # 点击build详情页面
        cp.click(10, *em.projects_view_build)
        time.sleep(3)
        # 获取编译页面的文本关键字
        tx1 = cp.text(10, *em.build_result)
        tx2 = cp.text(10, *em.build_deploy)
        cp.click(10, *em.build_more)
        tx3 = cp.text(10, *em.build_more_abi)
        new_url = connect_db1.current_url

        try:
            assert case['text']['tx1'] in tx1
            assert case['text']['tx2'] in tx2
            assert case['text']['tx3'] in tx3
            assert get_ini_data('url', 'new_url') in new_url
            logger.info("测试编号:{},测试标题:{},执行成功！".format(case['case_id'], case['case_title'][2]))
        except AssertionError as e:
            get_picture(connect_db1, case['case_title'][2])  # 失败截图
            logger.error(
                "测试编号:{},测试标题:{},执行失败!实际结果:{}".format(case['case_id'], case['case_title'][2], e))
            logger.exception(e)
            raise e

    ids3 = ['测试{}'.format(case['case_title'][3]) for case in cases]

    @allure.suite('EVM生态合约部署')
    @allure.description("EVM生态合约部署")
    @pytest.mark.parametrize('case', cases, ids=ids3)
    def test_deploy(self, case, connect_db):
        allure.dynamic.title(case['case_title'][3])
        allure.attach(body=get_ini_data('url', 'get_url'), name='请求路径')
        cp = CreateProject(connect_db)
        lens = len(get_yaml_data(DATA_EVM))
        # 登录项目地址
        cp.geturl(get_ini_data('url', 'get_url'))
        cp.longin(get_ini_data('github', 'user'), get_ini_data('github', 'passwd'))
        # 链接小狐狸钱包
        cp.metamask_login(get_ini_data('github', 'passwd'))
        # 链接后刷新网络
        time.sleep(3)
        connect_db.refresh()
        # 点击部署按钮
        cp.contract_deploy(case['case_data'], lens)
        if case['case_data'] == 'Contract_EVM_NFT_z':
            cp.deploy_evm_nft('aaa', 'bbb', '111', 1, 4)
        else:
            cp.deploy_evm(1, 4)
        cp.deploy_evm_confirm('Dx3826729')
        cp.driver.implicitly_wait(20)
        time.sleep(3)
        tx = cp.text(20, *em.ops_projects)

        try:
            assert case['text']['tx4'] in tx
            assert case['text']['tx5'] in tx
            logger.info("测试编号:{},测试标题:{},执行成功！".format(case['case_id'], case['case_title'][3]))
        except AssertionError as ea:
            get_picture(connect_db, case['case_title'][3])  # 失败截图
            logger.error(
                "测试编号:{},测试标题:{},执行失败!实际结果:{}".format(case['case_id'], case['case_title'][3], ea))
            logger.exception(ea)
            raise ea

    ids4 = ['测试{}'.format(case['case_title'][4]) for case in cases]

    @allure.suite('EVM生态合约删除')
    @allure.description("EVM生态合约删除")
    @pytest.mark.parametrize('case', cases, ids=ids4)
    def test_delete(self, case, connect_db):
        allure.dynamic.title(case['case_title'][4])
        allure.attach(body=get_ini_data('url', 'get_url'), name='请求路径')
        cp = CreateProject(connect_db)
        # 登录网址
        cp.geturl(get_ini_data('url', 'get_url'))
        cp.longin(get_ini_data('github', 'user'), get_ini_data('github', 'passwd'))
        # 从.ini文件中获取github的库名和密码
        sth = get_ini_data('github', 'storehouse')
        psw = get_ini_data('github', 'passwd')
        lens = len(get_yaml_data(DATA_EVM))
        # 点击github链接，跳转至github页面
        cp.click(15, By.CSS_SELECTOR,
                 'a[href="https://github.com/{}.git"]'.format('{}/{}'.format(sth, case['case_data'])))
        cp.window(-1)
        # 删除github中的项目
        cp.delete_project_github(sth, case['case_data'], '{}/{}'.format(sth, case['case_data']))
        # 输入github密码确认删除
        cp.delete_project_passwd(psw)
        # 判断被删除的项目在GitHub中是否存在
        ast = cp.iselement(10, By.CSS_SELECTOR, 'a[href="/{}"]'.format('{}/{}'.format(sth, case['case_data'])))
        # 切换至hamster主页面
        cp.window(0)
        cp.driver.refresh()
        # 点击进入hamster的项目管理页
        cp.contract_projects(case['case_data'], lens)
        # 删除hamster的项目
        cp.delete_project_hamster()
        # 点击项目名称进入项目详情
        time.sleep(6)
        connect_db.implicitly_wait(15)
        connect_db.refresh()
        # 判断被删除的元素在该项目中是否还存在
        ast1 = cp.iselement(10, By.CSS_SELECTOR,
                            'a[href="https://github.com/{}.git"]'.format('{}/{}'.format(sth, case['case_data'])))

        try:
            assert ast is False
            assert ast1 is False
            logger.info("测试编号:{},测试标题:{},执行成功！".format(case['case_id'], case['case_title'][4]))
        except AssertionError as e:
            get_picture(connect_db, case['case_title'][4])  # 失败截图
            logger.error(
                "测试编号:{},测试标题:{},执行失败!实际结果:{}".format(case['case_id'], case['case_title'][4], e))
            logger.exception(e)
            raise e


if __name__ == '__main__':
    pytest.main(['-vs', __file__])
