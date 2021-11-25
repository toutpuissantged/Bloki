from chaine import Blockchaine
from unittest import TestCase, main

# teste de la class Blockchaine

class BlockChaineTests (TestCase) :
    
    def test_get_previous_block(self) :
        chaine = Blockchaine()
        self.assertEqual(chaine.get_previous_block(), chaine.chain[0])
    
    def test_create_block(self) :
        chaine = Blockchaine()
        self.assertEqual(chaine.create_block(1, '0'), {'index': 1, 'timestamp': 1547144734.935, 'proof': 1, 'previous_hash': '0', 'transactions': []})
    
    def test_hash(self) :
        chaine = Blockchaine()
        self.assertEqual(chaine.hash({'index': 1, 'timestamp': 1547144734.935, 'proof': 1, 'previous_hash': '0', 'transactions': []}), '0')
    
    def test_proof_of_work(self) :
        chaine = Blockchaine()
        self.assertEqual(chaine.proof_of_work(1), 2)
    
    def test_is_chain_valid(self) :
        chaine = Blockchaine()
        self.assertTrue(chaine.is_chain_valid(chaine.chain))
    
    def test_is_chain_valid_false(self) :
        chaine = Blockchaine()
        chaine.chain[1]['proof'] = 1
        self.assertFalse(chaine.is_chain_valid(chaine.chain))
    
    def test_is_chain_valid_false_2(self) :
        chaine = Blockchaine()

if __name__ == '__main__':
    main()