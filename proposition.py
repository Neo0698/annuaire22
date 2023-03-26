
class tendancy():
	def multiple_average(list_numbers):
		"""
		prend une variable list_numbers: list de nombre entier ou flottant
		est calcul les moyennes d'heures,des heures ayant un écart strictement plus petit que 3
		renvoi un list de nombre float, correspondant aux moyennes des tranches venant le plus dans la liste
		"""
		list_averages=[]

		for nb in list_numbers:
			index=-1
			for el in range(len(list_averages)):
				if((list_averages[el][0]/list_averages[el][1])>nb-3 and (list_averages[el][0]/list_averages[el][1])<nb+3):
					index=el
					
			if(index==-1):
				index=len(list_averages)
				list_averages.append([nb,1])
			else:
				
				list_averages[index][0]+=nb
				list_averages[index][1]+=1



		re_list_averages=[]
		for el in list_averages:
			
			re_list_averages.append(el[0]/el[1])
		
		return re_list_averages
	def get_time_adequacy(users_json,phone_number,time_hour):
		"""
		prend 3 variables:
				users_json:dictionnaire de tous les utilisateurs avec leur information
				phone_number:le numero de téléphone de l'utilisateur ayant une ressemblance de 100% avec la personne recherchait
				time_hour:entier comprenant l'heur actuel
		"""
		list_average=tendancy.multiple_average(users_json[phone_number]["time"])
		
		
		nb_exception=0#commence un compteur des nombres d'heures ayant 2h de plus de décalage avec la ou les moyenne(s)
		nb_in_range=0#commence un compteur des nombres d'heure n'ayant pas plus de 2h de décalage avec la moyenne(s)
		nb_same_time=0
		for el in users_json[phone_number]["time"]:
			if(el==time_hour):
				nb_same_time+=1
			in_average=False
			for average in list_average:
				if(el>average+2 or el<average-2):
					in_average=True

			if(in_average):
				nb_in_range+=1
			else:
				nb_exception+=1
		
		if(nb_in_range>nb_exception):
			re_dic={"type":"tandency","average":list_average,"nb_same_hour":nb_same_time}
		elif(nb_same_time>1):
			re_dic={"type":"start-tandency","average":list_average,"nb_same_hour":nb_same_time}
		else:
			re_dic={"type":"none","average":list_average,"nb_same_hour":nb_same_time}
		
		return re_dic
	def get_theme_adequacy(description,time_hour,current_day):
		job_theme_list=["travail","entreprise","chômage","emploi","colègue"]
		close_people_theme_list=["ami","copin","copain","famille"]
		job_theme=find_theme_in_string(description,job_theme_list)
		close_people=find_theme_in_string(description,close_people_theme_list)
		if(job_theme==True and close_people==False):
			if(current_day!=6 or current_day!=7):
				if(time_hour>8 and time_hour<18):
					return True

		if(job_theme==False and close_people==True):
			
			if(current_day==6 or current_day==7):
				return True
			elif(time_hour>=18):
				return True


		return False
	def get_day_tendancy(user_day,todays_day):
		"""
		prend 2 variables:
			user_day:liste d'entier, correspondant au numero du jour de la semaine indexé en 0
			todays_day:entier correspondat au numéro du jour actuel de la semaine aussi indexé en 0
		"""
		counter=0
		for day in user_day:
			if(day==todays_day):
				counter+=1
		return counter


	def name_charasteritics_average(name_characteristics,list_name):
		"""

		trouve qu'elle critère du nom ou prénom permet de le différencer des autres prénoms ayant des critères trop différents pour trouver les critère qui permet de regrouper le prénom avec d'autre similères
		et renvoi qu'elle critère permet de faire cela
		"""
		criteria=[("genre",),("age",),("genre","age")]
		criteria_average={"('genre',)":{"somme_max":0,"somme_min":0,"nb":0},"('age',)":{"somme_max":0,"somme_min":0,"nb":0},"('genre', 'age')":{"somme_max":0,"somme_min":0,"nb":0}}
		smallest_range=25
		smallest_range_text=()

		for criteria_list in criteria:
			min_=24
			max_=0
			
			for name in list_name["name_data"]:
				finder=True
				for el in criteria_list:

					if(list_name["name_data"][name][el]!=name_characteristics[el]):
						finder=False
				if(finder):

					for time_el in list_name["name_data"][name]["time"]:
						if(time_el<min_):
							min_=time_el
						elif(time_el>max_):
							max_=time_el
					criteria_average[str(criteria_list)]["somme_min"]+=min_
					criteria_average[str(criteria_list)]["somme_max"]+=max_
					
					criteria_average[str(criteria_list)]["nb"]+=1
		
		for el in criteria:
			if(criteria_average[str(el)]["nb"]>1):
				if((criteria_average[str(el)]["somme_max"]/criteria_average[str(el)]["nb"])-(criteria_average[str(el)]["somme_min"]/criteria_average[str(el)]["nb"])<smallest_range):
					smallest_range_text=el
		
		return smallest_range_text


	



