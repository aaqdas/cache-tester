from cache_utils import *
import macros
def cache_gen_phys_addr(numTestCases):
    return generate_random_numbers(numTestCases,macros.PHYSICAL_ADDRESS_SZ)

def write_phys_addr_to_file(filename,data=[]):
    if not data:
        phys_addr_data = cache_gen_phys_addr(macros.TEST_CASES)
    with open(f"{macros.WRITE_PATH}{filename}.bin",'w') as fd:
        for lines in range(0,len(phys_addr_data)):
            fd.write(phys_addr_data[lines])
            fd.write('\n')
        fd.close()
    return phys_addr_data