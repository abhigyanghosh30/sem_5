pragma solidity >=0.4.24;

contract Tic {
    
    uint8 public games;
    uint8 public cm;
    address p1;
    address p2;
    uint8 p1_wins;
    uint8 p2_wins;
    address owner;
    uint public timecounter;

    enum Board { Empty, X, O}
    Board[3][3] board;
    
    constructor() public  {
        // require(msg.value==1 ether);
        // p1 = msg.sender;
        
        owner=msg.sender;
        p1_wins=0;
        p2_wins=0;
        games=0;
        cm=0;
        for(uint8 i=0;i<3;i++)
        {
            for(uint8 j=0;j<3;j++)
            {
                board[i][j]=Board.Empty;
            }
        }
        
    }

    function getCurrentTime() public view returns(uint){
        return now;
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
        require(owner!= msg.sender);
        require( msg.value == 4 ether);
        require(cm==0);
        if(p1==address(0x0))
            p1 = msg.sender;
        else if(p2==address(0x0))
        {
            require(p1!=msg.sender);
            p2 = msg.sender;
            timecounter = now + 10 minutes;
        }
    }
    
    function startNewGame() public {
        require(over());
        require(games<3);
        cm=0;
        games+=1;
        //owner=0x0;
        for(uint8 i=0;i<3;i++)
        {
            
            for(uint8 j=0;j<3;j++)
            {
                board[i][j]=Board.Empty;
            }
        }
        timecounter = now + 10 minutes;
        
    }
    
    //Printing the board
    
    function printBoard() public view returns(string){
        
        return string(abi.encodePacked("\n",printrow(0),"\n",printrow(1),"\n",printrow(2)));
    }   
    
    
    function printrow(uint8 y) public view returns(string memory _row)  {
        
        return string(abi.encodePacked(tostring(y,0)," | ",tostring(y,1)," | ",tostring(y,2)));
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
    
    function PlayerMoves(uint8 m) public {
        require(m<10 &&  m>0);
        if(m<=3)
        {
            Move(0,m-1);
        }
        else if(m > 3 && m<=6)
        {
            Move(1,m-4);
        }
        else
        {
            Move(2,m-7);
        }
    }
    
    function Move(uint8 x, uint8 y) public
    {
        require(cm<9);
        require(InBounds(x,y));
        require(!over());
        require(turn()==msg.sender);
        require(timecounter - now > 0);
        require(board[x][y]==Board.Empty);
        // require(!over());
        board[x][y] = player();
        cm+=1;
        timecounter = now + 10 minutes;
        
        if(over())
            declareWinner();

        //return (true,cm);
    
        
    }
    
    function claimTimeout() public{
        require(now > timecounter);
        if(turn()==p1){
            p2.transfer(address(this).balance);
        }
        if(turn()==p2){
            p1.transfer(address(this).balance);
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
    
    function over() public view returns(bool) {
        if(cm == 9 || Winner() != Board.Empty )
        {
            return true;
        }
            
        return false;
        
    }
    
    function declareWinner() public {
        if(Winner()==Board.X){
            p1_wins+=1;
            p1.transfer(2 ether);
        }
        if(Winner()==Board.O){
            p2_wins+=1;
            p2.transfer(2 ether);
        }
        if(Winner()==Board.Empty){
            owner.transfer(1 ether);
            owner.transfer(1 ether);
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
   function FinalWinner() public view returns(address) {
       require(games==3);
       if(p1_wins > p2_wins)
       return p1;
       else if(p2_wins > p1_wins)
       return p2;
       else
       return owner;
   }
}
