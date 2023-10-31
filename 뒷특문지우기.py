import os
import re

base_folder = "G:/내 드라이브/NAS/comic/책/[임시]/09 자"

for root, dirs, files in os.walk(base_folder):
    for folder_name in dirs:
        original_name = folder_name
        
        # 폴더 숫자 및 괄호 제거
        new_name = re.sub(r'\([^)]*\)', '', original_name).strip()
        new_name = re.sub(r'\d+[~\s-]*\d*.*$', '', original_name).strip()
        
        if new_name != original_name:
            original_path = os.path.join(root, folder_name)
            new_path = os.path.join(root, new_name)
            
            try:
                os.rename(original_path, new_path)
                print(f'폴더 이름 변경: {original_name} -> {new_name}')
            except Exception as e:
                print(f'폴더 이름 변경 실패: {original_name} -> {new_name}')
                print(f'에러 메시지: {str(e)}')
