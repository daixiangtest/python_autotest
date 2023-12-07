import os

"""
使用常量对路径进行管理
好处: 代码使用非绝对路径,可移植性高
"""

# 获取项目路径
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# 测试用例执行文件所在路径
CASE_DIR = os.path.join(BASE_DIR, r'test_cases')
CASE_LOGIN = os.path.join(CASE_DIR, r'test_login\test_login.py')
CASE_CONTRACT = os.path.join(CASE_DIR, r'test_contract\test_contract_evm.py')
CASE_IPFS = os.path.join(CASE_DIR, r'test_frontend\test_frontend_ipfs.py')
CASE_CONTAINER = os.path.join(CASE_DIR, r'test_frontend/test_frontend_container.py')
CASE_APTOS = os.path.join(CASE_DIR, r'test_contract/test_contract_aptos.py')
CASE_SUI = os.path.join(CASE_DIR, r'test_contract/test_contract_sui.py')
CASE_STARKNET = os.path.join(CASE_DIR, r'test_contract/test_contract_starknet.py')
CASE_ICP_FRONTEND = os.path.join(CASE_DIR, r'test_icp/test_icp_frontend.py')
# 测试数据所在路径
DATA_DIR = os.path.join(BASE_DIR, 'datas')
DATA_YAML = os.path.join(DATA_DIR, 'hamster_login.yaml')
DATA_EVM = os.path.join(DATA_DIR, 'hamster_contract_evm.yaml')
DATA_IPFS = os.path.join(DATA_DIR, 'hamster_frontend_ipfs.yaml')
DATA_CONTAINER = os.path.join(DATA_DIR, 'hamster_frontend_container.yaml')
DATA_APTOS = os.path.join(DATA_DIR, 'hamster_contract_aptos.yaml')
DATA_SUI = os.path.join(DATA_DIR, "hamster_contract_sui.yaml")
DATA_STARKNET = os.path.join(DATA_DIR, "hamster_contract_starknet.yaml")
DATA_ICP = os.path.join(DATA_DIR, "hamster_icp_frontend.yaml")
# log所在路径
LOG_DIR = os.path.join(BASE_DIR, 'logs')
INFO_FILE = os.path.join(LOG_DIR, 'info.log')
ERROR_FILE = os.path.join(LOG_DIR, 'error.log')

# 测试报告所在路径
REPORT_DIR = os.path.join(BASE_DIR, 'reports')
REPORT_JSON = os.path.join(REPORT_DIR, 'allure_json')
REPORT_HTML = os.path.join(REPORT_DIR, 'allure_html')

# 测试截图所在路径
PICTURE_DIR = os.path.join(BASE_DIR, 'picture')

# 获取config.ini目录
CFI = os.path.join(BASE_DIR, 'confs/confing.ini')

if __name__ == '__main__':
    print(BASE_DIR)
    print(CASE_DIR)
    print(DATA_YAML)
    print(REPORT_DIR)
    print(DATA_CONTAINER)
