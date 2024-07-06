import getopt, sys
import os
import math
import numpy as np
from cache_utils import *
from cache_gen_phys_addr import *
from cache_logger import *
import macros
# WRITE_PATH = "../init_files/"
# PHYSICAL_ADDRESS_SZ = 16
# BYTES_PER_WORD = 4
# def int_to_n_bits_bin(n,bits):
#     """
#     Converts an integer to a binary string without the '0b' prefix.
    
#     Parameters:
#     n (int): The integer to convert.

#     Returns:
#     str: The binary representation of the integer.
#     """
#     return format(n, f'0{bits}b')


# def generate_random_numbers(n,bits):
#     """
#     Generates a list of n random numbers in the range 0 to 2^32-1.
    
#     Parameters:
#     n (int): The number of random numbers to generate.

#     Returns:
#     List[int]: A list containing n random numbers in the specified range.
#     """
#     return [int_to_n_bits_bin(random.randint(0, 2**bits - 1),bits) for _ in range(n)]

def write_cache_to_file(filename,data):
    with open(f"{macros.WRITE_PATH}{filename}.bin",'w') as fd:
        for block in range(0,len(data[0][:])):
            for field in range(0,len(data)):
                fd.write(data[field][block])
            fd.write('\n')
        fd.close()



def cache_init(blocks,wordsPerBlock,associativity):
    if not os.path.isdir(macros.WRITE_PATH):
        os.mkdir(macros.WRITE_PATH)
    
    # Generates and Writes Physical Address To Files and Returns List of Physical Addresses in Binary String
    cache_phys_addr = write_phys_addr_to_file('phys_addr_buffer')
    # Computes Size of Cache Tag in Bits
    cacheTagSize= macros.PHYSICAL_ADDRESS_SZ-math.log2(wordsPerBlock*macros.BYTES_PER_WORD)-math.log2(blocks)
    cacheData = []
    for ways in range(0,associativity):   
        cacheWay = []
        cacheWay.append(generate_random_numbers(blocks,1))             #Cache Valid Bits
        cacheWay.append(generate_random_numbers(blocks,cacheTagSize))  #Cache Tags
        for words in range(0,wordsPerBlock):
            cacheWay.append(generate_random_numbers(blocks,32))
        write_cache_to_file(f"way{ways}",cacheWay)
        cacheData.append(cacheWay)
        print(f"Cache Size (Ways,Fields,Blocks){np.array(cacheData).shape}")

    cache_computed_tag         = [compute_tag(addr,blocks,wordsPerBlock) for addr in cache_phys_addr]
    cache_computed_byte_offset = [compute_byte_offset(addr,wordsPerBlock) for addr in cache_phys_addr]
    cache_computed_block_idx = [compute_block_idx(addr,blocks,wordsPerBlock) for addr in cache_phys_addr]
    log_accesses('access',cacheData,cache_phys_addr,cache_computed_tag,cache_computed_block_idx,cache_computed_byte_offset,associativity)
    #print(np.array(cacheWay).shape)
    # print(cacheWay[0][0])     
    # print(len(cacheWay[0]))
                   

if __name__=='__main__':
    argumentList = sys.argv[1:]

    options = "hb:w:a:"

    long_options = ["help", "blocks", "words-per-block", "associativity"]

    try:
        # Parsing argument
        arguments, values = getopt.getopt(argumentList, options, long_options)
        #print(arguments)
        #print(values)
        # checking each argument
        for currentArgument, currentValue in arguments:

            if currentArgument in ("-h", "--Help"):
                print ("""
-h   --help              Displays Help Output
-b   --blocks            Input for Total Required Blocks/Lines
-w   --words-per-block   Input for Total Words Per Block/Line
-a   --associativity     Input for Associativity of Set""")
            
            elif currentArgument in ("-b", "--blocks"):
                cacheBlocks = int(currentValue)
                # print ("Total Blocks:", currentValue)

            elif currentArgument in ("-w", "--words-per-block"):
               cacheWordsPerBlock = int(currentValue)
            #    print ("Words Per Block:", currentValue)
                
            elif currentArgument in ("-a", "--associativity"):
                cacheAssociativity = int(currentValue)
                # print ("Associativity Per Block:", currentValue)
            
    except getopt.error as err:
        # output error, and return with an error code
        print (str(err))

    cache_init(cacheBlocks,cacheWordsPerBlock,cacheAssociativity)