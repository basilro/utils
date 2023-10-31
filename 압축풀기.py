import os
import zipfile
import py7zr

def extract_files(file_path):
    if file_path.endswith(".zip") or file_path.endswith(".7z"):
        if file_path.endswith(".zip"):
            with zipfile.ZipFile(file_path, "r") as zip_ref:
                files = zip_ref.namelist()
        else:
            with py7zr.SevenZipFile(file_path, mode='r') as zip_ref:
                files = zip_ref.getnames()

        for file in files:
            # print(os.path.splitext(file))
            extract_folder = os.path.join(os.path.dirname(file_path), os.path.splitext(os.path.basename(file_path))[0])
            print(extract_folder)
            if file.endswith('/'):
                folder_path = extract_folder
                os.makedirs(folder_path, exist_ok=True)

folder_path = "G:/내 드라이브/NAS/comic/책/[다운]/!테스트"

for root, dirs, files in os.walk(folder_path):
    for file in files:
        file_path = os.path.join(root, file)
        extract_files(file_path)
