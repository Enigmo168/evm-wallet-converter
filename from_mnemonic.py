from eth_account import Account
from loguru import logger


logger.info('Converting mnemonic phrases into private keys...')

Account.enable_unaudited_hdwallet_features()

with open('data/mnemonics.txt', 'r') as file:
    mnemonics = file.read().splitlines()

with open('data/private_keys.txt', 'w') as file:
    for mnemonic in mnemonics:
        private_key = Account.from_mnemonic(mnemonic).key.hex()
        file.write(f'{private_key}\n')

logger.success('Successfully')
