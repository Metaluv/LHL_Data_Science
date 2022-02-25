from collections import ChainMap

dict1 = { 'a' : 1, 'b' : 2 }
dict2 = { 'c' : 3, 'b' : 4 }
chain_map = ChainMap(dict1, dict2)
print(list(chain_map.keys()))
print(list(chain_map.values()))