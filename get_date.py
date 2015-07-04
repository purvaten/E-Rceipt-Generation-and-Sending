def get_date(date=""):
	import re,time
	date_data = date.split()

	current_date_format = re.compile(r'\d+:\d+')
	other_date_format = re.compile(r'\w+ \d+')
	if current_date_format.search(date)!= None:
		date_value = (time.strftime("%d/%m/%Y"))
		return date_value
	elif other_date_format.search(date)!= None:
		date_value = date_data[1]
	month_value=""
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
	return date