def find_theme_in_string(data,theme_list):
	"""
		prend 2 variables:
		data:chaine de charactère
		theme_list:list de chaine de charactère que la fonction doit trouver dans data
		renvoi si une des chaines des charactères dans la liste theme_list est dans data
	"""
	for word in theme_list:
		if(data.find(word)!=-1):
			return True
	return False

def get_similarities(search,users_list):
	"""
	prend 2 variables:
		search:chaine de charactère comprenant la recherche de l'utilisateur
		users_list:dictionnaire comprenant des numéros de téléphones en cléf est un dictionnaire avec les informations du numéros de téléphone
	calcul grace à l'argument 'username' du dictionnaire de chaque numéro de téléphone si le prénom ou le numéro à une ressemblance strictement supèrieur à 55%
	renvoi une list de tuple contenant en index 0, le numero de téléphone et en index 1 la ressemblance de la valeur contenu dans la clef 'username' avec la recherche de l'utilisateur

	"""
	users_by_score=[]
	last_option_score=[]

	if(search.find(" ")!=-1):
		for el in list(users_list.keys()):
			
			if(((str(users_list[el]["username"])+" "+str(users_list[el]["lastname"])+" "+str(el))).lower().find(search)!=-1):
				
				users_by_score.append((el,1.1))
	
	else:
		for el in list(users_list.keys()):
			score=0
			last_score=0
			for letter in search.lower():

				if((str(users_list[el]["username"])).lower().count(str(letter))==search.count(letter)):
					score+=1
				if((str(users_list[el]["username"])).lower().find(str(letter))!=-1):

					last_score+=1
			if(len(search)>len(users_list[el]["username"])):
				biggest_word=len(search)
			else:
				biggest_word=len(users_list[el]["username"])
			min_score=0.55
			print(users_list[el]["username"])
			print(last_score/len(search))
			if(len(search)>4):
				min_score=0.8
			if(score/biggest_word>min_score):
				users_by_score.append((el,score/biggest_word))
			elif(last_score/len(search)>0.55):
				if(last_score/len(search)==1):
					users_by_score.append((el,score/biggest_word))
				last_option_score.append((el,score/biggest_word))


		for el in list(users_list.keys()):
			score=0

			for letter in search.lower():

				if((str(users_list[el]["lastname"])).lower().find(str(letter))!=-1 ):
					score+=1

			if(len(search)>len(users_list[el]["lastname"])):
				biggest_word=len(search)
			else:
				biggest_word=len(users_list[el]["lastname"])
			min_score=0.55
			if(len(search)>4):
				min_score=0.8
			if(score/biggest_word>min_score):
				users_by_score.append((el,score/biggest_word))



		for el in list(users_list.keys()):
			score=0

			for letter in search.lower().split(" "):

				if((str(users_list[el]["comment"])+str(el)).lower().find(str(letter))!=-1 ):

					score+=1


			if(score/len(search.split(" "))>0.8):
				users_by_score.append((el,score/len(search.split(" "))))
	if(users_by_score==[]):
		users_by_score=last_option_score
	users_by_score.sort()
	if(len(users_by_score)>3):
		users_by_score=users_by_score[:4]
	return users_by_score

