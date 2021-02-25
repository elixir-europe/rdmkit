import os
import re

pagesdir = 'pages'
white_list= ['Google', 'Research Data Management Kit', 'Data Management Plan', 'Data Management Planning', 'DMP', 'RDMKit', 'I ', 'NeLS', 'ELIXIR', 'GitHub']

for subdir, dirs, files in os.walk(pagesdir):
    for file_name in files:
        if os.path.splitext(file_name)[1] == '.md':
            with open(subdir + '/' + file_name) as f:
                read_data = f.readlines()
                for i,line in enumerate(read_data):
                    title = re.search(r'^title: (.*)\n', line)
                    heading = re.search(r'^#+ (.*)\n', line)
                    if title or heading:
                        if title:
                            pro_line = line.replace(title.group(1), title.group(1).capitalize())
                        else:
                            pro_line = line.replace(heading.group(1), heading.group(1).capitalize())

                        for key in white_list:
                            if key.lower() in pro_line:
                                pro_line = pro_line.replace(key.lower(), key)
                        read_data[i] = pro_line
            with open(subdir + '/' + file_name, 'w') as ff:
                ff.writelines(read_data)
