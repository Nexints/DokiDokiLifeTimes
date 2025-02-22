# Day 2 - Act 0

label day2:
    # Routes:
    # Route 2 - Walk and go out
    # Route 3 - Walk and no going out
    # Route 4 - No walk

    # Morning
    stop music fadeout 0.5
    scene black
    with wipeleft
    scene mcpov
    $ pause(0.01)
    scene black
    with dissolve_cg
    play music t2
    scene bg bedroom
    with dissolve_scene_half
    "It's a brand new day, and I still have school."
    "Tuesdays are generally just as hard as mondays, sadly."
    if satire_mode == True:
        "I suddenly get the urge to buy {i}a weapon of mass destruction{/i} from America."
        "{i}Especially after what happened with Wallace in the real world.{/i}"
        "I'll decide later though."
    "I still have to go to school, otherwise both Sayori and my mom will have a word with me."
    "I seriously need help..."

    # Making food - Adding additional dialogue for certain routes.
    scene black
    with wipeleft
    scene bg kitchen
    with wipeleft
    "I have a bit more time this morning, so I'll try to cook something."
    "Yesterday, my mom cooked something for me, but she's not here today."
    if satire_mode == True:
        "Maybe something happened with my mom."
        "I'll have to investigate it later."
    
    # Finishing cooking - Multiple Routes
    # If intelligence is more than 0, cooking has completed successfully.
    # If not, a disaster occurs, and if satire_mode is true, the MC gets re-incarnated into another world.
    # To be continued... in Doki Doki Isekai (an extention of DDLT)
    scene black
    with wipeleft
    stop music fadeout 0.5
    if gameSkill < 2:
        scene bg kitchen
        with wipeleft
        play music t8
        "I ended up cooking something myself."
        "It doesn't look terrible, and I'd be willing to eat it myself."
        "I'll pack this up and go to school."
    else:
        if satire_mode == True:
            scene breakdown
            with wipeleft
            play music mend
            "... Where did I awaken into?"
            "What happened-"
            x "Hello."
            x "You have died."
            "Oh."
            "Wait, HOLD ON?"
            "I'm still confused on how I got here."
            "I was just cooking something for myself to go to school."
            mc "What happened?"
            show sayori base afm happ om at f11
            s "And why am I here?"
            x "You two must have various questions."
            x "Let's go one by one."
            x "[player], you suffered an unfortunate ending."
            x "You were trying to cook something, but you weren't lucky and died while trying."
            x "Not only that, but you took out Sayori, who lived close to you and was within range of the fire."
            "I see."
            "I feel bad for Sayori though, who got caught up in all of this."
            "I'll try to reconcile with her while I have the chance to."
            s "Oh..."
            mc "I'm sorry, Sayori."
            mc "I've killed us both."
            if isekai_flag == True: # Flag, used to indicate the existance of Doki Doki Isekai.
                x "Don't worry. Both of you will be reincarnated into another world."
                x "Welcome..."
                stop music fadeout 0.5
                scene black
                with wipeleft
                x "... to the world of {i}Doki Doki Isekai{/i}."
                scene black
                with wipeleft
                $ persistent.act = 1001
                $ persistent.name = "Doki Doki Isekai: Act 1"
                $ renpy.save_persistent()
                return
            else:
                x "And now for you, [persistent.playername]."
                player "Yeah-?"
                player "Wait, how are you talking to me?"
                x "Restart this mod, and make better choices next time."
                x "For the sake of [player], Sayori, Yuri, Natsuki and Monika."
                x "Good luck next time."
                player "Fine... I guess."
                stop music fadeout 0.5
                scene black
                with wipeleft
            return
        else:
            scene bg kitchen
            with wipeleft
            play music t7
            "I made a terrible dish."
            "Oh well, I'll just have to get something from the school cafeteria."
            scene black
            with wipeleft
            stop music fadeout 0.5
    if route == 2:
        "I pack my things and meet up with Sayori outside, walking to school together."
    else:
        "I pack my things and rush off to school, neglecting Sayori."
    
    
    scene black
    with wipeleft
    stop music fadeout 0.5
    scene bg residential_day
    with wipeleft
    play music t2
    "Sayori's right outside the door."

    # Not completed yet!
    $ persistent.name = "Doki Doki LifeTimes: Act 1"
    $ renpy.save_persistent()
    return