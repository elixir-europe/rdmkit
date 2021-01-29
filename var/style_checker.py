import os
import re

pagesdir = 'pages/'
white_list= ['Data Management Plan', 'Data Management Planning', 'Data Management', 'DMP', 'RDMKit', 'I', 'NeLS', 'ELIXIR', 'IT']

for subdir, dirs, files in os.walk(pagesdir):
    for file_name in files:
        if os.path.splitext(file_name)[1] == '.md':
            with open(subdir + file_name) as f:
                read_data = f.readlines()
                for line in read_data:
                    if line 