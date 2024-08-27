from web3 import Web3, AsyncWeb3


# w3 = await AsyncWeb3(AsyncWeb3.WebSocketProvider('wss://sepolia.infura.io/ws/v3/6e8d1dfe785a4520b17b45a7c6c194f1'))

w3 = Web3(Web3.HTTPProvider('https://sepolia.infura.io/v3/6e8d1dfe785a4520b17b45a7c6c194f1'))
# r = w3.is_connected()

lb = w3.eth.get_block('latest')

print(lb.number)
print(Web3.to_hex(lb.hash))
