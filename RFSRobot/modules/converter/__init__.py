from os import listdir, mkdir
from .converter import convert

if "raw_files" not in listdir(): mkdir("raw_files")
if "downloads" not in listdir(): mkdir("downloads")
