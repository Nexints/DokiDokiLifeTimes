## script.rpy

# This is the main script that Ren'Py calls upon to start
# your mod's story! 

init python:
    import os
    currentuser = os.environ.get( 'USERNAME', 
                os.environ.get( 'USER', 
                os.environ.get( 'LNAME', 
                os.environ.get( 'LOGNAME', 'Player' ))))

label start:

    # This label configures the anticheat number for the game after Act 1.
    # It is recommended to leave this as-is and use the following in your script:
    #   $ persistent.anticheat = renpy.random.randint(X, Y) 
    #   X - The minimum number | Y - The maximum number
    $ anticheat = persistent.anticheat

    # This variable sets the chapter number to 0 to use in the mod.
    $ chapter = 0

    # This variable controls whether the player can dismiss a pause in-game.
    $ _dismiss_pause = config.developer

    # Obtain current user
    $ persistent.current_user = currentuser

    ## Names of the Characters
    # These variables set up the names of the characters in the game.
    # To add a character, use the following example below: 
    #   $ mi_name = "Mike". 
    # Don't forget to add the character to 'definitions.rpy'!
    $ x_name = "Nexint"
    $ f_name = "Girl 1"
    $ s_name = "???"
    $ m_name = "Girl 3"
    $ n_name = "Girl 2"
    $ y_name = "Girl 1"
    $ w_name = "Wallace"
    $ player = persistent.playername
    $ rc_name = "Rainclouds"

    # This variable controls whether the quick menu in the textbox is enabled.
    $ quick_menu = True

    # This variable c ontrols whether we want normal or glitched dialogue
    # For glitched dialogue, use 'style.edited'.
    $ style.say_dialogue = style.normal

    # This variable controls whether Sayori is dead. It is recommended to leave
    # this as-is.
    $ in_sayori_kill = None
    
    # These variables controls whether the player can skip dialogue or transitions.
    $ allow_skipping = True
    $ config.allow_skipping = True

    ## The Main Part of the Script
    # This is where your script code is called!
    # 'persistent.playthrough' controls the playthrough number the player is on i.e (Act 1, 2, 3, 4)

    # Reset playthrough
    $ persistent.playthrough = 0

    # First playthrough intro!
    if persistent.firstRunDDLT == 0:
        $ persistent.firstRunDDLT = 1
        $ renpy.save_persistent()
        call intro_act0 from _call_intro_act0
    elif persistent.act == 0: # Option to skip the intro. Only available when Act 0 is called.
        menu:
            "Do you wish to see the Act 0 intro?"
            "Yes":
                call intro_act0 from _call_intro_act0
            "No":
                "Skipping intro..."
                call skippedIntro_act0 from _call_skippedIntro_act0
    
    # Determines which act to call, Game needs to restart each act.
    # When all acts are released, this will be redundant.
    if persistent.act == 0:
        # Prologue (Act 0)
        call prologue from _call_prologue
        call end_demo from _call_end_demo
    else:
        menu:
            "Do you wish to go back to Act 0 of DDLT?"
            "Yes":
                "Setting act to 0 and resetting persistent variables."
                $ resetGlobals()
                "This mod will reset back to act 0 of DDLT. You will be kicked out."
                $ renpy.quit()
            "No":
                if persistent.act == 1001:
                    "This content hasn't released yet."
                    "Regardless, I wish you the best of luck."
                    call isekaiIntro
                else:
                    "There's nothing for you here."
                    "This is all the content inside the mod currently."

    # Sync persistent variables with non persistent parts.
    $ syncActToGlobal()
    $ renpy.quit() 
    # End Demo

    ## Example on calling scripts from DDLC.
    # if persistent.playthrough == 0:
    #     # This variable sets the chapter number to X depending on the chapter
    #     # your player is experiencing ATM.
    #     $ chapter = 0

    #     # This call statement calls your script label to be played.
    #     call ch0_main
        
    #     # This call statement calls the poem mini-game to be played.
    #     call poem

    #     ## Day 1
    #     $ chapter = 1
    #     call ch1_main

    #     # This call statement calls the poem sharing minigame to be played.
    #     call poemresponse_start
    #     call ch1_end

    #     call poem

    #     ## Day 2
    #     $ chapter = 2
    #     call ch2_main
    #     call poemresponse_start
    #     call ch2_end

    #     call poem

    #     ## Day 3
    #     $ chapter = 3
    #     call ch3_main
    #     call poemresponse_start
    #     call ch3_end

    #     ## Day 4
    #     $ chapter = 4
    #     call ch4_main

    #     # This python statement writes a file from within the game to the game folder
    #     # or to the Android/data/[modname]/files/game folder.
    #     python:
    #         if renpy.android and renpy.version_tuple == (6, 99, 12, 4, 2187):
    #             try: file(os.environ['ANDROID_PUBLIC'] + "/hxppy thxughts.png")
    #             except IOError: open(os.environ['ANDROID_PUBLIC'] + "/hxppy thxughts.png", "wb").write(renpy.file("hxppy thxughts.png").read())
    #         elif renpy.android:
    #             try: renpy.file(os.environ['ANDROID_PUBLIC'] + "/hxppy thxughts.png")
    #             except IOError: open(os.environ['ANDROID_PUBLIC'] + "/hxppy thxughts.png", "wb").write(renpy.file("hxppy thxughts.png").read())
    #         else:
    #             try: renpy.file(config.basedir + "/hxppy thxughts.png")
    #             except IOError: open(config.basedir + "/hxppy thxughts.png", "wb").write(renpy.file("hxppy thxughts.png").read())

    #     ## Day 5
    #     $ chapter = 5
    #     call ch5_main

    #     # This call statement ends the game but doesn't play the credits.
    #     call endgame
    #     return

    # elif persistent.playthrough == 1:
    #     $ chapter = 0
    #     call ch10_main
        
    #     # This jump statement jumps over to Act 2 from Act 1.
    #     jump playthrough2


    # elif persistent.playthrough == 2:
    #     ## Day 1 - Act 2
    #     $ chapter = 0
    #     call ch20_main
    #     label playthrough2:
    #         call poem

    #         python:
    #             if renpy.android and renpy.version_tuple == (6, 99, 12, 4, 2187):
    #                 try: file(os.environ['ANDROID_PUBLIC'] + "/CAN YOU HEAR ME.txt")
    #                 except IOError: open(os.environ['ANDROID_PUBLIC'] + "/CAN YOU HEAR ME.txt", "wb").write(renpy.file("CAN YOU HEAR ME.txt").read())
    #             elif renpy.android:
    #                 try: renpy.file(os.environ['ANDROID_PUBLIC'] + "/CAN YOU HEAR ME.txt")
    #                 except IOError: open(os.environ['ANDROID_PUBLIC'] + "/CAN YOU HEAR ME.txt", "wb").write(renpy.file("CAN YOU HEAR ME.txt").read())
    #             else:
    #                 try: renpy.file(config.basedir + "/CAN YOU HEAR ME.txt")
    #                 except IOError: open(config.basedir + "/CAN YOU HEAR ME.txt", "wb").write(renpy.file("CAN YOU HEAR ME.txt").read())

    #         ## Day 2 - Act 2
    #         $ chapter = 1
    #         call ch21_main
    #         call poemresponse_start
    #         call ch21_end

    #         # This call statement calls the poem mini-game with no transition.
    #         call poem(False)

    #         python:
    #             if renpy.android and renpy.version_tuple == (6, 99, 12, 4, 2187):
    #                 try: file(os.environ['ANDROID_PUBLIC'] + "/iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii.txt")
    #                 except IOError: open(os.environ['ANDROID_PUBLIC'] + "/iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii.txt", "wb").write(renpy.file("iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii.txt").read())
    #             elif renpy.android:
    #                 try: renpy.file(os.environ['ANDROID_PUBLIC'] + "/iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii.txt")
    #                 except IOError: open(os.environ['ANDROID_PUBLIC'] + "/iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii.txt", "wb").write(renpy.file("iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii.txt").read())
    #             else:
    #                 try: renpy.file(config.basedir + "/iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii.txt")
    #                 except IOError: open(config.basedir + "/iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii.txt", "wb").write(renpy.file("iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii.txt").read())

    #         ## Day 3 - Act 2
    #         $ chapter = 2
    #         call ch22_main
    #         call poemresponse_start
    #         call ch22_end

    #         call poem(False)

    #         ## Day 4 - Act 2
    #         $ chapter = 3
    #         call ch23_main

    #         # This if statement calls either a special poem response game or play
    #         # as normal.
    #         if y_appeal >= 3:
    #             call poemresponse_start2
    #         else:
    #             call poemresponse_start

    #         # This if statement is leftover code from DDLC where if your game is
    #         # a demo that it ends the game fully.
    #         if persistent.demo:
    #             stop music fadeout 2.0
    #             scene black with dissolve_cg
    #             "End of demo"
    #             return

    #         call ch23_end
    #         return

    # elif persistent.playthrough == 3:
    #     jump ch30_main

    # elif persistent.playthrough == 4:
    #     ## Day 1 - Act 4
    #     $ chapter = 0
    #     call ch40_main
    #     jump credits

# This label is where the game 'ends' during Act 1.
label endgame(pause_length=4.0):
    $ quick_menu = False
    stop music fadeout 2.0
    scene black
    show end
    with dissolve_scene_full
    pause pause_length
    $ quick_menu = True
    return
