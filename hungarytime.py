# Made by CatFishing4Guyz#7903 on Discord, gimme praise

import discord
import pytz
import os
from datetime import datetime as dt
from discord import Option

bot = discord.Bot(activity = discord.Activity(
                                type=discord.ActivityType.watching, 
                                name="ur mom undress."))

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

MY_GUILD_ID = os.getenv('GUILD_ID')
@bot.slash_command(guild_ids=[MY_GUILD_ID], description="Check the time in various timezones")
async def time(ctx, timezone: Option(str, required=False, default="Europe/Budapest",
                                     description="Tell the time where?")):
    DST = " If DST is in effect, the actual time is an hour ahead."
    def Time(Timezone):
        return dt.now(pytz.timezone(f"{Timezone}")).strftime(f"It is %d %B %Y, %H:%M in {Timezone}.") + DST
    await ctx.respond(Time(timezone))
    
    # not working
    try:
        pass
    except UnknownTimeZoneError:
        await ctx.respond("Not a valid timezone. Check out this gist for a list of timezones: \n"
                          "<https://gist.github.com/heyalexej/8bf688fd67d7199be4a1682b3eec7568>")

@bot.slash_command(guild_ids=[MY_GUILD_ID], description="Send the link to the GitHub repository.")
async def github(ctx):
    await ctx.respond("Hi! You can visit my repository here:\n"
                      "https://github.com/CatFishing4Guyz/hungarytime_discordbot")

@bot.slash_command(guild_ids=[MY_GUILD_ID], description="Sends the list of commands, most are self-explanatory")
async def help(ctx):
    await ctx.respond("Options:\n"
                      "`time` - tell the time in various timezones\n"
                      "`help` - show this message\n" 
                      "`github` - sends the link to my repository\n")

bot.run(os.getenv('TOKEN'))