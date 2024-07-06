label end:
    play music "main-menu-music.mp3"
    scene bg_santa_workshop with fade
    show brochar at left with moveinleft
    bro "Hello Mr. Santa, we're back!!"

    show santachar at right with moveinright
    santa "Hello children, how is the hunt for the presents going on?"
        
    hide brochar with dissolve
    show sischar at left with moveinleft

    if c<3:
        if c==2:
            sis "Yes, we've found 2 presents so far!!"
        elif c==1:
            sis "Yes, we've only found a single present!"
        else:
            sis "Sadly no, we haven't found any of the presents"

        santa "Is that so? Well thank you for you effort, while your here why not sit down for cup of hot chocolate?"
        menu:
            "Sit down for a cup of coffee":
                user "Yes, it would be our pleasure!"
                santa "Very well, I shall get the cup"

                hide santachar
                hide sischar
                with dissolve
                scene black with advtransbite
                "Time passes as the 4 sit down and have a hot cup of chocolate and marshmallow"
                pause(1.3)
                
                scene bg_santa_workshop with advtransbite
                show brochar at left with moveinleft
                bro "Thank you for the hospitality, shall we get back on the search?"
                hide brochar with dissolve

                show sischar at left with moveinleft
                sis "Yes the chocolate warmed me up, let's be on our way"

                show santachar at right with moveinright
                santa "See you soon children, be well!!"
                user "See you soon Mr. Santa"

                jump pro3

            "Refuse the offer and head out to find present":
                user "I must refuse the kind offer Mr. Santa"
                sis "Yes, we must find the present before Christmas comes"
                santa "Very well, Your dedication inspires me. Be well children!!"

                jump pro3
            
    else:
        sis "We've managed to find all the presents Mr. Santa"
        hide sischar with dissolve

        show brochar at left with moveinleft
        bro "And right before Christmas time, was a close call"
        santa "Wonderful, would you children like to deliver the presents with me?"
        hide brochar with dissolve

        show sischar at left with moveinleft
        sis "Yess!! It would be an honour"
        user "Can we??"
        santa "Ofcourse, It's the least I can do for the children that helped me."
        hide sischar
        hide santachar with dissolve

        scene black with dissolve
        $ renpy.movie_cutscene("images/santa.webm")

        scene bg_sky with fade
        show santachar at right with moveinright
        santa "So tell me about the adventure you went through for the 1st present..."
        user "It was stormy in our way for the 1st present..."
        menu:
            "I was scared and my brother gave me the strength to move forward":
                santa "A family that supports each other, impressive haha. And then?"
                user "We made our way to a shelter"
            "I was the bravest among us and led us to shelter nearby":
                show brochar at left with moveinleft
                bro "Hahaha, sure you were you little liar"
                santa "Hoho, seems like I missed out on some fun time"
        show sischar at left with moveinleft
        sis "We encountered a few bullies they gave us quite a hard time"
        hide sischar with dissolve
        show brochar at left with moveinleft
        if OptReasoned:
            bro "Our young [sib] gathered the courage and Reasoned with them"
            bro "They understood and went their way without causing trouble"
        elif OptStoodup:
            bro "Our young [sib] gathered the courage and Stood Up against them"
            bro "They got scared and ran with their tails between their legs, hahaha"
        santa "Ahh, it was a good decision to overcome that problem"
        hide brochar with dissolve
        show sischar at left with moveinleft
        sis "You'll never guess, we found the first present at the house we seeked refuge in."
        santa "Oh my, seems like luck was on your side. As expected of the children that found my bag hoho"
        santa "Now tell me about the adventure of the second gift"
        hide sischar with dissolve
        show brochar at left with moveinleft
        bro "As we were hungry, we went into a restaurant to order lunch"
        hide brochar with dissolve
        show sischar at left with moveinleft
        sis "I must admit, the food was fantastic but I cannot say the same for the shop owner"
        santa "Hoho, it seems like you had bone to pick with the shop owner"
        sis "Well it's cause..."
        menu:
            "He was kind to us but not to others":
                user "I suspect he only liked people based on their skin tone"
                santa "Ho? Why do you say so?"
            "His food had something weird in it":
                user "Apparently it would only be edible to people of specific skin tone"
                santa "Hahaha, I see the store owner was selective of his customers..."
        user "There was a kind women who came in to order lunch like us"
        sis "But the store owner refused to serve her due to her dark skin tone"
        hide sischar with dissolve
        show brochar at left with moveinleft
        bro "Our Little one stood up once again against discrimination"
        menu:
            "Stop... you'll make me blush":
                user "I only did what was right, nothing more!"
            "Hehe... praise me more":
                user "I felt it was the right thing to do, so I just did it"
        santa "Hoho, young [gender]..."
        if shouted:
            santa "To think the younglin that shouted in the front door was such a brave man, hoho"
        elif knocked:
            santa "To think the young [gender] who knocked on my door was this brave, impressive hoho"
        else:
            santa "To think the boy who was scared to knock my door was a brave one, hoho nice one"
        bro "That's our young [sib] for you, we're proud of you!!"
        hide brochar with dissolve
        show sischar at left with moveinleft
        sis "We ate with the kind lady, and you wouldn't guess it..."
        sis "She apparently came across the present and gave it to \"Lost and Found\""
        santa "Hoho, the light of luck must shine brightly upon you lots"
        santa "Such an interesting tale and actions you have taken"
        label d8:
            scene bg_sky with fade
            show santachar at right with moveinright
            menu:
                santa "What is it you learned from the 1st trial?"
                "Stand up to bullies":
                    user "They only bully us cause we do nothing when they supress us"
                "Reason with bullies":
                    user "They maybe kind enough to understand us"
                "You must bully others":
                    user "Those with power must dominate Those that are weak"
                    santa "Not quite the answer I was looking for.... I am dissapointed"
                    jump protection
                "Do nothing if you are bullied":
                    user "Do nothing and just suffer is the way"
                    santa "Not quite the answer I was looking for.... I am dissapointed"
                    jump protection
        show sischar at left with moveinleft
        sis "It was quite an interesting and meaningful adventure"
        hide sischar with dissolve
        show brochar at left with moveinleft
        bro "Haha, it was. I wouldnt want to go through that again"
        label d9:
            scene bg_sky with fade
            show santachar at right with moveinright
            santa "Well well, what about the 2nd trail?"
            menu:
                santa "What did you learn from that?"
                "Discriminate against minority":
                    user "The minority is a minority for a reason"
                    santa "Not quite the answer I was looking for.... I am dissapointed"
                    jump discrimination
                "Discriminate against the weak and different":
                    user "The strong and perfect exist to dominate"
                    santa "Not quite the answer I was looking for.... I am dissapointed"
                    jump discrimination
                "Do not Discriminate":
                    user "It is never the right choice to discriminate"
                    user "No matter the circumstance or person"
                    santa "Impressively learnt young one"
        show brochar at left with moveinleft
        bro "Thats right, we should even stand up against discrimination"
        santa "That's right, you children will grow up well"
        santa "Now that the night is drawing to a close, shall I drop you home?"
        bro "Its been a long day and I could use some great sleep"
        hide brochar with dissolve
        show sischar at left with moveinleft
        sis "I cant wait to tell granny about what happened today!!"
        santa "Hohoho, off we go!!"

        scene black with dissolve
        $ renpy.movie_cutscene("images/end.webm")

        #end credits
        
    return