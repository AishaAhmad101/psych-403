#=====================
#IMPORT MODULES
#=====================
import numpy as np
from psychopy import core, gui, visual, event, gui, visual, monitors
import json
import os
import random
from datetime import datetime
import time

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
exp_info = {'subject_nr':0, 'age':0, 'handedness':('right','left','ambi'), 'gender':"", "session": 1}

my_dlg = gui.Dlg(title="Subject Info")
my_dlg.addText('exp_info')
my_dlg.addFixedField('session:',1) # doesn't allow user to change value from preset
my_dlg.addField('subject_nr:',0)
my_dlg.addField('age:',0)
my_dlg.addField('gender:', "")
my_dlg.addField('handedness:', choices=['right','left','ambi'])

print("All variables have been created! Now ready to show the dialog box!")
ok_data = my_dlg.show()

today_date = str(datetime.now())
ok_data.append(today_date)

filename = str(ok_data[1]) + '_' + today_date + '.csv'
sub_dir = os.path.join(main_dir,'sub_info',filename)

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
stimulus_height = 400
stimulus_width = 400
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
mon = monitors.Monitor('myMonitor', width=35.56, distance=60) 
mon.setSizePix([2736,1824])

#-define the window (size, color, units, fullscreen mode) using psychopy functions
win = visual.Window(monitor=mon, size=(800,800), color=[-1,-1,-1], units="pix", fullscr=False)

#-define experiment start text unsing psychopy functions
start_msg = 'Welcome to my experiment!'
start_text = visual.TextStim(win, text=start_msg)

#-define block (start)/end text using psychopy functions
start_msg = "Start of trial"
block_msg = "Press any key to continue to the next block."
end_trial_msg = "End of trial"

#-define stimuli using psychopy functions
start_text = visual.TextStim(win, text=start_msg) #text=start_msg is the same as writing text="Welcome to my experiment!"
block_text = visual.TextStim(win, text=block_msg)
end_trial_text = visual.TextStim(win, text=end_trial_msg)

#-create response time clock
#-make mouse pointer invisible

#=====================
#START EXPERIMENT
#=====================
#-present start message text
start_text.draw()
win.flip()

#-allow participant to begin experiment with button press
event.waitKeys()

#=====================
#BLOCK SEQUENCE
#=====================
#-for loop for nBlocks *
for block in range(blocks):
    #-present block start message
    block_text.draw()
    win.flip() 
    event.waitKeys()

    #-randomize order of trials here *
    random.shuffle(pics)
    
    #=====================
    #TRIAL SEQUENCE
    #=====================    
    #-for loop for nTrials *
    for trial in range(trials):
        #-set stimuli and stimulus properties for the current trial
        fix_text = visual.TextStim(win, text='+')
        pic_loc = os.path.join(image_dir,pics[trial]) #point to the specific image
        my_image = visual.ImageStim(win, image=pic_loc, size=(stimulus_height,stimulus_width))
        
        #=====================
        #START TRIAL
        #=====================
        #-draw fixation
        fix_text.draw()
        #-flip window
        win.flip()
        #-wait time (stimulus duration)
        time.sleep(stimulus_duration)
        
        #-draw image
        my_image.draw()
        #-flip window
        win.flip()
        #-wait time (stimulus duration)
        time.sleep(stimulus_duration)
        
        #-draw end trial text
        end_trial_text.draw()
        #-flip window
        win.flip()
        #-wait time (stimulus duration)
        time.sleep(stimulus_duration)
        
#======================
# END OF EXPERIMENT
#======================        
#-close window
win.close()