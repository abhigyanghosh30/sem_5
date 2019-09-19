pragma solidity >= 0.4.24;

contract moneys {
    uint256 balance;
    constructor () public {
        balance = 0;
    }

    function transferETH(address recipient) public payable{
        recipient.transfer(msg.value);
    }

}