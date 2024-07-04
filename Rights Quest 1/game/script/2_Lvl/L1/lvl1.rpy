default OptReasoned = False
default OptStoodup = False

label L1:
    play music "main-menu-music.mp3"
    #The Right to Protection granted the strength to shield oneself and others from harm
    if L1complete==True:
        jump completedD
    else: 
        pass
    scene bg_snow_field with fade
    show heavysnow1
    show heavysnow2
    show heavysnow3

    "The kids walk downtown looking for Santa's missing presents. Ominous dark clouds roll in."

    show sischar at right with moveinright
    sis "Oh no guys, it looks like we’re going to be stuck in a really bad snowstorm!"

    show brochar at left with moveinleft
    bro "We need to find shelter before the storm hits!"

    show sischar at right
    sis "But where can we go? We’re too far from any buildings."
    
    show brochar at left 
    bro "Let’s go to that abandoned shed over there, we’ll be safe in there until the storm eases up."
    
    show sischar at right 
    sis "But isn’t that dangerous? It could collapse in the storm."
    
    show brochar at left 
    bro "We don’t have much of a choice. We’ll just have to be careful."
    with dissolve

    menu:
        "I'm scared":
            user "I’m a little worried, will we be okay?"
            show brochar at left with moveinleft
            bro "Don’t worry kiddo, of course we'll be okay. We can do this if we stick together! We’re right by your side."
            show sischar at right with moveinright
            sis "You got that right, Keith! Lead the way!"
            pass
        "Go to the shed.":
            user "Let’s go quick before the storm gets worse!"
            show brochar at left with moveinleft
            bro "Let's go!"
            show sischar at right with moveinright
            sis "Lead the way, Keith!"
            pass
    hide brochar
    hide sischar

    "The Children rush through the storm towards the old shed."
    scene bg_inside_shed with fade
    show brochar at left with moveinleft
    bro "Everyone get inside, quick!"
    hide brochar

    "They huddle together inside the shed, the storm raging outside"

    show sischar at right with moveinright
    sis "I'm a little scared."
    show brochar at left with moveinleft    
    bro "Don't worry Eileen. We'll stay together and keep each other safe."
    sis "I hope this storm clears out soon."
    bro "Remember what we learned about the right to protection? We have the strength to shield ourselves and others from harm!"
    sis "That’s right! We can't control the storm, but we can control how we react to it!"
    "Suddenly, the children hear footsteps approaching. A group of elderly kids known for causing trouble appears."

    hide brochar
    hide sischar

    show bullychar at left with moveinleft
    bully "Well, well, well, what do we have here? A bunch of scared little kids hiding from the storm?"
    show sischar at right with moveinright
    sis "Leave us alone! We’re not bothering anyone."
    bully "Oh, but you are bothering us. This is our territory, and we don’t like outsiders."
    
    label d7:
        scene bg_inside_shed with dissolve
        menu:
            "Stand up for ourselves.":
                hide bullychar
                hide sischar
                user "We won’t let you intimidate us! Stand your ground!"
                show brochar at left with moveinleft
                bro "We have the right to protect ourselves and others from harm. And we won’t let you hurt us!"
                show bullychar at right with moveinright
                bully "Fine, have it your way. But this isn’t over!"
                $OptStoodup = True
            "Reason with them.":
                hide bullychar
                hide sischar
                user "Let’s try to reason with them, we don’t want any trouble."
                show sischar at left with moveinleft
                sis "We don't mean to be here, as soon as the storm gets better, we'll leave."
                show bullychar at right with moveinright
                bully "Hmph, fine. But stay out of our way."
                $OptReasoned = True
            "Stay silent.":
                show bullychar at right with moveinright
                bully "Such weaklings, no one will know if you get hurt today"
                show sischar at left with moveinleft
                sis "No... please dont hurt us..."
                bully "Too late miss!!"
                #game failed screen
                jump protection
                            
    hide brochar
    hide sischar
    hide bullychar
    with dissolve

    "The bully leaves without causing any harm."
    
    show sischar at right with moveinright
    sis "Looks like the storm is clearing out! How about we leave this shed and continue our journey to find Santa’s present?"
    menu:
        "Let’s stay here for some more time.":
            sis "Okay, we'll stay here for some more time."
            menu:
                "Let’s stay here for some more time.":
                    sis "We should get going."
                "Let’s leave to go find Santa’s present now!":
                    sis "Okay! Let's Go!" 
        "Let’s leave to go find Santa’s present now!":
            sis "Okay! Let's Go!"    

    hide sischar
    show brochar at left with moveinleft
    bro "Oh wait! is that what I think it is?!"
    show sischar at right with moveinright
    sis "Oh my goodness, look! Is that Santa's present?!"

    jump hidden3
    
    label foundhiddenitem1:
        pass

    show sischar at left with moveinleft
    sis "Yay! We found one of Santa's missing presents!"
    show brochar at right with moveinright
    bro "Good job! We only have a few more to go!"

    $L1complete=True
    $c = c+1

    jump pro3

