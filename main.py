from src.core.chaine import Blockchaine 
from time import time
import json
from src.config.dir import Dir

class Main : 
    def __init__(self) -> None:
        self.data_directory = Dir().get_data_directory()
        self.blockchain = Blockchaine()
    
    def run(self) -> None:
        ti = time()
        for i in range(10):
            t1 = time()
            block =  self.blockchain.get_previous_block()
            print(block)
            new_prof = self.blockchain.proof_of_work(block['proof'])
            self.blockchain.create_block(new_prof, self.blockchain.hash(block))
            t2 = time()
            print(f'{i} : {t2-t1}')
        self.write_blockchain()
        print(self.blockchain.is_chain_valid(self.blockchain.chain))


    def write_blockchain(self) -> None:
        self.blockchain.write_blockchain()
    

if __name__ == '__main__':
    Main().run()