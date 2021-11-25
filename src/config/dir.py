
class Dir :
    
    def __init__(self) -> None:
        self.data = {
            "data_directory" : "data/blockchain.json"
        }

    def get_data_directory(self) -> str:
        return self.data["data_directory"]
     