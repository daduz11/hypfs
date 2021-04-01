#  HYPFS


This project was carried out for an assignment of Blockchain and Cryptocurrencies course at the University of Bologna. 

The proposal provides the implementation of a Decentralized keywords Search Engine based on a hypercube structure and integrated with IPFS using Python.

## Executables
* **menu.py**: script that provides a user-friendly command line UI.
* **start_daemons.py**: script useful for starting two IPFS processes.
* **start_servers.py**: script useful for starting 2^HYPERCUBE_SIZE servers processes, and the hop_counter.
* **bench.py**: script used for testing.

## Folders
* **src**: contains all the scripts of the hypercube and node implementation.  
* **results**: contains the results of tests carried out with the *bench.py* script.
* **objects**: contains the objects downloaded from IPFS.
* **test_files**: used for generating random files.

## References
The project is inspired by
* [The IPFS Search Engine](https://ieeexplore.ieee.org/abstract/document/8958437)
* [Keyword search in DHT-based peer-to-peer networks](https://ieeexplore.ieee.org/document/4062563)
* [IPFS](https://docs.ipfs.io/)
* [py-ipfs-http-client](https://github.com/ipfs-shipyard/py-ipfs-http-client)

## License
[Apache License 2.0](./LICENSE)