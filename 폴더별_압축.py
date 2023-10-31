import os
import shutil
from zipfile import ZipFile

#폴더별 압축 후 삭제
def compress_folders(folder_path):
    for root, dirs, _ in os.walk(folder_path, topdown=False):
        for directory in dirs:
            child_folder = os.path.join(root, directory)
            grandchild_folders = [os.path.join(child_folder, grandchild) for grandchild in os.listdir(child_folder)]

            for grandchild in grandchild_folders:
                if os.path.isdir(grandchild):
                    with ZipFile(f"{grandchild}.zip", "w", allowZip64=True) as zipf:
                        for foldername, subfolders, filenames in os.walk(grandchild):
                            for filename in filenames:
                                file_path = os.path.join(foldername, filename)
                                arcname = os.path.relpath(file_path, grandchild)
                                zipf.write(file_path, arcname)
                    shutil.rmtree(grandchild)
                    print(f"Compressed and deleted {grandchild}.zip")

if __name__ == "__main__":
    folder_to_search = "D:/webtoon/hitomi_downloaded_navertoon"
    compress_folders(folder_to_search)

