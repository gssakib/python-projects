from sys import argv

script, file_1, file_2 = argv


open(file_2, 'w').write(open(file_1, 'r').read()) #one line of code copying contents of file_1 to file_2

 










