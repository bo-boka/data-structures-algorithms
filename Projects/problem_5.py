
import hashlib
from datetime import datetime


class Block:

    def __init__(self, timestamp, data, previous_hash=None):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.prev = None

    def calc_hash(self):

        sha = hashlib.sha256()

        sha.update(self.timestamp.encode('utf-8'))
        sha.update(self.data.encode('utf-8'))
        if self.previous_hash:
            sha.update(self.previous_hash.encode('utf-8'))

        return sha.hexdigest()


class Blockchain:

    def __init__(self):
        self.tail = None

    def add_block(self, data):

        timestamp = datetime.utcnow().strftime("%m/%d/%Y, %H:%M:%S:%f")
        if self.tail is None:
            self.tail = Block(timestamp, data)
            return

        previous_hash = self.tail.hash
        new_block = Block(timestamp, data, previous_hash)
        new_block.prev = self.tail
        self.tail = new_block

    def convert_blockchain_to_list(self):

        a_list = list()

        if self.tail is None:
            return []

        block = self.tail

        while block:
            a_list.append(block.hash)
            block = block.prev

        return a_list


# Test case 1
print('======== Test 1: Happy Path')

bc = Blockchain()
bc.add_block('first data')
bc.add_block('second data')
bc.add_block('third data')
print(bc.convert_blockchain_to_list())      # list of 3 block hashes


# Test case 2
print('======== Test 2: one block')

bc = Blockchain()
bc.add_block('first data')
print(bc.convert_blockchain_to_list())      # list of 1 block hash


# Test case 3
print('======== Test 3: empty blockchain')

bc = Blockchain()
print(bc.convert_blockchain_to_list())      # empty list
