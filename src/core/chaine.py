import hashlib, json , datetime

from src.config.dir import Dir

class Blockchaine :
    def __init__(self):
        self.dir = Dir()
        self.chain = self.read_blockchain()
        self.create_block(proof = 1, previous_hash = '0')
        

    def read_blockchain(self):
        try:
            with open(self.dir.get_data_directory(), 'r') as file:
                return json.loads(file.read())
        except FileNotFoundError :
            return []
        except json.decoder.JSONDecodeError:
            return []

    def write_blockchain(self):
        with open(self.dir.get_data_directory(), 'w') as file:
            file.write(json.dumps(self.chain))
    
    def mine_block(self):
        previous_block = self.get_previous_block()
        previous_proof = previous_block['proof']
        proof = self.proof_of_work(previous_proof)
        previous_hash = self.hash(previous_block)
        block = self.create_block(proof, previous_hash)
        return block
    
    
    def create_block(self, proof, previous_hash):
        block = {'index': len(self.chain) + 1,
                 'timestamp': str(datetime.datetime.now()),
                 'proof': proof,
                 'previous_hash': previous_hash}
        self.chain.append(block)
        return block
    
    def get_previous_block(self):
        return self.chain[-1]
    
    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False
        while check_proof is False:
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] == '0000':
                check_proof = True
            else:
                new_proof += 1
        return new_proof
    
    def hash(self, block):
        encoded_block = json.dumps(block, sort_keys = True).encode()
        return hashlib.sha256(encoded_block).hexdigest()
    
    def is_chain_valid(self, chain):
        previous_block = chain[0]
        block_index = 1
        while block_index < len(chain):
            block = chain[block_index]
            if block['previous_hash'] != self.hash(previous_block):
                return False
            previous_proof = previous_block['proof']
            proof = block['proof']
            hash_operation = hashlib.sha256(str(proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] != '0000':
                return False
            previous_block = block
            block_index += 1
        return True
    