import os
import shutil
import datetime

def backup_files(source_dir, destination_dir):
    today = datetime.date.today()
     
    #f=mean formeting string
    backup_files_name = os.path.join(destination_dir, f"backup_{today}.tar.gz")
    #backup_files_name.replace >> .tar.gz because shutil.make_archive will add it automatically
    shutil.make_archive (backup_files_name.replace('.tar.gz', ''), 'gztar',source_dir) #type of tar > gztar mean =tar+gzip 
    
    #print (f"Backup of {source_dir} completed successfully and saved to {backup_files_name}")


    print(backup_files_name)
    
source_directory = 'D:/Python-For-DevOps-Practice/backup'
 
destination_directory = 'D:/Python-For-DevOps-Practice/backup_files'

backup_files(source_directory,  destination_directory)