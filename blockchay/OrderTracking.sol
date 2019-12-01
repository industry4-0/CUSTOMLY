pragma solidity >=0.5.10;

contract OrderTracking {
  struct Order {
    uint32 orderId;
    uint32 clientId;
    string phoneConfig;
    bool started;
    bool complete;
    bool canceled;
  }

  mapping(uint32 => uint32[]) public clientOrders;
  Order[] orders;

  event OrderReceived(uint32 indexed orderId, uint32 indexed clientId, string phoneConfig);

  constructor() public {
  }

  function testDeployment() public pure returns (string memory) {
    return "Success!";
  }

  function newOrder(
    uint32 clientId,
    string memory phoneConfig
  ) public returns (uint32 orderId) {

    orderId = uint32(orders.length); // length will always match the new order's index in the array
    orders.push(Order({
      orderId : orderId,
      clientId : clientId,
      started : false, complete : false, canceled : false,
      phoneConfig : phoneConfig
      }));
    clientOrders[clientId].push(orderId);
    emit OrderReceived(orderId, clientId, phoneConfig);
  }

  function viewClientOrders(uint32 clientId) public view returns (uint32[] memory) {
      return clientOrders[clientId];
  }

  function viewOrder(uint32 orderId) public view returns (string memory) {
    return orders[orderId].phoneConfig;
  }

  function startOrder(uint32 orderId) public {
    require(!orders[orderId].canceled && !orders[orderId].complete, "The order cannot be started because it is already terminated.");
    orders[orderId].started = true;
  }

  function cancelOrder(uint32 orderId) public {
    require(!orders[orderId].complete, "The order is has already been completed and cannot be marked as canceled.");
    require(!orders[orderId].started, "The order is already being processed and cannot be canceled at this stage.");
    // this must come second
    orders[orderId].canceled = true;
  }

  function completeOrder(uint32 orderId) public {
    require(!orders[orderId].canceled, "The order is has already been canceled and cannot be marked as complete.");
    orders[orderId].complete = true;
  }
}

