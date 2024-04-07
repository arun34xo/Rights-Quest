label Bear:
    #The Right to Protection granted the strength to shield oneself and others from harm
    hide owl
    hide unicorn
    with dissolve
    show bear at right with move
    bear "Very well young one, follow me..."
    show bro at left with moveinleft
    bro "Don't fall behind"

    hide bro
    hide bear
    with dissolve
    scene somewhere with fade
    "trial"
    $ bearcomplete = True
    $ c = c+1
    jump choice2
    