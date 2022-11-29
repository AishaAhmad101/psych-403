PsychoPy keypress exercises:

1.

```
from psychopy import core, event, visual, monitors

mon = monitors.Monitor('myMonitor', width=35.56, distance=60)
mon.setSizePix([1920, 1080])
win = visual.Window(monitor=mon, size=(400,400), color=[-1,-1,-1])

nTrials=10
my_text=visual.TextStim(win)
fix=visual.TextStim(win, text='+')

for trial in range(nTrials):

    keys = event.getKeys(keyList=['1','2']) #put getkeys HERE
    my_text.text = "trial %i" %trial #insert integer into the string with %i

    fix.draw()
    win.flip()
    core.wait(2)

    event.clearEvents() #clear events HERE

    my_text.draw()
    win.flip()
    core.wait(1)

    print("keys that were pressed", keys) #which keys were pressed?

    if keys:
        sub_resp = keys[0] #only take first response

    print("response that was counted", sub_resp)

win.close()
```

2.  If you put event.ClearEvents inside the trial loop it clears the keys in between the trials. If we unindent the line after "if keys:" we will get an indentation error because something needs to be indented after an if statement. Assuming we also remove the if statement after unindenting the line after "if keys:" we will get an error if the user inputs no keys as we will be trying to access index 0 of nothing.


Recording data exercises:

1.

```
from psychopy import core, event, visual, monitors

#monitor specs
mon = monitors.Monitor('myMonitor', width=35.56, distance=60)
mon.setSizePix([1920, 1080])
win = visual.Window(monitor=mon, size=(400,400), color=[-1,-1,-1])

#blocks, trials, stims, and clocks
nBlocks=2
nTrials=4
my_text=visual.TextStim(win)
rt_clock = core.Clock()  # create a response time clock
cd_timer = core.CountdownTimer() #add countdown timer

#prefill lists for responses
experiment_data = {'keys': [], 'subjectRT': [[0]*nTrials]*nBlocks, 'subjectAcc': [[0]*nTrials]*nBlocks, 'correct': [[0]*nTrials]*nBlocks}
prob = [[0]*nTrials]*nBlocks

#create problems and solutions to show
math_problems = ['1+3=','1+1=','3-2=','4-1='] #write a list of simple arithmetic
solutions = [4,2,1,3] #write solutions
prob_sol = list(zip(math_problems,solutions))

for block in range(nBlocks):
    for trial in range(nTrials):
        #what problem will be shown and what is the correct response?
        prob[block][trial] = prob_sol[np.random.choice(4)]
        experiment_data['correct'[block][trial]] = prob[block][trial][1]

        rt_clock.reset()  # reset timing for every trial
        cd_timer.add(3) #add 3 seconds

        event.clearEvents(eventType='keyboard')  # reset keys for every trial

        count=-1 #for counting keys
        while cd_timer.getTime() > 0: #for 3 seconds

            my_text.text = prob[block][trial][0] #present the problem for that trial
            my_text.draw()
            win.flip()

            #collect keypresses after first flip
            keys = event.getKeys(keyList=['1','2','3','4','escape'])

            if keys:
                count=count+1 #count up the number of times a key is pressed

                if count == 0: #if this is the first time a key is pressed
                    #get RT for first response in that loop
                    experiment_data["subjectRT"[block][trial]] = rt_clock.getTime()
                    #get key for only the first response in that loop
                    experiment_data['subjectRT'[block][trial]] = keys[0] #remove from list

        #record subject accuracy
        #correct- remembers keys are saved as strings
        if experiment_data['subjectRT'[block][trial]] == str(experiment_data['correct'[block][trial]]):
            experiment_data['subjectAcc'[block][trial]] = 1 #arbitrary number for accurate response
        #incorrect- remember keys are saved as strings
        elif experiment_data['subjectRT'[block][trial]] != str(experiment_data['correct'[block][trial]]):
            experiment_data['subjectAcc'[block][trial]] = 2 #arbitrary number for inaccurate response
                                    #(should be something other than 0 to distinguish
                                    #from non-responses)

        experiment_data[keys].extend(keys)

        #print results
        print('problem=', prob[block][trial], 'correct response=',
              experiment_data['correct'[block][trial]], 'subject response=',experiment_data['subjectRT'[block][trial]],
              'subject accuracy=',experiment_data['subjectAcc'[block][trial]])

win.close()
```

