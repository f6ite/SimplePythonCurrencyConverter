currencyName=["0","XAF","ARS","AUD","BSD","BRL","BGN","CAD","CLP","CNY","COP","HRK","CYP","CZK","DKK","LTC","BTC","XCD","EEK","EUR","FJD","XPF","GHS","GTQ","HNL","HKD","HUF","ISK","INR","IDR","ILS","JMD","JPY","LVL","LTL","MYR","MXN","MAD","MMK","ANG","NZD","NOK","PKR","PAB","PEN","PHP","PLN","GOLD","QAR","RON","RUB","SAR","RSD","SGD","ZAR","KRW","LKR","SEK","CHF","TWD","THB","TTD","TND","TRY","AED","GBP","USD","VND","VEF"]

currencyValue=[0,582.43,14.32,1.30,1.0,3.74,1.73,1.2835,663.85,6.4825,2991.92,6.6401,0.519911,23.987,6.6060,0.00546121,0.00002128,2.6898,11.73,0.88,2.0501,105.90,3.8245,7.8792,22.550,7.7564,276.56,124.49,66.573,13232.29,3.7828,121.78,109.14,0.62,3.05,3.91,17.42,9.70,1178.2,1.79,1.45,8.24,104.67,1.0,3.27,46.14,3.82,0.000813,3.64,3.97,66.07,3.75,109.14,1.36,14.56,1151.75,146.25,8.14,0.97,32.41,35.11,6.60,2.02,2.85,3.67,0.71,1.0,22309.50,9.95,]

currencyDict = dict()
for i in range(0,len(currencyName)):
	currencyDict[currencyName[i]]=currencyValue[i]
 
amount = eval(input("How much would you like to convert (In USD)? "))
currency = input("In which currency ? ")
 
def usdToCurrency(amount,currency):
	return amount*currency
 
if currency in currencyDict.keys():
	print(str(amount) + 'USD represents ' + str(usdToCurrency(amount,currencyDict[currency])) + currency + '.')
else:
	print("The currency you entered is invalid")