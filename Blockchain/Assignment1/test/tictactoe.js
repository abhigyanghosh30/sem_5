var TicTacToe = artifacts.require('tic');

contract('tic',function(accounts){
    it("should deploy the contract",()=>{
        return TicTacToe.deployed().then((instance)=>{
            return instance.getBalance();
        }).then((balance)=>{
            assert.equal(balance.valueOf(), web3.utils.toWei("1","ether"), "1 ether wasnot paid");
        });
    });
});