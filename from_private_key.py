from eth_account import Account
from loguru import logger


logger.info('Converting private keys to addresses...')

with open('data/private_keys.txt', 'r') as file:
    keys = file.read().splitlines()


with open('data/addresses.txt', 'w') as file:
    for key in keys:
        address = Account.from_key(key).address
        file.write(f"{address}\n")

logger.success('Successfully')
