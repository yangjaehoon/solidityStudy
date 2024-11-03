// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract MultiSendPolygon {

    address public owner;

    constructor() {
        owner = msg.sender;
    }

    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function.");
        _;
    }

    // 다중 전송 함수
    function multiSend(address[] calldata recipients, uint256[] calldata amounts) external payable onlyOwner {
        require(recipients.length == amounts.length, "Recipients and amounts length mismatch");

        uint256 totalAmount = 0;

        // 총 전송 금액 계산
        for (uint256 i = 0; i < amounts.length; i++) {
            totalAmount += amounts[i];
        }
        
        require(msg.value == totalAmount, "Insufficient total amount provided");

        // 각 수신자에게 MATIC 전송
        for (uint256 i = 0; i < recipients.length; i++) {
            (bool success, ) = recipients[i].call{value: amounts[i]}("");
            require(success, "Transfer failed for one of the recipients");
        }
    }

    // 컨트랙트 잔액 조회
    function getBalance() external view returns (uint256) {
        return address(this).balance;
    }

    // 컨트랙트 종료 및 잔액 회수
    function withdraw() external onlyOwner {
        payable(owner).transfer(address(this).balance);
    }
}
