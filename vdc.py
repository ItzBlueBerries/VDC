import discord
from discord.embeds import Embed
from discord.ext import commands
from discord.message import DeletedReferencedMessage
from dotenv import load_dotenv
import os
from typing import Collection, List
from io import BytesIO
import asyncio
import json
from discord_slash import SlashCommand, SlashContext
import random

intents = discord.Intents.all()

load_dotenv()

TOKEN = os.getenv("TOKEN")
PREFIX = os.getenv("PREFIX")

client = commands.Bot(command_prefix=PREFIX, intents=intents)
slash = SlashCommand(client, sync_commands=True)

guild_ids = [865936964439638042]

@client.event
async def on_ready():
    # while True:
    #     with open("FruitScript/coolspam.fruitscript", "a") as f:
    #         message = f"FRUITSCRIPT : COOL SPAM, LOL."
    #         f.write(f'{message}\n\n')
    #         await asyncio.sleep(10201904019410491192491024)
    #         f.close()
    # guild = client.get_guild(865936964439638042)
    # member_count = guild.members
    activity = discord.Game(name='Server bot for Visual Discord Code. 😎 | .help')
    await client.change_presence(activity=activity)
    print(f'{client.user} is Online.')

    with open("FruitScript/login.fruitscript", "a") as f:
        message = f"{client.user} has logged in."
        f.write(f'{message}\n\n')
        f.close()

# @client.event
# async def on_raw_reaction_add(payload):
#     message_id = payload.message_id

#     if message_id == 866511422619779082:
#         guild_id = payload.guild_id
#         guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)

#         if payload.emoji.name == '1️⃣':
#             # print('Gettin\' C / C++ Role 🤠')
#             role = discord.utils.get(guild.roles, name='C / C++')
#         elif payload.emoji.name == '2️⃣':
#             # print('Gettin\' Javascript Role 🤠')
#             role = discord.utils.get(guild.roles, name='Javascript')
#         if payload.emoji.name == '3️⃣':
#             # print('Gettin\' C / C++ Role 🤠')
#             role = discord.utils.get(guild.roles, name='Java')
#         elif payload.emoji.name == '4️⃣':
#             # print('Gettin\' Javascript Role 🤠')
#             role = discord.utils.get(guild.roles, name='Python')      
#         if payload.emoji.name == '5️⃣':
#             # print('Gettin\' C / C++ Role 🤠')
#             role = discord.utils.get(guild.roles, name='Typescript')
#         elif payload.emoji.name == '6️⃣':
#             # print('Gettin\' Javascript Role 🤠')
#             role = discord.utils.get(guild.roles, name='Lua')
#         if payload.emoji.name == '7️⃣':
#             # print('Gettin\' C / C++ Role 🤠')
#             role = discord.utils.get(guild.roles, name='Haxe')
#         elif payload.emoji.name == '8️⃣':
#             # print('Gettin\' Javascript Role 🤠')
#             role = discord.utils.get(guild.roles, name='Assembly')
#         else:
#             role = discord.utils.get(guild.roles, name=payload.emoji.name)

#         if role is not None:
#             print(role.name)
#             member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
#             if member is not None:
#                 await member.add_roles(role)
#                 print('Ay! Someone got a role, lol. 🤠')
#             else:
#                 print('Member not found, oof, lol. 🤠')
#         else:
#             print('Role not found, oof, lol. 🤠')

# @client.event
# async def on_raw_reaction_remove(payload):
#     print('...')

# FruitScript Lol

@slash.slash(name='vdc', description='Gives information on Visual Discord Code.', guild_ids=guild_ids)
async def vdc(ctx):
    VDC = discord.Embed(title='Visual Discord Code', description='Information on VISUAL DISCORD CODE~!', colour=discord.Colour.blurple())

    VDC.add_field(name='Description', 
                    value='Visual Discord Code is a programming server for programmers, non-programmers and any such, they provide coding help and such. If you are a programmer I recommend this server, I am the server bot of this server and have been programmed by one of the creators.', inline=False)
    VDC.add_field(name='Creators',
                    value='`Fruitsy#6513` & `GWebDev#3166` created this server out of it starting out as a testing server for both of them.')
    VDC.add_field(name='Featured Staff Members',
                    value=f'{yes}')
    VDC.add_field(name='Shareable Invite', 
                    value='`https://discord.gg/vwZP83zN6b`')

    await ctx.send(embed=VDC)

with open('FruitScript/featured.fruitscript', 'r') as file:
    yes = "".join(file.readlines())

