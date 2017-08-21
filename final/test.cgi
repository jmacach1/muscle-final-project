#!/usr/local/bin/python3
#Jerald Macachor
#Advance Practical Computer Concepts for Bioinformatics
#August 19, 2017

#Project Final - Muscle Alignment Bioinformatics Tool
# This cgi script will execute a Muscle Alignment
# with sequences takent from index.html
# and print it on a jinja template (results.html)

import jinja2
import cgi
#---------------- HTML template -----------------------#

# This line tells the template loader where to search for template files
templateLoader = jinja2.FileSystemLoader(searchpath="./templates")

# This creates your environment and loads a specific template
env = jinja2.Environment(loader=templateLoader)
template = env.get_template('test_template.html')

#########################################################

#---------------- Body -----------------------#

print("Content-Type:text/html\n\n")
print(template.render())

#########################################################
