

import os

study_Mat_Dir = r'study_Material'

IGNORE = [".DS_Store", "jpg", "png","images"]

study_Mat_Contents = [f for f in os.listdir(study_Mat_Dir) if f not in IGNORE]


for grade in study_Mat_Contents:
    subjects_path = os.path.join(study_Mat_Dir,grade)
    subjects = [sub for sub in os.listdir(subjects_path) if sub not in IGNORE]
    for subject in subjects:
        chapters_path = os.path.join(subjects_path,subject)
        chapters = [chap for chap in os.listdir(chapters_path) if chap not in IGNORE]
        for chapter in chapters:
            topics_path = os.path.join(chapters_path,chapter)
            topics = [tpc for tpc in os.listdir(topics_path) if tpc not in IGNORE]
            for topic in topics:
                if "MOC" in topic:
                    title = chapter[7:]
                    nav_order = int(chapter[2:4])
                    liquid = f"""---
layout: default
title: {title} - MOC
nav_order: {nav_order}
has_children: true
---\n"""
                else:
                    title = topic[12:].strip('.md')
                    nav_order = int(topic[7:9])
                    liquid = f"""---
layout: default
title: {title}
parent: {chapter[7:]} - MOC
nav_order: {nav_order}
---\n"""
                writeTo_Dir = f'github_Pages_Docs/{grade}/{subject}/{chapter}/'
                
                #making directory for docs if no directory exists
                try: os.makedirs(writeTo_Dir)
                except:pass

                github_PathToMD = os.path.join(writeTo_Dir, topic)
                study_Mat_Notes_PathToMD = os.path.join(topics_path, topic)
                
                #reading content of original notes
                with open(study_Mat_Notes_PathToMD, 'r') as file:
                    contents = file.read()
                
                #creating and writing to file in github_Pages_Docs
                with open(github_PathToMD,'w') as file:
                    file.write(liquid)
                    file.write(contents)