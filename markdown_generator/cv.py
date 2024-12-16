## Takes as input the json files, and outputs nicely formatted text for my cv. 

import os
import json

with open('publications.json', 'r') as f:
  data = json.load(f)

publications = data["publications"]

output_publications = {}

for paper in publications:
    author_strings = []
    for author in paper["authors"]:
        first_name = author.split(" ")[0]
        last_name = author.split(" ")[1:]

        if str.strip(last_name[0]) == "Cassee":
            author_strings.append(f"\\textbf{{{first_name[0]}. {' '.join(last_name)}}}")
        else:
            author_strings.append(f"{first_name[0]}. {' '.join(last_name)}")

    author_string = ", ".join(author_strings)

    
    year = paper["date"][:4]

    if "venue" in paper:
        paper_string = f"\\years{{{year}}} {author_string} ({year}), ``{paper['title']}'' in {paper['venue']}. \\\\"
    else:
        paper_string = f"\\years{{{year}}} {author_string} ({year}), ``{paper['title']}''. \\\\"
    
    if paper["type"] not in output_publications:
        output_publications[paper["type"]] = []
        
    output_publications[paper["type"]].append(paper_string)

# Service

with open('service.json', 'r') as f:
  data = json.load(f)

service = data["data"]

known_service = ["Journal Review", "Program Committee", "Conference Organization"]

service_items = {}

for service_name in known_service:
    service_items[service_name] = []

for service in service:


    if service['type'] == "Journal Review":
        service_string = f"Reviewed for {service['description']}\\\\"
    elif service['type'] == "Program Committee":
        service_string = f"\\years{{{service['year']}}} {service['description']}\\\\"
    elif service['type'] == "Conference Organization":
        service_string = f"\\years{{{service['year']}}} {service['description']}\\\\"
    else:
        raise ValueError(f"Unrecognized service type: {service['type']}")

    service_items[service['type']].append(service_string)


# Output

print(f"\\section*{{Publications}}")

for key in output_publications:
    print(f"\\subsection*{{{key.capitalize()} Articles}}")
    for paper in output_publications[key]:
        print(paper)


print(f"\\section*{{Service}}")

for key in service_items:
    print(f"\\subsection*{{{key.capitalize()}}}")
    for service in service_items[key]:
        print(service)
    
    