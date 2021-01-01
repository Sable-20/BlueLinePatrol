Hi! this is Misaka speaking. please feel free to look at the rest of my github even though its defunct it wont really matter.

onto to actually configuring the bot.

first you just need to invite the bot I assume you have done, if not just dm me and ask me for another link which i can provide.(this bot is a private bot so this is addressed to the person I am making the bot for.)

2.) you need to find the bot in the list of roles and drag the bot itself(NOTE: N O T T H E S E R V E R B O T R O L E) IT MUST BE THE ROLE OF THE BOT ITSELF. look for the bots name. it will likely be near the bottom.

2.5) drag the bot role to JUST BELOW the highest role you do not want the bot to affect
    
    2.5 continued)
        i really have no idea why its like but just roll with it. so place it below trial mod if you want them to have permission to perform commands on anyone with a role below them. im looking into it but i believe its just a discord py issue which is another reason why ive been sneakily converting it to js on the side.

3.) dm me and let me know what time you want it activated or if you want it activated right away. I will start it up and you can give a sneak peek.


#########################################################
#########################################################

ALL COMMANDS WITH NOTABLE ISSUES

#########################################################
########################################################


ban, kick, mute, and most moderation commands(exclduing purge, lockdown, nuke, and slowmode)
    - none of them can affect anyone higher up in the role hierarchy than the bot itself. no you do not need to make the bot visible above all others just moving its role is fine

    - in theory you could simply substitute it for moving the server bot role up but I dont know how that would affect it I am in the process of testing it

HMUTE
    - for whatever reason it still removes all roles so consider it hardmute.

OK BOOMER
    - uh sometimes doesnt work not positive why, im revisiting links later

REPORT
    - WORK IN PROGRESS DO NOT ASSUME IT WORKS IT HAS NOT EVEN BEEN TESTED