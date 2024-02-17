# Explanation for Blockchain Implementation

## Data Structure Choice:

In this implementation, a linked list structure is chosen to represent the blockchain. Each block in the blockchain is represented by a node in the linked list. This choice is made because a linked list allows for efficient insertion of new blocks at the head, which corresponds to the most recent block in the blockchain. Additionally, linked lists provide easy traversal from the most recent block to the genesis block (the first block) by following the pointers to the previous blocks. This structure suits the append-only nature of blockchains where new blocks are added sequentially.

## Time Efficiency:

- Adding a new block to the blockchain has a time complexity of O(1). This is because the new block is always added at the head of the linked list, which can be done in constant time.
- Traversing the blockchain to print all blocks has a time complexity of O(n), where n is the number of blocks in the blockchain. This is because we need to iterate through each block in the linked list to print its information.

## Space Efficiency:

- The space complexity of the blockchain implementation is O(n), where n is the number of blocks in the blockchain. This is because each block in the blockchain requires memory to store its timestamp, data, hash, and a reference to the previous block. As the number of blocks grows, the memory used by the blockchain also grows linearly.
