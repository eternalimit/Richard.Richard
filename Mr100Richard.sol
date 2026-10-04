// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Mr100Richard {
    string public name = "Mr100Richard";
    string public symbol = "MR100";
    mapping(address => uint256) public balances;

    function mintMr100() public {
        balances[msg.sender] += 1;
    }
}
