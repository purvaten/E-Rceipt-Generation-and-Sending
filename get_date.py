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
	month_names = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
	month_number = month_names.index(month)+1
	if month_number<10:
		month_value='0'+str(month_number)
	else:
		month_value=str(month_number)
	date = date_value+"/"+month_value+"/2015"
	return date