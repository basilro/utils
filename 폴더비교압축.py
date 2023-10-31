import os
import shutil
import zipfile

path_a = "G:/내 드라이브/NAS/범철/down/hitomi_down_webtoon\hitomi_downloaded_kakaowebtoon"
path_b = "G:/내 드라이브/NAS/comic/업데이트웹툰"

A_folder_list = os.listdir(path_a)
B_folder_list = os.listdir(path_b)

all_cnt = len(A_folder_list)
now_cnt = 0

# A폴더에만 있는 폴더를 찾아서 B폴더에 생성
for folder_name in A_folder_list:
    now_cnt = now_cnt + 1
    print(folder_name)
    print(str(now_cnt) + '/' + str(all_cnt))
    if folder_name == 'desktop.ini': continue
    if folder_name not in B_folder_list:
        new_folder_path = os.path.join(path_b, folder_name)
        os.mkdir(new_folder_path)

    folder_names = []
    zip_names = []

    for root, dirs, files in os.walk(os.path.join(path_a,folder_name)):
        for name in dirs:
            folder_names.append(name)

    for filename in os.listdir(os.path.join(path_b,folder_name)):
        if filename.endswith(".zip"):
            zip_names.append(filename.split("#")[0].replace('.zip',''))

    # A 폴더에 존재하는 폴더 중, B 폴더에 해당하는 압축파일이 없는 경우에만 압축파일 생성
    for sub_folder_name in folder_names:
        # print(sub_folder_name)
        if sub_folder_name not in zip_names:
            print(os.path.join(folder_name,sub_folder_name))
            with zipfile.ZipFile(os.path.join(path_a, folder_name, f"{sub_folder_name}.zip"), 'w', zipfile.ZIP_DEFLATED) as zipf:
                for root, dirs, files in os.walk(os.path.join(path_a, folder_name, sub_folder_name)):
                    for file in files:
                        zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), os.path.join(path_a, folder_name, sub_folder_name)))
                        
            shutil.move(os.path.join(path_a, folder_name, f"{sub_folder_name}.zip"), os.path.join(path_b, folder_name, f"{sub_folder_name}.zip"))