import os
import time


dir_path = "/data"  # шлях до каталогу для зберігання файлів

while True:
    files = os.listdir(dir_path)

    if len(files) == 0:
        print("No files found")
    else:
        for file_name in files:
            file_path = os.path.join(dir_path, file_name)

            with open(file_path, "r") as f:
                content = f.read()
                
            print(f"File: {file_name}, Content: {content}")
            
    time.sleep(30)