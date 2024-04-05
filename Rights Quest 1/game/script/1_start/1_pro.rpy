default debug_gameplay_only = False #easier to jump btw files

label pro1:
    scene black with dissolve
    "As the summer vacation starts a band of 3 friend's go and visit their friend's grandma who lived by the ocean"
    scene bg_house with fade
    "The grandma always captured the heart of the children with the unique stories that would secretly hold moral values that would be needed by the children"

    scene black with dissolve
    show granny_shadow
    gran "Oh my, It seems [p1] slept off"
    show granny_shadow at left with move

    show sis_shadow
    sis "Wake up!! Granny is going to share a story with us!!"
    show sis_shadow at right 
    with move

    #hide all
    show bg_living at blink
    pause(2.0)
    scene bg_living

    show sis at right with moveinright
    sis "Wow, someone slept like a baby"

    show bro at left with moveinleft
    bro "Do you even remember who you are?"

    user "Yeah kind of..."

    bro "Really? Whats your name then?"

    #hide all
    scene black with fade

    label name_set:
        $ name = renpy.input("My name is...", default="Luke")
        $ name = name.strip()
        $ name = name.lower()

        if name == "keith" :
            "{i}(That's my brother's name...){/i}"
            jump name_set
        elif name == "eileen" :
            "{i}(That's my sister's name...){/i}"
            jump name_set
        
        $ name = name.title()

        menu:
            "{i}(My name is : [name], right?){/i}"
            "Yes":
                "My name's [name]"
            "No":
                "I might have slept too much..."
                jump name_set
    
    scene bg_living with dissolve
    show bro at right with moveinright
    bro "The sleeping princess is finally awake"
    
    show granny at left with moveinleft
    gran "Lets not make fun of the young one, now shall we begin?"    

    hide bro
    show sis at right with moveinright
    sis "Yes Granny lets begin!!"
    
    #hide all
    scene black with fade
    show granny at left with dissolve:
        alpha 0.5 #transparency
    gran "Once upon a time, there lived 3 young children."
    scene bg_town with dissolve #with 3kids
    gran "Although they were young, they were mature at heart"
    gran "On a snowy day, as Christmas draws near the children venture to a nearby forest to (what?)"

    scene bg_town2 with fade #wo 3kids
    show bro at right with moveinright
    bro "Let's not be too late and get back"

    show sis at left with moveinleft
    sis "Hey, I spot with my eyes something red"

    bro "Where?"

    jump mini1

    label redbag:
        pass
    
    show bro at right with moveinright
    bro "Hmmm, it's not something you would find lying around in a forest..."

    show sis at left with moveinleft
    sis "There's a tag that says to return to user"

    bro "What do we do?"

    label d1:
        menu:
            "Let's return it":
                pass
            "Do nothing...":
                sis "Let's return it to the owner, the person who lost it may be worried..."
                jump d1

    jump pro2