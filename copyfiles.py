import glob
import os
import shutil

src = '.'
dest = r'/Volumes/Seagate Backup Plus Drive/VPN-forwarded_Honeypots_Dataset/HTTP_logs'

for file_path in glob.glob(os.path.join(src, '**', '*http*'), recursive=True):
    new_path = os.path.join(dest, os.path.basename(file_path))
    shutil.copy(file_path, new_path)
    print('Done', file_path)
