from brownie import SimpleStorage, accounts

def test_deploy():
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})
    starting_value = simple_storage.retrieve()
    expected = 0
    assert starting_value == expected

def test_updating_storage():
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})
    simple_storage.store(15, {"fromt": account})
    expected = 15
    assert simple_storage.retrieve() == expected