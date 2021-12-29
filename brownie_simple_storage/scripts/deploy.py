from brownie import accounts, config, SimpleStorage


def deploy_simple_storage():
    account = accounts.add(config["wallets"]["from_key"])
    simple_storage = SimpleStorage.deploy({"from": account})
    stored_value = simple_storage.retrieve()
    print(stored_value)
    transaction = simple_storage.store(15, {"from":account})
    transaction.wait(1)
    updated = simple_storage.retrieve()
    print(updated)

def main():
    deploy_simple_storage()