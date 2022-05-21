# Made by CatFishing4Guyz#8137 on Discord, gimme praise

import discord
import pytz
import asyncio
import os
from datetime import datetime as dt

# Time Zones
Hungary = pytz.timezone('Europe/Budapest')
Philippines = pytz.timezone("Asia/Manila")
Alaska = pytz.timezone("US/Alaska")
Mountain = pytz.timezone("US/Mountain")
Central = pytz.timezone("US/Central")
EST = pytz.timezone("US/Eastern")
Samoa = pytz.timezone("US/Samoa")
UK = pytz.timezone("GMT")
Pacific = pytz.timezone("US/Pacific")
India = pytz.timezone("Asia/Kolkata")

# DST reminder
DST = " If DST is in effect, the actual time is an hour ahead."

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

@bot.slash_command(guild_ids=[831412377869221899, 929320814724124722], description="Sends the time in Hungary.")
async def time(ctx):
    hungary = dt.now(Hungary)
    await ctx.respond(hungary.strftime("It is %H:%M in Hungary.") + DST)

@bot.slash_command(guild_ids=[831412377869221899, 929320814724124722], description="Sends the time in the Philippines.")
async def philippines(ctx):
    phil = dt.now(Philippines)       
    await ctx.respond(phil.strftime("It is %H:%M in the Philippines.") + DST)

@bot.slash_command(guild_ids=[831412377869221899, 929320814724124722], description="Sends the Alaskan time.")
async def alaska(ctx):
    alaska = dt.now(Alaska)      
    await ctx.respond(alaska.strftime("It is %H:%M in Alaska, USA.")  + DST)

@bot.slash_command(guild_ids=[831412377869221899, 929320814724124722], description="Sends the time in Mountain Standard Time.")
async def mountain(ctx):
    mountain = dt.now(Mountain)      
    await ctx.respond(mountain.strftime("It is %H:%M in Mountain Time.") + DST)

@bot.slash_command(guild_ids=[831412377869221899, 929320814724124722], description="Sends the time in Central Time.")
async def central(ctx):
    central = dt.now(Central)
    await ctx.respond(central.strftime("It is %H:%M in US Central Time.") + DST)

@bot.slash_command(guild_ids=[831412377869221899, 929320814724124722], description="Sends the time in EST.")
async def eastern(ctx):
    est = dt.now(EST)
    await ctx.respond(est.strftime("It is %H:%M, Eastern Standard Time.") + DST)

@bot.slash_command(guild_ids=[831412377869221899, 929320814724124722], description="Sends the time in American Samoa.")
async def samoa(ctx):
    samoa = dt.now(Samoa)
    await ctx.respond(samoa.strftime("It is %H:%M in the American Samoa.") + DST)

@bot.slash_command(guild_ids=[831412377869221899, 929320814724124722], description="Sends the time in the UK.")
async def uk(ctx):
    uk = dt.now(UK)
    await ctx.respond(uk.strftime("It is %H:%M in the UK.") + DST)

@bot.slash_command(guild_ids=[831412377869221899, 929320814724124722], description="Sends the time in Pacific Time.")
async def pacific(ctx):
    pacific = dt.now(Pacific) 
    await ctx.respond(pacific.strftime("It is %H:%M in Pacific Time.") + DST)

@bot.slash_command(guild_ids=[831412377869221899, 929320814724124722], description="Sends the time in India.")
async def india(ctx):
    india = dt.now(India) 
    await ctx.respond(india.strftime("It is %H:%M in India.") + DST)

# Intended to be like a clock tower
@bot.slash_command(guild_ids=[831412377869221899, 929320814724124722], description="Sends the time in Hungary every hour.")
async def timekeep(ctx):
    await ctx.respond("Timekeep initialized.")
    await asyncio.sleep(1)
    while True:
        hungary = dt.now(Hungary)
        await ctx.channel.send(hungary.strftime("Ding Dong! It is %H:%M in Hungary.") + DST)
        await asyncio.sleep(3600)
        if message.content == "stop":
            break

@bot.slash_command(guild_ids=[831412377869221899, 929320814724124722], description="Send the link to the GitHub repo.")
async def github(ctx):
    await ctx.respond("Hi! You can visit my repository here:\n"
                      "https://github.com/CatFishing4Guyz/hungarytime_discordbot")

@bot.slash_command(guild_ids=[831412377869221899, 929320814724124722], description="Sends the list of commands, most are self-explanatory")
async def help(ctx):
    await ctx.respond("Options:\n"
                      "`help` - show this message\n" 
                      "`github` - sends the link to my repository\n"
                      "`time` - tells the time in Hungary\n"
                      "`timekeep` - sends an update on Hungary's time every hour,"
                      " like a clock tower\n"
                      "`philippines` - tells the time in the Philippines\n"
                      "`alaska` - tells the time in Alaska\n"
                      "`mountain` - tells the US Mountain Time\n"
                      "`central` - tells the US Central Time\n"
                      "`eastern` - tells the US Eastern Standard Time\n"
                      "`pacific` - tell the US Pacific Time\n"
                      "`samoa` - tell the time in the American Samoa\n"
                      "`uk` - tell the time in the United Kingdom\n")

bot.run(os.getenv('TOKEN'))