import os
import json

with open('service.json', 'r') as f:
  data = json.load(f)

service = data["data"]

for service in service:
    md_filename = f"{service['year']}-{service['description']}.md"

    md = "---\n"
    md += "collection: service\n"
    md += f"description: {service['description']}\n"
    md += f"year: {service['year']}\n"
    md += f"type: {service['type']}\n"
    
    md += "---"

    md_filename = os.path.basename(md_filename)
       
    with open("../_service/" + md_filename, 'w') as f:
        f.write(md)