def get_similarities_of_description(exemple_description,users_json,user_alwready_in):
	"""
	prend 3 variables:
			exemple_description: chaine de charactère, contenant les descriptions des utilisateur ou le numéro de téléphone ou le nom de l'utilisateur à une 
									ressemblance de 100%
			users_json:dictionnaire de tous les utilisateurs avec leur information
			user_alwready_in:liste de tuple(couplet) des utilisateur étant dans la partie des résultats
	"""

	user_w_score=[]
	not_useful=["de","la","le","des","en"]
	for user in list(users_json.keys()):
		if(str(user_alwready_in).find(user)==-1):
			i=0
			text=users_json[user]["comment_w_def"]
			for word in text.split(" "):
				if(len(word)>1):
					if(exemple_description.find(word)!=-1 and word not in not_useful):
						
						i+=1

			
			if(i/len(text.split(" "))>0.5):
				
				user_w_score.append((user,i/len(text.split(" "))))
	user_w_score.sort(reverse=True)
	user_w_score=user_w_score[:4]
	re_text=""
	for el in user_w_score:

		re_text+='<a href="tel:'+el[0]+'">'+el[0]+"</a>"+"\n"+users_json[el[0]]["username"]+"\n"+users_json[el[0]]["comment"]+"\n--------\n"
	
	return re_text




