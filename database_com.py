def encoder_mot_cle(texte, mot_cle):
    # Dictionnaire de correspondance entre les lettres et les chiffres
    correspondance = {
        'A': 0,'B': 1,'C': 2,'D': 3,
        'E': 4,'F': 5,'G': 6,'H': 7,
        'I': 8,'J': 9,'K': 10,'L': 11,
        'M': 12,'N': 13,'O': 14,'P': 15,
        'Q': 16,'R': 17,'S': 18,'T': 19,
        'U': 20,'V': 21,'W': 22,'X': 23,
        'Y': 24,'Z': 25
    }
    alphabet="abcdefghijklmnopqrstuvwxyz"
    i=0
    for el in ["0","1","2","3","4","5","6","7","8","9","*","$","ç","!","?",";",",","."]:
        mot_cle=mot_cle.replace(el,alphabet[i])
        i+=1
        
    # Convertir le mot-clé en une clé numérique
    key_num = sum([correspondance[lettre.upper()] for lettre in mot_cle])

    # Encoder chaque lettre du texte
    texte_encode = ''
    for lettre in texte:
        if lettre.isalpha():
            # Convertir la lettre en un nombre
            lettre_num = correspondance[lettre.upper()]

            # Ajouter la clé numérique à la lettre
            lettre_encodee_num = (lettre_num + key_num) % 26

            # Convertir le nombre en lettre
            lettre_encodee = list(correspondance.keys())[list(correspondance.values()).index(lettre_encodee_num)]

            # Ajouter la lettre encodée au texte encodé
            texte_encode += lettre_encodee
        else:
            # Ajouter les caractères spéciaux tels quels au texte encodé
            texte_encode += lettre

    return texte_encode

