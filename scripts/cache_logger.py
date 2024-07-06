import macros
from cache_utils import *

def log_accesses(filename,cache,physAddr,tags,blockIdx,byteOffset,numberOfWays):
    """
    Parameters:

    cache(list) : Complete Cache with Multiple Ways

    """
    TAG_FIELD = 1
    VALID_FIELD = 0
    hit = 0
    with open(f"{macros.WRITE_PATH}{filename}.log",'w') as fd:
        for test_case in range(0,len(physAddr)):
            for way in range(0,numberOfWays):
                if(cache[way][TAG_FIELD][blockIdx[test_case]] == tags[test_case] and cache[way][VALID_FIELD][blockIdx[test_case]] == 1):
                    hit = 1
                    fd.write(f"HIT! ; PA: {bin_to_int(physAddr[test_case])} ; Accessed Data: {cache[way][2+byteOffset][blockIdx[test_case]]}\n")
                    break
            if not hit: fd.write(f"MISS! ; PA: {bin_to_int(physAddr[test_case])} ; Accessed Data: 0\n")
                 
             
    
    fd.close()
                

