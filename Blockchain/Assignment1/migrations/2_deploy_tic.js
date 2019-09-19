const TicTacToe = artifacts.require('tic');
const Moneys = artifacts.require('moneys');

module.exports = function(deployer, network, accounts){
    deployer.deploy(TicTacToe,{from:accounts[0]});
    deployer.deploy(Moneys);
}