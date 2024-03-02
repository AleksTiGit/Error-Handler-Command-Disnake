# The code for the bot is not in this repository
# There is only an error handler here

import disnake
from disnake.ext import commands

# For commands:

bot = commands.Bot(command_prefix='!', intents=disnake.Intents.default())

@bot.event
async def on_command_error(inter: disnake.ApplicationCommandInteraction, error):
  if isinstance(error, commands.MissingPermissions):
    #Instead of commands.Missing Permissions you insert your error
    embed = disnake.Embed(
        title='TITLE',
        description='Description',
        color=disnake.Color.from_rgb(rgb_color_code))
    await inter.send(embed=embed, ephemeral=True)

# For slash-commands:

bot = commands.InteractionBot(intents=disnake.Intents.default())

@bot.event
async def on_slash_command_error(inter: disnake.ApplicationCommandInteraction, error):
  if isinstance(error, commands.MissingPermissions):
    #Instead of commands.Missing Permissions you insert your error
    embed = disnake.Embed(
        title='TITLE',
        description='Description',
        color=disnake.Color.from_rgb(rgb_color_code))
    await inter.send(embed=embed, ephemeral=True)
