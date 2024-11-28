#  Git repository test

This is a test Readme Markdown file for creating a git commit.

<<<<<<< HEAD
This is the dev branch before.
=======
Nihao :)
>>>>>>> 017c90557c77c0f174beb6102bd9b0e315791d90

```solidity
// Red

/// SPDX-License-Identifier: MIT
pragma solidity ^0.8.18;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract AuroraToken2024 is ERC20{
    address public issuer;

    mapping(address => uint256) public consecutive_wins;
    uint256 last_hash;
    uint256 FACTOR = 57896044618658097711785492504343953926634992332820282019728792003956564819968;

    constructor() ERC20("AuroraToken2024", "ATK2024"){
        _mint(msg.sender,1000000*10**18);
        issuer = msg.sender;
    }

    modifier onlyIssuer{
        require(msg.sender==issuer,"Caller is not issuer.");
        _;
    }

    function Fundings() public{
        require(balanceOf(msg.sender) < 1*10**17,"You can still flip the coin.");
        require(balanceOf(issuer) > 1*10**18,"Not enough ATK2024 supplies, plz contact the issuer.");
        _approve(issuer, msg.sender, 1*10**18);
        transferFrom(issuer,msg.sender,1*10**18);
    }

    function softMint(uint256 _amount) public onlyIssuer{
        _mint(msg.sender,_amount*10**18);
    }

    function CoinFlipping(bool _guess) public returns(bool){
        require(balanceOf(msg.sender) >= 1*10**17,"Insufficient balance.");
        transfer(issuer, 1*10**17);
        uint256 guessing_value = uint256(keccak256(abi.encodePacked(msg.sender,blockhash(block.number - 1))));
        
        if(last_hash == guessing_value){
            revert();
        }

        last_hash=guessing_value;
        uint256 coin_flip_result = guessing_value / FACTOR;
        bool side = coin_flip_result == 1 ? true : false;

        if(side==_guess){
            consecutive_wins[msg.sender]++;
            _approve(issuer, msg.sender, 11*10**17);
            transferFrom(issuer,msg.sender,11*10**17);
            return true;
        }
        else{
            consecutive_wins[msg.sender] = 0;
            return false;
        }
    }

    function Minimum_Guarantee() public{
        require(balanceOf(msg.sender) >= 50*10**18,"You don't have enough ATK2024s to skip the level.");
        transfer(issuer, 50*10**18);
        consecutive_wins[msg.sender]=10;
    }

    function Verification(address _verifier) public view returns(bool){
        return consecutive_wins[_verifier] >= 10 ? true : false;
    }
}
```

