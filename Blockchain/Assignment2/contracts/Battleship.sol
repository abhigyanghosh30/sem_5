pragma solidity >=0.4.0 <0.7.0;


contract Battleship{
    
    address player1;
    address player2;
    enum SquareState {Empty, X, O}
    SquareState[10][10] board_1;
    SquareState[10][10] board_2;
    SquareState[10][10] board_guess_1; // Stores guesses made by player 1
    SquareState[10][10] board_guess_2; // Stores guesses made by player 2
    uint public timelock;
    
    constructor() public payable {
        player1 = msg.sender;
    }
    
    function joinGame() public payable{
        require(msg.sender!=player1);
        require(msg.value==address(this).balance);
        player2 = msg.sender;
    }
    function getAddress() public view returns(address,address){
        return (player1,player2);
    }
    
    function initialize_board(SquareState[][] _board_state) public memory{
        if(msg.sender==player1){
            require(isEmpty(board_1));
            
        }
        if(msg.sender==player2){
            require(isEmpty(board_2));
        }
    }
}