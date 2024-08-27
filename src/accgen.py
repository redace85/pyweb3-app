# pip install ecdsa

from ecdsa import SigningKey, SECP256k1
from eth_keys import keys

priv = SigningKey.generate(curve=SECP256k1)

pub = priv.get_verifying_key().to_string()
print("Public key1: ", pub.hex())

# eth_pk
pk = keys.PrivateKey(priv.to_string())

print("Private key1:", priv.to_string().hex())
print("Private key2:", pk)

print("Public key2: ", pk.public_key)

print("Addr: ", pk.public_key.to_checksum_address())

