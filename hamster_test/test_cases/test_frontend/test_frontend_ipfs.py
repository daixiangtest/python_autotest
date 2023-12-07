import allure
import time
import pytest
from selenium.webdriver.common.by import By
from hamster_test.comms.constants import DATA_IPFS
from hamster_test.comms.log_utils import get_logger
from hamster_test.comms.yaml_utils import get_yaml_data, get_picture, get_ini_data
from hamster_test.web.selenium.page.create_project import CreateProject
from hamster_test.web.selenium.elenium import elenium as em

logger = get_logger()


@allure.epic('hamster系统')
@allure.feature("FrontEnd项目合约")
@allure.parent_suite('FrontEnd项目合约')
class TestFrontEnd:
    cases = get_yaml_data(DATA_IPFS)  # 读取yaml文件中的测试数据
    ids = ['测试{}'.format(case['case_title'][0]) for case in cases]

    # @allure.suite('IPFS生态创建合约')
    # @allure.description("IPFS生态创建合约")
    # @pytest.mark.parametrize('case', cases, ids=ids)
    # def test_create(self, case, connect_db):
    #     allure.dynamic.title(case['case_title'][0])
    #     allure.attach(get_ini_data('url', 'get_url'), name='请求路径')
    #     cp = CreateProject(connect_db)
    #     # 登录项目网址
    #     cp.geturl(get_ini_data('url', 'get_url'))
    #     # 登录项目
    #     cp.longin(get_ini_data('github', 'user'), get_ini_data('github', 'passwd'))
    #     # 点击创建项目
    #     if cp.iselement(5, *em.project_frontend):
    #         cp.click(5, *em.create_project)
    #     # 打开ipfs合约的展示页面
    #     cp.open_frontend_ipfs()
    #     # 点击对应的合约
    #     cp.click(10, *em.frontend_ipfs[case['case_id'] - 1])
    #     # 查看view中的前端模板，并获取里面的文本信息
    #     cp.click(10, *em.create_frontend_view)
    #     tx1 = cp.get_frontend_view(case['case_id'])
    #     print(tx1)
    #     time.sleep(3)
    #     # 创建前端项目并命名
    #     cp.create_by_template(case['case_data'])
    #     # 返回到project页面
    #     cp.click(30, *em.back_to_project)
    #     # 获取文本和URL地址
    #     tx2 = cp.find_elements(10, *em.project_contract_names)[0].text
    #     url = connect_db.current_url
    #     try:
    #         assert get_ini_data('url', 'new_url') in url  # 断言URL地址与预期一致
    #         assert case['text']['tx1'] in tx1  # 断言文本信息是都存在
    #         assert case['case_data'] in tx2
    #         logger.info("测试编号:{},测试标题:{},执行成功！".format(case['case_id'], case['case_title'][0]))
    #     except AssertionError as e:
    #         get_picture(connect_db, case['case_title'][0])  # 失败截图
    #         logger.error(
    #             "测试编号:{},测试标题:{},执行失败!实际结果:{}".format(case['case_id'], case['case_title'][0], e))
    #         logger.exception(e)
    #         raise e

    # ids1 = ['测试{}'.format(case['case_title'][1]) for case in cases]
    #
    # @allure.suite('IPFS生态检查合约')
    # @allure.description("IPFS生态检查合约")
    # @pytest.mark.parametrize('case', cases, ids=ids1)
    # def test_check(self, case, connect_db):
    #     allure.dynamic.title(case['case_title'][1])
    #     allure.attach(body=get_ini_data('url', 'get_url'), name='请求路径')
    #     cp = CreateProject(connect_db)
    #     cp.geturl(get_ini_data('url', 'get_url'))  # 输入项目地址
    #     lens = len(get_yaml_data(DATA_IPFS))
    #     # 登录项目
    #     cp.longin(get_ini_data('github', 'user'), get_ini_data('github', 'passwd'))
    #     cp.click(10, *em.project_frontend)
    #     # 点击项目详情按钮
    #     cp.frontend_projects(case['case_data'], lens)
    #     # 点击检查按钮
    #     cp.clicks(10, *em.projects_check)
    #     # 判断代码是否检查成功
    #     cp.wait_recent(200, *em.projects_recent_check)
    #     # 点击检查详情页面
    #     cp.click(10, *em.projects_view_check)
    #     # 获取页面的文本信息
    #     time.sleep(3)
    #     tx1 = cp.text(10, *em.frontend_check_fulllog)
    #     tx2 = cp.text(10, *em.frontend_check_Result)
    #     new_url = connect_db.current_url
    #     print(tx1, tx2)
    #
    #     try:
    #         assert case['text']['tx2'] in tx1
    #         assert case['text']['tx3'] in tx2
    #         assert get_ini_data('url', 'new_url') in new_url
    #         logger.info("测试编号:{},测试标题:{},执行成功！".format(case['case_id'], case['case_title'][1]))
    #     except AssertionError as e:
    #         get_picture(connect_db, case['case_title'][1])  # 失败截图
    #         logger.error(
    #             "测试编号:{},测试标题:{},执行失败!实际结果:{}".format(case['case_id'], case['case_title'][1], e))
    #         logger.exception(e)
    #         raise e
    #
    # ids2 = ['测试{}'.format(case['case_title'][2]) for case in cases]
    #
    # @allure.suite('IPFS生态构建合约')
    # @allure.description("IPFS生态构建合约")
    # @pytest.mark.parametrize('case', cases, ids=ids2)
    # def test_build(self, case, connect_db):
    #     allure.dynamic.title(case['case_title'][2])
    #     allure.attach(body=get_ini_data('url', 'get_url'), name='请求路径')
    #     cp = CreateProject(connect_db)
    #     cp.geturl(get_ini_data('url', 'get_url'))  # 输入项目地址
    #     lens = len(get_yaml_data(DATA_IPFS))
    #     # 登录项目
    #     cp.longin(get_ini_data('github', 'user'), get_ini_data('github', 'passwd'))
    #     cp.click(10, *em.project_frontend)
    #     # 点击项目详情按钮
    #     cp.frontend_projects(case['case_data'], lens)
    #     cp.click(10, *em.projects_build)
    #     cp.wait_recent(200, *em.projects_recent_build)
    #     tx1 = cp.text(10, *em.projects_deploy_now)
    #     print(tx1)
    #
    #     new_url = cp.driver.current_url
    #     try:
    #         assert case['text']['tx4'] in tx1
    #         assert get_ini_data('url', 'new_url') in new_url
    #         logger.info("测试编号:{},测试标题:{},执行成功！".format(case['case_id'], case['case_title'][2]))
    #     except AssertionError as e:
    #         get_picture(connect_db, case['case_title'][2])  # 失败截图
    #         logger.error(
    #             "测试编号:{},测试标题:{},执行失败!实际结果:{}".format(case['case_id'], case['case_title'][2], e))
    #         logger.exception(e)
    #         raise e

    ids3 = ['测试{}'.format(case['case_title'][3]) for case in cases]

    @allure.suite('IPFS生态部署合约')
    @allure.description("IPFS生态部署合约")
    @pytest.mark.parametrize('case', cases, ids=ids3)
    def test_deploy(self, case, connect_db):
        allure.dynamic.title(case['case_title'][3])
        allure.attach(body=get_ini_data('url', 'get_url'), name='请求路径')
        cp = CreateProject(connect_db)
        cp.geturl(get_ini_data('url', 'get_url'))  # 输入项目地址
        lens = len(get_yaml_data(DATA_IPFS))
        # 登录项目
        cp.longin(get_ini_data('github', 'user'), get_ini_data('github', 'passwd'))
        cp.click(10, *em.project_frontend)
        # 点击项目详情按钮
        cp.frontend_projects(case['case_data'], lens)
        # 点击deploy按钮
        cp.click(10, *em.projects_deploy)
        # 等待deploy成功
        cp.wait_recent(100, *em.projects_recent_deploy)
        # 点击view打开ops页面
        cp.clicks(10, *em.projects_view_frontend)
        # 获取ops页面的文本信息
        tx1 = cp.text(10, *em.frontend_ops_status)
        tx2 = cp.text(10, *em.frontend_ops_package)
        # 点击链接打开模板展示
        cp.click(10, *em.frontend_ops_domains)
        tx3 = cp.get_frontend_view(case['case_id'])

        new_url = connect_db.current_url
        try:
            assert case['text']['tx3'] in tx1
            assert case['case_data'] in tx2
            assert case['text']['tx1'] in tx3
            assert get_ini_data('url', 'new_url') in new_url
            logger.info("测试编号:{},测试标题:{},执行成功！".format(case['case_id'], case['case_title'][3]))
        except AssertionError as e:
            get_picture(connect_db, case['case_title'][3])  # 失败截图
            logger.error(
                "测试编号:{},测试标题:{},执行失败!实际结果:{}".format(case['case_id'], case['case_title'][3], e))
            logger.exception(e)
            raise e

    ids4 = ['测试{}'.format(case['case_title'][4]) for case in cases]

    @allure.suite('IPFS生态删除合约')
    @allure.description("IPFS生态删除合约")
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
        lens = len(get_yaml_data(DATA_IPFS))
        # 点击前端项目模块
        cp.click(10, *em.project_frontend)
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
        cp.frontend_projects(case['case_data'], lens)
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
