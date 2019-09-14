
pragma solidity >=0.4.24;

contract tic {
    
    uint8 games;
    uint8 cm;
    address p1;
    address p2;


    enum Board { Empty, X, O}
    Board[3][3] board;
    
    constructor() public payable {
        require(msg.value==1 ether);
        p1 = msg.sender;
        games=0;
        cm=0;
    }
    
    function getBalance() public view returns (uint256) {
        return address(this).balance;
    }
    
    function printPlayers() public view returns(address,address){
        return(p1,p2);
    }
    
    function turn() public view returns(address) {
        if(games == 0 || games == 1)
        {
            if(cm %2 ==0 )
            return p1;
            else
            return p2;
        }
        else if(games == 2 || games ==3)
        {
            if(cm%2==0)
            return p2;
            else
            return p1;
        }
    }
    
    function joinGame() public payable{
        require(p1!=0x0 && p1!= msg.sender);
        require( msg.value == 1 ether);
        p2 = msg.sender;
        
    }
    
    function startNewGame() public {
        cm=0;
        games+=1;
    }
    
    //Printing the board
    
    function printBoard() public view returns(string ) {
        
        return string(abi.encodePacked("\n",printrow(0),"\n",printrow(1),"\n",printrow(2)));
    }
    
    
    function printrow(uint8 y) public view returns(string)  {
        
        return string(abi.encodePacked(tostring(0,y),"|",tostring(1,y),"|",tostring(2,y)));
    }
    
    function tostring(uint8 x, uint8 y) public view returns(string)
    {
        //require(InBounds(x,y));
        if(board[x][y]==Board.X)
        {
            return "X";
        }
        if(board[x][y]==Board.O)
        {
            return "O";
        }
        if(board[x][y]==Board.Empty)
        {
            return " ";
        }
    }
    
    function Move(uint8 x, uint8 y) public returns(bool ,uint8 )
    {
       
        //require(cm<=9);
        require(InBounds(x,y));
        require(!over());
        require(turn()==msg.sender);
        
        if(board[x][y] != Board.Empty) {
            return (false,cm);
        }
        else {
            board[x][y] = player();
            cm+=1;
            return (true,cm);
        }
        
        
    }
    
    function InBounds(uint8 x, uint8 y) public pure returns(bool){
     
        return (x>=0 && x<3 && y>=0 && y<3);
        
        
    }
    
    function player() public view returns(Board)
    {
        if(getCurrAdd()==p1)
        {
            return Board.X;
        }
        if(getCurrAdd()==p2)
        {
            return Board.O;
        }
    }
    
    function getCurrAdd() public view returns(address) {
        return msg.sender;
    }
    
    function over() public returns(bool) {
        if(cm > 9 || Winner() != Board.Empty )
        {
            declareWinner();
            startNewGame();
            return true;
        }
            
        return false;
        
    }
    
    function declareWinner() public {
        if(Winner()==Board.X)
            p1.transfer(2 ether);
        if(Winner()==Board.O)
            p2.transfer(2 ether);
        if(Winner()==Board.Empty){
            p1.transfer(1 ether);
            p2.transfer(1 ether);
        }
    }
    
    function Winner() public view returns(Board) {
        
        for (uint8 i = 0; i < 3; i++) {
            if (board[i][0] == board[i][1] && board[i][1] == board[i][2] && board[i][0] != Board.Empty) {
                return board[i][0];
            }
        }
        
        for (uint8 j = 0; j < 3; j++) {
            if (board[0][j] == board[1][j] && board[1][j] == board[2][j] && board[0][j] != Board.Empty) {
                return board[0][j];
            }
        }
        
        if(board[0][0] == board[1][1] && board[1][1] == board[2][2] && board[0][0] != Board.Empty)
        {
            return board[0][0];
        }
        
        if(board[0][2] == board[1][1] && board[1][1] == board[2][0] && board[0][2] != Board.Empty)
        {
            return board[0][2];
        }
        
        return Board.Empty;
    }
   //games +=  1;
}

