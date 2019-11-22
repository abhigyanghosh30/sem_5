const TicTacToe = artifacts.require('Tic');
const Moneys = artifacts.require('moneys');

module.exports = function(deployer, network, accounts){
    deployer.deploy(TicTacToe,{from:accounts[0]});
    deployer.deploy(Moneys);
}