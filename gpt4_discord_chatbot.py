import os
import discord
from discord.ext import commands
import openai

# Set up the GPT-4 API key and Discord bot token
openai.api_key =
TOKEN = 

# Set up the Discord bot
bot = commands.Bot(command_prefix='!', intents = discord.Intents.all())


# Define the command for the chatbot
@bot.command(name="chat")
async def chat(ctx, *, message: str):
    try:
        # Use the GPT-4 API to generate a response
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=f"User: {message}\nAI:",
            max_tokens=50,
            n=1,
            stop=None,
            temperature=0.8,
        )

        # Extract the response and send it back to the Discord channel
        answer = response.choices[0].text.strip()
        await ctx.send(f"AI: {answer}")
    except Exception as e:
        print(e)
        await ctx.send("Sorry, there was an error processing your request.")

# Start the Discord bot
bot.run(TOKEN)
