pragma solidity >= 0.4.24;

contract PDA{
    struct Player {
        bool vote;
        address delegate;
    }
    struct Proposal {
        uint voteCount;
    }
    
    Player player1;
    Player player2;
    
    constructor() public {
        
    }
    
    
    function getResult() public{
        
    }
}