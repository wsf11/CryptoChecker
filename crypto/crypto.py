__author__ = "Winston Frick"

import json
import boto3
from coinmarketcap import Market

def lambda_handler(event, context):
	client = boto3.client('sns')
	coinmarketcap = Market()

	bitcoin = coinmarketcap.ticker("Bitcoin")[0]
	ethereum = coinmarketcap.ticker("Ethereum")[0]
	litecoin = coinmarketcap.ticker("Litecoin")[0]
	
	# Bitcoin daily price. Daily Percent Change. Weekly Percent Change. 
	btc_price = bitcoin["price_usd"]
	btc_daily_change = bitcoin["percent_change_24h"]
	btc_weekly_change = bitcoin["percent_change_7d"]

	# Ethereum daily price. Daily Percent Change. Weekly Percent Change. 
	eth_price = ethereum["price_usd"]
	eth_daily_change = ethereum["percent_change_24h"]
	eth_weekly_change = ethereum["percent_change_7d"]

	# Litecoin daily price. Daily Percent Change. Weekly Percent Change. 
	ltc_price = litecoin["price_usd"]
	ltc_daily_change = litecoin["percent_change_24h"]
	ltc_weekly_change = litecoin["percent_change_7d"]

	# Printing for sanity purposes to see the display in the Lambda Console
	print("Bitcoin Price:", btc_price,"| 24H%D:", btc_daily_change,"| 7D%D", btc_weekly_change)

	print("Ethereum Price:", eth_price,"| 24H%D:", eth_daily_change,"| 7D%D", eth_weekly_change)

	print("Litecoin Price:", ltc_price,"| 24H%D:", ltc_daily_change,"| 7D%D", ltc_weekly_change)

	# Response that will be texted to your phone number
	response = client.publish(
		PhoneNumber='xxxxxxxxxxx',
		Message="-Bitcoin Price: " + btc_price + " | 24H%D: " + btc_daily_change + " | 7D%D " + btc_weekly_change + "\n"
		+ "-Ethereum Price: " + eth_price + " | 24H%D: " + eth_daily_change + " | 7D%D " + eth_weekly_change + "\n"
		+ "-Litecoin Price: " + ltc_price + " | 24H%D: " + ltc_daily_change + " | 7D%D " + ltc_weekly_change,
		MessageStructure='String'
	)
