# End of demo.

label end_demo:
    scene black
    with wipeleft
    scene breakdown
    with wipeleft
    "This is where the demo ends."
    "We're around 2\% done with the mod, so sit tight as the mod develops further!"
    "This mod will not be finished for a very long time."
    return

label end:
    scene black
    with wipeleft
    window hide
    scene breakdown
    with wipeleft
    play music m1
    $ console_history = []
    $ run_input(input="print(actEnding)", output="Act 0 has concluded.")
    $ run_input(input="print(thankYou)", output="Thank you for playing through act 0.")
    $ run_input(input="print(disclaimer)", output="This is a multi-part mod. Playing through Act 0 is recommended before playing other parts.")
    window show
    "Continue by clicking anywhere."
    window hide
    hide screen console_screen
    return