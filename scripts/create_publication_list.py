import pandas as pd

def generate_html_list(input_excel, output_file):
    # Read the Excel file
    df = pd.read_excel(input_excel)
    
    # Sort by pub_year (newest to oldest)
    df = df.sort_values(by="pub_year", ascending=False)
    
    # Open the output file in write mode
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("<ol>\n")  # Start ordered list
        previous_year = None
        
        for _, row in df.iterrows():
            parts = []
            
            # Check for new year header
            if pd.notna(row.get("pub_year")) and row["pub_year"] != "MISSING":
                current_year = row["pub_year"]
                if current_year != previous_year:
                    f.write(f"<h2>{current_year}</h2>\n")
                    previous_year = current_year
            
            # Process authors if available and not 'MISSING'
            if pd.notna(row.get("authors")) and row["authors"] != "MISSING":
                if ';' in row["authors"]:
                    authors = row["authors"].split(';')  # Split by ';'
                    formatted_authors = []
                    for name in authors:
                        formatted_name = " ".join(name.strip().split(", ")[::-1])  # Swap first and last names
                        formatted_name = formatted_name.replace("Anoop Kunchukuttan", "<b>Anoop Kunchukuttan</b>")
                        formatted_authors.append(formatted_name)
                    authors_str = ", ".join(formatted_authors).rstrip(',')  # Join back with ',' and remove trailing comma
                    parts.append(authors_str)
                else:
                    author_name = row["authors"].replace("Anoop Kunchukuttan", "<b>Anoop Kunchukuttan</b>")
                    parts.append(author_name)  # Keep as is if no ';'
            
            if pd.notna(row.get("title")) and row["title"] != "MISSING":
                parts.append(f"<i>{row['title']}</i>")
            
            if pd.notna(row.get("conference")) and row["conference"] != "MISSING":
                parts.append(f"{row['conference']}")
            
            if pd.notna(row.get("pub_url")) and row["pub_url"] != "MISSING":
                parts.append(f'<a href="{row["pub_url"]}">[paper]</a>')
            
            # Generate and write HTML list item only if there are valid parts
            if parts:
                html_line = f'<li> {". ".join(parts)} </li>\n'
                f.write(html_line)
        f.write("</ol>\n")  # End ordered list

# Example usage
generate_html_list("anoop_publications.xlsx", "output.html")
