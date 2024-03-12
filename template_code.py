# string_template_py.py is a simple python code for having templates stand in for strings. example say, you create a word document with text as follows: 'my name is R, and I am 12 years'

#we can create a template such that 'my name is $name, and I am $age years'

#we can also import data set to fill in such string template and create a new word document or text file for each.

# the aim is to automate the boring and tedious stuff ;)
import os 
import pandas as pd
data_df = pd.DataFrame([ 
    ['Amankwah',24,'Techiman','Delali'],
    ['Emma',27,'Tech','Vicky']], columns=['names','age','town','ladies'])
print(data_df)
print('=================================')
import docx2txt
from docx import Document
from string import Template
doc_txt = docx2txt.process('template_trial.docx')
print(doc_txt)
print('==================================')
n_doc = Template(doc_txt)
print(type(n_doc))
os.mkdir('template_documents')
os.chdir('template_documents')
#code below is for the creation of docx files for the above template
for i,j,k,l in zip(list(data_df.names),list(data_df.age),list(data_df.town),list(data_df.ladies)):
    s = n_doc.substitute(name=i, age=j, town=k, ladies=l)
    doc_file = Document()
    doc_file.add_paragraph(s)
    doc_file.save(i+'.docx')
    

# code below is for the creation of txt files for the above template
'''for i,j,k,l in zip(list(data_df.names),list(data_df.age),list(data_df.town),list(data_df.ladies)):
    text_file = open(i+'.txt','w')
    s = n_doc.substitute(name=i, age=j, town=k, ladies=l)
    text_file.write(s)
    text_file.close()'''
