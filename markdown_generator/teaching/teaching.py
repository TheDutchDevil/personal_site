
# coding: utf-8


import pandas as pd


publications = pd.read_csv("teaching.csv", header=0)

publications = publications.fillna('')


# ## Escape special characters
# 
# YAML is very picky about how it takes a valid string, so we are replacing single and double quotes (and ampersands) with their HTML encoded equivilents. This makes them look not so readable in raw format, but they are parsed and rendered nicely.

html_escape_table = {
    "&": "&amp;",
    '"': "&quot;",
    "'": "&apos;"
    }

def html_escape(text):
    """Produce entities within text."""
    return "".join(html_escape_table.get(c,c) for c in text)


# ## Creating the markdown files
# 
# This is where the heavy lifting is done. This loops through all the rows in the TSV dataframe, then starts to concatentate a big string (```md```) that contains the markdown for each type. It does the YAML metadata first, then does the description for the individual page. If you don't want something to appear (like the "Recommended citation")


import os
for row, item in publications.iterrows():
    
    md_filename = str(item.date) + "-" + item.course_name + ".md"
    html_filename = str(item.date) + "-" + item.course_name
    year = item.when[:4]
    
    ## YAML variables
    
    md = "---\ncourse_name: \""   + item.course_name + '"\n'
    
    md += """collection: teaching"""
    
    md += """\npermalink: /teaching/""" + html_filename
    
    md += "\ndescription: '" + html_escape(item.course_description) + "'"
    
    md += "\nwhen: '" + str(item.when) +"'"

    md += "\ndate: " + str(item.date)
    
    md += "\nrole: '" + html_escape(item.course_role) + "'"
    
    md += "\n---"
    
    ## Markdown description for individual page
    
    
    md_filename = os.path.basename(md_filename)
       
    with open("../../_teaching/" + md_filename, 'w') as f:
        f.write(md)
