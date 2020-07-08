list_sections = ('System Administration',
'Bioinformatician',
'Policy Support',
'Data Management Support',
'Planning',
'Collecting,
'Processing', 
'Analysing', 
'Publishing & Sharing', 
'Preserving',
'Storage', 
'Security & Privacy', 'Data Transfer', 'Metadata Management', 'Data Sustainability', 'Compliance Monitoring & Measurement')

summary = "Empty summary"

example = "\n## Subtitle 1\n\nSome text that you can fill in"

for title in list_sections:

    permalinklink = title.lower().replace(" ", "_")

    header_md = f"---\ntitle: {title}\nkeywords:\nsummary: {summary}\nsidebar: main\npermalink: {permalinklink}.html\n---\n"

    with open(f'pages/{permalinklink}.md', 'w') as md:
        md.write(header_md)
        md.write(example)
    sidebar =  f"- title: {title}\n  url: /{permalinklink}.html\n  output: web"
    print (sidebar)