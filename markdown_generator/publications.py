
# coding: utf-8

# # Publications markdown generator for academicpages
# 
# Takes a TSV of publications with metadata and converts them for use with [academicpages.github.io](academicpages.github.io). This is an interactive Jupyter notebook, with the core python code in publications.py. Run either from the `markdown_generator` folder after replacing `publications.tsv` with one that fits your format.
# 
# TODO: Make this work with BibTex and other databases of citations, rather than Stuart's non-standard TSV format and citation style.
# 

# ## Data format
# 
# The TSV needs to have the following columns: pub_date, title, venue, excerpt, citation, site_url, and paper_url, with a header at the top. 
# 
# - `excerpt` and `paper_url` can be blank, but the others must have values. 
# - `pub_date` must be formatted as YYYY-MM-DD.
# - `url_slug` will be the descriptive part of the .md file and the permalink URL for the page about the paper. The .md file will be `YYYY-MM-DD-[url_slug].md` and the permalink will be `https://[yourdomain]/publications/YYYY-MM-DD-[url_slug]`


# ## Import pandas
# 
# We are using the very handy pandas library for dataframes.

# In[2]:

import pandas as pd


# ## Import TSV
# 
# Pandas makes this easy with the read_csv function. We are using a TSV, so we specify the separator as a tab, or `\t`.
# 
# I found it important to put this data in a tab-separated values format, because there are a lot of commas in this kind of data and comma-separated values can get messed up. However, you can modify the import statement, as pandas also has read_excel(), read_json(), and others.

# In[4]:

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

# In[5]:

import os
import json

with open('publications.json', 'r') as f:
  data = json.load(f)

publications = data["publications"]

for paper in publications:
    author_strings = []
    for author in paper["authors"]:
        first_name = author.split(" ")[0]
        last_name = author.split(" ")[1:]

        author_strings.append(f"{first_name[0]}. {' '.join(last_name)}")

    author_string = ", ".join(author_strings)

    paper_url = f"https://cassee.dev/files/{paper['filename']}"
    
    md_filename = paper["date"] + "-" + paper["id"] + ".md"
    html_filename = paper["date"] + "-" + paper["id"]
    year = paper["date"][:4]
    
    ## YAML variables
    
    md = "---\ntitle: \""   + paper["title"] + '"\n'
    
    md += """collection: publications"""
    
    md += """\npermalink: /publication/""" + html_filename

    md += "\nauthors: " + author_string 
    
    md += "\ndate: " + paper["date"]

    md += "\ntype: " + paper["type"]
    
    if "venue" in paper:
        md += "\nvenue: '" + html_escape(paper["venue"]) + "'"
    
    md += "\npaperurl: '" + paper_url + "'"

    if "slides_url" in paper >= 0:
        md += "\nslidesurl: '" + paper["slides_url"] + "'"      

    if "repo_url" in paper >= 0:
        md += "\nrepourl: '" + paper["repo_url"] + "'"
    
    
    md += "\n---"
    
    ## Markdown description for individual page
    
    md += "\n\n<a href='" + paper_url + "'>Download paper here</a>\n" 
        
    md_filename = os.path.basename(md_filename)
       
    with open("../_publications/" + md_filename, 'w') as f:
        f.write(md)