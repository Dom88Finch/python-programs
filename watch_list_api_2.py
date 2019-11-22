# Below is an API for tracking several prices from my watch list from amazon


import requests  # allows us to access a url
import smtplib
from bs4 import BeautifulSoup  
import pandas as pd
import numpy as np

pd.set_option('display.max_columns', None) 

URL = "https://www.amazon.co.uk/Logic-Keyboard-Shortcut-Cover-Magic-Pro-X/dp/B01HBTSSQU?pf_rd_p=7b6f4c5f-dc85-44e8-9c64-01c5dc81e1ae&pd_rd_wg=VIm8q&pf_rd_r=PDMS8EC5JBKQGQND094E&ref_=pd_gw_unk&pd_rd_w=IMlDz&pd_rd_r=937e985a-04fc-407f-b3a5-c97fcfc0a27f"
URL2 = "https://www.amazon.co.uk/Logic-Keyboard-Cover-MacBook-Faster/dp/B01MR915O9?pf_rd_p=d79debb4-4345-4c84-ba3c-629cad270cf9&pd_rd_wg=swyYG&pf_rd_r=JPC243DT2H893Z6YPZRP&ref_=pd_gw_cr_simh&pd_rd_w=O9jht&pd_rd_r=bc0808b0-50fa-4022-a831-8ee07a3502d6"
URL3 = "https://www.amazon.co.uk/GRAFIT-Classic-Polarized-Sunglasses-Protection/dp/B07D345HLL/ref=pd_sbs_107_3/257-2823289-3775811?_encoding=UTF8&pd_rd_i=B07D345HLL&pd_rd_r=bacce188-89be-4b1d-b79a-698568c2608d&pd_rd_w=l46AU&pd_rd_wg=t5HeE&pf_rd_p=cc188cba-1892-42b3-956f-6c67d0ab7a00&pf_rd_r=R50007EC9WQ624N3K047&refRID=R50007EC9WQ624N3K047"

URL_master = [URL,URL2,URL3]

headers =  {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'}

name =[]
cost =[]
supplier =[]


pages = range(0,len(URL_master))
print(pages)

def check_price():

	
	for i in pages:# iterates over all Urls

		page = requests.get(URL_master[i], headers = headers)
		soup = BeautifulSoup(page.content, 'html.parser')


		# name of product
		title = soup.find(id= "title").get_text().strip()
		name.append(title)

		# price information of product
		price = soup.find(id="price_inside_buybox").get_text().strip() # removes empty space
		convert_price = float(price[1:].replace(',',''))
		cost.append(convert_price)

		# Seller information
		seller = soup.find(id="bylineInfo").get_text().strip()
		supplier.append(seller)

	return name, cost,supplier

check_price()







def send_mail():
	server = smplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	server.ehlo()

	server.login('ENTER YOUR EMAIL', 'PASSWORD')

	subject = 'Price fell down!'
	body = ' Check the amazon link  '

	msg = f"Subject: {subject}\n\n{body}"

	server.send_mail(
		'EMAIL',  # from 
		'EMAIL',  # to 
		msg
		)
	print( "HEY, Email has been sent to you. Click link to buy item!")

	server.quit()



data = {"product":name, "original_cost": cost, "seller_info":supplier,"website":URL_master}
A= pd.DataFrame.from_dict(data)


A["current_cost"] = A.original_cost -3
#A["percentage_reduction"]= A.original_cost.apply(lambda y: (1- (y/(A.current_cost))))
A["percentage_reduction %"]=(1- A.current_cost/A.original_cost)*100
A["cost_decreased"]= A.original_cost.apply(lambda x: x > 10)

print(A)



print(A['cost_decreased'] == True)
	
	






## To do list
# 1) Find a way to convert this code to use a class 

# class Example:

# 	def __init__(self,name,cost,supplier):
# 		self.name = name
# 		self.cost = cost
# 		self.supplier = supplier






# 2) Create a new list with the original cost. compare these new values to the current values
#    if the cost has decreased, then cost_decreased  = True

 # eg. duplicate one oof the columns s.t. 


# 2.5) new column that caluclate the percentage of decrease of the product.


# 3) Now add the function that sends an email with links for the product.










