import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
from typing import Collection, List
from io import BytesIO
import asyncio

intents = discord.Intents.all()

load_dotenv()

TOKEN = os.getenv("TOKEN")
PREFIX = os.getenv("PREFIX")

client = commands.Bot(command_prefix=PREFIX, intents=intents)

@client.event
async def on_ready():
    # guild = client.get_guild(865936964439638042)
    # member_count = guild.members
    activity = discord.Game(name='Server bot for Visual Discord Code. 😎 | .help')
    await client.change_presence(activity=activity)
    print(f'{client.user} is Online.')

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

@client.group(invoke_without_command=True)
async def vdc(ctx):
    VDC = discord.Embed(title='Visual Discord Code', description='Information on VISUAL DISCORD CODE~!', colour=discord.Colour.blurple())

    VDC.add_field(name='Description', 
                    value='Visual Discord Code is a programming server for programmers, non-programmers and any such, they provide coding help and such. If you are a programmer I recommend this server, I am the server bot of this server and have been programmed by one of the creators.', inline=False)
    VDC.add_field(name='Creators',
                    value='`Fruitsy#6513` & `GWebDev#3166` created this server out of it starting out as a testing server for both of them.')
    VDC.add_field(name='Featured Staff Members',
                    value='`None at the moment.`')
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
async def report(ctx):
    return

async def fetch_attachments(attachments: List[discord.Attachment]) -> List[discord.File]:
    return await asyncio.gather(*[attachment.to_file() for attachment in attachments])

@client.event
async def on_message(message):
    if message.author.bot:
        return

    if not isinstance(message.channel, discord.DMChannel):
        return

    creator_dm_channel = client.get_channel(866532573396467722)
    cloned_message = await creator_dm_channel.send(
        f"Woah I was DMed by {message.author}: \n```\uFEFF{message.content}```",
        files=await fetch_attachments(message.attachments),
    )

    def reply_check(m):
        if not m.reference:
            return False

        return m.reference.message_id == cloned_message.id

    reply = await client.wait_for("message", check=reply_check)
    await message.reply(reply.content, files=await fetch_attachments(reply.attachments))

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