import discord
import asyncio
import os
import ftplib

client = discord.Client()
ftp = ftplib.FTP()

os.system("title Bubble Bot (CONSOLE)")
os.system("color c")
os.system("cls")

msg_id = ""
msg_user = ""

@client.event
async def on_ready():
	
	ftp.connect("158.69.12.206", 21)
	ftp.login("IspaiHd@outlook.com.2646", "94Qr7Wjcd6")
	
	ftp.cwd("bot")
	
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
	
		embed = discord.Embed(title="** Ajuda **", description="**Comandos:\n\n$denunciar [nome] [motivo] = Denunciar Usuario\n$form = Formulario para Staffs\n$youtuber = Requisitos para cargo Youtuber\n$qualidade [mensagem] = Mandar mensagens de qualidade\n$embed [mensagem] Mandar mensagens destacadas (apenas para cargos administradores)\n$votar [votacao] = Cria uma votacao (apenas para cargos administradores)\n$encerrarvotacao = Encerrar votacao atual (apenas para cargos administradores)\n$parceria = Requisitos para parceria\n$ip = Ip do servidor\n$twitter = Twitter do servidor\n$ban [usuario] = Bane usuario do servidor (apenas para cargos administradores)\n\nMODULOS:\n\nANTI-FLOOD (BLOQUEA FRASES COM MAIS DE 800 CARACTERES)\nANTI-PALAVROES (BLOQUEA PALAVROES)**", color=0xff0000)
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
			
			global botmsg
			global votacao_a
		
			votacao = str(message.content[6:])
		
			votacao_a = "**" + "Votacao aberta por:" + str(message.author) + "\n\n" + "Assunto: __" + votacao + "__" + "\n\n" + "**"
		
			embed = discord.Embed(title="** Votacao! **", description=votacao_a, color=0xff00ff)
			botmsg = await client.send_message(message.channel, embed=embed)
			await client.add_reaction(botmsg, "✅")
			await client.add_reaction(botmsg, "❎")
			
			global emoji_1
			emoji_1 = 0
			global emoji_2
			emoji_2 = 0
			
			await client.delete_message(message)
			
	if message.content.lower().startswith("$encerrarvotacao"):
		
		if message.author.server_permissions.administrator:
			
			if emoji_1 > emoji_2:
				
				emoji_1 = 0
				emoji_2 = 0
				
				encerramento_a = "** Votacao: **" + "**" + votacao_a + "**" + "\n\n" + "**Foi aprovada com sucesso!**"
				

				embed = discord.Embed(title="** Votacao Encerrada! **", description=encerramento_a, color=0xff00ff)
				botmsg = await client.send_message(message.channel, embed=embed)
				
				await client.delete_message(message)
			
			
			elif emoji_2 > emoji_1:
			
				emoji_1 = 0
				emoji_2 = 0
				
				encerramento_a = "** Votacao: " + votacao_a + "\n\n" + "Foi negada com sucesso '-'!" + "**"
				

				embed = discord.Embed(title="** Votacao Encerrada! **", description=encerramento_a, color=0xff00ff)
				botmsg = await client.send_message(message.channel, embed=embed)
				
				await client.delete_message(message)

			elif emoji_2 == emoji_1:
			
				emoji_1 = 0
				emoji_2 = 0
				
				encerramento_a = "** Votacao: " + votacao_a + "\n\n" + "Caramba houve um empate!" + "**"
				

				embed = discord.Embed(title="** Votacao Encerrada! **", description=encerramento_a, color=0xff00ff)
				botmsg = await client.send_message(message.channel, embed=embed)
				
				await client.delete_message(message)
		
	if message.content.lower().startswith("$parceria"):
			
		embed = discord.Embed(title="** Requisitos Parceria **", description="**Requisitos para parceria com o servidor discord.\n\n\n-Canal no youtube com no minímo 100 inscritos\n-O grupo do seu discord tem que ter no minímo 20 membros\n-Ser ativo no youtube\n**", color=0x0000ff)
		await client.send_message(message.channel, embed=embed)
		
	if message.content.lower().startswith("$ban"):

		if message.author.server_permissions.administrator:
		
			usuario = message.mentions[0]
			
			await client.send_message(usuario, "** Bem eu nao consigo ler mentes...\nMais uma melda que voce fez eu sei!\nPor isso eu me diverti banindo voce :yum: **")
		
			await client.ban(usuario)
			await client.send_message(discord.Object("438020809047408661"), "**Usuario banido:{}**".format(usuario))
			await client.send_message(discord.Object("438020809047408661"), "**Banido pelo admin:{}**".format(message.author))
			await delete_message(message)
			
			
		
	if message.content.lower().startswith("$ip"):
			
		embed = discord.Embed(title="** Ip do Servidor **", description="**IP:158.69.12.206:25588 -- Minecraft 1.8 : Pirata/Original**", color=0x660066)
		await client.send_message(message.channel, embed=embed)
		
	if message.content.lower().startswith("$twitter"):
			
		embed = discord.Embed(title="** Twitter do Servidor **", description="** https://twitter.com/BubbleGamesMC?s=09 **", color=0x0066ff)
		await client.send_message(message.channel, embed=embed)
		
	if message.content.lower().startswith("$loteria"):
		
		try:
			ftp.connect("158.69.12.206", 21)
			ftp.login("IspaiHd@outlook.com.2646", "94Qr7Wjcd6")
	
			ftp.cwd("bot")
		
			try:

				ftp.retrbinary('RETR %s' % str(message.author), open(str(message.author), 'wb').write)
				author_loteria = open(str(message.author), "r").read()
				
				ftp.cwd("loteria")
				
				ftp.retrbinary('RETR %s' % "loteria.atual", open("loteria.atual"), 'wb').write)
				loteria_a = open("loteria.atual", "r").read()
				
				ftp.pwd()
				ftp.cwd("bot")
				
				embed = discord.Embed(title="** Loteria Atual **", description="**\n Descricao:{} **".format(loteria_a), color=0x7FFF00)
				await client.send_message(message.channel, embed=embed)
				
				
			except:
				
				file = open(str(message.author), "w")
				file.write("0")
				file.close()
				
				file = open(str(message.author),'rb')   
				file_v = "STOR " + str(message.author)
				ftp.storbinary(file_v, file)
				
				author_loteria = open(str(message.author), "r").read()
				
				ftp.cwd("loteria")
				
				ftp.retrbinary('RETR %s' % "loteria.atual", open("loteria.atual"), 'wb').write)
				loteria_a = open("loteria.atual", "r").read()
				
				ftp.pwd()
				ftp.cwd("bot")
				
				embed = discord.Embed(title="** Loteria Atual **", description="**\n Descricao:{} **".format(loteria_a), color=0x7FFF00)
				await client.send_message(message.channel, embed=embed)
				
				
		
		except:
			
			
			try:

				ftp.retrbinary('RETR %s' % str(message.author), open(str(message.author), 'wb').write)
				file = open(str(message.author), "r").read()
				print(file)
				
			except:
				
				try:

					ftp.retrbinary('RETR %s' % str(message.author), open(str(message.author), 'wb').write)
					author_loteria = open(str(message.author), "r").read()
				
					ftp.cwd("loteria")
				
					ftp.retrbinary('RETR %s' % "loteria.atual", open("loteria.atual"), 'wb').write)
					loteria_a = open("loteria.atual", "r").read()
				
					ftp.pwd()
					ftp.cwd("bot")
				
					embed = discord.Embed(title="** Loteria Atual **", description="**\n Descricao:{} **".format(loteria_a), color=0x7FFF00)
					await client.send_message(message.channel, embed=embed)
				
				
				except:
				
					file = open(str(message.author), "w")
					file.write("0")
					file.close()
				
					file = open(str(message.author),'rb')   
					file_v = "STOR " + str(message.author)
					ftp.storbinary(file_v, file)
				
					author_loteria = open(str(message.author), "r").read()
				
					ftp.cwd("loteria")
				
					ftp.retrbinary('RETR %s' % "loteria.atual", open("loteria.atual"), 'wb').write)
					loteria_a = open("loteria.atual", "r").read()
				
					ftp.pwd()
					ftp.cwd("bot")
				
					embed = discord.Embed(title="** Loteria Atual **", description="**\n Descricao:{} **".format(loteria_a), color=0x7FFF00)
					await client.send_message(message.channel, embed=embed)
				
				
				

				
				
			

	
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
			
	global msg_id
	msg_id = botmsg.id
	global msg_user
	msg_user = message.author

	
	
	
@client.event
async def on_reaction_add(reaction, user):
		
		global emoji_1
		global emoji_2
		
		
		msg = reaction.message
		
		if reaction.emoji == "✅" and msg.id == msg_id:
			
			emoji_1 = emoji_1 + 1
			print(emoji_1)
			
		if reaction.emoji == "❎" and msg.id == msg_id:
			
			emoji_2 = emoji_2 + 1
			print(emoji_2)
			
	
@client.event
async def on_reaction_remove(reaction, user):
	
		global emoji_1
		global emoji_2
	
		
		msg = reaction.message
		
		if reaction.emoji == "✅" and msg.id == msg_id:
			
			emoji_1 = emoji_1 - 1
			print(emoji_1)
			
			
		if reaction.emoji == "❎" and msg.id == msg_id:

			emoji_2 = emoji_2 - 1
			print(emoji_2)


client.run("NDMyMzA2OTQ5ODg3ODg1MzEz.DarYxQ.5gSmC0ajY2G6Ul8gUMbFL4yyllo")
