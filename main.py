from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import getpass
import time,re
import docx
from docx import table
import form_filling
import os
import convert_to_pdf
import project3
import reg_no

f = open('coep_mun.txt', 'r')
text = f.read()
split = text.splitlines()
email_id = split[0]
print email_id
password = split[1]
print password
path = split[2]
data_obtained =  project3.scrape_email(email_id, password)


for list_element in data_obtained:
	date = list_element[0]

	date_data = date.split()

	current_date_format = re.compile(r'\d+:\d+')
	other_date_format = re.compile(r'\w+ \d+')
	if current_date_format.search(date)!= None:
		date_value = (time.strftime("%d/%m/%Y"))
	elif other_date_format.search(date)!= None:
		date_value = date_data[1]
		
	month = date_data[0]
	if month == "Jun":
		month_value = "06"
	elif month =="Jul":
		month_value = "07"
	elif month == "Aug":
		month_value = "08"
	elif month =="Sep":
		month_value = "09"
	elif month == "Oct":
		month_value = "10"
	elif month == "Nov":
		month_value = "11"

	date = date_value+"/"+month_value+"/2015"

	name = list_element[1]
	price = "1300"
	no = reg_no.search(name)

	form_filling.form_filling(date, name, price, no )
	filename = form_filling.form_filling(date, name, price, no )
	print filename

	convert_to_pdf.convert_to_pdf(filename, path)




