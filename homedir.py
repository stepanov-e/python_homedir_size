import os
import shutil
import datetime

def get_directory_size(directory):
    total_size = 0
    for dirpath, _, filenames in os.walk(directory):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            if os.path.exists(filepath):
              total_size += os.path.getsize(filepath)
    return total_size


directory = "/home/"
script_dir = os.path.dirname(os.path.abspath(__file__))
userdir = os.listdir(directory)


i=0
while i < len(userdir):
  size_in_bytes = get_directory_size('/home/'+userdir[i])
  size_in_mb = int(size_in_bytes / (1024 * 1024))
  current_date = datetime.datetime.now()

  with open(script_dir+'/homedirs_python.txt', 'a') as file:
    file.write(f"{current_date} size {size_in_mb} Mb (size in bytes: {size_in_bytes}) {directory}{userdir[i]}\n")
  with open(script_dir+'/homedirs_python.html', 'a') as file:
    file.write(f"{current_date} &nbsp&nbsp size {size_in_mb} Mb (size in bytes: {size_in_bytes}) &nbsp&nbsp {directory}{userdir[i]}<br>\n")

  i += 1


source_file = script_dir+"/homedirs_python.html"
destination_file = "/var/www/html/homedirs_python.html"

shutil.copy(source_file, destination_file)
