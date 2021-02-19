import secrets
from coincurve import PublicKey
from Crypto.Hash import keccak

clan_tag = input('Input desired clan tag: ').lower()
n = len(clan_tag)

try:
    x = int(clan_tag, 16)
except ValueError:
    print(f'Error: "{clan_tag}" is not valid hex.')
    exit(1)

while True:
    # Generate a private key
    p_hash_obj = keccak.new(digest_bits=256)
    seed = secrets.token_bytes(32)
    p_hash_obj.update(seed)
    p = p_hash_obj.digest()

    # Derive the public key
    q = PublicKey.from_valid_secret(p).format(compressed=False)[1:]

    # Hash public key into account address
    addr_hash_obj = keccak.new(digest_bits=256)
    addr_hash_obj.update(q)
    address = addr_hash_obj.digest()[-20:]
    if address.hex()[-n:] == clan_tag:
        print('Seed       : ' + seed.hex())
        print('Private key: ' + p_hash_obj.hexdigest())
        print('Public key : ' + q.hex())
        print('Address    : ' + address.hex())
        print('Never share the seed or private key with anyone!')
        print('Never share the seed or private key with anyone!')
        print('Never share the seed or private key with anyone!')
        break
