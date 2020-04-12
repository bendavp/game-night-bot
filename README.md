# Game Night Bot
## A Discord bot, written in Python3 to help manage game nights.

### Completed features/commands:
* Roll die: Rolls a specified number of die with a specified number of sides. 
    * Usage: `!roll <number of die> <number of sides>`

### Planned features/commands:
* Keep track of a list of games, including:
    * Free:
        * CAH: https://pretendyoure.xyz/zy/
        * Catan: https://hexs.io/ OR https://colonist.io/ 
            * max 4; 5+ players is _currently_ $9/mo
        * Codenames: https://codenames.plus/
        * Krunker (online FPS): https://krunker.io
        * Games from Steam, streamed via Discord Live
            * Jackbox (Party Pack 3: Quiplash 2, Trivia Murder Party, Guesspionage, Tee K.O., Drawful 2)
            * Keep Talking and Nobody Explodes (best w/2-3 people)
    * Purchase req'd:
        * Steam
            * Golf with Friends
            * Uno
            * Civ V
        * Minecraft
            * Hypixel minigames: mc.hypixel.net
* Polls
    * Admin role can create a poll
    * Admin role can add options to a poll
    * Admin role can start a poll
    * Anyone can vote on a poll only once, but may change their vote
    * Admin role can close a poll
    * Support for multiple ongoing polls
        * Anyone can get a list of the ongoing polls
    * Optional poll expiration
        * i.e. poll will close in e.x. 1y, 1mo, 1d, 1m, 1s, etc. 