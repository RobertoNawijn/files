__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"




#import module os
import os
#import shell utilities
import shutil
#to return absolute path
import os.path
# change the current working directory
# to specified path
os.chdir('C:\\winc\\files')
#opslaan definitie
currentPath = os.getcwd()
print(currentPath)
#directory name opslaan
directory_name = "cache"
#passing currentpath en dir name together
path = os.path.join (currentPath, directory_name)
#specify name of zipfile
zip_file = currentPath + "\\data.zip"
#function no arguments
def clean_cache():
    if os.path.exists(path):
    #if already exists, delete folder cache
     shutil.rmtree(path)
    #create empty folder named cache in curr dir
    os.mkdir(path)
    #uitvoeren functie
clean_cache()

#specified path

#import zipunpackfile
from zipfile import ZipFile
#function w 2 arguments in specfc order
def cache_zip(zip_file_path, cache_dir_path):
    #unpack zipfile into clean cache folder
    #open the zip_file in read mode
    with ZipFile(zip_file, "r") as zip_ref:
        #extract all files to another directory
        zip_ref.extractall("cache")
#cache_zip

#function no arguments(returns list of all the files in the cache)
def cached_files():
    #moet uiteindelijk n lijst opleveren dus
    files_list = []
    path = "C:\\winc\\files\\cache"
    os.path.abspath(".\cache")
    print(os.path.abspath(".\cache"))
    #for loop check every file make a path to every file
    #"path aangemaakt zodat hij absoluut blijft"   
    filenames = os.listdir(path)
    print (filenames)
    for filename in filenames:
        filepath = os.path.join(path, filename)
        files_list.append(filepath)
    #moet uiteindelijk gereturned worden
    print(files_list)
    return files_list



#definieer variabele word
word = "password"
#om list te bewaren die ik in cached_files hb gemaakt
list_of_files = cached_files()
#functie met een argument
def find_password(list_of_files):
    #itereer over files
    for file in list_of_files:
        with open(file, "r") as file_obj:
            lines = file_obj.readlines()
            print (lines)
            for line in lines:
            #zoek naar password
            #for word in files
                if word in line:
                    print(line)
                    #use split method to extract word from given string
    return word
find_password(cached_files())

   
       


