def search(name):
	searchfile = open("reg_ppl.txt", "r")
	for line in searchfile:
		if name in line:
			return 0
	searchfile.close()
	#no = insert_element(name)
	return 1


def insert_element(name):
	f = open('reg_ppl.txt', 'r+')
	ppl = f.read()
	splits = ppl.splitlines()
	no = 1512001 + len(splits)
	f.write("\n"+str(no)+" "+name)
	f.close()
	return no
	