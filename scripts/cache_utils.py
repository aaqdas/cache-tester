
import random
import math
import macros

def int_to_n_bits_bin(n,bits=16):
    """
    Converts an integer to a binary string without the '0b' prefix.
    
    Parameters:
    n (int): The integer to convert.

    Returns:
    str: The binary representation of the integer.
    """
    return format(n, f'0{int(bits)}b')

def bin_to_int(bin_str):
    """
    Converts a binary string to an integer.
    
    Parameters:
    bin_str (str): The binary string to convert.

    Returns:
    int: The integer representation of the binary string.
    """
    return int(bin_str, 2)

def pad_binary_strings(bin_str1, bin_str2):
    """
    Pads the shorter of two binary strings with leading zeros to make them the same length.
    
    Parameters:
    bin_str1 (str): The first binary string.
    bin_str2 (str): The second binary string.

    Returns:
    Tuple[str, str]: The padded binary strings.
    """
    max_len = max(len(bin_str1), len(bin_str2))
    bin_str1 = bin_str1.zfill(max_len)
    bin_str2 = bin_str2.zfill(max_len)
    return bin_str1, bin_str2

def and_binary_strings(bin_str1, bin_str2):
    """
    Computes the bitwise AND of two binary strings with padding.
    
    Parameters:
    bin_str1 (str): The first binary string.
    bin_str2 (str): The second binary string.

    Returns:
    str: The binary string resulting from the bitwise AND operation.
    """
    # Pad the binary strings to make them the same length
    bin_str1, bin_str2 = pad_binary_strings(bin_str1, bin_str2)
    
    # Perform the AND operation bit by bit
    result = ''.join('1' if bin_str1[i] == '1' and bin_str2[i] == '1' else '0' for i in range(len(bin_str1)))
    
    return result

def generate_random_numbers(n,bits):
    """
    Generates a list of n random numbers in the range 0 to 2^32-1.
    
    Parameters:
    n (int): The number of random numbers to generate.

    Returns:
    List[int]: A list containing n random numbers in the specified range.
    """
    return [int_to_n_bits_bin(random.randint(0, 2**bits - 1),bits) for _ in range(n)]


def compute_tag(physAddr,blocks,wordsPerBlock):
    """
    Computes Tag from Physical Address
    
    Parameters:
    physAddr        (binary string): Physical Address in a String of 0s and 1s
    blocks          (int)          : Number of blocks in cache 
    wordsPerBlock   (int)          : Number of words per block in cache
    bytesPerWord    (int)          : Number of bytes in each word

    Returns:
    (binary_string): Tag Bits in a String of 0s and 1s
    """
    return (physAddr[0:-int(math.log2(wordsPerBlock*macros.BYTES_PER_WORD)+math.log2(blocks))])



def compute_byte_offset(physAddr,wordsPerBlock):
    return bin_to_int(physAddr) & (macros.BYTES_PER_WORD*wordsPerBlock-1)
    # return bin_to_int(and_binary_strings(physAddr,int_to_n_bits_bin(macros.BYTES_PER_WORD*wordsPerBlock-1,macros.PHYSICAL_ADDRESS_SZ)))

def compute_block_idx(physAddr,blocks,wordsPerBlock):
    return (bin_to_int(physAddr) & ((blocks-1) * (macros.BYTES_PER_WORD * wordsPerBlock)))//(macros.BYTES_PER_WORD * wordsPerBlock)