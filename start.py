import discord
import asyncio
import os

client = discord.Client()

os.system("title Bubble Bot (CONSOLE)")
os.system("color c")
os.system("cls")

@client.event
async def on_ready():

	await client.send_message(discord.Object("426087124593278988"), "**VROTEI PRA PUDER DAR UMAS CENSURAS HEHE**")
	await client.change_presence(game=discord.Game(name='$ajuda = Comandos'))
	print("")
	print("Bubble Bot Iniciado!")
	print("")
	
	
	
@client.event
async def on_message(message):

	if message.content.lower().startswith("$denunciar"):
	
		nome_denunciado = message.content[11:]
		await client.delete_message(message)
		
		denuncia_texto = "**Denuncia Feita Por:" + str(message.author) + "\n\nDenuncia Feita: " + nome_denunciado + "**"
		
		embed = discord.Embed(title="** Nova Denuncia **", description=denuncia_texto, color=0xff0000)
		
		await client.send_message(discord.Object("432189181457072129"), embed=embed)
		
	if message.content.lower().startswith("$youtuber"):
	
		embed = discord.Embed(title="** Requisitos Youtuber **", description="**Tag YouTuber : 130 subs + 1 vídeo no servidor com no mínimo 20 visualizações e 5 likes\n\nTag YouTuber Plus : 300 subs + 2 videos no server com no mínimo 60 visualizações e 20 likes**", color=0x0000ff)
		await client.send_message(message.channel, embed=embed)

	if message.content.lower().startswith("$form"):
	
		embed = discord.Embed(title="** Formulario para Staffs **", description="https://docs.google.com/forms/u/3/d/1hlJrKhrrGO1J0oXYJbzApJ2g4HfklvmfR0NbodwneBs/edit?usp=drive_web", color=0xcc6600)
		await client.send_message(message.channel, embed=embed)

	if message.content.lower().startswith("$ajuda"):
	
		embed = discord.Embed(title="** Ajuda **", description="**Comandos:\n\n$denunciar (nome) (motivo) = Denunciar Usuario\n$form = Formulario para Staffs\n$youtuber = Requisitos para cargo Youtuber **", color=0xff0000)
		await client.send_message(message.author, embed=embed)
		await client.delete_message(message)

	if message.content.lower().startswith("$embed"):
	
		if message.author.server_permissions.administrator:
	
			titulo = "**" + str(message.author) + "**"
		
			mensagem_embed = "**" + message.content[7:] + "**"
		
			embed = discord.Embed(title=titulo, description=mensagem_embed, color=0xff0000)
			await client.send_message(message.channel, embed=embed)
			await client.delete_message(message)
		
	else:
	
		frase = message.content.lower()
		
		
		if "PORRA".lower() in frase:
		
			palava = "**" + str(message.author) + " TUTUTU UM PALAVRAO FOI DETECTADO" + "**"
			
			embed = discord.Embed(title="** AVAST DETECTOR DE PALAVROES **", description=palava, color=0x00ff00)
			await client.send_message(message.channel, embed=embed)
			await client.delete_message(message)
			
		elif "MERDA".lower() in frase:
		
			palava = "**" + str(message.author) + " TUTUTU UM PALAVRAO FOI DETECTADO" + "**"
			
			embed = discord.Embed(title="** AVAST DETECTOR DE PALAVROES **", description=palava, color=0x00ff00)
			await client.send_message(message.channel, embed=embed)
			await client.delete_message(message)
			
		elif "FILHO DA PUTA".lower() in frase:
		
			palava = "**" + str(message.author) + " TUTUTU UM PALAVRAO FOI DETECTADO" + "**"
			
			embed = discord.Embed(title="** AVAST DETECTOR DE PALAVROES **", description=palava, color=0x00ff00)
			await client.send_message(message.channel, embed=embed)
			await client.delete_message(message)
			
		elif "CARALHO".lower() in frase:
		
			palava = "**" + str(message.author) + " TUTUTU UM PALAVRAO FOI DETECTADO" + "**"
			
			embed = discord.Embed(title="** AVAST DETECTOR DE PALAVROES **", description=palava, color=0x00ff00)
			await client.send_message(message.channel, embed=embed)
			await client.delete_message(message)
			
		elif "KRL".lower() in frase:
		
			palava = "**" + str(message.author) + " TUTUTU UM PALAVRAO FOI DETECTADO" + "**"
			
			embed = discord.Embed(title="** AVAST DETECTOR DE PALAVROES **", description=palava, color=0x00ff00)
			await client.send_message(message.channel, embed=embed)
			await client.delete_message(message)
			
		elif "PUTA QUE PARIU".lower() in frase:
		
			palava = "**" + str(message.author) + " TUTUTU UM PALAVRAO FOI DETECTADO" + "**"
			
			embed = discord.Embed(title="** AVAST DETECTOR DE PALAVROES **", description=palava, color=0x00ff00)
			await client.send_message(message.channel, embed=embed)
			await client.delete_message(message)
			
		elif "VAI TOMA NO CU".lower() in frase:
		
			palava = "**" + str(message.author) + " TUTUTU UM PALAVRAO FOI DETECTADO" + "**"
			
			embed = discord.Embed(title="** AVAST DETECTOR DE PALAVROES **", description=palava, color=0x00ff00)
			await client.send_message(message.channel, embed=embed)
			await client.delete_message(message)
			
		elif "BUCETA".lower() in frase:
		
			palava = "**" + str(message.author) + " TUTUTU UM PALAVRAO FOI DETECTADO" + "**"
			
			embed = discord.Embed(title="** AVAST DETECTOR DE PALAVROES **", description=palava, color=0x00ff00)
			await client.send_message(message.channel, embed=embed)
			await client.delete_message(message)
			
		elif "PQP".lower() in frase:
		
			palava = "**" + str(message.author) + " TUTUTU UM PALAVRAO FOI DETECTADO" + "**"
			
			embed = discord.Embed(title="** AVAST DETECTOR DE PALAVROES **", description=palava, color=0x00ff00)
			await client.send_message(message.channel, embed=embed)
			await client.delete_message(message)
			
			
		elif "FDP".lower() in frase:
		
			palava = "**" + str(message.author) + " TUTUTU UM PALAVRAO FOI DETECTADO" + "**"
			
			embed = discord.Embed(title="** AVAST DETECTOR DE PALAVROES **", description=palava, color=0x00ff00)
			await client.send_message(message.channel, embed=embed)
			await client.delete_message(message)
			
			
		elif "VTNC".lower() in frase:
		
			palava = "**" + str(message.author) + " TUTUTU UM PALAVRAO FOI DETECTADO" + "**"
			
			embed = discord.Embed(title="** AVAST DETECTOR DE PALAVROES **", description=palava, color=0x00ff00)
			await client.send_message(message.channel, embed=embed)
			await client.delete_message(message)
	
		elif "BOIOLA".lower() in frase:
		
			palava = "**" + str(message.author) + " TUTUTU UM PALAVRAO FOI DETECTADO" + "**"
			
			embed = discord.Embed(title="** AVAST DETECTOR DE PALAVROES **", description=palava, color=0x00ff00)
			await client.send_message(message.channel, embed=embed)
			await client.delete_message(message)
			
		elif "ROLA".lower() in frase:
		
			palava = "**" + str(message.author) + " TUTUTU UM PALAVRAO FOI DETECTADO" + "**"
			
			embed = discord.Embed(title="** AVAST DETECTOR DE PALAVROES **", description=palava, color=0x00ff00)
			await client.send_message(message.channel, embed=embed)
			await client.delete_message(message)
			
		elif "PAU NO CU".lower() in frase:
		
			palava = "**" + str(message.author) + " TUTUTU UM PALAVRAO FOI DETECTADO" + "**"
			
			embed = discord.Embed(title="** AVAST DETECTOR DE PALAVROES **", description=palava, color=0x00ff00)
			await client.send_message(message.channel, embed=embed)
			await client.delete_message(message)
			
		elif "BENGA".lower() in frase:
		
			palava = "**" + str(message.author) + " TUTUTU UM PALAVRAO FOI DETECTADO" + "**"
			
			embed = discord.Embed(title="** AVAST DETECTOR DE PALAVROES **", description=palava, color=0x00ff00)
			await client.send_message(message.channel, embed=embed)
			await client.delete_message(message)
			
		elif "GAY".lower() in frase:
		
			palava = "**" + str(message.author) + " TUTUTU UM PALAVRAO FOI DETECTADO" + "**"
			
			embed = discord.Embed(title="** AVAST DETECTOR DE PALAVROES **", description=palava, color=0x00ff00)
			await client.send_message(message.channel, embed=embed)
			await client.delete_message(message)
			
		elif "VIADO".lower() in frase:
		
			palava = "**" + str(message.author) + " TUTUTU UM PALAVRAO FOI DETECTADO" + "**"
			
			embed = discord.Embed(title="** AVAST DETECTOR DE PALAVROES **", description=palava, color=0x00ff00)
			await client.send_message(message.channel, embed=embed)
			await client.delete_message(message)
			
		elif "BIXA".lower() in frase:
		
			palava = "**" + str(message.author) + " TUTUTU UM PALAVRAO FOI DETECTADO" + "**"
			
			embed = discord.Embed(title="** AVAST DETECTOR DE PALAVROES **", description=palava, color=0x00ff00)
			await client.send_message(message.channel, embed=embed)
			await client.delete_message(message)

		elif "PUTO".lower() in frase:
		
			palava = "**" + str(message.author) + " TUTUTU UM PALAVRAO FOI DETECTADO" + "**"
			
			embed = discord.Embed(title="** AVAST DETECTOR DE PALAVROES **", description=palava, color=0x00ff00)
			await client.send_message(message.channel, embed=embed)
			await client.delete_message(message)
			
	
		elif "PUTAO".lower() in frase:
		
			palava = "**" + str(message.author) + " TUTUTU UM PALAVRAO FOI DETECTADO" + "**"
			
			embed = discord.Embed(title="** AVAST DETECTOR DE PALAVROES **", description=palava, color=0x00ff00)
			await client.send_message(message.channel, embed=embed)
			await client.delete_message(message)
			
		elif "GAYZAO".lower() in frase:
		
			palava = "**" + str(message.author) + " TUTUTU UM PALAVRAO FOI DETECTADO" + "**"
			
			embed = discord.Embed(title="** AVAST DETECTOR DE PALAVROES **", description=palava, color=0x00ff00)
			await client.send_message(message.channel, embed=embed)
			await client.delete_message(message)
	
		elif "BIXAO".lower() in frase:
		
			palava = "**" + str(message.author) + " TUTUTU UM PALAVRAO FOI DETECTADO" + "**"
			
			embed = discord.Embed(title="** AVAST DETECTOR DE PALAVROES **", description=palava, color=0x00ff00)
			await client.send_message(message.channel, embed=embed)
			await client.delete_message(message)

			
		elif "CUZAO".lower() in frase:
		
			palava = "**" + str(message.author) + " TUTUTU UM PALAVRAO FOI DETECTADO" + "**"
			
			embed = discord.Embed(title="** AVAST DETECTOR DE PALAVROES **", description=palava, color=0x00ff00)
			await client.send_message(message.channel, embed=embed)
			await client.delete_message(message)
			
		elif "FODA-SE".lower() in frase:
		
			palava = "**" + str(message.author) + " TUTUTU UM PALAVRAO FOI DETECTADO" + "**"
			
			embed = discord.Embed(title="** AVAST DETECTOR DE PALAVROES **", description=palava, color=0x00ff00)
			await client.send_message(message.channel, embed=embed)
			await client.delete_message(message)
			
		elif "FODASE".lower() in frase:
		
			palava = "**" + str(message.author) + " TUTUTU UM PALAVRAO FOI DETECTADO" + "**"
			
			embed = discord.Embed(title="** AVAST DETECTOR DE PALAVROES **", description=palava, color=0x00ff00)
			await client.send_message(message.channel, embed=embed)
			await client.delete_message(message)
			
		elif "FDS".lower() in frase:
		
			palava = "**" + str(message.author) + " TUTUTU UM PALAVRAO FOI DETECTADO" + "**"
			
			embed = discord.Embed(title="** AVAST DETECTOR DE PALAVROES **", description=palava, color=0x00ff00)
			await client.send_message(message.channel, embed=embed)
			await client.delete_message(message)

	


client.run("NDMyMzA2OTQ5ODg3ODg1MzEz.DarYxQ.5gSmC0ajY2G6Ul8gUMbFL4yyllo")