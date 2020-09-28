import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
PREFIXE = os.getenv('PREFIXE')
ROLEBASE = os.getenv('ROLEBASE')

#client = commands.Bot(command_prefix='$')
client = commands.Bot(command_prefix=PREFIXE)

@client.event
async def on_ready():
    print(
        f'{client.user} est connecter au guild(serveur) suivant \n'
    )

    for guild  in client.guilds:
        print(f'- {guild.name} ')


@client.event
async def on_raw_reaction_add(payload):
    if (payload.emoji.name == "🆗"):
        ServeurRoles = payload.member.guild.roles
        for Role in ServeurRoles:
            if Role.name == ROLEBASE:
                await payload.member.add_roles(Role)
        #print('ok')
    print(f'reaction {payload.emoji}ajouté par {payload.member}')


@client.event
async def on_member_join(member):
    channel = member.guild.system_channel
    if channel is not None:
        await channel.send(f'Bienvenus {member.mention} sur le serveur ! ')

@client.command(name='list')
async def _list(ctx, arg):
    await ctx.send(arg)

@client.command(name='aide')
async def _aide(ctx):
    await ctx.send(f'```Aide : \nlist -> renvois la valeur fournis\nmsgrolemembre -> Poste le message pour avoir le role membre\nbonjours -> Dit bonjours```')


@client.command(name='bonjours')
async def _bonjours(ctx):
    await ctx.send(f'Bonjours {ctx.author.mention} ! ')




@client.command(name='msgRoleMembre')
async def _msgRoleMembre(ctx):
    channel = ctx.message.channel
    
    await channel.send(f'```reagis avec :ok: sur ce message pour avoir le role membre !```')
    messages = await channel.history(limit=3).flatten()
    for message in messages:
        if (message.content == '```reagis avec :ok: sur ce message pour avoir le role membre !```'):
            await message.add_reaction('🆗')

    #await message(ctx.message.channel.last_message_id).add_reaction('🆗')

client.run(TOKEN)