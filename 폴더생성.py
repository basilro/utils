import os
import re
import logging

path = '/mnt/gdrive/comic/책/[다운]'

def remove_brackets(file_name):
    return (re.sub(r"\[.*?\]", "", file_name)).strip()

for filename in os.listdir(path):
    if filename.endswith('.txt'):
        print("dir name : " + remove_brackets(filename.split('.txt')[0].replace('+',' ').replace('_',' ')))
        dir_name = remove_brackets(filename.split('.txt')[0].replace('+',' ').replace('_',' '))
        os.makedirs(os.path.join(path, dir_name), exist_ok=True)
        os.rename(os.path.join(path, filename), os.path.join(path, dir_name, filename.replace('+',' ').replace('_',' ')))
    elif filename.endswith('.epub'):
        print("dir name : " + remove_brackets(filename.split('.epub')[0].replace('+',' ').replace('_',' ')))
        dir_name = remove_brackets(filename.split('.epub')[0].replace('+',' ').replace('_',' '))
        os.makedirs(os.path.join(path, dir_name), exist_ok=True)
        os.rename(os.path.join(path, filename), os.path.join(path, dir_name, filename.replace('+',' ').replace('_',' ')))

print("폴더생성 종료")