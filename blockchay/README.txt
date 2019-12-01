Setting up Ethereum RPC

 - Download Geth 1.9.8 https://geth.ethereum.org/downloads/
 - Install
 - Create project dir
 - Create genesis.json file
 - Write the following json inside:
    {
		"config": {
		"chainId": 143,
		"homesteadBlock": 0,
		"eip150Block": 0,
		"eip155Block": 0,
		"eip158Block": 0
		},
		"alloc": {},
		"difficulty" : "0x40000",
		"gasLimit"   : "0x88800000"
	}
 - mkdir "blkchain" inside the project dir
 - run: geth --datadir blkchain init genesis.json
 - this will create the genesis block
 - To start the geth service run:
	geth --port 3000 --networkid 58343 --nodiscover --datadir=./blkchain --maxpeers=0 --rpc --rpcport 8543 --rpcaddr 0.0.0.0 --rpccorsdomain "*" --rpcapi "eth,net,web3,personal,miner" --allow-insecure-unlock --minerthreads "1" --ws --wsport 8544 --wsorigins "*" --wsaddr 0.0.0.0
 - Open new terminal and run: geth attach http://localhost:8543
 - On JS console create an account running:
   personal.newAccount("seed")
   personal.unlockAccount(web3.eth.coinbase, "seed", 0)
 - Start mining by running: miner.start(1)
 
Alternatively:
Checkout the blockchay project and run the master_script.sh where the first argument is the data dir and the second argument is the genesis.json file:
./master_script.sh /path/to/blkchain /path/to/genesis.json
