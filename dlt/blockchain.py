# blockchain.py
import hashlib
import time


class Token:
    def __init__(self, sender, receiver, value):
        self.sender = sender
        self.receiver = receiver
        self.value = value

    def __str__(self):
        return f"Sender: {self.sender}, Receiver: {self.receiver}, Value: {self.value}"


class Block:
    def get_block_data(self):
        return {
            'index': self.index,
            'timestamp': self.timestamp,
            'data': self.data,
            'hash': self.hash,
            'previous_hash': self.previous_hash,
            'tokens': self.tokens
        }

    def __init__(self, index, data, previous_hash):
        self.index = index
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.tokens = []
        self.hash = self.compute_hash()

    def add_token(self, token):
        self.tokens.append(token)

    def compute_hash(self):
        sha = hashlib.sha256()
        block_header = str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash)
        sha.update(block_header.encode())
        return sha.hexdigest()


class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = Block(0, "Genesis Block", "0")
        self.chain.append(genesis_block)

    def get_last_block(self):
        return self.chain[-1] if self.chain else None

    def add_block(self, data):
        last_block = self.get_last_block()
        new_block = Block(last_block.index + 1, data, last_block.hash)
        self.chain.append(new_block)

    def is_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.hash != current_block.compute_hash():
                return False

            if current_block.previous_hash != previous_block.hash:
                return False

        return True

    def add_tokens_to_block(self, block, tokens):
        for token in tokens:
            block.add_token(token)

    def display_chain(self):
        for block in self.chain:
            print(f"Block {block.index}:")
            print(f"Timestamp: {block.timestamp}")
            print(f"Data: {block.data}")
            print(f"Hash: {block.hash}")
            print(f"Previous Hash: {block.previous_hash}")
            print("Tokens:")
            for token in block.tokens:
                print(f"Sender: {token.sender}, Receiver: {token.receiver}, Value: {token.value}")
            print("\n")