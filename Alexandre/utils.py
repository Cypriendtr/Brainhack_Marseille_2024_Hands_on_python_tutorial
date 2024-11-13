import tqdm
import time
import os

cwd = os.getcwd()

def func_timer(duration:float):
    """
    Parameters
    ---------
    duration : Duration in minutes
    Returns
    ---------
    Progress bar of the duration referenced
    """

    dur_sec = duration * 60
    for i in tqdm.trange(dur_sec, ncols=90, desc="Exercise timer", ascii="_|"):
        time.sleep(1)