@client.group(invoke_without_command=True)
async def vdc(ctx):
    """ [desc, creators, featuredsm, sinv] """
    VDC = discord.Embed(title='Visual Discord Code', description='Information on VISUAL DISCORD CODE~!', colour=discord.Colour.blurple())

    VDC.add_field(name='Description', 
                    value='Visual Discord Code is a programming server for programmers, non-programmers and any such, they provide coding help and such. If you are a programmer I recommend this server, I am the server bot of this server and have been programmed by one of the creators.', inline=False)
    VDC.add_field(name='Creators',
                    value='`Fruitsy#6513` & `GWebDev#3166` created this server out of it starting out as a testing server for both of them.')
    VDC.add_field(name='Featured Staff Members',
                    value=f'{yes}')
    VDC.add_field(name='Shareable Invite', 
                    value='`https://discord.gg/vwZP83zN6b`')

    await ctx.send(embed=VDC)

@vdc.command(aliases=['desc'])
async def description(ctx):
    VDC_DESC = discord.Embed(title='Description', description='Visual Discord Code is a programming server for programmers, non-programmers and any such, they provide coding help and such. If you are a programmer I recommend this server, I am the server bot of this server and have been programmed by one of the creators.', colour=discord.Colour.blurple())

    await ctx.send(embed=VDC_DESC)

@vdc.command(aliases=['owners'])
async def creators(ctx):
    VDC_CREATORS = discord.Embed(title='Creators', description='`Fruitsy#6513` & `GWebDev#3166` created this server out of it starting out as a testing server for both of them.', colour=discord.Colour.blurple())

    await ctx.send(embed=VDC_CREATORS)

@vdc.command(aliases=['fsm'])
async def featuredsm(ctx):
    VDC_FEATURED = discord.Embed(title='Featured Staff Members', description='`None at the moment.`', colour=discord.Colour.blurple())

    await ctx.send(embed=VDC_FEATURED)

@vdc.command(aliases=['sinv'])
async def shareinv(ctx):
    VDC_INVITE = discord.Embed(title='Shareable Invite', description='`https://discord.gg/vwZP83zN6b`', colour=discord.Colour.blurple())

    await ctx.send(embed=VDC_INVITE)

@client.command()
async def report(ctx, member : discord.Member,*, report):
    channel = client.get_channel(866679746665644032)

    if report is None:
        await ctx.send('Description of Report?')
        return

    reportEmbed = discord.Embed(title='Report Message', description=f'New report that you should review..', colour=discord.Colour.blurple())
    
    reportEmbed.add_field(name='Reporter', value=f'<@{ctx.message.author.id}>')
    reportEmbed.add_field(name='Reported', value=f'{member.mention}')
    reportEmbed.add_field(name='Description of Report', value=f'`{report}`')

    await channel.send(embed=reportEmbed)
    await ctx.send('Your report has been logged.')

    with open("FruitScript/report.fruitscript", "a") as f:
        message = str(report)
        f.write(f'{ctx.message.author} Reported {member} || {message}\n\n')
        f.close()

@slash.slash(name='report', description='Reports a member.', guild_ids=guild_ids)
async def report(ctx, member : discord.Member,*, report):
    channel = client.get_channel(866679746665644032)

    if report is None:
        await ctx.send('Description of Report?')
        return

    reportEmbed = discord.Embed(title='Report Message', description=f'New report that you should review..', colour=discord.Colour.blurple())
    
    reportEmbed.add_field(name='Reporter', value=f'<@{ctx.author.id}>')
    reportEmbed.add_field(name='Reported', value=f'{member.mention}')
    reportEmbed.add_field(name='Description of Report', value=f'`{report}`')

    await channel.send(embed=reportEmbed)
    await ctx.send('Your report has been logged.')

    with open("FruitScript/report.fruitscript", "a") as f:
        message = str(report)
        f.write(f'{ctx.author} Reported {member} || {message}\n\n')
        f.close()

@client.command()
@commands.is_owner()
async def feature(ctx, message):
    with open("FruitScript/featured.fruitscript", "a") as f:
        message = str(message)
        f.write(f'`{message}`, ')
        f.close()
    
    await ctx.send(f'I have successfully added `{message}` to the featured staff list.')

async def fetch_attachments(attachments: List[discord.Attachment]) -> List[discord.File]:
    return await asyncio.gather(*[attachment.to_file() for attachment in attachments])

# @client.event
# async def on_message(message):
#     if message.author.bot:
#         return

#     if not isinstance(message.channel, discord.DMChannel):
#         return

#     creator_dm_channel = client.get_channel(866532573396467722)
#     cloned_message = await creator_dm_channel.send(
#         f"Woah I was DMed by {message.author}: \n```\uFEFF{message.content}```",
#         files=await fetch_attachments(message.attachments),
#     )

