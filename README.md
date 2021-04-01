#  HYPFS

<img src="https://github.com/daduz11/hypfs/blob/master/sys_arch.png" width="100%" align="center">


This project was carried out for an assignment of Blockchain and Cryptocurrencies course at the University of Bologna. 

The proposal provides the implementation of a Decentralized keywords Search Engine based on a hypercube structure and integrated with IPFS using Python.

##  Folders and Executables
 ####
* **src**: contains all the scripts of the hypercube and node implementation.  
* **results**: contains the results of tests carried out with the *bench.py* script.
* **objects**: contains the objects downloaded from IPFS.
* **test_files**: used for generating random files.
####
* **menu.py**: script that provides a user-friendly command line UI.
* **start_daemons.py**: script useful for starting two IPFS processes.
* **start_servers.py**: script useful for starting 2^HYPERCUBE_SIZE servers processes, and the hop_counter.
* **bench.py**: script used for testing.
  

## Dependencies
* [ipfshttpclient](https://pypi.org/project/ipfshttpclient/)
* [networkx](https://pypi.org/project/networkx/)
* [requests](https://pypi.org/project/requests/)
* [Flask](https://pypi.org/project/Flask/)
* [windows-curses](https://pypi.org/project/windows-curses/)
* [openpyxl](https://pypi.org/project/openpyxl/) (for testing)

It is also possible (and suggested) to use the virtual environment provided in the main directory. Apparently in the *ipfshttpclient/client/__ init__.py* there was a bug about versioning, therefore, the lines 64 and 65 have been commented out.

## src/config.py
* **HYPERCUBE_SIZE**: defines the hypercube data structure dimension, i.e. the number of network's nodes.
* **SUPERSET_THRESHOLD**: limits the number of objects returned by superset search.


## Usage
    python start_daemons.py
    python start_servers.py
    python menu.py /ip4/127.0.0.1/tcp/5001 1


## References
The project is inspired by
* [The IPFS Search Engine](https://ieeexplore.ieee.org/abstract/document/8958437)
* [Keyword search in DHT-based peer-to-peer networks](https://ieeexplore.ieee.org/document/4062563)
* [IPFS](https://docs.ipfs.io/)
* [py-ipfs-http-client](https://github.com/ipfs-shipyard/py-ipfs-http-client)

## License
[Apache License 2.0](./LICENSE)