class external_data:
	def synonyme_getter(mot,importation_manager):
		"""
		prend 2 variables:
			data:liste correspondant aux mots a installer
			importation_manager: modules s'occupant de l'importation de toutes les bibliotèques

		récupère sur le site autourdumot les synonymes du mot et renvoi une chaine de charactère avec les synonymes séparé par des points virgules
		"""
		html_text = importation_manager.requests.get("https://www.autourdumot.fr/champ-lexical/"+mot).text#recupère le code html du site
		soup = importation_manager.BeautifulSoup(html_text, 'html.parser')#converti au format "html.parser"
		
		synonyme=""
		for el_div in soup.find_all("div"):#crée une liste de chaque balise div avec son contenu
			if(el_div.find('class="col-12"') !=-1 and str(el_div).count("<li>")>0):#regarde si il y a la balise avec la classe col-12 est si la balise li est présente plus de n fois
				
				for el in str(el_div).split("\n"):
					
					if(el.find("<div")==-1 and el.find("<ul")==-1 and el.find("<li") !=-1):

						synonyme+=str(el).replace("<li>","").replace("</li>","")+";"#rajoute un synonyme trouvé
		synonyme2=";"
		i=0
		for el in synonyme.split(";"):
			if(synonyme2.find(el)==-1 and el.find("<a")==-1 and i<4):#enlève les éléments qui ne sont pas recherché
				synonyme2+=el+";"
				i+=1
		
		return synonyme2 # Renvoie tous les synonymes récoltés séparé par des points virgules, dans une variable de type chaine de charactère(string)
		
		
	def definition(data, importation_manager):
		"""
		prend 2 variables:
			data:liste correspondant aux mots a installer
			importation_manager: modules s'occupant de l'importation de toutes les bibliotèques
		"""
		take_of_parts=['class="ExempleDefinition">','class="ExempleDefinition">','class="numDef">','class="indicateurDefinition">',"<i>","</ul>","</article","</i>",':class="ExempleDefinition">',"</li>","</li",'=']
		for el in data:

			#print(el)
			html_text = importation_manager.requests.get("https://www.larousse.fr/dictionnaires/francais/"+el).text
			soup = importation_manager.BeautifulSoup(html_text, 'html.parser')
			def_data=""#variable contenant la definition
			type_data=""#variable contenant la classe gramatical d'un mot
			gender_data=""#variable contenant le genre d'un mot pour se qui sont genré
		
			
			for el_div in soup.find_all("article"):#liste de tous les éléments articles dans le code html du site récupéré avant

				if(str(el_div).find("DivisionDefinition") !=-1 ):#si l'élément contient comme nom de classe DivisionDefinition cela veut dire qu'elle contient le text d'une possibilité de définition donné par le dictionnaire

					#print("_____________________________")
					data=str(el_div)[str(el_div).find('<li class="DivisionDefinition">')+31:]#on recupère le text après la balise li de la classe portant le nom DivisionDefinition
					data=str(data).replace("<span","")
					data=data.replace("</span>","")
				
					
					data=data.split('<li class="DivisionDefinition">')
					i_data=0
					for el_def in data:
						
					
						if(len(el_def)>5 and i_data<4 and def_data==""):
							i_data+=1

							el_def=el_def.replace("\n","")
							el_def=el_def.replace("\r","")
							el_def=el_def.replace("  ","")
							el_def=el_def.replace("	","")
							el_def=el_def[el_def.find('class="numDef">')+15:]
							el_def=el_def[:el_def.find('class=')]#on enlève les impurtés
							def_data+=el_def+";"#on rajoute a une variable la definition s'éparé des autres propositions de définition par un point virgule
				if(str(el_div).find("CatgramDefinition") !=-1):
					
					data=(str(el_div).split('CatgramDefinition">')[1].split("</p>")[0])
					try:
						gender_data=data.split(" ")[1]
					except:
						gender_data="masculin"
					type_data=data.split(" ")[0]
			
			if(type_data=="nom" or type_data=="verbe" or type_data=="adjectif"):#limite l'implémentation dans le fichier words.txt des mots étant des noms, verbes, adjectif
				if(def_data !="" and type_data !="" and gender_data !=""):
					
					
					
					for take_part in take_of_parts:
						def_data=str(def_data).replace(take_part,"")#on enlève les impurtés
					
					synonyme=external_data.synonyme_getter(el,importation_manager)#on récupère aussi les synonymes du mot
					
					with open("words.txt","a")as fic:
						fic.write("{}\n".format((el+"="+str(def_data.replace("\n",""))+synonyme+"="+type_data+"="+gender_data).encode('utf-8')))
					
					return el+"="+str(def_data.replace("\n","").split(":")[0])+synonyme
			return ""
	def text_w_definition_manager(text,import_manager):
		"""
			prend 2 variables:
				text:chaine de charactère, d'une phrase
				import_manager
			s'occupe de renvoyer une chaine de charactère avec les mots plus leur defintion

		"""
		
		text=text.replace("e "," ")
		text=text.replace(" ","#")
		original_text=text
		word_alwready_known=""
		
		

		for line in open("words.txt","r",encoding="utf-8"):
			
			if(text.find(str(line[:line.find("=")])[2:])!=-1):
				if(len(str(line[:line.find("=")])[2:])>2):
					word_alwready_known+=line[:line.find("=")]
					
					text=text.replace("#"+str(line.split("=")[0])[2:]+"#","#"+line.split("=")[1]+"#")

		for word in original_text.split(" "):
			if(word_alwready_known.find(word)==-1):
				if(len(word)>2):
					
					
					definition=external_data.definition([word],import_manager)
					if(len(definition.split("="))>1):
						text=text.replace("#"+definition.split("=")[0]+"#","#"+definition.split("=")[0]+" "+definition.split("=")[1]+"#")
		
		return text

