import os
import urllib.request
import gzip
import shutil

def load_dataset(data_dir="data"):

    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    
    txt_path = os.path.join(data_dir, "web-Google.txt")
    
    if not os.path.exists(txt_path):
       print("Data doesnot exist.")
        
    else:
        print("Dataset already exists.")
        
    return txt_path
