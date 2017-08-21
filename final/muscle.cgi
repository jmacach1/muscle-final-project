#!/usr/local/bin/python3
#Jerald Macachor
#Advance Practical Computer Concepts for Bioinformatics
#August 19, 2017

#Project Final - Muscle Alignment Bioinformatics Tool
# This cgi script will execute a Muscle Alignment
# with sequences takent from index.html
# and print it on a jinja template (results.html)

import os
import jinja2
import cgi 

#---------------- HTML template -----------------------#

# This line tells the template loader where to search for template files
templateLoader = jinja2.FileSystemLoader(searchpath="./templates")

# This creates your environment and loads a specific template
env = jinja2.Environment(loader=templateLoader)
template = env.get_template('results.html')

template.trim_blocks = False
template.lstrip_blocks = False
template.strip_trailing_newlines = False


#########################################################

#----------------------- Body ---------------------------#

## Gets the form inputs from search.html 
form = cgi.FieldStorage()
faaSeqs = form.getvalue("inputTextArea")

## Open the temp file and place faaSeq in the temp.fa file.
tmp = open("temp.fa", "w+")
tmp.write(faaSeqs)
tmp.close()

## Call the muscle program to execute an alignment with temp.fa
stream = os.popen("muscle -in temp.fa -clw")

## Place the MUSCLE stream into an array of strings called result.
result = []
for i in stream:
     result.append(str(i))



print("Content-Type:text/html\n\n")
print(template.render(results = result, trim_blocks = False))
