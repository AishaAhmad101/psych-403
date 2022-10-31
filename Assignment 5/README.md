Experiment structure exercises:

See attached file

Import exercises:

import numpy as np
from psychopy import core, gui, visual, event
import json
import os
import random

Directory exercises:

#=====================
#PATH SETTINGS
#=====================
#-define the main directory where you will keep all of your experiment files
main_dir = os.getcwd()

#-define the directory where you will save your data
data_dir = os.path.join(main_dir,'data')

#-if you will be presenting images, define the image directory
image_dir = os.path.join(main_dir,'images')

#-check that these directories exist
print(os.path.isdir(data_dir))
print(os.path.isdir(image_dir))

#=====================
#PREPARE CONDITION LISTS
#=====================
#-check if files to be used during the experiment (e.g., images) exist
for pic in pics:
if pic in os.listdir(image_dir):
print(pic + " was found!")
else:
raise Exception("The image lists do not match up!")
