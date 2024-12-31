#example bot

import discord
from discord.ext import commands, tasks
from RedditNewsScraping import get_news #importing scraper function
import time

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix = "!", intents = intents)

#set up channel id where it'll communicate (replace with your own channel ID)
CHANNEL_ID = 'Here CHANNEL ID INT'

#DEFINE time intervla for fetching cyber news (24 hours = 86400 secs)
FETCH_INTERVAL = 604800 #weekly in seconds.

#to track the last time the bot got reddit posts
last_reddit_fetch = 0

#defining function so bot gets posts once every week
@tasks.loop(seconds=FETCH_INTERVAL) # allows us to create a weekly loop, fetch posts is activated.
async def fetch_posts(): #fetches posts, creates embed and posts to a discord channel.
    global last_reddit_fetch
    current_time = time.time()
    
    
    #check if it's been enough time to fetch
    if current_time - last_reddit_fetch >= FETCH_INTERVAL:
        #fetch posts from Reddit
        posts = get_news()
        last_reddit_fetch = current_time #update time of last fetch
        
        #get channel object
        channel = bot.get_channel(CHANNEL_ID)
        
        #create link embed for daily news
        embed = discord.Embed( #formatting of embed
            title="Cybersecurity News of The Week",
            description="Here's the trending cybersecurity news for the week.",
            color=discord.Color.blue()
        )
        
        #add each post to this embed that the bot posts via looping 1 by 1 
        for post in posts: 
            embed.add_field(
                name=post['Title'],
                value=f"[Read more]({post['URL']})\n Category: {post['Category']}",
                inline=False
            )
            
        
        
        #send it to discord
        await channel.send(embed=embed) #sends embed to channel 
        print(f"Posted {len(posts)} news articles to Discord.")
         
    else: #if not enough time has passed.
        print(f"No new posts have been fetched. Time until next fetch: {FETCH_INTERVAL - (current_time - last_reddit_fetch)} seconds")
        
    
 #start task when bot is ready
@bot.event #bot listens for specific event, on_ready is the event, in which bot successfully connects to discord and is ready
async def on_ready(): #performs task that may take time without block bots other tasks.
    print(f"Bot is ready") #prints message to console to confirm it works
    fetch_posts.start() #start getting posts #starts the background task that happens every 24h
        
#run the bot
    
bot.run('Discord API Key Here')

