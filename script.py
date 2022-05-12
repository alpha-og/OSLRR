import os
directory = r'...'  
files = [f for f in os.listdir(directory)]
for file in files:
    my_file = open(file, "r")
    file_content = my_file.read()
    my_file.close()
    my_file = open(file, "r")
    my_file.seek(0)
    my_file.write(f"""---
layout: default
title: (Example) {file[12:]}
nav_order: {file[7:9]}
has_children: true
---""" + file_content)
    my_file.close()