
import hashlib
from datetime import datetime


class Block:

    def __init__(self, timestamp, data, previous_hash=0):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def calc_hash(self):

        sha = hashlib.sha256()

        timestamp_hash_str = self.timestamp.encode('utf-8')
        data_hash_str = self.data.encode('utf-8')
        if self.previous_hash:
            previous_hash_str = self.timestamp.encode('utf-8')
            sha.update(previous_hash_str)

        sha.update(timestamp_hash_str)
        sha.update(data_hash_str)

        return sha.hexdigest()


class Blockchain:

    def __init__(self):
        self.tail = None

    def add_block(self, data):

        timestamp = datetime.now().strftime("%m/%d/%Y, %H:%M:%S:%f")
        print(f'timestamp1: {timestamp}')
        if self.tail is None:
            self.tail = Block(timestamp, data)
            return

        previous_hash = self.tail.hash
        self.tail = Block(timestamp, data, previous_hash)


bc = Blockchain()
bc.add_block('first data')
bc.add_block('second data')
