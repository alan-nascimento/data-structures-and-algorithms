from typing import Optional
import hashlib
import datetime


class Block:
    def __init__(self, timestamp: datetime.datetime, data: str, previous_hash: str):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.previous_block: Optional[Block] = None  # Reference to the previous block

    def calc_hash(self) -> str:
        sha = hashlib.sha256()
        hash_str = (
            str(self.timestamp) + str(self.data) + str(self.previous_hash)
        ).encode("utf-8")
        sha.update(hash_str)
        return sha.hexdigest()


class Blockchain:
    def __init__(self):
        self.head = None

    def add_block(self, data: str) -> None:
        if not self.head:
            self.head = Block(datetime.datetime.utcnow(), data, "0")
        else:
            new_block = Block(datetime.datetime.utcnow(), data, self.head.hash)
            new_block.previous_block = self.head
            self.head = new_block

    def print_blocks(self) -> None:
        current_block = self.head
        while current_block:
            print("Timestamp:", current_block.timestamp)
            print("Data:", current_block.data)
            print("Hash:", current_block.hash)
            print("Previous Hash:", current_block.previous_hash)
            print("\n")
            current_block = current_block.previous_block


# Test cases
if __name__ == "__main__":
    blockchain = Blockchain()

    # Test Case 1: Adding blocks to the blockchain
    blockchain.add_block("Block 0")
    blockchain.add_block("Block 1")
    blockchain.add_block("Block 2")

    # Test Case 2: Adding edge cases (e.g., empty or null values)
    blockchain.add_block("")  # Adding an empty block
    blockchain.add_block(None)  # Adding a block with null data

    # Test Case 3: Adding a very large value
    blockchain.add_block("This is a very large value" * 1000)

    # Print all blocks
    blockchain.print_blocks()

    # Asserts
    assert blockchain.head.data == "This is a very large value" * 1000
    assert blockchain.head.previous_block.data is None
    assert len(blockchain.head.previous_hash) == 64
