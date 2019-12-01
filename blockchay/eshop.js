import Web3 from 'web3';

export {newOrder, viewOrder, viewClientOrders, testDeployment};

const web3 = new Web3('ws://localhost:8544');
const from = web3.eth.coinbase; 
const gasPrice = '1';
const gas = 5000000;
const contractAddress = '0xC2E05aE483580E93CdCfd5555921C8eEA7f253f1';
const abi = [
  {
    "constant": false,
    "inputs": [
      {
        "internalType": "uint32",
        "name": "orderId",
        "type": "uint32"
      }
    ],
    "name": "cancelOrder",
    "outputs": [],
    "payable": false,
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "constant": false,
    "inputs": [
      {
        "internalType": "uint32",
        "name": "orderId",
        "type": "uint32"
      }
    ],
    "name": "completeOrder",
    "outputs": [],
    "payable": false,
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "constant": false,
    "inputs": [
      {
        "internalType": "uint32",
        "name": "clientId",
        "type": "uint32"
      },
      {
        "internalType": "string",
        "name": "phoneConfig",
        "type": "string"
      }
    ],
    "name": "newOrder",
    "outputs": [
      {
        "internalType": "uint32",
        "name": "orderId",
        "type": "uint32"
      }
    ],
    "payable": false,
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "constant": false,
    "inputs": [
      {
        "internalType": "uint32",
        "name": "orderId",
        "type": "uint32"
      }
    ],
    "name": "startOrder",
    "outputs": [],
    "payable": false,
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [],
    "payable": false,
    "stateMutability": "nonpayable",
    "type": "constructor"
  },
  {
    "anonymous": false,
    "inputs": [
      {
        "indexed": true,
        "internalType": "uint32",
        "name": "orderId",
        "type": "uint32"
      },
      {
        "indexed": true,
        "internalType": "uint32",
        "name": "clientId",
        "type": "uint32"
      },
      {
        "indexed": false,
        "internalType": "string",
        "name": "phoneConfig",
        "type": "string"
      }
    ],
    "name": "OrderReceived",
    "type": "event"
  },
  {
    "constant": true,
    "inputs": [
      {
        "internalType": "uint32",
        "name": "",
        "type": "uint32"
      },
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "name": "clientOrders",
    "outputs": [
      {
        "internalType": "uint32",
        "name": "",
        "type": "uint32"
      }
    ],
    "payable": false,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": true,
    "inputs": [],
    "name": "testDeployment",
    "outputs": [
      {
        "internalType": "string",
        "name": "",
        "type": "string"
      }
    ],
    "payable": false,
    "stateMutability": "pure",
    "type": "function"
  },
  {
    "constant": true,
    "inputs": [
      {
        "internalType": "uint32",
        "name": "clientId",
        "type": "uint32"
      }
    ],
    "name": "viewClientOrders",
    "outputs": [
      {
        "internalType": "uint32[]",
        "name": "",
        "type": "uint32[]"
      }
    ],
    "payable": false,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": true,
    "inputs": [
      {
        "internalType": "uint32",
        "name": "orderId",
        "type": "uint32"
      }
    ],
    "name": "viewOrder",
    "outputs": [
      {
        "internalType": "string",
        "name": "",
        "type": "string"
      }
    ],
    "payable": false,
    "stateMutability": "view",
    "type": "function"
  }
];

const contract = new web3.eth.Contract(abi, contractAddress);
contract.options.from = from;
contract.options.gasPrice = gasPrice;
contract.options.gas = gas;

async function testDeployment() {
  const testDeployment = contract.methods['testDeployment']();
  await checkGasOrThrow(testDeployment);
  return await testDeployment.call();
}

async function newOrder(clientId, phoneConfigStr) {
  phoneConfigStr = encodeURI(phoneConfigStr);
  const newOrder = contract.methods['newOrder'](clientId, phoneConfigStr);
  await checkGasOrThrow(newOrder);
  return await newOrder.send();
}

async function viewOrder(orderId) {
  const viewOrder = contract.methods['viewOrder'](orderId);
  await checkGasOrThrow(viewOrder);
  return await viewOrder.call();
}

async function viewClientOrders(clientId) {
  const viewClientOrders = contract.methods['viewClientOrders'](clientId);
  await checkGasOrThrow(viewClientOrders);
  return await viewClientOrders.call();
}

function checkGasOrThrow(contractMethod) {
  return new Promise((resolve, reject) => {
    contractMethod.estimateGas(function(error, amount) {
      if (error) {
        reject(error);
      } else {
        if (amount < gas) {
          resolve();
        } else {
          reject();
        }
      }
    });
  });
}
