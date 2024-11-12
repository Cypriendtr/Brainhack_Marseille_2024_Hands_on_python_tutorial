from tqdm import tqdm
import time
import os

cwd = os.getcwd()

def progress_bar(min):
    
    duration = min*60
    
    for i in tqdm(range(duration)):
        time.sleep(1)