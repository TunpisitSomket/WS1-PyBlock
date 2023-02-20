import json
from web3 import Web3
from flask import Flask, render_template

app = Flask(__name__)


class CallABI:
    def __init__(self):
        self.url = "http://127.0.0.1:7545"
        self.web3 = Web3(Web3.HTTPProvider(self.url))
        self.web3.eth.defaultAccount = self.web3.eth.accounts[0]
        self.abi = json.loads('''[
	{
		"constant": true,
		"inputs": [],
		"name": "get",
		"outputs": [
			{
				"name": "",
				"type": "string"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	}
]''')
        self.abi_address = "0x52A5DF582Acf126801fa56ba003b13dB2F79b5Ac"
        self.contract = self.web3.eth.contract(address=self.abi_address, abi=self.abi)

    def get(self):
        return self.contract.functions.get().call()


@app.route('/get')
def index():
    call_abi = CallABI()
    data = call_abi.get()
    return render_template('index.html', data=data)


if __name__ == '__main__':
    app.run(debug=True)
