import os
import docx

def convert_to_pdf(filename=""):

	print "cp \"~/PDF/"+filename+".pdf \" \"./"+filename+".pdf\""
	print "lowriter --pt pdf \""+filename+".docx\""
	os.system("lowriter --pt pdf \""+filename+".docx\"")
	os.system("cp \"~/PDF/"+filename+".pdf \" \"./"+filename+".pdf\"")

convert_to_pdf('haggu3')