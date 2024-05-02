default debug_gameplay_only = False #easier to jump btw files

label pro1:
    scene black with dissolve
    "As the summer vacation starts a band of 3 friend's go and visit their friend's grandma who lived by the ocean"
    scene bg_house with fade
    "The grandma always captured the heart of the children with the unique stories that would secretly hold moral values that would be needed by the children"

    scene black with dissolve
    show grannychar at left with moveinleft:
        alpha 0.25
    gran "Oh my, It seems [p1] slept off"

    show sischar main at right with moveinright:
        alpha 0.25
    sis "Wake up!! Granny is going to share a story with us!!"

    #hide all
    show bg_living at blink
    scene bg_living with dissolve

    show sischar main at right with moveinright
    sis "Wow, someone slept like a baby"

    show brochar main at left with moveinleft
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
            "{i}(That's my friends's name...){/i}"
            jump name_set
        elif name == "eileen" :
            "{i}(That's my friends's name...){/i}"
            jump name_set
        
        $ name = name.title()

        menu:
            "{i}(My name is : [name], right?){/i}"
            "Yes":
                user "My name's [name]"
            "No":
                user "I might have slept too much..."
                jump name_set
    
    scene bg_living with dissolve
    show brochar main at right with moveinright
    bro "The sleeping princess is finally awake"
    
    show grannychar at left with moveinleft
    gran "Lets not make fun of the young one, now shall we begin?"    

    hide brochar with moveoutright
    show sischar main at right with moveinright
    sis "Yes Granny lets begin!!"
    
    scene black with fade
    show grannychar at left with dissolve:
        alpha 0.5 #transparency
    gran "Once upon a time, there lived 3 young children."
    
    scene bg_forestwkid with dissolve #with 3kids
    gran "Although they were young, they were mature at heart"
    gran "On a snowy day, as Christmas draws near the children ventured to a nearby forest to gather firewood and play in the snow"

    scene bg_forest1 with fade #w hint in bg
    show brochar at right with moveinright
    bro "Let's not be too late and get back"

    show sischar at left with moveinleft
    sis "Hey, I spot with my eyes something {color=#FF0000}Red{/color}"

    bro "Where?"

    jump mini1

    label redbag:
        pass
    
    show brochar at right with moveinright
    bro "Hmmm, it's not something you would find lying around in a forest..."

    show sischar at left with moveinleft
    sis "There's a tag that says '{u}If found, please return to {i}address{/i}{/u}'"

    bro "What do we do?"

    label d1:
        menu:
            user "Let's... "
            "Let's return it":
                pass
            "Do nothing...":
                sis "Let's return it to the owner, the person who lost it may be worried..."
                jump d1

    jump pro2