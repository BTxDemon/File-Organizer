import shutil
import psutil
import os

disk = 'C:\\Users\\Piyush Kumar\\Desktop'

extension = {
        '.mp3': 'Mp3 Files',
        '.mp4': 'Mp4 Files',
        '.mkv': 'Mp4 Files',
        '.jpg': 'Important Images',
        '.jpeg': 'Important Images',
        '.png': 'Images',
        '.PNG': 'Images',
        '.pdf': 'Pdf Files',
        '.txt': 'Text Files'
    }

for files in os.listdir(disk):
    for ext in extension:
        if (files.endswith(ext)):
            key = files[-(len(ext)):]

            src_path = os.path.join(disk, files)
            if (os.path.isdir(f'{disk}\\{extension[key]}')):
                pass
            else:
                os.mkdir(f'{disk}\\{extension[key]}')
            
            shutil.move(src_path, f'{disk}\\{extension[key]}')
            print(f'Succesfully Moved : {files}')