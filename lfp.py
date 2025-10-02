#%%

import os 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from neo.io.blackrockio import BlackrockIO as bio

#%%

PROJECTS_DIR = '/home/henniglab/Documents/projects'
DATADIR = os.path.join(PROJECTS_DIR, 'data','ns5')
TASK_NAMES = ['podcast','pursuit','rotations','fortune']

#%%

os.listdir(os.path.join(DATADIR, 'pursuit'))
# %%
