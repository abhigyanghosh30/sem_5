const TicTacToe = artifacts.require('tic');
// var Web3 = require("../node_modules/web3/");
// web3 = new Web3(new Web3.providers.HttpProvider("http://localhost:9545"));

module.exports = function(deployer, network, accounts){
    deployer.deploy(TicTacToe,{from:accounts[0],value:web3.utils.toWei("1","ether")});
}