## Hungary Time, the Discord bot
I decided Googling the time in Hungary to see whether the server admin (who is Hungarian)
was awake or not was too tiring, so I made this abomination.

[Invite the bot.](https://discord.com/api/oauth2/authorize?client_id=849610604763283496&permissions=2048&scope=bot%20applications.commands)

I'm not adding a way to tell the actual time with DST in effect, I don't know how to do that.
If you do, hmu.

Other than Hungary, I've added other timezones, right now there's:

`Alaska`
  
`Mountain`
 
`Philippines`

`Central`

`Eastern` 

`Samoa`

`UK`

`Pacific`

`India`

To use, your bot's token, then make a new environment variable named `TOKEN`, and paste your
bot's token in the value.

*Note: Using `guild_ids` is nice if you want to update the commands immediately, but it also
might cause a 405 error which I have no idea how to fix. This is harmless but it gets annoying
and might scare you.*

### If you're wondering what the modules are for, here's an explanation
`py-cord` is a maintained fork of `discord.py`, an API wrapper which was abandoned last year.
Also be sure to add `--pre` at the end of `pip install py-cord` since the prerelease has the slash 
commands and other things.

`pytz` provides the timezones and stuff.

`datetime` uses `pytz` to tell the time in those timezones.

Lastly, if you want to host it yourself all the time, you can use
[this random Medium article](https://medium.com/analytics-vidhya/how-to-host-a-discord-py-bot-on-heroku-and-github-d54a4d62a99e).
It's a bit outdated but it mostly works. There was also a [security breach](https://status.heroku.com/incidents/2413)
that happened recently, so attempting to connect your GitHub account won't work (Internal server error).
In the meantime, just do what [this StackOverflow answer](https://stackoverflow.com/a/71895325) says.

## Credits
CatFishing4Guyz, coding the bot, suggestions, testing.

Swemit, testing, and encouragement.

Thank you for the help :)