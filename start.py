import discord
import asyncio
import os

client = discord.Client()

os.system("title Bubble Bot (CONSOLE)")
os.system("color c")
os.system("cls")

msg_id = ""
msg_user = ""

@client.event
async def on_ready():

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
		await client.send_message(message.author, "**Usuario denunciado com sucesso!**")
		await client.send_message(message.author, "**Um membro da staff ira ver a denuncia e julgala!**")
		
	if message.content.lower().startswith("$youtuber"):
	
		embed = discord.Embed(title="** Requisitos Youtuber **", description="**Tag YouTuber : 130 subs + 1 vídeo no servidor com no mínimo 20 visualizações e 5 likes\n\nTag YouTuber Plus : 300 subs + 2 videos no server com no mínimo 60 visualizações e 20 likes**", color=0x0000ff)
		await client.send_message(message.channel, embed=embed)

	if message.content.lower().startswith("$form"):
	
		embed = discord.Embed(title="** Formulario para Staffs **", description="https://docs.google.com/forms/u/3/d/1hlJrKhrrGO1J0oXYJbzApJ2g4HfklvmfR0NbodwneBs/edit?usp=drive_web", color=0xcc6600)
		await client.send_message(message.channel, embed=embed)

	if message.content.lower().startswith("$ajuda"):
	
		embed = discord.Embed(title="** Ajuda **", description="**Comandos:\n\n$denunciar [nome] [motivo] = Denunciar Usuario\n$form = Formulario para Staffs\n$youtuber = Requisitos para cargo Youtuber\n$qualidade [mensagem] = Mandar mensagens de qualidade\n$embed [mensagem] Mandar mensagens destacadas (apenas para cargos administradores)\n$votar [votacao] = Cria uma votacao (apenas para cargos administradores)\nMODULOS:\n\nANTI-FLOOD (BLOQUEA FRASES COM MAIS DE 800 CARACTERES)\nANTI-PALAVROES (BLOQUEA PALAVROES)**", color=0xff0000)
		await client.send_message(message.author, embed=embed)
		await client.delete_message(message)

	if message.content.lower().startswith("$embed"):
	
		if message.author.server_permissions.administrator:
	
			titulo = "**" + str(message.author) + "**"
		
			mensagem_embed = "**" + message.content[7:] + "**"
		
			embed = discord.Embed(title=titulo, description=mensagem_embed, color=0xff0000)
			await client.send_message(message.channel, embed=embed)
			await client.delete_message(message)
			
	if message.content.lower().startswith("$qualidade"):
		
		texto_qualidade = message.content[11:]
		texto_qualidade = texto_qualidade.upper()
		
		texto_qualidade = texto_qualidade.replace(" ", "  ")
		
		texto_qualidade = texto_qualidade.replace("A", " A ")
		texto_qualidade = texto_qualidade.replace("B", " B ")
		texto_qualidade = texto_qualidade.replace("C", " C ")
		texto_qualidade = texto_qualidade.replace("D", " D ")
		texto_qualidade = texto_qualidade.replace("E", " E ")
		texto_qualidade = texto_qualidade.replace("F", " F ")
		texto_qualidade = texto_qualidade.replace("G", " G ")
		texto_qualidade = texto_qualidade.replace("H", " H ")
		texto_qualidade = texto_qualidade.replace("I", " I ")
		texto_qualidade = texto_qualidade.replace("J", " J ")
		texto_qualidade = texto_qualidade.replace("K", " K ")
		texto_qualidade = texto_qualidade.replace("L", " L ")
		texto_qualidade = texto_qualidade.replace("M", " M ")
		texto_qualidade = texto_qualidade.replace("N", " N ")
		texto_qualidade = texto_qualidade.replace("O", " O ")
		texto_qualidade = texto_qualidade.replace("P", " P ")
		texto_qualidade = texto_qualidade.replace("Q", " Q ")
		texto_qualidade = texto_qualidade.replace("R", " R ")
		texto_qualidade = texto_qualidade.replace("S", " S ")
		texto_qualidade = texto_qualidade.replace("T", " T ")
		texto_qualidade = texto_qualidade.replace("U", " U ")
		texto_qualidade = texto_qualidade.replace("V", " V ")
		texto_qualidade = texto_qualidade.replace("W", " W ")
		texto_qualidade = texto_qualidade.replace("X", " X ")
		texto_qualidade = texto_qualidade.replace("Y", " Y ")
		texto_qualidade = texto_qualidade.replace("Z", " Z ")
		
		mensagem_a = "**" + str(message.author) + " : " + texto_qualidade + "**"
		
		await client.send_message(message.channel, mensagem_a)
		await client.delete_message(message)
		
	if message.content.lower().startswith("$votar"):
		
		if message.author.server_permissions.administrator:
		
			votacao = str(message.content[6:])
		
			votacao_a = "**" + "Votacao aberta por:" + str(message.author) + "\n\n" + "Assunto: __" + votacao + "__" + "\n\n" + "**"
		
			embed = discord.Embed(title="** Votacao! **", description=votacao_a, color=0xff00ff)
			botmsg = await client.send_message(message.channel, embed=embed)
			await client.add_reaction(botmsg, ":white_check_mark:")
			await client.add_reaction(botmsg, ":x:")
			

	else:
	
		frase = message.content.lower()
		
		if frase.count("") >= 800:
			
			palava = "**" + " MANERA AI O " + str(message.author) + " " + str(frase.count("")) + " CARACTERES ..." + "**"
			
			embed = discord.Embed(title="** ANTI-FLOOD **", description=palava, color=0x00ff00)
			await client.send_message(message.channel, embed=embed)
			await client.delete_message(message)
			
		
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
			
		elif "FILHA DA PUTA".lower() in frase:
		
			palava = "**" + str(message.author) + " TUTUTU UM PALAVRAO FOI DETECTADO" + "**"
			
			embed = discord.Embed(title="** AVAST DETECTOR DE PALAVROES **", description=palava, color=0x00ff00)
			await client.send_message(message.channel, embed=embed)
			await client.delete_message(message)
			
	global botmsg
	global msg_id
	msg_id = botmsg.id
	global msg_user
	msg_user = message.author
	
	
	
@client.event
async def on_reaction_add(reaction, user):
	if message.author.server_permissions.administrator:
		
		msg = reaction.message
		
		if reaction.emoji == ":white_check_mark:" and msg.id == msg_id:
			print("teste")
		if reaction.emoji == ":white_check_mark:" and msg.id == msg_id:
			print("teste2")
	
@client.event
async def on_reaction_remove(reaction, user):
	
	if message.author.server_permissions.administrator:
		
		msg = reaction.message
		
		if reaction.emoji == ":white_check_mark:" and msg.id == msg_id:
			print("teste-")
		if reaction.emoji == ":white_check_mark:" and msg.id == msg_id:
			print("teste2-")


client.run("NDMyMzA2OTQ5ODg3ODg1MzEz.DarYxQ.5gSmC0ajY2G6Ul8gUMbFL4yyllo")