#     def reply_check(m):
#         if not m.reference:
#             return False

#         return m.reference.message_id == cloned_message.id

#     reply = await client.wait_for("message", check=reply_check)
#     await message.reply(reply.content, files=await fetch_attachments(reply.attachments))

@client.command()
async def ping(ctx, pinged):
    if pinged == '<@':
        await ctx.send('I said supply a tag. :/')
        return
    elif pinged == '@':
        await ctx.send('I said supply a tag. :/')
        return
    else:
        await ctx.send(f'{ctx.message.author.mention}')

        with open("FruitScript/pinged.fruitscript", "a") as f:
            message = f"{pinged} idk"
            f.write(f'{message}\n')
            f.close()

# @slash.slash(name='test', description='test', guild_ids=guild_ids)
# async def test(ctx, arg1, arg2):
#     await ctx.send(f'{random.choice([arg1, arg2])}')

@client.event
async def on_member_join(member):
    channel = client.get_channel(865936964439638047)

    welcomeEmbed = discord.Embed(title='Welcoming~!', description=f'Welcome to {member.guild.name}, {member.mention}! Please read <#866164519222247435>.', colour=discord.Colour.blurple())

    await channel.send(f'{member.mention}', embed=welcomeEmbed)

    with open("FruitScript/welcome.fruitscript", "a") as f:
        message = f"{member} joined Visual Discord Code."
        f.write(f'{message}\n\n')
        f.close()

@client.event
async def on_member_remove(member):
    channel = client.get_channel(865936964439638047)

    welcomeEmbed = discord.Embed(title='Goodbye~!', description=f'{member.mention}, thanks for your time staying here!', colour=discord.Colour.blurple())

    await channel.send(f'{member.mention}', embed=welcomeEmbed)

    with open("FruitScript/goodbye.fruitscript", "a") as f:
        message = f"{member} left Visual Discord Code."
        f.write(f'{message}\n\n')
        f.close()

@client.event
async def on_command_error(ctx: commands.Context, error: commands.CommandError):
    if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(error)
            print(error)
            return

    elif isinstance(error, commands.CommandNotFound):
        await ctx.send(error)
        print(error)
        return

    elif isinstance(error, commands.BotMissingPermissions):
        await ctx.send(error)
        print(error)
        return

    elif isinstance(error, commands.BadArgument):
        await ctx.send(error)
        print(error)
        return
    
    elif isinstance(error, commands.DisabledCommand):
        await ctx.send(error)
        print(error)
        return
    
    elif isinstance(error, commands.ExtensionAlreadyLoaded):
        await ctx.send(error)
        print(error)
        return
    
    elif isinstance(error, commands.ExtensionError):
        await ctx.send(error)
        print(error)
        return
    
    elif isinstance(error, commands.ExtensionFailed):
        await ctx.send(error)
        print(error)
        return
    
    elif isinstance(error, commands.ExtensionNotFound):
        await ctx.send(error)
        print(error)
        return

    elif isinstance(error, commands.ExtensionNotLoaded):
        await ctx.send(error)
        print(error)
        return
    
    elif isinstance(error, commands.MissingRole):
        await ctx.send(error)
        print(error)
        return
    
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send(error)
        print(error)
        return

    elif isinstance(error, commands.BotMissingRole):
        await ctx.send(error)
        print(error)
        return
    
    elif isinstance(error, commands.MemberNotFound):
        await ctx.send(error)
        print(error)
        return
    
    elif isinstance(error, commands.NoPrivateMessage):
        await ctx.send(error)
        print(error)
        return

    elif isinstance(error, commands.NotOwner):
        await ctx.send(error)
        print(error)
        return
    
    elif isinstance(error, commands.MessageNotFound):
        await ctx.send(error)
        print(error)
        return
    
    elif isinstance(error, commands.RoleNotFound):
        await ctx.send(error)
        print(error)
        return
    
    elif isinstance(error, commands.UserNotFound):
        await ctx.send(error)
        print(error)
        return
    
    elif isinstance(error, commands.EmojiNotFound):
        await ctx.send(error)
        print(error)
        return

    elif isinstance(error, commands.GuildNotFound):
        await ctx.send(error)
        print(error)
        return
    
    elif isinstance(error, commands.ChannelNotFound):
        await ctx.send(error)
        print(error)
        return
    
    elif isinstance(error, commands.CommandInvokeError):
        await ctx.send(error)
        print(error)
        return
    
    elif isinstance(error, commands.TooManyArguments):
        await ctx.send(error)
        print(error)
        return
    
    elif isinstance(error, commands.CommandOnCooldown):
        await ctx.send(error)
        print(error)
        return

    else:

        raise error

client.run(TOKEN)