class Registry:
	def creat_account(email,password,importation_manager,path_user):
		"""
		prend 4 variables:
			email:chaine de charactère correspondant à l'address email du compte
			password:chaine de charactère correspondant au mot de pass du compte de l'utilisateur
			importation_manager:module avec toutes les importations et les bibliothèques externes
			path_user:chaine de charactère avec le chemin du fichier json contenant les comptes
		ajoute le compte au fichier serveur
		"""
		fichier=open(path_user,"r")
		data_base=importation_manager.json.load(fichier)
		fichier.close()
		if(email not in data_base.keys()):
			data_base[email]={"password":encoder_mot_cle(password,password[:2]),"connection_t_week":False,"email":True,"pseudo":email[:4]}
			f=open(path_user,"w")
			importation_manager.json.dump(data_base, f)
			f.close()
			return "Utilisateur ajouté"
		return "Pas de compte"

	def add(user,data,dictionnary_lang,importation_manager):
		"""
		prend 3 variables:
				user:chaine de charactère correspondant à un numéro de téléphone
				data:dictionnaire avec les informaions sur cette utilisateur doit contenir les clef suivantes "username","lastname","email","address","comment"
				dictionnary_lang:dictionnaire des phrases dans la langue adéquate associé a une clef specifique pour toutes les langues

		"""
		arguments=["username","lastname","email","address","comment"]
		for argument in arguments:
			if(str(data.keys()).find(argument)==-1):
				raise Exception("missing argument in dictionnary")
		f=open("data.json","r")
		data_base=importation_manager.json.load(f)
		f.close()
		f=open("data.json","w")
		print(data)
		data_base[user]=data
		importation_manager.json.dump(data_base, f)
		f.close()
		return dictionnary_lang["add_successfully"]
	def get_user_data(user,importation_manager):
		"""
		prend 2 variables:
			user:chaine de charactère correspondant au numero de telephone auquel il faut aller cherche les informations
			importation_manager:module en charge de toutes les importations
			renvoi un dictionnaire des informations de l'utilisateur cherché
		"""
		f=open("data.json","r")
		users_json=importation_manager.json.load(f)
		return users_json[user]

	def add_time_search_user(user,users_json,importation_manager):
		"""
		prend 2 variables user et users_json
		user:string correspondant a un numéro de telephone dans la base de donnée
		users_json: dictionnaire correspondant à la base de donnée de tous les numéros de télphone et leur données correspondant
		la fonction ajoute ensuite a la liste de tout les temps dans le dictionnaire de l'utilisateur, le temps acutel 
		renvoi ensuite le dictionnaire mise à jour
		"""
		actual_time =importation_manager.datetime.datetime.now()
		users_json[user]["time"].append(actual_time.hour)
		if(len(users_json[user]["time"])>9):
			del users_json[user]["time"][0]
		with open('data.json', 'w') as outfile:
			importation_manager.json.dump(users_json, outfile)
		return users_json
	def add_day_search_user(user,users_json,importation_manager):
		"""
		prend 2 variables user et users_json
		user:string correspondant a un numéro de telephone dans la base de donnée
		users_json: dictionnaire correspondant à la base de donnée de tous les numéros de télphone et leur données correspondant
		la fonction ajoute ensuite a la liste de tout les temps dans le dictionnaire de l'utilisateur, le temps acutel 
		renvoi ensuite le dictionnaire mise à jour
		"""
		actual_day = importation_manager.datetime.date.today().day
		users_json[user]["day"].append(actual_day)
		if(len(users_json[user]["day"])>9):
			del users_json[user]["day"][0]
		with open('data.json', 'w') as outfile:
			importation_manager.json.dump(users_json, outfile)
		return users_json
	def delete(user,dictionnary_lang,importation_manager):
		"""
		user:chaine de charactère d'un numéro de téléphone
		dictionnary_lang:dictionnaire des phrases dans la langue adéquate associé a une clef specifique pour toutes les langues
		importation_manager:modules, de toutes les bibliothèque disponible
		
		recrie la base de donnée sans l'utilisateur donné dans la variable user
		renvoi une chaine de characère d'une phrase informatif de si la modification à été possible dans la langue mit dans les paramètres
		"""
		try:
			f=open("data.json","r")
			data_base=importation_manager.json.load(f)
			f.close()
			del data_base[user]
			f=open("data.json","w")
			
			importation_manager.json.dump(data_base, f)
			f.close()
		except KeyError:
			return dictionnary_lang["KeyError"].format(user)
		
		return dictionnary_lang["change_information"]
		