2.

```
from psychopy import core, event, visual, monitors

#monitor specs
mon = monitors.Monitor('myMonitor', width=35.56, distance=60)
mon.setSizePix([1920, 1080])
win = visual.Window(monitor=mon, size=(400,400), color=[-1,-1,-1])

#blocks, trials, stims, and clocks
nBlocks=2
nTrials=4
my_text=visual.TextStim(win)
rt_clock = core.Clock()  # create a response time clock
cd_timer = core.CountdownTimer() #add countdown timer

#create problems and solutions to show
math_problems = ['1+3=','1+1=','3-2=','4-1='] #write a list of simple arithmetic
solutions = [4,2,1,3] #write solutions
prob_sol = list(zip(math_problems,solutions))

for block in range(nBlocks):
    #prefill lists for responses
    experiment_data = {'keys': [], 'subjectRT': [], 'subjectAcc': [], 'correct': []}
    prob = []

    for trial in range(nTrials):
        #what problem will be shown and what is the correct response?
        prob[trial] = prob_sol[np.random.choice(4)]
        experiment_data['correct'[trial]] = prob[trial][1]

        rt_clock.reset()  # reset timing for every trial
        cd_timer.add(3) #add 3 seconds

        event.clearEvents(eventType='keyboard')  # reset keys for every trial

        count=-1 #for counting keys
        while cd_timer.getTime() > 0: #for 3 seconds

            my_text.text = prob[trial][0] #present the problem for that trial
            my_text.draw()
            win.flip()

            #collect keypresses after first flip
            keys = event.getKeys(keyList=['1','2','3','4','escape'])

            if keys:
                count=count+1 #count up the number of times a key is pressed

                if count == 0: #if this is the first time a key is pressed
                    #get RT for first response in that loop
                    experiment_data['subjectRT'[trial]] = rt_clock.getTime()
                    #get key for only the first response in that loop
                    experiment_data['subjectRT'[trial]] = keys[0] #remove from list

        #record subject accuracy
        #correct- remembers keys are saved as strings
        if experiment_data['subjectRT'[trial]] == str(experiment_data['correct'[trial]]):
            experiment_data['subjectAcc'[trial]] = 1 #arbitrary number for accurate response
        #incorrect- remember keys are saved as strings
        elif experiment_data['subjectRT'[trial]] != str(experiment_data['correct'[trial]]):
            experiment_data['subjectAcc'[trial]] = 2 #arbitrary number for inaccurate response
                                    #(should be something other than 0 to distinguish
                                    #from non-responses)

        #print results
        print('problem=', prob[trial], 'correct response=',
              experiment_data['correct'[trial]], 'subject response=',experiment_data['subjectRT'[trial]],
              'subject accuracy=',experiment_data['subjectAcc'[trial]])

win.close()
```

Save csv exercises:

1.

```
import csv

# run experiment

experiment_data = {"keys": [1, 2, 3, 4], "subjectRT": [
    0.1, 0.2, 0.3, 0.4], "subjectAcc": [1, 1, 2, 2], "correct": [True, True, False, False]}

with open('csv_export.csv', 'w', newline='') as csvfile:
    fieldnames = list(experiment_data.keys())
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow(experiment_data)
```

Save json exercises:

1.

```
import json

# run experiment

experiment_data = {"keys": [1, 2, 3, 4], "subjectRT": [
    0.1, 0.2, 0.3, 0.4], "subjectAcc": [1, 1, 2, 2], "correct": [True, True, False, False]}

with open("json_export.json", 'w') as outfile:
    json.dump(experiment_data, outfile)
```

Read JSON exercises

1.

```
import pandas as pd

df = pd.read_json("json_export.json")
print(df)

print(sum(df.subjectRT)/len(df.subjectRT))
```

2.

```
import pandas as pd

df = pd.read_json("json_export.json")
print(df)

acc_trials = df.loc[df['correct'] == True]
print(acc_trials)

print(sum(acc_trials.subjectRT)/len(acc_trials.subjectRT))
```

3.

```
import pandas as pd

df = pd.read_json("json_export.json")
print(df)

acc_trials = df.loc[df['response'] != 0]
print(acc_trials)

print(sum(acc_trials.subjectRT)/len(acc_trials.subjectRT))

```
