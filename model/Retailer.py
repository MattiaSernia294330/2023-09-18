from dataclasses import dataclass
@dataclass
class Retailer:
    code:int
    name:str
    def __hash__(self):
        return hash(self.code)