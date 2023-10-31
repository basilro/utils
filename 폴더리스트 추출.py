import os

root_dir = '/mnt/ndrive/comic/책/[연재] 이미지'
output_file = '연재리스트.txt'

output_file = os.path.join(root_dir, output_file)

with open(output_file, 'w') as f:
    for subdir, dirs, files in os.walk(root_dir):
        for dir in dirs:
            print(dir)
            f.write(os.path.join(dir) + '\n')