label end:

    scene bg_santa_workshop with fade
    show brochar at left with moveinleft
    bro "Hello Mr. Santa, we're back!!"

    show santachar at right with moveinright
    santa "Hello children, how is the hunt for the presents going on?"
        
    hide bro with dissolve
    show sischar at left with moveinleft

    if c<3:
        if c=2:
            sis "Yes, we've found 2 presents so far!!"
        elif c=1:
            sis "Yes, we've only found a single present!"
        else:
            sis "Sadly no, we haven't found any of the presents"

        santa "Is that so? Well thank you for you effort, while your here why not sit down for cup of coffee?"
        menu:
            "Sit down for a cup of coffee":
                me "Yes, it would be our pleasure!"
                santa "Very well, I shall get the cup"

                hide santa
                hide sischar
                with dissolve
                pause(4.0)

                show brochar at left with moveinleft
                bro "Thank you for the hospitality, shall we get back on the search?"
                hide brochar with dissolve

                show sischar at left with moveinleft
                sis "Yes, let's be on our way"

                show santachar at right with moveinright
                santa "See you soon children, be well!!"
                me "See you soon Mr. Santa"

                jump retry

            "Refuse the offer and head out to find present":
                me "I must refuse the kind offer Mr. Santa"
                sis "Yes, we must find the present before Christmas comes"
                santa "Very well, Your dedication inspires me. Be well children!!"

                jump retry
            
    else:
        sis "We've managed to find all the presents Mr. Santa"
        hide sischar with dissolve

        show brochar at left with moveinleft
        bro "And right before Christmas time, was a close call"
        santa "Wonderful, would you children like to deliver the presents with me?"

        show sischar at left with moveinleft
        sis "Yess!! It would be an honour"
        me "Can we??"
        santa "Ofcourse, It's the least I can do for the children that helped me."

        #end stuff - incomplete
        
    return