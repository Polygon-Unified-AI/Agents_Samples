from .cv_info_extractor import CvInfoExtractor, CvInfo

# on run, delete the temp folder
from shutil import rmtree
from os import path, mkdir

if path.exists("temp"):
    rmtree("temp")  

# recreate the temp folder
mkdir("temp")