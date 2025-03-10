import pandas as pd


def generate_html_list(input_excel, output_file):
    # Read the Excel file
    df = pd.read_excel(input_excel)
    
    # Sort by pub_year (newest to oldest)
    df = df.sort_values(by="pub_year", ascending=False)
    
    # Extract and clean unique keywords
    all_keywords = set()
    for keywords in df["keyword"].dropna():
        all_keywords.update(keywords.split('/'))
    keywords = sorted(all_keywords)
    
    # Open the output file in write mode
    with open(output_file, 'w', encoding='utf-8') as f:
        # Generate keyword filters in a compact horizontal layout
        f.write("<h2>Filter by Research Area:</h2>\n")
        f.write("<div style='display: flex; flex-wrap: wrap; gap: 10px;'>\n")
        f.write("<button onclick=\"filterList('all')\">Show All</button>\n")
        for keyword in keywords:
            f.write(f"<button onclick=\"filterList('{keyword}')\">{keyword}</button>\n")
        f.write("</div>\n")
        
        f.write("<ol id='publicationList' style='padding-left: 20px;'>\n")  # Start ordered list
        
        year_headers = {}
        publication_lines = []
        
        for _, row in df.iterrows():
            parts = []
            
            if pd.notna(row.get("title")) and row["title"] != "MISSING":
                parts.append(f"<div><b style='color: green;'>{row['title']}</b></div>")
            
            # Process authors if available and not 'MISSING'
            if pd.notna(row.get("authors")) and row["authors"] != "MISSING":
                if ';' in row["authors"]:
                    authors = row["authors"].split(';')  # Split by ';'
                    formatted_authors = []
                    for name in authors:
                        formatted_name = " ".join(name.strip().split(", ")[::-1])  # Swap first and last names
                        formatted_name = formatted_name.replace("Anoop Kunchukuttan", "<u>Anoop Kunchukuttan</u>")
                        formatted_authors.append(formatted_name)
                    authors_str = ", ".join(formatted_authors).rstrip(',')  # Join back with ',' and remove trailing comma
                    parts.append(f"<div>{authors_str}</div>")
                else:
                    author_name = row["authors"].replace("Anoop Kunchukuttan", "<u>Anoop Kunchukuttan</u>")
                    parts.append(f"<div>{author_name}</div>")  # Keep as is if no ';'
            
            if pd.notna(row.get("conference")) and row["conference"] != "MISSING":
                conference_text = f"<b>{row['conference']}</b>"
                if pd.notna(row.get("pub_year")) and row["pub_year"] != "MISSING":
                    conference_text += f", {row['pub_year']}"
                parts.append(f"<div>{conference_text}</div>")
            
            if pd.notna(row.get("pub_url")) and row["pub_url"] != "MISSING":
                parts.append(f"<div><a href='{row['pub_url']}'>[paper]</a></div>")
            
            # Get keywords for filtering
            keyword_classes = []
            if pd.notna(row.get("keyword")) and row["keyword"] != "MISSING":
                keyword_classes = [kw.strip().replace(" ", "_") for kw in row["keyword"].split('/')]
            keyword_class_str = " ".join(keyword_classes)
            
            # Generate and store HTML list item only if there are valid parts
            if parts:
                year = row["pub_year"] if pd.notna(row.get("pub_year")) and row["pub_year"] != "MISSING" else "Unknown"
                if year not in year_headers:
                    year_headers[year] = f'<h2 class="year-header {year}">{year}</h2>\n'
                html_line = f'<li class="publication-item {keyword_class_str} {year}" style="margin-bottom: 15px;">\n' + "\n".join(parts) + "\n</li>\n"
                publication_lines.append((year, html_line))
        
        # Write filtered publication list
        written_years = set()
        for year, line in publication_lines:
            if year not in written_years:
                f.write(year_headers[year])
                written_years.add(year)
            f.write(line)
        
        f.write("</ol>\n")  # End ordered list
        
        # Add JavaScript for filtering with year visibility control
        f.write("""
        <script>
        function filterList(keyword) {
            let items = document.querySelectorAll('.publication-item');
            let years = document.querySelectorAll('.year-header');
            let visibleYears = new Set();
            
            items.forEach(item => {
                let classes = item.className.split(" ");
                let keywordMatch = (keyword === 'all' || classes.includes(keyword.replace(" ", "_")));
                
                if (keywordMatch) {
                    item.style.display = '';
                    visibleYears.add(classes[classes.length - 1]); // Capture the year class
                } else {
                    item.style.display = 'none';
                }
            });
            
            years.forEach(year => {
                let yearClass = year.classList[1];
                if (visibleYears.has(yearClass)) {
                    year.style.display = '';
                } else {
                    year.style.display = 'none';
                }
            });
        }
        </script>
        """)

# Example usage
generate_html_list("my_publications.xlsx", "my_publications.html")