def get_search_users(user,importation_manager):
	"""
	prend une variable:
		user: chaine de charactère contenant soit un numéro de téléphone, soit un nom d'utilisateur
		dans un premier temp le programme établie tous les prénoms ayant une ressemblance de plus de 55% avec la variable user
		ensuite en fonction des habitudes d'appelle en fonction des heures, des jours, ou de la description la fonction classe les numéros
		ou l'utilisateur devrait être plus interressé.
	retourne une chaine de charactère avec les résultats de la recherche de l'utilisateur

	"""

	f=open("data.json")
	users_json=importation_manager.json.load(f)
	f.close()
	f=open("names.json","r")
	list_name=importation_manager.json.load(f)
	f.close()
	ressemblance_mineur=0
	user_with_finall_score=[]
	time_hour=importation_manager.datetime.datetime.now().hour
	current_day=importation_manager.datetime.date.today().day
	time_users_score={}
	users_activities_score={}
	exemple_description=""
	return_list=""
	
	#********fin de l'initialisation des variables****************



	data=(get_similarities(user,users_json))#cherche dans le fichier tous les numéros ou nom ou prénom ayant une similitude strictement superieur à 55%
	
	for el in data:
		
		if(el[1]==1):
			exemple_description+=users_json[el[0]]["comment_w_def"]
			users_json=importation_manager.database_com.Registry.add_day_search_user(el[0],users_json,importation_manager)
			users_json=importation_manager.database_com.Registry.add_time_search_user(el[0],users_json,importation_manager)#pour tous les utilisateurs dans la liste data si le prénom cherché à une ressemblance de 100% avec l'utilisateur recherché ajoute a la liste temps dans son dictionnair
	
	might_interest=get_similarities_of_description(exemple_description,users_json,data)
	
	for number in data:
		time_parameters=(tendancy.get_time_adequacy(users_json,number[0],time_hour))
		
		if(time_parameters["type"]=="none"):#si la valeur de la clef type de type_parameters est d'une chaine de charactère est égale à "none" alors le dictionnaire de la clef du numéro est égal à un tuple ou l'index 0 est égal a un score de 0.1 et ou l'index 1 est égal au nombre de fois ou l'utilisateur à était cherché à la même heure
			time_users_score[number[0]]=(0.1,time_parameters["nb_same_hour"])
		elif(time_parameters["type"]=="tandency"):#si la valeur de la clef type de type_parameters est d'une chaine de charactère est égale à "tandency" alors le dictionnaire de la clef du numéro est égal à un tuple ou l'index 0 est égal a un score de 0.3 et ou l'index 1 est égal au nombre de fois ou l'utilisateur à était cherché à la même heure
			time_users_score[number[0]]=(0.3,time_parameters["nb_same_hour"])
		elif(time_parameters["type"]=="start-tandency"):#si la valeur de la clef type de type_parameters est d'une chaine de charactère est égale à "start-tandency"(correspondant à plus d'une recherche fait à la même heure mais une moyenne ayant une difference avec l'heure actuel plus de 1) alors le dictionnaire time_user_score de la clef du numéro est égal à un tuple ou l'index 0 est égal a un score de 0.3 et ou l'index 1 est égal au nombre de fois ou l'utilisateur à était cherché à la même heure
			time_users_score[number[0]]=(0.2,time_parameters["nb_same_hour"])
		else:#sinon mêtre dans le dictionnaire time_users_score de la clef du numéro de l'utilisateur un tuple d'index 0, un score de 0.0 et d'index 1 le nombre fois 
			time_users_score[number[0]]=(0.0,time_parameters["nb_same_hour"])
	
	#*********calcul du score avec la ressemblance de critère entre prénom*******
	ref_user={}
	user_criteria=()
	criteria_name_similitude={}
	for number in data:
		
		if(number[1]==1):#si le username d'un numéro de la base de données à une ressemblance de 100% avec la recherche(calculer avec la fonction get_similarities)
			if(users_json[number[0]]["username"] in list_name["name_data"].keys()):
				
				
				ref_user=list_name["name_data"][users_json[number[0]]["username"]]
				user_criteria=tendancy.name_charasteritics_average(list_name["name_data"][users_json[number[0]]["username"]],list_name)#cherche qu'elle critère pour les utilisateurs ayant une ressemblance de 100% avec la recherche permet de les différencer de la masse tout en ayant une ressemble avec un nombre minime d'autre prénom 
	
	try:
		for number in data:
			if(str(list_name["name_data"].keys()).find(users_json[number[0]]["username"])!=-1):
				finder=True
				for el in user_criteria:
					
					if(list_name["name_data"][users_json[number[0]]["username"]][el]!=ref_user[el]):
						finder=False
				if(finder):#rajoute un score au prenom ayant les mêmes critères considérée comme diferenciateur pour classer les prénoms en fonction de si il représente au prénom cherché
					criteria_name_similitude[number[0]]=0.1
				else:
					criteria_name_similitude[number[0]]=0.0
			else:
				criteria_name_similitude[number[0]]=0.0
	except Exception as e:
		print(e)
		pass
			

	i=0

	#**********Calcul du score final*********
	

	for number in data:
		ressemblance_mineur=0
		if(tendancy.get_theme_adequacy(users_json[number[0]]["comment"],time_hour,current_day)):
			ressemblance_mineur+=0.1
		ressemblance_mineur+=tendancy.get_day_tendancy(users_json[number[0]]["day"],current_day)*0.1
		
		user_with_finall_score.append((data[i][1]+(1+time_users_score[number[0]][0]+(0.15*time_users_score[number[0]][1]))+ressemblance_mineur+criteria_name_similitude[number[0]],number[0]))
		
		i+=1
	user_with_finall_score.sort(key=lambda a:a[0],reverse=True)#classe dans un ordre decroissant les utilisateurs grâce à leur score
	
	#*******création de variable approprié pour renvoi******
	for el in user_with_finall_score:
		
		return_list+=users_json[el[1]]["username"]+" "+users_json[el[1]]["lastname"]+'<br><a href="tel:'+el[1]+'">'+el[1]+"</a><br>"+users_json[el[1]]["email"]+"<br><p>"+users_json[el[1]]["address"]+"<p>"+users_json[el[1]]["comment"]+"<p>--------<p>"

	return return_list,might_interest
