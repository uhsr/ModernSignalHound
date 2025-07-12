# ModernSignalHound: Decentralized Price Alerts Powered by Pyth

ModernSignalHound is a decentralized application enabling users to receive real-time price alerts based on Pyth oracle data. It leverages smart contracts for defining alert conditions and WebSocket technology for instant notifications on price deviations meeting those conditions. This system provides a trustless and automated way to monitor on-chain price feeds, ensuring users are promptly informed of critical market movements. The project aims to bridge the gap between decentralized data sources and real-time notification systems, empowering users with timely and actionable insights without relying on centralized intermediaries.

This project tackles the inherent latency challenges associated with monitoring blockchain data. Traditional methods often involve polling on-chain data or relying on centralized services, which can introduce delays and potential points of failure. ModernSignalHound addresses these issues by employing smart contracts to store alert configurations and a WebSocket server that actively monitors the Pyth price feeds. When a defined price threshold is crossed, the smart contract emits an event, triggering the WebSocket server to push a notification to subscribed users. This architecture ensures near real-time alerts with verifiable data integrity.

The system's modular design promotes extensibility and adaptability. The smart contract component is written in Solidity and deployed on an EVM-compatible blockchain. The WebSocket server is built using Python and utilizes the asyncio library for efficient asynchronous operations. The client-side application can be any platform capable of establishing a WebSocket connection and parsing the alert notifications. This flexibility allows developers to integrate ModernSignalHound into a wide range of existing applications and workflows. The project prioritizes security and reliability by adhering to best practices in smart contract development and network communication.

## Key Features

*   **Decentralized Alert Configuration:** Alert conditions (e.g., price threshold, asset pair) are defined and stored within smart contracts, ensuring transparency and immutability. A user can interact with the smart contract to create, modify or delete price alerts.
*   **Real-time Price Monitoring:** The Python-based WebSocket server actively listens to Pyth oracle updates, enabling immediate detection of price deviations. The server subscribes to relevant price feeds from the Pyth network.
*   **WebSocket-Based Notifications:** Users receive instant alerts via WebSocket connections, minimizing latency compared to traditional polling methods. The notifications include the asset pair, current price, and the trigger event that activated the alert.
*   **Pyth Oracle Integration:** Leverages the Pyth network for highly accurate and reliable price data. The system validates the price data's timestamp and confidence intervals to ensure data integrity.
*   **EVM Compatibility:** The smart contracts are designed to be deployed on any EVM-compatible blockchain, providing flexibility in choosing the underlying blockchain infrastructure. Currently designed for deployment on Polygon Mumbai Testnet.
*   **Asynchronous Architecture:** The WebSocket server utilizes asyncio to handle multiple concurrent connections and price feed updates efficiently. This ensures scalability and responsiveness, even under high load.
*   **Configurable Alert Parameters:** Users can customize alert parameters, such as the price threshold, deviation percentage, and notification frequency, to tailor the system to their specific needs.

## Technology Stack

*   **Solidity:** Used for writing the smart contracts that store alert configurations and emit events upon price triggers. Solidity version 0.8.0 or higher is recommended.
*   **Python:** The primary language for the WebSocket server, responsible for monitoring price feeds and sending notifications. Python version 3.8 or higher is required.
*   **Web3.py:** A Python library for interacting with Ethereum-compatible blockchains. Used to interact with the smart contracts and retrieve events.
*   **Asyncio:** Python's built-in asynchronous programming library. Enables the WebSocket server to handle multiple concurrent connections efficiently.
*   **WebSockets:** A communication protocol providing full-duplex communication channels over a single TCP connection. Used for real-time notification delivery.
*   **Pyth Network SDK:** Used to subscribe and decode price feed updates from the Pyth oracle. It retrieves price data from the Pyth on-chain data source.
*   **Brownie:** (Optional) A Python-based development and testing framework for smart contracts. It simplifies deployment, testing, and interaction with the smart contracts.

## Installation

1.  Clone the repository:
    git clone https://github.com/uhsr/ModernSignalHound.git
    cd ModernSignalHound

2.  Install Python dependencies:
    pip install -r requirements.txt

3.  Install Brownie (if you choose to use it for smart contract deployment and testing):
    pip install eth-brownie

4.  Deploy the Smart Contract: Navigate to the `contracts` directory and deploy the smart contract to a testnet or mainnet. You can use Remix, Hardhat, or Brownie for this purpose. Ensure you have the necessary funds and a configured wallet. For Brownie, you might use a command like `brownie run scripts/deploy.py --network polygon-mumbai`.

5.  Configure the WebSocket Server: Create a `.env` file in the root directory and populate it with the necessary environment variables (see Configuration section).

## Configuration

The following environment variables are required for the WebSocket server:

*   `WEB3_PROVIDER_URI`: The URI of your Ethereum node (e.g., Infura, Alchemy, or a local node). Example: `https://polygon-mumbai.infura.io/v3/<YOUR_INFURA_PROJECT_ID>`
*   `CONTRACT_ADDRESS`: The address of the deployed smart contract. Example: `0x1234567890abcdef1234567890abcdef12345678`
*   `PYTH_CONTRACT_ADDRESS`: The address of the Pyth contract on the target chain.
*   `PRIVATE_KEY`: The private key of the wallet address used to deploy the smart contract and interact with the web3 provider. Important: Never expose your private key in a public repository.
*   `WS_PORT`: The port number for the WebSocket server. Default: `8765`
*   `PYTH_PRICE_IDS`: Comma separated list of Pyth Price IDs to subscribe to, example: `0xe62df6c8b4a85fe1a67db53aca7a28a09ef28a843b5efdd1262394473e6f260a,0xabcdef0123456789abcdef0123456789abcdef0123456789abcdef0123456789`

Example `.env` file:

WEB3_PROVIDER_URI=https://polygon-mumbai.infura.io/v3/<YOUR_INFURA_PROJECT_ID>
CONTRACT_ADDRESS=0x1234567890abcdef1234567890abcdef12345678
PYTH_CONTRACT_ADDRESS=0xabcd
PRIVATE_KEY=YOUR_PRIVATE_KEY
WS_PORT=8765
PYTH_PRICE_IDS=0xe62df6c8b4a85fe1a67db53aca7a28a09ef28a843b5efdd1262394473e6f260a,0xabcdef0123456789abcdef0123456789abcdef0123456789abcdef0123456789

## Usage

1.  Start the WebSocket server:
    python websocket_server.py

2.  Interact with the Smart Contract: Use web3.py or another library to interact with the deployed smart contract. Create and manage alerts by calling the appropriate functions in the contract.

3.  Connect to the WebSocket: Create a client application that connects to the WebSocket server at `ws://localhost:<WS_PORT>`. The server will push notifications when price alerts are triggered. Example WebSocket connection Javascript code:

    const websocket = new WebSocket('ws://localhost:8765');

    websocket.onmessage = (event) => {
      console.log('Received:', event.data);
    };

## Contributing

We welcome contributions to ModernSignalHound! Please follow these guidelines:

*   Fork the repository and create a branch for your feature or bug fix.
*   Write clear and concise commit messages.
*   Submit a pull request with a detailed description of your changes.
*   Ensure your code adheres to the project's coding style.
*   Include unit tests for any new functionality.

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/uhsr/ModernSignalHound/blob/main/LICENSE) file for details.

## Acknowledgements

We would like to thank the Pyth Network team for providing a reliable and decentralized price data solution.