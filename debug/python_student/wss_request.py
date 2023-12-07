import ssl
import time

"""
测试websocket接口
"""
import websocket

count = 0
# url = ['wss://api.zan.top/node/ws/v1/eth/goerli/f3f0feb84b3147b79c0a05fbe9952cf4',
#        "wss://api.zan.top/node/ws/v1/eth/mainnet/f3f0feb84b3147b79c0a05fbe9952cf4",
#        "wss://api.zan.top/node/ws/v1/eth/sepolia/f3f0feb84b3147b79c0a05fbe9952cf4"]
url = ['wss://api.zan.top/node/ws/v1/bsc/mainnet/f3f0feb84b3147b79c0a05fbe9952cf4',
       'wss://api.zan.top/node/ws/v1/bsc/testnet/f3f0feb84b3147b79c0a05fbe9952cf4']

# url = ['wss://api.zan.top/node/ws/v1/polygon/mainnet/f3f0feb84b3147b79c0a05fbe9952cf4',
#        'wss://api.zan.top/node/ws/v1/polygon/mumbai/f3f0feb84b3147b79c0a05fbe9952cf4']

a = 0
methods = ["eth_blockNumber", "eth_blockNumber1", "eth_blockNumber2", "eth_blockNumber3", "eth_blockNumber4",
           "eth_blockNumber5", "eth_blockNumber6"]
while True:

    for method in methods:
        ws = websocket.WebSocket()  # 获取对象加载安全证书
        ws.connect(url[a])  # 建立链接
        ws.send('{"method":' + method + ',"params":[],"id":1,"jsonrpc":"2.0"}')  # 发送请求数据
        res = ws.recv()  # 获取响应结果

        print(res)
        ws.close()
    count += 1
    a += 1
    if a == len(url):
        a = 0
    if count == 30:
        break
    time.sleep(10)
