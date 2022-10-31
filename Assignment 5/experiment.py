#=====================
#IMPORT MODULES
#=====================
import numpy as np
from psychopy import core, gui, visual, event
import json
import os
import random

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
#COLLECT PARTICIPANT INFO
#=====================
#-create a dialogue box that will collect current participant number, age, gender, handedness
#get date and time
#-create a unique filename for the data

#=====================
#STIMULUS AND TRIAL SETTINGS
#=====================
#-number of trials and blocks *
blocks = 2
trials = 10

#-stimulus names (and stimulus extensions, if images) *
stimulus_name = "face"
stimulus_extension = ".jpg"

#-stimulus properties like size, orientation, location, duration *
stimulus_height = 200
stimulus_width = 200
stimulus_orientation = "landscape"
stimulus_location = "center"
stimulus_duration = 1

#-start message text *
start_message = "Images will be shown to you for 1 seconds each to determine how long it takes you to find a face."

#=====================
#PREPARE CONDITION LISTS
#=====================
#-check if files to be used during the experiment (e.g., images) exist
#-create counterbalanced list of all conditions *
pics = []

for i in range(1,11):
    if i < 10:
        pics.append(stimulus_name + "0" + str(i) + stimulus_extension)
    else:
        pics.append(stimulus_name + str(i) + stimulus_extension)

#-check if files to be used during the experiment (e.g., images) exist
for pic in pics:
    if pic in os.listdir(image_dir):
        print(pic + " was found!")
    else:
        raise Exception("The image lists do not match up!")

#=====================
#PREPARE DATA COLLECTION LISTS
#=====================
#-create an empty list for correct responses (e.g., "on this trial, a response of X is #correct") *
correct_list = []

#-create an empty list for participant responses (e.g., "on this trial, response was a #X") *
response_list = []

#-create an empty list for response accuracy collection (e.g., "was participant #correct?") *
accuracy_list = []

#-create an empty list for response time collection *
response_time_list = []

#-create an empty list for recording the order of stimulus identities *
identity_order_list = []

#-create an empty list for recording the order of stimulus properties *
property_order_list = []

#=====================
#CREATION OF WINDOW AND STIMULI
#=====================
#-define the monitor settings using psychopy functions
#-define the window (size, color, units, fullscreen mode) using psychopy functions
#-define experiment start text unsing psychopy functions
#-define block (start)/end text using psychopy functions
#-define stimuli using psychopy functions
#-create response time clock
#-make mouse pointer invisible

#=====================
#START EXPERIMENT
#=====================
#-present start message text
#-allow participant to begin experiment with button press

#=====================
#BLOCK SEQUENCE
#=====================
#-for loop for nBlocks *
for i in range(blocks):
    #-present block start message
    #-randomize order of trials here *
    random.shuffle(pics)

    #-reset response time clock here
    
    #=====================
    #TRIAL SEQUENCE
    #=====================    
    #-for loop for nTrials *
    for j in range(trials):
        pass
        #-set stimuli and stimulus properties for the current trial
        #-empty keypresses
        
        #=====================
        #START TRIAL
        #=====================   
        #-draw stimulus
        #-flip window
        #-wait time (stimulus duration)
        #-draw stimulus
        #-...
        
        #-collect subject response for that trial
        #-collect subject response time for that trial
        #-collect accuracy for that trial
        
#======================
# END OF EXPERIMENT
#======================        
#-write data to a file
#-close window
#-quit experiment