## Hungary Time, the Discord bot
I decided Googling the time in Hungary to see whether the server admin (who is Hungarian) was awake
or not was too tiring, so I made this abomination.

[Invite the bot.](https://discord.com/api/oauth2/authorize?client_id=1041597587297419344&permissions=277025392640&scope=bot%20applications.commands)

I'm not adding a way to tell the actual time with DST in effect, I don't know how to do that. If
you do, hmu.

Other than Hungary, this bot supports every timezone `pytz` has to offer. Check [this gist](https://gist.github.com/heyalexej/8bf688fd67d7199be4a1682b3eec7568)
by heyalexej for the list.

### If you're wondering what the modules are for, here's an explanation
`py-cord` is a maintained fork of `discord.py`, an API wrapper which was abandoned last year.
Also be sure to add `--pre` at the end of `pip install py-cord` since the prerelease has the
slash commands and other things.

`pytz` provides the timezones and stuff.

`datetime` uses `pytz` to tell the time in those timezones.

## Credits
CatFishing4Guyz, coding the bot, suggestions, testing.

xChibi Robo, testing, suggestions.

Thank you for the help :)