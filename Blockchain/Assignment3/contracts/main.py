import json
from web3 import Web3
from solc import compile_files, link_code, compile_source


w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))

def deploy_contract(contract_interface):
    contract = w3.eth.contract(
        abi=contract_interface['abi'],
        bytecode=contract_interface['bin']
    )
    tx_hash =contract.constructor().transact(transaction={'from':w3.eth.accounts[2]})
    tx_receipt = w3.eth.getTransactionReceipt(tx_hash)
    return tx_receipt['contractAddress']

contracts = compile_files(['Deployment.sol','TicTacToe.sol'])
game_contract = contracts.pop("TicTacToe.sol:Tic")
deployment_link = contracts.pop("Deployment.sol:DeployTic")

deployment_address = {
    "Deployment.sol:DeployTic": deploy_contract(deployment_link)
}

game_contract['bin'] = link_code(game_contract['bin'],deployment_address)

with open('data.json', 'w') as outfile:
    data = {
        "abi": game_contract['abi'],
        "contract_address": deploy_contract(game_contract)
    }
    json.dump(data, outfile, indent=4, sort_keys=True)