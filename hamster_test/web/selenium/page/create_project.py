import time

from selenium.webdriver import Keys

from hamster_test.comms.yaml_utils import get_picture
from hamster_test.web.selenium.page.object_page import Hamster
from selenium.webdriver.common.by import By
from selenium import webdriver
from hamster_test.comms.log_utils import get_logger
from hamster_test.comms.yaml_utils import get_ini_data
from hamster_test.web.selenium.elenium import elenium as em


class CreateProject(Hamster):
    def login_pass(self):
        token = get_ini_data("url", "token")
        self.driver.execute_script(
            f'localStorage.setItem("token","{token}")')
        self.driver.refresh()

    # git登录页面的操作
    def longin(self, value1, value2):
        """

        :param value1: 输入用户名或者邮箱账户
        :param value2: 输入密码
        :return:
        """
        if self.iselement(5, *em.login_github):
            self.click(10, *em.login_github)
            self.window(-1)
            if self.iselement(10, *em.sed_login):
                self.send_keys(10, *em.sed_login, value1)
                self.send_keys(10, *em.sed_password, value2)
                self.click(10, *em.click_commit)
            if self.iselement(5, *em.github_empower):
                self.clicks(10, *em.github_empower)
            if self.iselement(10, By.ID, 'id="otp"'):
                print('登录需要验证码')
                time.sleep(60)
        self.window(0)
        # if self.iselement(10, *em.create_project):
        #     self.click(5, *em.create_project)

    # 打开evm合约的项目展示
    def open_evm(self):
        self.target(10, *em.create_next)

    # 打开aptos合约的项目展示
    def open_aptos(self):
        self.find_elements(5, *em.create_ecosystems)[1].click()
        self.target(10, *em.create_next)

    # 打开starkware合约的项目展示
    def open_starknet(self):
        self.find_elements(5, *em.create_ecosystems)[3].click()
        self.target(10, *em.create_next)

    # 打开sui合约的项目展示
    def open_sui(self):
        self.find_elements(5, *em.create_ecosystems)[4].click()
        self.target(10, *em.create_next)

    # 打开前端Ipfs合约的项目展示
    def open_frontend_ipfs(self):
        time.sleep(3)
        self.driver.find_element(*em.create_frontend).click()
        time.sleep(3)
        self.target(10, *em.create_next)

    # 打开前端container合约的项目展示
    def open_frontend_container(self):
        time.sleep(3)
        self.driver.find_element(*em.create_frontend).click()
        time.sleep(3)
        self.driver.find_element(*em.create_container).click()
        time.sleep(3)
        self.target(10, *em.create_next)

    def open_icp_frontend(self):
        time.sleep(3)
        self.driver.find_element(*em.create_frontend).click()
        self.find_elements(5, *em.create_frontend_deployments)[2].click()
        time.sleep(3)
        self.target(10, *em.create_next)

    # 创建项目合约的操作页面
    def create_by_template(self, value):
        """

        :param value:创建项目的名称
        :return:
        """
        self.click(10, *em.create_by_template)
        self.send_keys(10, *em.send_project_name, value)
        self.click(10, *em.click_create)

    # 点击所选项目的详情页面
    def contract_projects(self, name, len):
        """

        :param name: 项目名称
        :param len: 创建项目的数量
        :return:
        """
        for i in range(len):
            if i > 0 and i % 10 == 0:
                self.find_elements(5, *em.project_switch_pages)[1].click()
                time.sleep(3)
            el = self.find_elements(10, *em.project_contract_names)[i % 10]
            tx = el.text
            if name == tx:
                self.driver.execute_script(
                    r'document.querySelector("#rc-tabs-0-panel-1 > div > div:nth-child({}) > div > div > div.first > div.flex.items-center > div.project-title.text-\\[24px\\].font-bold.cursor-pointer.hover\\:open-link-css").click()'.format(i % 10+1))
                # self.find_elements(10, *em.project_contract_names)[i % 10].click()
                break
            if i == len - 1 and name != tx:
                print(f'项目名称{name}没有找到')
                raise Exception

    # 点击所选前端项目的详情页面
    def frontend_projects(self, name, len):
        """

        :param name: 项目名称
        :param len: 创建项目的数量
        :return:
        """
        for i in range(len):
            el = self.find_elements(10, *em.project_contract_names)[i]
            tx = el.text
            if name in tx:
                el.click()
                break
            if i == len - 1 and name not in tx:
                print(f'项目名称{name}没有找到')
                raise Exception

    # 点击项目检查的check按钮
    def contract_check(self, name, len):
        """

        :param name:项目名称
        :param len: 创建项目的数量
        :return:
        """
        for i in range(len):
            tx = self.text(10, *em.project_contract_names[i])
            if name in tx:
                self.click(5, *em.project_contract_checks[i])
                break

    # 点击项目构建按钮
    def contract_build(self, name, len):
        """

          :param name:项目名称
          :param len: 创建项目的数量
          :return:
          """
        for i in range(len):
            tx = self.text(5, *em.project_contract_names[i])
            if name in tx:
                self.click(5, *em.project_contract_builds[i])
                time.sleep(3)
                break

    # 点击项目合约部署deploy按钮
    def contract_deploy(self, name, len):
        """

          :param name:项目名称
          :param len: 创建项目的数量
          :return:
        """
        for i in range(len):
            tx = self.find_elements(5, *em.project_contract_names)[i].text
            if name in tx:
                self.click(5, *em.project_contract_deploys[i])
                break

    # 点击项目的合约调用ops按钮
    def contract_ops(self, name, len):
        """

          :param name:项目名称
          :param len: 创建项目的数量
          :return:
        """
        for i in range(len):
            tx = self.text(5, *em.project_contract_names[i])
            if name in tx:
                self.click(5, *em.project_contract_ops[i])
                break

    # 等待加载的状态是否成功
    def wait_recent(self, times, path, element):
        try:
            tm = 0
            a = 0
            while tm < times:
                time.sleep(3)
                tx = self.text(10, path, element)
                a += 1
                print(a)
                if 'Success' in tx:
                    break
                if 'Fail' in tx:
                    raise Exception
                tm += 1
                if tm % 20 == 0:
                    self.driver.refresh()
                if tm == times:
                    raise Exception
        except Exception as e:
            print('运行时间过长或失败')
            get_picture(self.driver, '检查或编译过长')  # 失败截图
            get_logger().error("检查或编译过长")
            raise e

    # 链接小狐狸钱包的登录操作
    def metamask_login(self, value):
        self.driver.implicitly_wait(15)
        windows = self.driver.window_handles
        # 判断钱包是否自动弹出
        if len(windows) >= 2:
            self.window(1)
            self.send_keys(10, *em.metamask_passwd, value)
            self.click(10, *em.metamask_login)
            self.window(0)
        # 判断钱包是否已经链接
        if self.iselement(1, *em.connect_wallet):
            self.click(5, *em.connect_wallet)
            time.sleep(1)
            shadow = self.driver.execute_script(em.js)
            time.sleep(3)
            windows = self.driver.window_handles
            # 判断钱包是否需要输入密码
            if len(windows) > 1:
                self.window(1)
                self.send_keys(10, *em.metamask_passwd, value)
                self.click(10, *em.metamask_login)
                self.window(0)

    # 部署evm的页面操作
    def deploy_evm(self, int1, int2):
        self.click(10, *em.deploy_evm_name)
        self.click(10, *em.deploy_evm_chain)
        self.click(10, *em.deploy_evm_chains[int1 - 1])
        self.click(10, *em.deploy_evm_network)
        self.click(10, *em.deploy_evm_networks[int2 - 1])
        self.click(10, *em.deploy_evm_click)

    # 部署evm的nft合约操作页面
    def deploy_evm_nft(self, value1, value2, value3, int1, int2):
        self.find_elements(10, *em.deploy_evm_name_nft)[1].click()
        self.send_keys(10, *em.deploy_evm_name_nfts[0], value1)
        self.send_keys(10, *em.deploy_evm_name_nfts[1], value2)
        self.send_keys(10, *em.deploy_evm_name_nfts[2], value3)
        self.click(10, *em.deploy_evm_name_nfts[3])
        self.click(10, *em.deploy_evm_chain)
        self.click(10, *em.deploy_evm_chains_nft[int1 - 1])
        self.click(10, *em.deploy_evm_network)
        self.click(10, *em.deploy_evm_networks_nft[int2 - 1])
        self.click(10, *em.deploy_evm_click)

    # 确认部署页面操作
    def deploy_evm_confirm(self, value):
        # print('debugger_address:', self.driver.caps['goog:chromeOptions']['debuggerAddress'])
        time.sleep(3)
        if len(self.driver.window_handles) >= 2:
            print(1)
            self.window(1)
            # 判断是否需要密码登录
            if self.iselement(10, *em.metamask_passwd):
                self.send_keys(10, *em.metamask_passwd, value)
                print(2)
                self.click(10, *em.metamask_login)
                time.sleep(5)
            a = self.driver.window_handles
            # 判断是的有新的弹窗
            if len(a) >= 2:
                self.window(-1)
                if self.iselement(5, *em.metamask_handoff):
                    self.clicks(10, *em.metamask_handoff)
                    print(2)
                if self.iselement(5, *em.metamask_know):
                    self.clicks(10, *em.metamask_know)
                    print(3)
                if self.iselement(5, *em.metamask_confirm):
                    print(1)
                    self.clicks(10, *em.metamask_confirm)
                    time.sleep(6)
            time.sleep(3)
            if len(self.driver.window_handles) == 1:
                self.window(0)
                if self.iselement(3, *em.deploy_evm_click):
                    self.clicks(10, *em.deploy_evm_click)
                    time.sleep(6)
                    self.window(1)
                    self.clicks(10, *em.metamask_confirm)
        time.sleep(3)

    # 删除github中的项目的页面操作
    def delete_project_github(self, sth, case, value):
        """

        :param sth: github的仓库名称
        :param case: 仓库中需要删除的项目名称
        :param value: 需要输入的仓库与项目名
        :return:
        """
        # 点击setting设置
        self.click(10, By.CSS_SELECTOR, 'a[href="/{}/settings"]'.format('{}/{}'.format(sth, case)))
        # 点击删除按钮
        self.target(10, *em.delete_this_repository)
        # 确认删除
        self.click(10, *em.delete_want)
        # 再次确认删除
        self.clicks(10, *em.delete_want)
        # 输入需要删除的库名
        time.sleep(3)
        self.send_keys(10, *em.delete_box, value)
        # 点击确认删除
        self.clicks(10, *em.delete_this_repository_to)

    # 判断删除github项目是否需要输入密码
    def delete_project_passwd(self, passwd):
        """

        :param passwd:所属github的密码
        :return:
        """
        if self.iselement(10, *em.delete_sudo_password):
            self.send_keys(10, *em.delete_sudo_password, passwd)
            self.click(10, *em.delete_password_submit)

    # 操作删除hamster的project项目
    def delete_project_hamster(self):
        self.click(10, *em.projects_hamster_delete)
        self.clicks(10, *em.projects_hamster_delete_yes)

    # 打开前端项目的展示模板并且返回对应的网页信息
    def get_frontend_view(self, num):
        """
        点击view获取view视图中的文本信息
        :param path: view按钮的元素属性
        :param element: view按钮的元素
        :num:获取视图的的标号
        :return: view打开的页面的值
        """
        try:
            # self.click(10, path, element)
            self.driver.implicitly_wait(15)
            self.window(1)
            tx = self.text(10, *em.frontend_view[num - 1])
            print(tx)
            self.window(0)
            return tx
        except Exception:
            self.window(0)
            return "获取文本失败"

    # metatrust检查弹窗页面
    def run_metatrust_evm(self, *args):
        """

        :param args:  metatrust 检查工具的选择
                      sa1: Mythril
                      sa2: MetaTrust Security Analyzer
                      sa3: MetaTrust Security Prover
                      osa1: MetaTrust Open Source Analyzer
                      cqa1: Solhint
                      cqa2: MetaTrust Code Quality
                      gua1: eth-gas-reporter
                      ai: AI
        :return:
        """

        if self.iselement(10, *em.project_check_metatrust_done):
            tools = args
            if "sa1" in tools:
                self.find_elements(10, *em.project_check_metatrust)[0].click()
            if "sa2" in tools:
                self.find_elements(10, *em.project_check_metatrust)[1].click()
            if "sa3" in tools:
                self.find_elements(10, *em.project_check_metatrust)[2].click()
            if "osa1" in tools:
                self.find_elements(10, *em.project_check_metatrust)[3].click()
            if "cqa1" in tools:
                self.find_elements(10, *em.project_check_metatrust)[4].click()
            if "cqa2" in tools:
                self.find_elements(10, *em.project_check_metatrust)[5].click()
            if "gua1" in tools:
                self.find_elements(10, *em.project_check_metatrust)[6].click()
            if "ai" in tools:
                self.find_elements(10, *em.project_check_metatrust)[7].click()
            self.click(10, *em.project_check_metatrust_done)
            time.sleep(300)

    # metatrus报告检查的结果验证
    def run_metatrust_evm_reports(self, *args):
        """

                :param args:  metatrust 检查工具的选择

                              sa1: Mythril
                              sa2: MetaTrust Security Analyzer
                              sa3: MetaTrust Security Prover
                              osa1: MetaTrust Open Source Analyzer
                              cqa1: Solhint
                              cqa2: MetaTrust Code Quality
                              gua1: eth-gas-reporter
                              ai: AI
                :return: 返回各个报告比对数据的结果集
                """
        tools = args
        lists = []
        num = 0
        if "sa2" in tools:
            tx1 = self.text(10, *em.metatrust_report_sa)
            self.click(10, *em.metatrust_report_sa)
            time.sleep(3)
            tx2 = self.text(10, *em.metatrust_report_result)
            self.driver.back()
            num += int(tx1)
            lists.append(tx1 == "".join(list(filter(str.isdigit, tx2))))
        if "sa3" in tools:
            tx1 = self.text(10, *em.metatrust_report_sp)
            self.click(10, *em.metatrust_report_sp)
            time.sleep(3)
            tx2 = self.text(10, *em.metatrust_report_result)
            self.driver.back()
            num += int(tx1)
            lists.append(tx1 == "".join(list(filter(str.isdigit, tx2))))
        if "sa1" in tools:
            tx1 = self.text(10, *em.metatrust_report_mythril)
            self.click(10, *em.metatrust_report_mythril)
            time.sleep(3)
            tx2 = self.text(10, *em.metatrust_report_result)
            self.driver.back()
            num += int(tx1)
            lists.append(tx1 == "".join(list(filter(str.isdigit, tx2))))
        if "osa1" in tools:
            tx1 = self.text(10, *em.metatrust_report_osa)
            self.click(10, *em.metatrust_report_osa)
            time.sleep(3)
            tx2 = self.text(10, *em.metatrust_report_result)
            self.driver.back()
            num += int(tx1)
            lists.append(int(tx1) == int("".join(list(filter(str.isdigit, tx2)))))
        if "cqa1" in tools:
            tx1 = self.text(10, *em.metatrust_report_cq)
            self.click(10, *em.metatrust_report_cq)
            time.sleep(3)
            tx2 = self.text(10, *em.metatrust_report_result)
            self.driver.back()
            num += int(tx1)
            lists.append(tx1 == "".join(list(filter(str.isdigit, tx2))))
        if "cqa2" in tools:
            tx1 = self.text(10, *em.metatrust_report_solhint)
            self.click(10, *em.metatrust_report_solhint)
            time.sleep(3)
            tx2 = self.text(10, *em.metatrust_report_result)
            self.driver.back()
            num += int(tx1)
            lists.append(tx1 == "".join(list(filter(str.isdigit, tx2))))
        if "gua1" in tools:
            tx1 = self.text(10, *em.metatrust_report_gas)
            self.click(10, *em.metatrust_report_gas_view)
            time.sleep(3)
            tx2 = self.text(10, *em.metatrust_report_result)
            self.driver.back()
            num += int(tx1)
            lists.append(tx1 == "".join(list(filter(str.isdigit, tx2))))
        if "ai" in tools:
            ast = self.iselement(10, *em.metatrust_report_ai)
            lists.append(ast)
        time.sleep(3)
        num1 = self.text(10, *em.check_issues)
        num2 = int("".join(list(filter(str.isdigit, num1))))
        lists.append(num == num2)
        # print(lists, num, num2)
        return lists

    # 获取谷歌邮箱的验证码
    def frontend_deploy_page(self, value):
        if self.iselement(10, *em.container_port):
            self.send_keys(10, *em.container_port, value)
            self.click(10, *em.frontend_deploy_done)

    # aptos的build弹窗页面
    def aptos_build_parameters(self):
        if self.iselement(5, *em.aptos_mokshyastaking):
            self.find_elements(10, *em.aptos_wallet_address)[0].click()
            time.sleep(8)
            self.clear(10, *em.aptos_mokshyastaking)
            self.send_keys(10, *em.aptos_mokshyastaking, (Keys.CONTROL, 'v'))
            self.find_elements(10, *em.aptos_wallet_address)[1].click()


if __name__ == '__main__':
    option = webdriver.ChromeOptions()
    option.add_argument(
        "--user-data-dir=" + get_ini_data('version', 'chrome_Default'))  # 添加获取到的配置文件路径
    option.add_experimental_option('detach', True)  # 浏览器不会自动关闭
    driver = webdriver.Chrome(chrome_options=option, options=option)  # 打开配置插件的chrome浏览器
    driver.maximize_window()  # 浏览器窗口最大化
    cp = CreateProject(driver)
    cp.geturl('https://develop.hamster.newtouch.com/projects')
