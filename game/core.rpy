init python:
    def syncGlobalToAct():
        # Sync Definitions
        global route, strength, intel, gameSkill, tardy, story_mode, satire_mode, name_mod
        route = persistent.route
        strength = persistent.str
        intel = persistent.intel
        gameSkill = persistent.gameSkill
        tardy = persistent.tardy
        story_mode = persistent.story_mode
        if story_mode == False:
            satire_mode = persistent.satire_mode
        else:
            satire_mode = False
        name_mod = persistent.name
        return
    def syncActToGlobal():
        global route, strength, intel, gameSkill, tardy, story_mode, satire_mode, name_mod
        persistent.route = route
        persistent.str = strength
        persistent.intel = intel
        persistent.gameSkill = gameSkill
        persistent.tardy = tardy
        persistent.story_mode = story_mode
        persistent.satire_mode = satire_mode
        persistent.name = name_mod
        renpy.save_persistent()
        return
    def resetGlobals():
        global route, strength, intel, gameSkill, tardy, story_mode, satire_mode, name_mod
        persistent.act = 0 # Determines Act
        persistent.route = 0 # Determines the route.
        persistent.str = 0 # Determines your strength.
        persistent.intel = 0 # Determines intelligence
        persistent.gameSkill = 0 # Determines gamer skill
        persistent.tardy = 0 # Tardiness in class. Decreased by doing homework.
        persistent.name = "Doki Doki LifeTimes: Act 0"
        renpy.save_persistent()
        return