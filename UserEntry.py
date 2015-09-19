# This is written for PYTHON 3
# Don't forget to install requests package

import requests
import json

apiKey = '93288ff12bdd4391f274efdec9889dc0'

customers=requests.get('http://api.reimaginebanking.com/customers?key=93288ff12bdd4391f274efdec9889dc0')
cdict={}
i=0
for i in range(len(customers.json())):
	fullName=customers.json()[i]['first_name']+' ' +customers.json()[i]['last_name']
	cdict[fullName]=customers.json()[i]['_id']
	customers.json()[i]
print(' Welcome to the Capital One Financial Expenditure Program')
Correct=False
while(Correct==False):
	userid = input('Please input your userid: ') #user id input
	for key in cdict:
		if (cdict[key]==userid):
			print ('Welcome ' + key+ '.')
			Correct=True
	if (Correct==False):
		print("I'm sorry, that's not a valid id. Try again"	)
accountdata= requests.get('http://api.reimaginebanking.com/customers/55e94a6af8d8770528e60d66/accounts?key=93288ff12bdd4391f274efdec9889dc0')
adict=[]
i=0
for i in range(len(accountdata.json())):
	nicknameaccounts=accountdata.json()[i]['nickname']
	adict.insert(i,nicknameaccounts)
print('Here are your following accounts:')
print (adict)
account=input("Which account would you like to look at?")
if (account in adict):
	accountinfo=requests.get('http://api.reimaginebanking.com/accounts/55e94a6cf8d8770528e6185f?key=93288ff12bdd4391f274efdec9889dc0')
	print(accountinfo.json())






# responseAction = {
# 	201 : lambda : print('It worked'),
# 	400 : lambda : print('Uh oh, something in your payload is wrong'),
# }

# # url = 'http://api.reimaginebanking.com/customers/{}/accounts?key={}'.format(customerId,apiKey)
# # payload = {
# #   "type": "Savings",
# #   "nickname": "This is a test",
# #   "rewards": 1000,
# #   "balance": 28000,	
# # }

# req = requests.post(
# 	url, 
# 	data=json.dumps(payload),
# 	headers={'content-type':'application/json'},
# 	)
