# Made by CatFishing4Guyz#8137 on Discord, gimme praise

import discord
import pytz
import asyncio
import os
from datetime import datetime as dt
from discord import Option

REPLACE_WITH_GUILD_ID = os.getenv('GUILD_ID')

bot = discord.Bot(activity = discord.Activity(
    type=discord.ActivityType.watching, 
    name="ur mom undress."))

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

"""
Remove the guild IDs and replace it
with your own server's ID if you want
slash commands to update immediately.

Enable developer mode in Discord and
right click on your server from the 
server list and select "Copy ID".

You might get a 405 error, but that's
harmless and it won't affect anything.
"""

@bot.slash_command(guild_ids=[REPLACE_WITH_GUILD_ID], description="Sends the time in Hungary.")
async def time(ctx, timezone: Option(str, required=False, default="Europe/Budapest",
                                     description="Tell the time where?",
                                     choices=[
                                        "Europe/Budapest",
                                        "Asia/Kolkata",
                                        "Asia/Manila",
                                        "Europe/London",
                                        "US/Alaska",
                                        "US/Central",
                                        "US/Eastern",
                                        "US/Mountain",
                                        "US/Pacific",
                                        "US/Samoa",
                                     ]
                              ),
               # Actually `bool`, but that doesn't work
               should_persist: Option(str, required=True, default="False",
                                      description="Hourly time update. Choose False if you don't care",
                                      choices=[
                                        "False",
                                        "True",
                                      ]
                               )
          ):
    DST = " If DST is in effect, the actual time is an hour ahead."
    def Time(Timezone):
        return dt.now(
            pytz.timezone(
                f"{Timezone}")).strftime(
                    f"It is %d %B %Y, %H:%M in {Timezone}.") + DST
    if bool(should_persist):
        # Definitely does not work
        await ctx.respond("Timekeep initialized.")
        await asyncio.sleep(1)
        while True:
            await ctx.send(Time("Europe/Budapest"))
            if ctx.content == "test":
                await ctx.reply("Test")
                break
    else:
        await ctx.respond(Time(timezone)) 

@bot.slash_command(guild_ids=[REPLACE_WITH_GUILD_ID], description="Send the link to the GitHub repository.")
async def github(ctx):
    await ctx.respond("Hi! You can visit my repository here:\n"
                      "https://github.com/CatFishing4Guyz/hungarytime_discordbot")

@bot.slash_command(guild_ids=[REPLACE_WITH_GUILD_ID], description="Sends the list of commands, most are self-explanatory")
async def help(ctx):
    await ctx.respond("Options:\n"
                      "`help` - show this message\n" 
                      "`github` - sends the link to my repository\n"
                      "`Hungary` - tells the time in Hungary\n"
                      "`Persistent` - sends an update on Hungary's time every hour,"
                      " like a clock tower\n"
                      "`Philippines` - tells the time in the Philippines\n"
                      "`Alaska` - tells the time in Alaska\n"
                      "`Mountain Time` - tells the US Mountain Time\n"
                      "`Central Time` - tells the US Central Time\n"
                      "`Eastern Time` - tells the US Eastern Standard Time\n"
                      "`Pacific Time` - tell the US Pacific Time\n"
                      "`American Samoa` - tell the time in the American Samoa\n"
                      "`United Kingdom` - tell the time in the United Kingdom\n")

bot.run(os.getenv('TOKEN'))