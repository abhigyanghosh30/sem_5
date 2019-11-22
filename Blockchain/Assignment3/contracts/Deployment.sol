pragma solidity >=0.4.24;
import './TicTacToe.sol';


contract DeployTic {
    address [] public deployedContracts;

    address public owner;
    constructor() public{
        owner = msg.sender;
    }

    function createGames() public returns(address){
        require(msg.sender == owner);

        address newContract = new Tic();
        deployedContracts.push(newContract);
        return newContract;

    }
}