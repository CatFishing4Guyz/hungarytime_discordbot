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

# Add DST reminder
ifDST = " If DST is in effect, the actual time is an hour ahead."

# Main body
bot = discord.Bot(activity = discord.Activity(
    type=discord.ActivityType.watching, 
    name="ur mom undress."))

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

"""
Remove the guild ID and replace
it with your own servers' if you want
slash commands to update immediately.

Enable developer mode in Discord and
right click on your server from the 
server list and select "Copy ID"
"""
@bot.slash_command(guild_ids=[831412377869221899], description="Sends the time in Hungary")
async def time(ctx):
    dt_hungary = dt.now(Hungary)
    timesend = dt_hungary.strftime("It is %H:%M in Hungary.")
    await ctx.respond(timesend + ifDST)

@bot.slash_command(guild_ids=[831412377869221899], description="Sends the time in the Philippines.")
async def philippines(ctx):
    dt_ph = dt.now(Philippines)
    ph_timesend = dt_ph.strftime("It is %H:%M in the Philippines.")        
    await ctx.respond(ph_timesend + ifDST)

@bot.slash_command(guild_ids=[831412377869221899], description="Sends the Alaskan time.")
async def alaska(ctx):
    dt_alaska = dt.now(Alaska)
    alaska_timesend = dt_alaska.strftime("It is %H:%M in Alaska, USA.")        
    await ctx.respond(alaska_timesend + ifDST)

@bot.slash_command(guild_ids=[831412377869221899], description="Sends the time in Mountain Standard Time.")
async def mountain(ctx):
    dt_mountain = dt.now(Mountain)
    mountain_timesend = dt_mountain.strftime("It is %H:%M in Mountain Time.")        
    await ctx.respond(mountain_timesend + ifDST)

@bot.slash_command(guild_ids=[831412377869221899], description="Sends the time in Central Time.")
async def central(ctx):
    dt_central = dt.now(Central)
    central_timesend = dt_central.strftime("It is %H:%M in US Central Time.")
    await ctx.respond(central_timesend + ifDST)

@bot.slash_command(guild_ids=[831412377869221899], description="Sends the time in EST.")
async def eastern(ctx):
    dt_est = dt.now(EST)
    est_timesend = dt_est.strftime("It is %H:%M, Eastern Standard Time.")
    await ctx.respond(est_timesend + ifDST)

@bot.slash_command(guild_ids=[831412377869221899], description="Sends the time in American Samoa.")
async def samoa(ctx):
    dt_samoa = dt.now(Samoa)
    samoa_timesend = dt_samoa.strftime("It is %H:%M in American Samoa.")
    await ctx.respond(samoa_timesend + ifDST)

@bot.slash_command(guild_ids=[831412377869221899], description="Sends the time in the UK.")
async def uk(ctx):
    dt_uk = dt.now(UK)
    uk_timesend = dt_uk.strftime("It is %H:%M in the UK.")
    await ctx.respond(uk_timesend + ifDST)

@bot.slash_command(guild_ids=[831412377869221899], description="Sends the time in Pacific Time")
async def pacific(ctx):
    dt_pacific = dt.now(Pacific)
    pacific_timesend = dt_pacific.strftime("It is %H:%M in Pacific Time.")
    await ctx.respond(pacific_timesend + ifDST)

@bot.slash_command(guild_ids=[831412377869221899], description="Send link to the GitHub repo.")
async def github(ctx):
    await ctx.respond("Hi! You can visit my repo here:\n"
                      "<https://github.com/Monkeys30/hungarytime_discordbot>")

@bot.slash_command(guild_ids=[831412377869221899], description="The help command")
async def help(ctx):
    await ctx.respond("Options:\n `help` - show this message\n" 
                      "`github` - share the repository link\n"
                      "`time` - tell the time in Hungary\n")

# Intended to be like a clock tower
@bot.slash_command(guild_ids=[831412377869221899], description="Sends the time in Hungary every hour.")
async def timekeep(ctx):
    await ctx.respond("Timekeep initialized.")
    await asyncio.sleep(1)
    while True:
        dt_hungary = dt.now(Hungary)
        timesend = dt_hungary.strftime("Ding Dong! It is %H:%M in Hungary.")
        await ctx.channel.send(timesend + ifDST)
        await asyncio.sleep(3600)

bot.run(os.getenv('TOKEN'))