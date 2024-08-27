# pip install ecdsa
# pip install pysha3
from ecdsa import SigningKey, SECP256k1
from eth_keys import keys

counter = 0
dot_num = 0
# target to search for startswith
target = 'Ace'
while True:
    # eth_pk
    pk = keys.PrivateKey(SigningKey.generate(curve=SECP256k1).to_string())
    address = pk.public_key.to_checksum_address()
    counter+=1
    if address.startswith(target,2,2+len(target)):
        print('Target Found!!!')

        print('Private key:', pk)
        print('Public key: ', pk.public_key)
        print('Address: ' + address)
        break
    else:
        if 0==counter%100:
            dot_num+=1
            dot_num %= 10
            blanks = '.'*dot_num+ ' '*(10-dot_num)
            print('Searching {} :{}'.format(blanks,counter), end='\r')
