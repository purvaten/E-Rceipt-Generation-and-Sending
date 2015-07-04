import os
import docx

def convert_to_pdf(filename, path):

	#print "cp \"~/PDF/"+filename+".pdf \" \"./"+filename+".pdf\""
	#print "lowriter --pt pdf \""+filename+".docx\""
	os.system("lowriter --pt pdf \""+filename+".docx\"")

	source = "/home/dell/PDF/"+filename+".pdf"
	destination = path+filename+".pdf"
	
	os.system("cp \""+source+"\" \""+destination+"\"")