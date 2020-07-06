list_sections = ('Online tools for DMP',
'Existing data',
'File formats',
'Data volume',
'Datasets Sharing',
'Data Licenses',
'Metadata',
'Identifiers',
'Ontology',
'Documentation for metadata',
'Costs for sharing and storing data',
'Data quality',
'Personal data')

summary = "Empty summary"

example = "\n## Subtitle 1\n\nSome text that you can fill in"

for title in list_sections:

    permalinklink = title.lower().replace(" ", "_")

    header_md = f"---\ntitle: {title}\nkeywords:\nsummary: {summary}\nsidebar: mydoc_sidebar\npermalink: {permalinklink}.html\n---\n"

    with open(f'pages/{permalinklink}.md', 'w') as md:
        md.write(header_md)
        md.write(example)
    sidebar =  f"- title: {title}\n  url: /{permalinklink}.html\n  output: web"
    print (sidebar)