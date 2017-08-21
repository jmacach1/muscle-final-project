#!/usr/local/bin/python3
#Jerald Macachor
#Advance Practical Computer Concepts for Bioinformatics
#Project Final

# This cgi script will execute a Muscle Alignment
# with sequences takent from index.html
# and print it on a jinja template (results.html)

import os
import jinja2
#import mysql.connector
#import cgi

#---------------- HTML template -----------------------#

# This line tells the template loader where to search for template files
templateLoader = jinja2.FileSystemLoader(searchpath="./templates")

# This creates your environment and loads a specific template
env = jinja2.Environment(loader=templateLoader)
template = env.get_template('results.html')

#########################################################

#---------------- Body -----------------------#
#os.system("muscle -in test01.fa -clw") ##muscle -in test01.fa -clwout test01.clw
stream = os.popen("muscle -in test01.fa -clw")

print("Content-Type:text/html\n\n")
print(template.render(results = stream))
