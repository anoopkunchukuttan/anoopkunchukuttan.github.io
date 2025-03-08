import pandas as pd

def generate_html_from_excel(file_path, output_file):
    # Read Excel file
    df = pd.read_excel(file_path)
    
    # Define the custom order for sections with singular names
    section_order = {
        "Tutorial": "Tutorials",
        "Keynote": "Keynotes",
        "Invited Talk": "Invited Talks",
        "Course Lecture": "Course Lectures"
    }
    
    # Initialize HTML content
    html_content = ""
    
    for singular_name, plural_name in section_order.items():
        group = df[df["type"] == singular_name]
        if not group.empty:
            html_content += f'<h2>{plural_name}</h2>\n'
            
            for _, row in group.iterrows():
                talk_title = f'<b><span style="color:green;">{row["talk_title"]}</span></b>'
                venue = f'<i>{row["venue"]}</i>'
                collaborators = f' with <i>{row["collaborators"]}</i>' if pd.notna(row["collaborators"]) else ""
                date = f'{row["date"]}'
                
                links = []
                if pd.notna(row["slides"]):
                    slides_link =  f"/files/{row['slides']}" if  row["slides"].find("http")!=0 else row["slides"]
                    links.append(f'<a href="{slides_link}">[slides]</a>')
                if pd.notna(row["video"]):
                    links.append(f'<a href="{row["video"]}">[video]</a>')
                links_line = " ".join(links)
                
                paragraph = f'<p>{talk_title}<br>{venue}{collaborators}<br>{date}<br>{links_line}</p>'
                html_content += paragraph + "\n"
    
    # Write to output HTML file
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(html_content)

# Read from "my_talks.xlsx" and output to "my_talks.html"
file_path = "my_talks.xlsx"
output_file = "my_talks.html"
generate_html_from_excel(file_path, output_file)
