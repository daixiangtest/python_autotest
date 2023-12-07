import allure
import time
import pytest
from selenium.webdriver.common.by import By
from hamster_test.comms.constants import DATA_SUI
from hamster_test.comms.log_utils import get_logger
from hamster_test.comms.yaml_utils import get_yaml_data, get_picture, get_ini_data
from hamster_test.web.selenium.page.create_project import CreateProject
from hamster_test.web.selenium.elenium import elenium as em

logger = get_logger()


@allure.epic('hamster系统')
@allure.feature("sui项目合约")
@allure.parent_suite('sui项目合约')
class TestSui:
    cases = get_yaml_data(DATA_SUI)  # 读取yaml文件中的测试数据
    ids = ['测试{}'.format(case['case_title'][0]) for case in cases]

    @allure.suite('sui生态创建合约')
    @allure.description("sui生态创建合约")
    @pytest.mark.parametrize('case', cases, ids=ids)
    def test_create(self, case, connect_db1):
        allure.dynamic.title(case['case_title'][0])
        allure.attach(body=get_ini_data('url', 'get_url'), name='请求路径')
        cp = CreateProject(connect_db1)
        # 登录项目网址
        cp.geturl(get_ini_data('url', 'get_url'))
        # 登录项目
        cp.login_pass()
        # cp.longin(get_ini_data('github', 'user'), get_ini_data('github', 'passwd'))
        # 点击创建项目
        if cp.iselement(5, *em.project_frontend):
            cp.click(5, *em.create_project)
        # 打开ipfs合约的展示页面
        cp.open_sui()
        # 点击对应的合约
        cp.find_elements(10, *em.contract_nfts)[case['case_id'] - 1].click()
        # 创建前端项目并命名
        cp.create_by_template(case['case_data'])
        # 返回到project页面
        cp.click(30, *em.back_to_project)
        # 获取文本和URL地址
        tx = cp.find_elements(10, *em.project_contract_names)[0].text
        print(tx)
        url = connect_db1.current_url
        try:
            assert get_ini_data('url', 'new_url') in url  # 断言URL地址与预期一致
            assert case['case_data'] in tx  # 断言文本信息是都存在
            logger.info("测试编号:{},测试标题:{},执行成功！".format(case['case_id'], case['case_title'][0]))
        except AssertionError as e:
            get_picture(connect_db1, case['case_title'][0])  # 失败截图
            logger.error(
                "测试编号:{},测试标题:{},执行失败!实际结果:{}".format(case['case_id'], case['case_title'][0], e))
            logger.exception(e)
            raise e

    ids1 = ['测试{}'.format(case['case_title'][1]) for case in cases]

    @allure.suite('sui生态检查合约')
    @allure.description("sui生态检查合约")
    @pytest.mark.parametrize('case', cases, ids=ids1)
    def test_check(self, case, connect_db):
        allure.dynamic.title(case['case_title'][1])
        allure.attach(body=get_ini_data('url', 'get_url'), name='请求路径')
        cp = CreateProject(connect_db)
        cp.geturl(get_ini_data('url', 'get_url'))  # 输入项目地址
        lens = len(get_yaml_data(DATA_SUI))
        # 登录项目
        cp.longin(get_ini_data('github', 'user'), get_ini_data('github', 'passwd'))
        # 点击项目详情按钮
        cp.contract_projects(case['case_data'], lens)
        # 点击检查按钮
        cp.clicks(10, *em.projects_check)
        time.sleep(5)
        connect_db.refresh()
        # 判断代码是否检查成功
        cp.wait_recent(200, *em.projects_recent_check)
        # 点击检查详情页面
        cp.click(10, *em.projects_view_check)
        # 获取页面的文本信息
        time.sleep(3)
        tx1 = cp.text(10, *em.frontend_check_fulllog)
        print(tx1)
        tx2 = cp.text(10, *em.frontend_check_Result)
        print(tx2)
        new_url = connect_db.current_url

        try:
            assert case['text']['tx1'] in tx1
            assert case['text']['tx2'] in tx2
            assert get_ini_data('url', 'new_url') in new_url
            logger.info("测试编号:{},测试标题:{},执行成功！".format(case['case_id'], case['case_title'][1]))
        except AssertionError as e:
            get_picture(connect_db, case['case_title'][1])  # 失败截图
            logger.error(
                "测试编号:{},测试标题:{},执行失败!实际结果:{}".format(case['case_id'], case['case_title'][1], e))
            logger.exception(e)
            raise e

    ids2 = ['测试{}'.format(case['case_title'][2]) for case in cases]

    @allure.suite('sui生态构建合约')
    @allure.description("sui生态构建合约")
    @pytest.mark.parametrize('case', cases, ids=ids2)
    def test_build(self, case, connect_db):
        allure.dynamic.title(case['case_title'][2])
        allure.attach(body=get_ini_data('url', 'get_url'), name='请求路径')
        cp = CreateProject(connect_db)
        cp.geturl(get_ini_data('url', 'get_url'))  # 输入项目地址
        lens = len(get_yaml_data(DATA_SUI))
        # 登录项目
        cp.longin(get_ini_data('github', 'user'), get_ini_data('github', 'passwd'))
        # 点击项目详情按钮
        cp.contract_projects(case['case_data'], lens)
        cp.click(10, *em.projects_build)
        time.sleep(5)
        connect_db.refresh()
        # 获取钱包地址复制到输入框中
        cp.wait_recent(200, *em.projects_recent_build)
        cp.click(10, *em.projects_view_build)
        # 获取编译页面的文本关键字
        time.sleep(3)
        tx1 = cp.text(10, *em.build_result)
        tx2 = cp.text(10, *em.build_deploy)
        cp.click(10, *em.build_more)
        tx3 = cp.text(10, *em.build_more_abi)
        new_url = connect_db.current_url
        print(tx1, tx2, tx3)

        try:
            assert case['text']['tx2'] in tx1
            assert case['text']['tx4'] in tx2
            assert case['text']['tx3'] in tx3
            assert get_ini_data('url', 'new_url') in new_url
            logger.info("测试编号:{},测试标题:{},执行成功！".format(case['case_id'], case['case_title'][2]))
        except AssertionError as e:
            get_picture(connect_db, case['case_title'][2])  # 失败截图
            logger.error(
                "测试编号:{},测试标题:{},执行失败!实际结果:{}".format(case['case_id'], case['case_title'][2], e))
            logger.exception(e)
            raise e

    ids3 = ['测试{}'.format(case['case_title'][3]) for case in cases]

    @allure.suite('sui生态部署合约')
    @allure.description("sui生态部署合约")
    @pytest.mark.parametrize('case', cases, ids=ids3)
    def test_deploy(self, case, connect_db):
        allure.dynamic.title(case['case_title'][3])
        allure.attach(body=get_ini_data('url', 'get_url'), name='请求路径')
        cp = CreateProject(connect_db)
        cp.geturl(get_ini_data('url', 'get_url'))  # 输入项目地址
        cp.driver.implicitly_wait(15)
        lens = len(get_yaml_data(DATA_SUI))
        # 登录项目
        cp.longin(get_ini_data('github', 'user'), get_ini_data('github', 'passwd'))
        # 点击项目详情按钮
        cp.contract_projects(case['case_data'], lens)
        # 点击deploy按钮
        cp.click(10, *em.projects_deploy)
        # 选择部署的网络
        cp.deploy_evm(1, 1)
        time.sleep(3)
        # 操作钱包交易
        windows = connect_db.window_handles
        print(windows)
        # 判断弹窗有没有成功开启
        if len(windows) == 1:
            print("选择的网络错误")
            get_picture(connect_db, case['case_title'][3])  # 失败截图
            logger.error("测试编号:{},测试标题:{},执行失败!实际结果:{}".format(case['case_id'], case['case_title'][3],
                                                                               "请手动切换网络"))
            raise Exception
        cp.window(1)
        cp.send_keys(10, *em.sui_password, "Dx3826729")
        cp.click(10, *em.sui_unlock)
        cp.clicks(20, *em.sui_approve)
        time.sleep(30)
        cp.window(-1)
        tx = cp.text(20, *em.ops_projects)
        new_url = connect_db.current_url

        try:
            assert case['text']['tx5'] in tx
            assert get_ini_data('url', 'new_url') in new_url
            logger.info("测试编号:{},测试标题:{},执行成功！".format(case['case_id'], case['case_title'][3]))
        except AssertionError as e:
            get_picture(connect_db, case['case_title'][3])  # 失败截图
            logger.error(
                "测试编号:{},测试标题:{},执行失败!实际结果:{}".format(case['case_id'], case['case_title'][3], e))
            logger.exception(e)
            raise e

    ids4 = ['测试{}'.format(case['case_title'][4]) for case in cases]

    @allure.suite('sui生态删除合约')
    @allure.description("sui生态删除合约")
    @pytest.mark.parametrize('case', cases, ids=ids4)
    def test_delete(self, case, connect_db):
        allure.dynamic.title(case['case_title'][4])
        allure.attach(body=get_ini_data('url', 'get_url'), name='请求路径')
        cp = CreateProject(connect_db)
        # 输入项目地址
        cp.geturl(get_ini_data('url', 'get_url'))
        cp.longin(get_ini_data('github', 'user'), get_ini_data('github', 'passwd'))
        # 从.ini文件中获取github的库名和密码
        sth = get_ini_data('github', 'storehouse')
        psw = get_ini_data('github', 'passwd')
        lens = len(get_yaml_data(DATA_SUI))
        # 点击github链接，跳转至github页面
        cp.click(15, By.CSS_SELECTOR,
                 'a[href="https://github.com/{}.git"]'.format('{}/{}'.format(sth, case['case_data'])))
        cp.window(-1)
        # 删除github中的项目
        cp.delete_project_github(sth, case['case_data'], '{}/{}'.format(sth, case['case_data']))
        # 输入github密码确认删除
        cp.delete_project_passwd(psw)
        # 判断被删除的项目在GitHub中是否存在
        ast = cp.iselement(5, By.CSS_SELECTOR, 'a[href="/{}"]'.format('{}/{}'.format(sth, case['case_data'])))
        # 切换至hamster主页面
        cp.window(0)
        cp.driver.refresh()
        # 点击进入hamster的项目管理页
        cp.contract_projects(case['case_data'], lens)
        # 删除hamster的项目
        cp.delete_project_hamster()
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
            get_picture(self.driver, case['case_title'][4])  # 失败截图
            logger.error(
                "测试编号:{},测试标题:{},执行失败!实际结果:{}".format(case['case_id'], case['case_title'][4], e))
            logger.exception(e)
            raise e


if __name__ == '__main__':
    pytest.main(['-vs', __file__])
