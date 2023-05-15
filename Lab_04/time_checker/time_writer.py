import os
import time


dir_path = "/data"  # шлях до каталогу для зберігання файлів

while True:
    current_time = time.strftime("%Y-%m-%d %H:%M:%S")  # поточний час з точністю до секунди
    current_time_file = current_time.replace(":", ".") # в імені txt файла не може бути двох крапок
    file_path = os.path.join(dir_path, f"{current_time_file}.txt")  # шлях до нового файла
  
    
    with open(file_path, "w") as f:   
        f.write(current_time)  # записати поточний час в файл
        f.close()       
  
  
 
    time.sleep(10)  # зачекати 10 секунд перед створенням наступного файлу
