pragma solidity ^0.4.24;

contract Battleship{
    
    address player1;
    address player2;
    enum SquareState {Empty, X, O}
    bytes32 [10][10] board_1;
    bytes32 [10][10] board_2;
    SquareState[10][10] board_guess_1; // Stores guesses made by player 1
    SquareState[10][10] board_guess_2; // Stores guesses made by player 2
    address turn;
    uint public timelock;
    
    constructor() public payable {
        player1 = msg.sender;
    }
    
    function isEmpty(bytes32[10][10] _board) public pure returns(bool){
        for(uint8 i=0;i<10;i++){
            for(uint8 j=0;j<10;j++){
                if(_board[i][j]!=bytes32(""))
                {
                    return false;
                }
            }
        }
        return true;
    }
    
    function joinGame() public payable{
        require(msg.sender!=player1);
        require(msg.value==address(this).balance);
        player2 = msg.sender;
        turn = player1;
        timelock = now;
    }
    function getAddress() public view returns(address,address){
        return (player1,player2);
    }
    
    function tostring(SquareState state) public pure returns(string)
    {
        if(SquareState.X == state){
            return "X";
        }
        if(SquareState.O == state){
            return "O";
        }
        if(SquareState.Empty == state){
            return " ";
        }
        //require(InBounds(x,y));

    }
    
    function initialize_board(SquareState[10][10] _board,string _salt) public view {
        if(msg.sender==player1){
            require(isEmpty(board_1));
            for(uint8 i=0;i<10;i++){
                for(uint8 j=0;j<10;j++){
                    keccak256(abi.encodePacked(tostring(_board[i][j]),_salt));
                }
            }
            
        }
        if(msg.sender==player2){
            require(isEmpty(board_2));
        }
    }
    
    
    
    function commit_move(uint8 x, uint8 y) public {
        if(msg.sender==player1){
            board_guess_1[x][y] = SquareState.O;  
        }
    }
    
    function reveal_move(uint8 x, uint8 y,string _salt) public view returns(bool){
        if(msg.sender==player1){
            return board_1[x][y] == keccak256(abi.encodePacked(tostring(board_guess_2[x][y]),_salt));
        }
        if(msg.sender==player2){
            return board_2[x][y] == keccak256(abi.encodePacked(tostring(board_guess_1[x][y]),_salt));
        }
    }
    
    // function to redeem ethers on timeout
    function claimTimeout() public {
        require(now > timelock);
        if(turn==player1){
            player2.transfer(address(this).balance);
        }
        if(turn==player2){
            player1.transfer(address(this).balance);
        }
    }
}