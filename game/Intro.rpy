# All the intros for each act and day.
# Act 0 intro

label intro_act0:
    # Introduction. The console and the intro video is introduced.
    stop music fadeout 0.5
    scene black
    with dissolve_scene_half
    play music m1
    $ console_history = []
    $ run_input(input="print(currentAct)", output="Current Act: Prologue (0).")
    $ run_input(input="print(currentDate)", output="Date: April 8, 2011.")
    $ run_input(input="print(disclaimer)", output="This is a multi-part mod. Playing through Act 0 is recommended before playing other parts.")
    $ pause(3)
    $ console_history = []
    $ run_input(input="print(disclaimerTwo)", output="Characters may not be perfectly accurate from the original game.")
    $ run_input(input="print(haveFun)", output="Have fun!")
    "Continue by clicking anywhere."
    window hide
    hide screen console_screen
    $ pause(0.25)
    $ renpy.movie_cutscene("mod_assets/videos/DDLT_Act_0.avi")
    $ pause(0.25)
    return

label skippedIntro_act0:
    # Intro if you skipped the disclaimers. Lets you know the act and the date.
    stop music fadeout 0.5
    scene black
    with dissolve_scene_half
    play music m1
    $ console_history = []
    $ run_input(input="print(currentAct)", output="Current Act: Prologue (0).")
    $ run_input(input="print(currentDate)", output="Date: April 11, 2011.")
    "Continue by clicking anywhere."
    window hide
    hide screen console_screen
    $ pause(0.25)
    return

label day2Intro:
    # Intro for day 2
    stop music fadeout 0.5
    scene black
    with dissolve_scene_half
    play music m1
    $ console_history = []
    $ run_input(input="print(currentAct)", output="Current Act: Prologue (0).")
    $ run_input(input="print(currentDate)", output="Date: April 12, 2011.")
    "Continue by clicking anywhere."
    window hide
    hide screen console_screen
    $ pause(0.25)
    call day2
    return

label isekaiIntro:
    # Intro for Doki Doki Isekai

    $ syncGlobalToAct()

    stop music fadeout 0.5
    scene black
    with dissolve_scene_half
    play music m1
    $ console_history = []
    $ run_input(input="print(currentAct)", output="Current Act: Reincarnation (Act ???).")
    $ run_input(input="print(currentDate)", output="Date: Jan. 1, 109 Post-Creation.")
    $ run_input(input="print(disclaimer)", output="This route is non canonical.")
    "Continue by clicking anywhere."
    
    # Print Stats
    $ console_history = []
    $ run_input(input="print(stats)", output="Strength: [strength], Intelligence: [intel], ") # Stats printed
    $ run_input(input="print(stats2)", output="Game Skill: [gameSkill], Tardiness: [tardy]")
    $ run_input(input="print(stats3)", output="(Debug) Route: [route]")
    $ pause(0.25)
    window hide
    hide screen console_screen
    $ pause(0.25)
    call isekai_start
    return