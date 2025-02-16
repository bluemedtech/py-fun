import hashlib
import time
from typing import List, Dict, Any

# Block class represents a single block in the blockchain
class Block:
    def __init__(self, index: int, previous_hash: str, timestamp: float, data: Dict[str, Any], nonce: int = 0):
        self.index = index  # Position of the block in the chain
        self.previous_hash = previous_hash  # Hash of the previous block
        self.timestamp = timestamp  # Time when the block was created
        self.data = data  # Data stored in the block (e.g., transactions)
        self.nonce = nonce  # A number used in mining to find a valid hash
        self.hash = self.calculate_hash()  # Hash of the current block

    # Calculate the hash of the block using SHA-256
    def calculate_hash(self) -> str:
        block_string = f"{self.index}{self.previous_hash}{self.timestamp}{self.data}{self.nonce}"
        return hashlib.sha256(block_string.encode()).hexdigest()

    # Mine the block by finding a hash that meets the difficulty criteria
    def mine_block(self, difficulty: int):
        target = "0" * difficulty  # The hash must start with a certain number of zeros
        while self.hash[:difficulty] != target:
            self.nonce += 1  # Increment the nonce
            self.hash = self.calculate_hash()  # Recalculate the hash
        print(f"Block mined: {self.hash}")


# Blockchain class represents the entire blockchain
class Blockchain:
    def __init__(self):
        self.chain: List[Block] = [self.create_genesis_block()]  # Initialize the chain with the genesis block
        self.difficulty = 4  # Difficulty level for mining (number of leading zeros required)
        self.pending_transactions: List[Dict[str, Any]] = []  # List of transactions waiting to be added to a block

    # Create the first block in the blockchain (genesis block)
    def create_genesis_block(self) -> Block:
        return Block(0, "0", time.time(), {"message": "Genesis Block"})

    # Get the latest block in the chain
    def get_latest_block(self) -> Block:
        return self.chain[-1]

    # Add a new block to the chain
    def add_block(self, new_block: Block):
        new_block.previous_hash = self.get_latest_block().hash  # Set the previous hash
        new_block.mine_block(self.difficulty)  # Mine the block
        self.chain.append(new_block)  # Add the block to the chain

    # Add a new transaction to the list of pending transactions
    def add_transaction(self, transaction: Dict[str, Any]):
        self.pending_transactions.append(transaction)

    # Mine pending transactions into a new block
    def mine_pending_transactions(self):
        new_block = Block(
            index=len(self.chain),
            previous_hash=self.get_latest_block().hash,
            timestamp=time.time(),
            data=self.pending_transactions,
        )
        self.add_block(new_block)
        self.pending_transactions = []  # Clear the pending transactions

    # Check if the blockchain is valid
    def is_chain_valid(self) -> bool:
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # Check if the current block's hash is correct
            if current_block.hash != current_block.calculate_hash():
                print("Invalid hash detected!")
                return False

            # Check if the previous hash matches
            if current_block.previous_hash != previous_block.hash:
                print("Invalid previous hash detected!")
                return False

        return True


# Create a new blockchain
brixcoin = Blockchain()

# Add some transactions
brixcoin.add_transaction({"from": "Alice", "to": "Bob", "amount": 50})
brixcoin.add_transaction({"from": "Bob", "to": "Charlie", "amount": 25})

# Mine the pending transactions into a new block
print("Mining block 1...")
brixcoin.mine_pending_transactions()

# Add more transactions
brixcoin.add_transaction({"from": "Charlie", "to": "Alice", "amount": 10})

# Mine another block
print("Mining block 2...")
brixcoin.mine_pending_transactions()

# Print the blockchain
print("\nBlockchain:")
for block in brixcoin.chain:
    print(f"Block {block.index} [Hash: {block.hash}, Previous Hash: {block.previous_hash}, Data: {block.data}]")

# Check if the blockchain is valid
print("\nIs blockchain valid?", brixcoin.is_chain_valid())