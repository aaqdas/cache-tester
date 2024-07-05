import getopt, sys
import os
import numpy as np
import random

WRITE_PATH = "../init_files/"

def int_to_bin(n):
    """
    Converts an integer to a binary string without the '0b' prefix.
    
    Parameters:
    n (int): The integer to convert.

    Returns:
    str: The binary representation of the integer.
    """
    return format(n, '032b')


def generate_random_numbers(n):
    """
    Generates a list of n random numbers in the range 0 to 2^32-1.
    
    Parameters:
    n (int): The number of random numbers to generate.

    Returns:
    List[int]: A list containing n random numbers in the specified range.
    """
    return [int_to_bin(random.randint(0, 2**32 - 1)) for _ in range(n)]

def write_cache_to_file(filename,data):
    with open(f"{WRITE_PATH}{filename}.bin",'w') as fd:
        for block in range(0,len(data[0][:])):
            for field in range(0,len(data)):
                fd.write(data[field][block])
            fd.write('\n')




def cache_init(blocks,wordsPerBlock,associativity,cache_type='set'):
    if not os.path.isdir(WRITE_PATH):
        os.mkdir(WRITE_PATH)
    
    for ways in range(0,associativity):   
        cacheData = []
        for words in range(0,wordsPerBlock):
            cacheData.append(generate_random_numbers(blocks))
        write_cache_to_file(f"way{ways}",cacheData)
        
    #print(np.array(cacheData).shape)
    # print(cacheData[0][0])     
    # print(len(cacheData[0]))
                   

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