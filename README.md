# Cache Tester
Cache Tester allows basic testing and validation of cache functionality. The user must create a cache design and instantiat the design inside the test bench. The cache is populated by the test data generated in 

# Tools Required
*	Cadence Xcelium
*	Python
*	Linux

## Prerequisites
Install the pre-requisities using the following commands
`sudo apt install python3 python3-pip`
`pip3 install -r requirements.txt`


# Getting Started

A skeleton and a verification framework is provided in the repository. Start with cloning the repository.
  ```bash
  $ git clone https://github.com/aaqdas/cache-tester.git
  ```
## Memory Initialization and Logs
The directory structure contains script files in `./scripts` which generate memory initialization files for caches in `./init_files` and log files in `./log`
`cache_init.py` is the main script, that takes different flags and generates initialization files for different configurations of caches. It takes blocks (-b), words per block (-w) and associativity (-a) as inputs. 
  ```bash
  $ python3 ./cache_init.py -b 256 -w 1 -a 1
  ```

## Simulation
Designed caches can be simulated by integrating your design in available testbench in `./tb` directory. The simulations must be run in Xcelium [Other tools can also be used but have not been tested].

The simulation testbench generates a log under the name `./log/core_access.log`

## Cache Evaluation
The cache results can be evaluated using comparison tool in scripts directory. The usage of the tool is as follows
  ```bash
  $ python3 ./check.py ../log/access.log ../log/core_access.log
  ```

  
