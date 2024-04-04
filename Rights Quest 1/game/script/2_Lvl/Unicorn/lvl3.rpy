label Unicorn:
    #The Right to Survival gave the power of healing and nourishment
    
    hide bear
    hide owl
    with dissolve
    show unicorn at right with move
    unicorn "Don't dilly dally, Let's be off"
    
    menu:
        "Let's be off!!":
            unicorn "Such an active child, I already like you"
        "Let's take our time...":
            unicorn "Up up and away, an adventure does not wait for us"

    hide unicorn with dissolve
    scene somewhere with fade
    "trial"

    $ unicorncomplete = True
    $ c = c+1
    jump choice2