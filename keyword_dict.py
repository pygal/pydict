import sys
import pickle
import shelve
from sys import argv



cmd_dict = shelve.open('file.txt', writeback=True)

script,key, value = argv
cmd_dict[key] = value
#cmd_dict[key].append(value)
print cmd_dict

#with open('file.txt', 'wb') as handle:
#     pickle.dump(cmd_dict, handle)

#with open('file.txt', 'rb') as handle:
#     b = pickle.loads(handle.read())

cmd_dict.close()

#print cmd_dict == b

