import os
import chardet

folder_path = '/mnt/gdrive/comic/책/[다운]'

for filename in os.listdir(folder_path):
    if filename.endswith('.txt'):
        file_path = os.path.join(folder_path, filename)
        with open(file_path, 'rb') as f:
            result = chardet.detect(f.read())
        if result['encoding'] != 'utf-8':
            print(filename)
            with open(file_path, 'r', encoding=result['encoding'], errors='ignore') as f:
                contents = f.read()
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(contents)

print("인코딩변환 종료")