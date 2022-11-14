Answers to my question 
Dialogue box exercises:

1.

```
exp_info = {'subject_nr':0, 'age':0, 'handedness':('right','left','ambi'), 'gender':('male','female','other','prefer not to say'), "session": 1}
```

2.

```
exp_info = {'subject_nr':0, 'age':0, 'handedness':('right','left','ambi'), 'gender':"", "session": 1}
```

Using DlgFromDict:

1.

```
my_dlg = gui.Dlg(title="Subject Info")
```

2.

```
my_dlg.addFixedField('session:',1)
```

Value cannot be changed from initial value.

3.

```
my_dlg.addFixedField('session:',1) # doesn't allow user to change value from preset
my_dlg.addField('subject_nr:',0)
my_dlg.addField('age:',0)
my_dlg.addField('gender:', "")
my_dlg.addField('handedness:', choices=['right','left','ambi'])
```

4.

```
print("All variables have been created! Now ready to show the dialog box!")
ok_data = my_dlg.show()
```

5.

```
#=====================
#COLLECT PARTICIPANT INFO
#=====================
#-create a dialogue box that will collect current participant number, age, gender, handedness
exp_info = {'subject_nr':0, 'age':0, 'handedness':('right','left','ambi'),
            'gender':('male','female','other','prefer not to say')}
my_dlg = gui.DlgFromDict(dictionary=exp_info)

#get date and time
exp_info["datetime"] = str(datetime.now())

#-create a unique filename for the data
filename = str(exp_info['subject_nr']) + '_' + exp_info['date'] + '.csv'
sub_dir = os.path.join(main_dir,'sub_info',filename)
```

Monitor and window exercises:

1. When you change the units you change the size of the window because different units have different sizes for example 1cm is not the same as 1px.
2. ColorSpace allows you to define the format you're using for your color. For example if oyu want to define colors in the RGB format you would set colorSpace to 'rgb'. Colors defined in the rgb colorspace would look different in the rgb255 colorspace. You can define colors by name.
3.

```
#=====================
#CREATION OF WINDOW AND STIMULI
#=====================
#-define the monitor settings using psychopy functions
mon = monitors.Monitor('myMonitor', width=35.56, distance=60)
mon.setSizePix([2736,1824])

#-define the window (size, color, units, fullscreen mode) using psychopy functions
win = visual.Window(monitor=mon, size=(800,800), color=[-1,-1,-1], units="pix", fullscr=True)
```

Stimulus exercises:

1.

```
my_image = visual.ImageStim(win, image=pic_loc, size=(400,400))
```

This compresses some images that are not perfectly square. To keep proper image dimensions we need to change only height or width.

2.

```
mon = monitors.Monitor('myMonitor', width=35.56, distance=60)
mon.setSizePix([2736,1824])

window_size = 800
win = visual.Window(monitor=mon, size=(window_size,window_size), color=[-1,-1,-1], units="pix", fullscr=True)

position_list = [[-window_size/4,window_size/4], [window_size/4,window_size/4], [window_size/4,-window_size/4], [-window_size/4,-window_size/4]]

for i in range(len(position_list)):
    pic_loc = os.path.join(image_dir,pics[i]) #point to the specific image
    my_image = visual.ImageStim(win, image=pic_loc, size=(stimulus_height, stimulus_width), pos=position_list[i])

    my_image.draw()
    win.flip()
    time.sleep(stimulus_duration)
```

We can calculate window location without trial-and-error by dividing window_size by 4 and setting appropriate negative values

3.

```
fix_text = visual.TextStim(win, text='+')
```

4.

```
#=====================
#CREATION OF WINDOW AND STIMULI
#=====================
#-define experiment start text unsing psychopy functions
start_msg = "Start of trial"

#-define block (start)/end text using psychopy functions
block_msg = "Press any key to continue to the next block."
end_trial_msg = "End of trial"

#-define stimuli using psychopy functions
start_text = visual.TextStim(win, text=start_msg) #text=start_msg is the same as writing text="Welcome to my experiment!"
block_text = visual.TextStim(win, text=block_msg)
end_trial_text = visual.TextStim(win, text=end_trial_msg)

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
        my_image = visual.ImageStim(win, image=pic_loc)

        #=====================
        #START TRIAL
        #=====================
        #-draw fixation
        fix_text.draw()
        #-flip window
        win.flip()
        #-wait time (stimulus duration)
        event.waitKeys()

        #-draw image
        my_image.draw()
        #-flip window
        win.flip()
        #-wait time (stimulus duration)
        event.waitKeys()

        #-draw end trial text
        end_trial_text.draw()
        #-flip window
        win.flip()
        #-wait time (stimulus duration)
        event.waitKeys()

#======================
# END OF EXPERIMENT
#======================
#-close window
win.close()
```
