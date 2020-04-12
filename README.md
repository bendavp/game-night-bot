# Game Night Bot
## A Discord bot, written in Python3 to help manage game nights. PRs welcome!

### About:
TODO

### Completed features/commands:
* Roll die: Rolls a specified number of die with a specified number of sides. 
    * Usage: `!roll <number of die> <number of sides>`
    * Thanks to Alex Ronquillo from Real Python!
        * https://realpython.com/how-to-make-a-discord-bot-python/

### Planned features/commands:
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