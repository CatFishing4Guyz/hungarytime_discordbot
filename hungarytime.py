# Made by CatFishing4Guyz#8137 on Discord, gimme praise

import discord
import pytz
import asyncio
import os
from datetime import datetime as dt
from discord import Option

DST = " If DST is in effect, the actual time is an hour ahead."

def Time(Timezone):
    match Timezone:
        case Timezone == "Hungary":
            return dt.now(pytz.timezone("Europe/Budapest")).strftime("It is %d %B %Y, %H:%M in Hungary.") + DST
        case Timezone == "Alaska":
            return dt.now(pytz.timezone("US/Alaska")).strftime("It is %d %B %Y, %H:%M in Alaska.") + DST
        case Timezone == "Central":
            return dt.now(pytz.timezone("US/Central")).strftime("It is %d %B %Y, %H:%M, Central Time.") + DST
        case Timezone == "Eastern":
            return dt.now(pytz.timezone("US/Eastern")).strftime("It is %d %B %Y, %H:%M, Eastern Time.") + DST
        case Timezone == "India":
            return dt.now(pytz.timezone("Asia/Kolkata")).strftime("It is %d %B %Y, %H:%M in India.") + DST
        case Timezone == "Mountain":
            return dt.now(pytz.timezone("US/Mountain")).strftime("It is %d %B %Y, %H:%M, Mountain Time.") + DST
        case Timezone == "Pacific":
            return dt.now(pytz.timezone("US/Pacific")).strftime("It is %d %B %Y, %H:%M, Pacific Time.") + DST
        case Timezone == "American Samoa":
            return dt.now(pytz.timezone("US/Samoa")).strftime("It is %d %B %Y, %H:%M in American Samoa.") + DST
        case Timezone == "United Kingdom":
            return dt.now(pytz.timezone("GMT")).strftime("It is %d %B %Y, %H:%M in the United Kingdom.") + DST

# Main body
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

@bot.slash_command(guild_ids=[831412377869221899], description="Sends the time in Hungary.")
async def time(ctx, timezone: Option(str, required=False, default="Hungary",
                                     description="Tell the time where?",
                                     choices=[
                                        "Hungary",
                                        "Persistent"
                                        "Alaska",
                                        "Central Time",
                                        "Eastern Time",
                                        "India",
                                        "Mountain Time",
                                        "Pacific Time",
                                        "Philippines"
                                        "American Samoa",
                                        "United Kingdom",
                                     ]
                              )
          ):
    if timezone == "Persistent":
        # Definitely does not work
        await ctx.respond("Timekeep initialized.")
        await asyncio.sleep(1)
        while True:
            await ctx.send(Timezone("Hungary"))
            if message.content == "stop":
                break
    else:
        await ctx.reply(Timezone(timezone))  

@bot.slash_command(guild_ids=[831412377869221899], description="Send the link to the GitHub repo.")
async def github(ctx):
    await ctx.respond("Hi! You can visit my repository here:\n"
                      "https://github.com/CatFishing4Guyz/hungarytime_discordbot")

@bot.slash_command(guild_ids=[831412377869221899], description="Sends the list of commands, most are self-explanatory")
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