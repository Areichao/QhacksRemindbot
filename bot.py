'''
simple bot to give test and class reminders 
''' 

import os 
import discord 
import asyncio
import dates
from dotenv import load_dotenv
from datetime import datetime
from keepalive import keepAlive

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()
links = {} #class links
test = {} #test dates
assignments = {} #assignment due dates

#dictionary arrays? array of dictionaries¿ thingies for links, tests, assignments instead of ^^^

def print_instructions():
    await message.channel.send(
        "**Feed Information**\n" +
        "\n**&addZoom** to add a zoom link for your class\n" +
        "**&addTest** to add a test day, gets removed after day has passed\n" +
        "**&addAssign** to add a due date for your assignments, gets removed after day has passed\n" +
        "\nType your information after the command (see examples)\n" +
        "\n**Get Information**\n" +
        "\n**&getLink** to get the link for your classes\n" +
        "**&getTest** to get all the test dates\n" +
        "**&getAssign** to get the due dates for assignments (dd/mm/yyyy)\n" +
        "\n**Examples**\n" +
        "&addZoom [link] [course name]\n" +
        "&addZoom ryerson.zoom.us/j/91234177013 math\n" +
        "&addTest [date] [subject name]\n" +
        "&addTest 03/12/2020 math\n" +
        "&addAssign [date] [assignment name]\n"+
        "&addAssign 14/12/2021 Politics Essay\n_ _"
        )

def addLink(link, course): #string, string 
    #add link and course to dictionary
    links[course] = link
    await message.channel.send("Yessir, use &getZoom to see all zoom links")
    #print(zoom_links) #here to test and see whats thing and then we just delete

def addTest(date): #dates object (also has name)
    #add test date and course to map
    _date = date.get_day + "/" + date.get_month + "/" + date.get_year
    test[date.get_name] = _date
    await message.channel.send("Gotchu bruhther, use &getTest to see test days")
    #print(test_dates)#here to test and see whats thing and then we just delete

def addAssign(date):
    #add assignment date    
    _date = date.get_day + "/" + date.get_month + "/" + date.get_year
    assignments[date.get_name] = _date
    await message.channel.send("Understood, use &getAssign to see assignments")
    #print(assignment_dates)#here to test and see whats thing and then we just delete

def getLink():
    #get and return the link for the class
    await message.channel.send(links)

def getTest():
    #get and return all tests date + time    
    #will be deleted after the day/time for it has passed? yes
    await message.channel.send(test)

def getAssign():
    #get and return due dates of assignemnts/tests
    #will be deleted after the day/time for it has passed? yea
    await message.channel.send(assignments)

def deleteLinks(course):
    if course in links:
        del links[course]

def deleteTest(date.get_name):
    if date.get_name in test:
        del test[date.get_name]

def deleteAssignments(date.get_name):
    if date.get_name in assignments:
        del assignments[date.get_name]
        
def reset():
    """ resets all dictionaries """
    lists.clear()
    test.clear()
    assignments.clear()

async def check_time():
    time_now = datetime.datetime.now



@tasks.loop(minutes=30)
async def check():
    check_time()

@check
async def before():
    await bot.wait_until_ready()

check.start()

@client.event
async def on_ready():
    await client.change_presence(activity = discord.activity(type=discord.ActivityType.watching, name="your mom"))
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return 
    
    if message.content.startswith('&addLink'):
        #call addzoom function
        answer = (message.content[9:]).split(' ') 

        link = answer[0]
        course = answer[1]

        addZoom(link, course)
        return 
    
    if message.content.startswith('&addTest'):
        #call addtest function
        answer = message.content[9:].split(' ')
        d = answer[0]

        date = dates() #test date
        date.set_day = d[:2]
        date.set_month = d[3:5]
        date.set_year = d[6:]
        date.set_name = answer[1]

        addTest(date)
        return
    
    if message.content.startswith('&addAssign'): 
        #call adddate function || assignments
        answer = message.content[11:].split(' ') #date assignment name
        d = answer[0]
        
        assignment = dates() #assignment info
        assignment.set_day = d[:2]
        assignment.set_month = d[3:5]
        assignment.set_year = d[6:]
        assignment.set_name = answer[1]

        addAssign(assignment)
        return 
    
    if message.content.startswith('&getLink'):
        #call getlink function, throws all links at person
        getLink()
        return

    if message.content.startswith('&getTest'):
        #call getdate function, send which assignment to get date for
        getTest()
        return 

    if message.content.startswith('&getAssign'):
        #call getdate function, send which assignment to get date for
        getAssign()
        return 

    if message.content.startswith('&help'):
        #print out commands
        print_instructions()
        return 

keepAlive()
client.run(os.getenv('TOKEN'))

#**********************************************cheat sheet**************************************************************************
'''
# Playing Status
await client.change_presence(activity=discord.Game('Sea of Thieves'))

# Stream Status
await client.change_presence(activity=discord.Streaming(name='Sea of Thieves', url='https://www.twitch.tv/your_channel_here'))

# Watching Status
await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='The Boys'))

# Listening Status
await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='The Boys'))


# Status for Long Running Commands TK
## Imports
import time

## Commands
@client.command()
async def longcommand(ctx):
    # Get previous activity
    previous_status = client.guilds[0].get_member(client.user.id).activity
    
    # Change activity for the task
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='to Your Commands!'))
    
    # Long Running Task
    time.sleep(5)
    await ctx.send('Task Complete!')
    
    # Reset the status
    await client.change_presence(activity=previous_status)

    
# Dynamic Content
## Create Dynamic Content/Text
activity_string = 'on {} servers.'.format(len(client.guilds))

## Change Status with Dynamic Content
await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=activity_string))

'''