const CALL_METHOD = process.argv.slice(2)[0]; // slice(2) throws away thefirst 2 args that are redundant
if(CALL_METHOD)
  console.log(`Will attempt to call contract method ${CALL_METHOD}`);

const fs = require("fs");
const Web3 = require("web3");
// const web3 = new Web3('http://localhost:8543');
const web3 = new Web3('ws://localhost:8544');
const config = JSON.parse(fs.readFileSync("config.json"));

(async function() {
  try {
    const ordertrackingContract = new web3.eth.Contract(config.contractAbi, config.contractAddress);
    ordertrackingContract.options.from = web3.eth.coinbase;
    ordertrackingContract.options.gasPrice = '1';
    ordertrackingContract.options.gas = config.gas; // safe Gas amount for the deployment

    setupEvents(ordertrackingContract);

    if(CALL_METHOD) {
      await callMethod(ordertrackingContract, CALL_METHOD);
    }
  } catch(e) {
    console.log(e);
  }


  while(true)
    await sleep(2000);

})();

async function sleep(ms) {
  return new Promise((res, rej) => {
    setTimeout(() => res(), ms);
  });
}

async function callMethod(contract, method) {
  console.log("About to call method " + CALL_METHOD);
  const methodCall = contract.methods[CALL_METHOD]();
  let gasEstimation;
  await methodCall.estimateGas({
    from: web3.eth.coinbase,
    gasPrice: '1',
    gas: config.gas
  }, function(error, gasAmount) {
    if(error) {
      console.log(`Error: ${error}`)
    }
    console.log(`Gas estimate: ${gasAmount}`);
    gasEstimation = gasAmount;
  });

  console.log(`Call contract gas estimation: ${gasEstimation}`);
  if(gasEstimation < contract.options.gas) {
    const res = await methodCall.call();
    console.log(`Result is ${res}`);
  } else {
    console.warn("Cannot initiate contract call, provided gas amount is under the required estimate");
  }
}

function setupEvents(contract) {
  console.log("Setting up event listeners");
  contract.events.OrderReceived(function(error, result) {
    console.log("OrderReceived event triggered.");
    if(error) {
      console.warn("There was an error with the order submission.");
    } else {
      const orderId = result.returnValues.orderId;
      const clientId = result.returnValues.clientId;
      const phoneConfig = result.returnValues.phoneConfig;
      console.log(`Received order ID ${orderId} from client ID ${clientId} for the following configuraiton: ${phoneConfig}`);
    }
  })
    .on('data', function(event) {
      console.log("NEW ORDER RECEIVED");
      console.log(event);
    })
    .on('changed', function(event) {
      console.log(`Event was removed (wut ?)\n${event}`);
    })
    .on('error', console.error);
}
