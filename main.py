from src.core.chaine import Blockchaine 
from time import time

Chaine = Blockchaine()

for i in range(100) :
    t1 = time() 
    block = Chaine.get_previous_block()
    new_prof = Chaine.proof_of_work(block['proof'])
    new_block = Chaine.create_block(new_prof, Chaine.hash(block))
    t2 = time()
    print(f'{i} : {t2-t1}')

print(Chaine.is_chain_valid(Chaine.chain))
