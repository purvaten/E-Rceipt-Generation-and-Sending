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
import get_date

f = open('coep_mun.txt', 'r')
text = f.read()
split = text.splitlines()
email_id = split[0]
print email_id
password = split[1]
print password
path = split[2]
data_obtained =  project3.scrape_email(email_id, password)
print data_obtained
for list_element in data_obtained:
	date = get_date.get_date(list_element[0])
	name = list_element[1]
	price = "1300"
	hasBeenSent = reg_no.search(name)
	if hasBeenSent==0:
		print name+" has already been sent a receipt"
		continue
	no = reg_no.insert_element(name)
	filename = form_filling.form_filling(date, name, price, no )
	print filename
	convert_to_pdf.convert_to_pdf(filename, path)