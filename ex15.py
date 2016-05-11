from sys import argv
filename = raw_input("Please give file name to open :  ")

txt = open(filename)

prt = txt.read()

print("The file that you asked to open is %r and the content of the file is : ") %(filename)

print prt


txt.close()




	











