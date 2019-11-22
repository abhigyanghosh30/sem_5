
var TicTacToe = artifacts.require('tic');

advanceTime = (time) => {
    return new Promise((resolve, reject) => {
        web3.currentProvider.send({
            jsonrpc: "2.0",
            method: "evm_increaseTime",
            params: [time],
            id: new Date().getTime()
        }, (err, result) => {
            if (err) { return reject(err); }
            return resolve(result);
        });
    });
}
contract('tic',function(accounts){
    it("Timeout checks",function(){
        return TicTacToe.deployed()
        .then(async (instance)=>{
            await instance.joinGame({from:accounts[5],value:web3.utils.toWei("4","ether")});
            await instance.joinGame({from:accounts[6],value:web3.utils.toWei("4","ether")});
            await instance.PlayerMoves(2,{from:accounts[5]});
            await advanceTime(7000);
            var init_bal = []
            await web3.eth.getBalance(accounts[5]).then((data)=>{init_bal[0]=data});
            await web3.eth.getBalance(accounts[6]).then((data)=>{init_bal[1]=data});
            
            await instance.claimTimeout();
            var final_bal = [];
            await web3.eth.getBalance(accounts[5]).then((data)=>{final_bal[0]=data});
            await web3.eth.getBalance(accounts[6]).then((data)=>{final_bal[1]=data});

            //since account[6] was late to reply, account[5] gets all the contract balance which is 8 eth
            assert.equal(parseFloat(final_bal[0])-parseFloat(init_bal[0]),(await web3.utils.toWei("8","ether")));
            assert.equal(parseFloat(final_bal[1])-parseFloat(init_bal[1]),0);
        })
    });
});

