import os
import docx

def convert_to_pdf(filename, path):

	#print "cp \"~/PDF/"+filename+".pdf \" \"./"+filename+".pdf\""
	#print "lowriter --pt pdf \""+filename+".docx\""
	home = os.path.expanduser('~')
	os.system("lowriter --pt pdf \""+filename+".docx\"")

	source = home+"/PDF/"+filename+".pdf"
	destination = path+filename+".pdf"
	#print "mv \""+source+"\" \""+destination+"\""
	os.system("mv \""+source+"\" \""+destination+"\"")