
var TicTacToe = artifacts.require('tic');
var Moneys = artifacts.require('moneys');

contract('tic',function(accounts){

    // Since we are using accounts[0] as the owner/deployer of the contract, so we exclude him from the testing

    it("should deploy the contract",()=>{
        return TicTacToe.deployed().then(async(instance)=>{
            var owner_ip;
            await instance.owner.call().then((data)=>{owner_ip = data});
            assert.equal(accounts[0],owner_ip);
            return instance.getBalance();
        })
        .then((balance)=>{
            assert.equal(balance.valueOf(), web3.utils.toWei("0","ether"), "Ether was paid. Contract should have zero ether before players join");
        });
    });

    it("Same player cannot join twice",async function(){
        return TicTacToe.deployed().then(async (instance)=>{
            try{
                await instance.joinGame({from:accounts[1],value:web3.utils.toWei("4","ether")});
                // trying to make accounts[1] join again
                await instance.joinGame({from:accounts[1],value:web3.utils.toWei("4","ether")});
            }
            catch(err){
                assert(true);
            }
        });
    });

    it("Player cannot join if he doesn't have enough money",async ()=>{
        return TicTacToe.deployed()
        .then(async (instance)=>{
            
            // making accounts[3] broke to check if he can afford to pay
            var balance;
            await web3.eth.getBalance(accounts[3]).then((data)=>{balance=data});
            var money_instance;
            await Moneys.deployed().then((instance)=>{money_instance = instance});
            var eth3 =  (await web3.utils.toWei("3","ether"));
            // console.log("initial balance",balance);
            balance = parseInt(balance);
            // console.log(balance > eth3);
            if(balance > eth3){
                balance -= parseInt(await web3.utils.toWei("2" ,"ether"));
            }
            else{
                balance = 1;
            }
            await money_instance.transferETH(accounts[4],{from:accounts[3],value:balance});            
            await web3.eth.getBalance(accounts[3]).then((data)=>{balance=data});
            return instance;
        })
        .then(async(instance)=>{
            try {
                await instance.joinGame({from:accounts[3],value:web3.utils.toWei("4","ether")});
                assert(false,"was able to make transaction without paying");
            }
            catch(err){
                assert(true,"cannot make move without full payment");
            }
        })
    });

    it("Otherwise players should be able to join",()=>{
        return TicTacToe.deployed()
        .then(async function(instance){
            await instance.joinGame({from:accounts[2],value:web3.utils.toWei("4","ether")});
            return instance.getBalance();
        })
        .then(async function(balance){
            assert.equal(balance,parseInt(await web3.utils.toWei("8","ether")));
        });
        
    });

    it("Unit test for turn taking function",()=>{
        return TicTacToe.deployed()
        .then(async function(instance){
            var a =[];
            await instance.turn().then((data)=>{a[0]=data});
            await instance.printPlayers().then((data)=>{a[1]=data['0']});
            return a;
        })
        .then((a)=>{
            assert.equal(a[0],a[1]);
        });
    });

    it("unit testing for InBounds",async function(){
        return TicTacToe.deployed()
        .then(async function(instance){
            var a = [];
            await instance.InBounds(0,0).then((data)=>{a.push(data)});
            await instance.InBounds(0,1).then((data)=>{a.push(data)});
            await instance.InBounds(0,2).then((data)=>{a.push(data)});
            await instance.InBounds(0,3).then((data)=>{a.push(data)});
            await instance.InBounds(1,0).then((data)=>{a.push(data)});
            await instance.InBounds(1,1).then((data)=>{a.push(data)});
            await instance.InBounds(1,2).then((data)=>{a.push(data)});
            await instance.InBounds(1,3).then((data)=>{a.push(data)});
            await instance.InBounds(2,0).then((data)=>{a.push(data)});
            await instance.InBounds(2,1).then((data)=>{a.push(data)});
            await instance.InBounds(2,2).then((data)=>{a.push(data)});
            await instance.InBounds(2,3).then((data)=>{a.push(data)});
            await instance.InBounds(3,0).then((data)=>{a.push(data)});
            await instance.InBounds(3,1).then((data)=>{a.push(data)});
            await instance.InBounds(3,2).then((data)=>{a.push(data)});
            await instance.InBounds(3,3).then((data)=>{a.push(data)});
            await instance.InBounds(-1,0).then((data)=>{a.push(data)});
            await instance.InBounds(-1,1).then((data)=>{a.push(data)});
            await instance.InBounds(-1,2).then((data)=>{a.push(data)});
            await instance.InBounds(-1,3).then((data)=>{a.push(data)});
            return a;
        }).then((resp)=>{
            truths = [ true,true,true,false,true,true,true,false,true,true,true,false,false,false,false,false,false,false,false,false];
            for(var i=0;i<=truths.length;i++)
            {
                assert.isTrue(truths[i]==resp[i]);
            }
        });
    });

    it("Players should be able to Move",()=>{
        return TicTacToe.deployed()
        .then(async function(instance){
            await instance.Move(0,0,{from:accounts[1]});
            await instance.Move(0,1,{from:accounts[2]});
            let a = [];
            await instance.tostring(0,0).then((data)=>{return a[0]=data;});
            await instance.tostring(0,1).then((data)=>{return a[1]=data;});
            return a;
        })
        .then(async function(values){
            // console.log(values);
            assert.equal(values[0].valueOf(),"X");
            assert.equal(values[1].valueOf(),"O");
        });
        
    });

    it("Payers cannot move out of turn",async ()=>{
        return TicTacToe.deployed()
        .then(async function(instance){
            try{
                await instance.Move(1,1,{from:accounts[2]});
            }
            catch(err)
            {
                assert(true);
            }
        });
    });

    it("Players should be able to Win",()=>{
        return TicTacToe.deployed()
        .then(async function(instance){
            await instance.Move(1,0,{from:accounts[1]});
            await instance.Move(1,1,{from:accounts[2]});
            await instance.Move(2,0,{from:accounts[1]});
            return instance.over();
        })
        .then(async function(values){
            assert.isTrue(values);
        }); 
    });

    it("Anyone should be able to start new game when the old game is over", ()=>{
        return TicTacToe.deployed()
        .then(async function(instance){
            await instance.startNewGame();
            var a=[];
            await instance.games.call().then((data)=>{a[0]=data});
            await instance.cm.call().then((data)=>{a[1]=data});
            return a;
        }).then((a)=>{
            assert.equal(a[0].valueOf(),1);
            assert.equal(a[1].valueOf(),0);
        });
    });

    it("After 4 games there should be a single winner",()=>{
        return TicTacToe.deployed()
        .then(async function(instance){
            // make player 1 win again (2 wins for him)
            var winner;
            var a=[];
            await instance.Move(0,0,{from:accounts[1]});
            await instance.Move(0,1,{from:accounts[2]});
            await instance.Move(1,0,{from:accounts[1]});
            await instance.Move(1,1,{from:accounts[2]});
            await instance.Move(2,0,{from:accounts[1]});
            await instance.Winner().then((data)=>{winner=data});
            assert.equal(winner,1);
            
            await instance.startNewGame();
            await instance.games.call().then((data)=>{a[0]=data});
            await instance.cm.call().then((data)=>{a[1]=data});
            assert.equal(a[0].valueOf(),2);
            assert.equal(a[1].valueOf(),0);

            //make player 1 win again (3 wins for him now)
            await instance.PlayerMoves(1,{from:accounts[2]});
            await instance.PlayerMoves(2,{from:accounts[1]});
            await instance.PlayerMoves(3,{from:accounts[2]});
            await instance.PlayerMoves(4,{from:accounts[1]});
            await instance.PlayerMoves(5,{from:accounts[2]});
            await instance.PlayerMoves(7,{from:accounts[1]});
            await instance.PlayerMoves(6,{from:accounts[2]});
            await instance.PlayerMoves(9,{from:accounts[1]});            
            await instance.PlayerMoves(8,{from:accounts[2]});
            await instance.Winner().then((data)=>{winner=data});
            assert.equal(winner,0);
            // console.log(winner);

            await instance.startNewGame();
            //make player 2 win now
            await instance.Move(0,0,{from:accounts[2]});
            await instance.Move(0,1,{from:accounts[1]});
            await instance.Move(1,0,{from:accounts[2]});
            await instance.Move(1,1,{from:accounts[1]});
            await instance.Move(2,0,{from:accounts[2]});
            await instance.Winner().then((data)=>{winner=data});
            assert.equal(winner,2);

            var win_add;
            await instance.FinalWinner().then((resp)=>{win_add=resp});
            assert.equal(win_add,accounts[1]);
        });
    });
});