const coinbase = process.argv.slice(2)[0];
console.log(`Generated coinbase address is: ${coinbase}`);
(async function () {
  var fs = require("fs");
  var Web3 = require("web3");
  var web3 = new Web3('http://localhost:8543');
  var config = JSON.parse(fs.readFileSync("config.json"));

  try {
    var ordertrackingContract = new web3.eth.Contract(config.contractAbi, config.contractAddress);
    ordertrackingContract.options.from = coinbase;
    ordertrackingContract.options.gasPrice = '1';
    ordertrackingContract.options.gas = config.gas; // safe Gas amount for the deployment

    while ((await web3.eth.getBalance(coinbase)) <= 0) {
      console.log("Waiting for ETH mining...");
      await sleep(2000);
    }
    console.log(`Eth balance is ${await web3.eth.getBalance(coinbase)}`);

    const deploymentObj = ordertrackingContract.deploy({
      data: config.contractBytecode
    });
    console.log("Attempting to estimate required gas amount for deployment");
    let gasEstimation = await deploymentObj.estimateGas();
    console.log(`Gas estimate for deployment: ${gasEstimation}`);
    let awaitDeploy = Promise.resolve();
    if (gasEstimation < ordertrackingContract.options.gas) {
      awaitDeploy = deploymentObj.send({}, function (error, transactionHash) {
	console.log(`Deployment finished with hash: ${transactionHash} and error ${error}`);
      });

      awaitDeploy
	.on('error', function (error) { console.log(`Error occurred during deployment: ${error}`) })
	.on('transactionHash', function (transactionHash) { console.log(`Transaction hash: ${transactionHash}`) })
	.on('receipt', function (receipt) { 
	  console.log(`Deployed contract address: ${receipt.contractAddress}`);
	})
	.then(function (newContractInstance) {
	  console.log(`New contract address: ${newContractInstance.options.address}`);
	})
	.catch(function (error) {
	  console.log(`Promise was rejected: ${error}`);
	});
      const result = await awaitDeploy;
      console.log(`Address ${result._address}`);
      config.contractAddress = result._address; 
      fs.writeFileSync("config.json", JSON.stringify(config, null, 1));
    } else {
      console.warn("Cannot deploy contract, provided Gas is under the estimation");
    }
  } catch (e) {
    console.log(e);
  }

  while (true)
    await sleep(2000);
})();

async function sleep(ms) {
  return new Promise((res, rej) => { setTimeout(() => res(), ms); });
}
