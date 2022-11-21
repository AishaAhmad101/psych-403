Wait Exercises

1.

```
#=====================
#START TRIAL
#=====================
#-draw fixation
fix_text.draw()
#-flip window
win.flip()
#-wait time (stimulus duration)
core.wait(stimulus_duration)

#-draw image
my_image.draw()
#-flip window
win.flip()
#-wait time (stimulus duration)
core.wait(stimulus_duration)

#-draw end trial text
end_trial_text.draw()
#-flip window
win.flip()
#-wait time (stimulus duration)
core.wait(stimulus_duration)
```

Clock Exercises

1.

```
nBlocks=2
nTrials=3

wait_timer = core.Clock()

for block in range(nBlocks):

    for trial in range(nTrials):
        wait_timer.reset()

        #-draw image
        my_image.draw()
        #-flip window
        win.flip()
        #-wait time (stimulus duration)
        core.wait(2)

        print(wait_timer.getTime())


win.close()
```

core.wait is pretty precise, it is only thousandths of seconds longer than the input time (2)

2.

```
nBlocks=2
nTrials=3

clock_wait_timer = core.Clock()

for block in range(nBlocks):

    for trial in range(nTrials):
        clock_wait_timer.reset()

        while clock_wait_timer.getTime() <=2:
            #-draw image
            my_image.draw()
            #-flip window
            win.flip()
            #-wait time (stimulus duration)

        print(clock_wait_timer.getTime())


win.close()
```

This is pretty precise but less precise than core.wait. This is usually hundredths of a second longer than the input time (2).

3.

```
nBlocks=2
nTrials=3

countdown_timer = core.CountdownTimer()

for block in range(nBlocks):

    for trial in range(nTrials):
        countdown_timer.reset()
        countdown_timer.add(2)

        while countdown_timer.getTime() > 0: #2 seconds
            my_image.draw() #draw
            win.flip() #show


win.close()
```

This is pretty precise but less precise than core.wait. This is usually hundredths of a second longer than the input time (2).

4.  See experiment.py

Frame-based timing Exercises

1.  See experiment.py

2.  See experiment.py. Only 11 frames were dropped during the experiment, therefore I kept frame-based timing
