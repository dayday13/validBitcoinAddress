import requests
from cryptoaddress import get_crypto_address
import cv2

balance_bitcoin= "https://blockchain.info/q/addressbalance" # find bitcoin balance for a specific address


class Functions:
    
    def balance_btc(address):
        """
        input: Bitcoin adress (string)
        output: balance in USD if valid, else returns a message
        """
        # The balance is returned in satoshi, than it converted to USD,
        # 1 satoshi = 0.0005683 USD
        

        if Functions.check_if_valid_btc(address)[1]==1:
            url = requests.get(balance_bitcoin + '/' + address).json()
            sat_usd = 'The balance for this address is {:.2f} USD.'.format(url, float(url) * 0.0005683)
            ans = Functions.check_if_valid_btc(address)[0] + "\n" + sat_usd

        elif Functions.check_if_valid_btc(address)[1]==0:
            ans= Functions.check_if_valid_btc(address)[0]

        return ans


    def check_if_valid_btc(address):
        """""
        for the "check_if_valid_btc" method
        input: Bitcoin adress (string)
        output: if this address is valid
        """
        try:
            bitcoin_address = get_crypto_address('BTC', address, network_type='mainnet')
            return ['Your address {} is a valid Bitcoin address!'.format(str(bitcoin_address)),1]

        except ValueError:
            return ["This is not a Bitcoin address! Try again!",0]


    def check_QR(img):
        """
        input: a QR code photo
        output: an address balance if the QR is an address, else return error massage
        """
        image = cv2.imread(img)
        resutle = UnicodeDecodeError
        detector = cv2.QRCodeDetector()
        data, vertices_array, binary_qrcode = detector.detectAndDecode(image) # 'data'- the address

        if vertices_array is not None:
            return Functions.balance_btc(data)

        else: 
            return "This is not a Bitcoin address! Try again!"

    
    
