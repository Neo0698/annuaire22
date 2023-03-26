import json  

def encoder_mot_cle(texte, mot_cle):
    # Dictionnaire de correspondance entre les lettres et les chiffres
    correspondance = {
        'A': 0,
        'B': 1,
        'C': 2,
        'D': 3,
        'E': 4,
        'F': 5,
        'G': 6,
        'H': 7,
        'I': 8,
        'J': 9,
        'K': 10,
        'L': 11,
        'M': 12,
        'N': 13,
        'O': 14,
        'P': 15,
        'Q': 16,
        'R': 17,
        'S': 18,
        'T': 19,
        'U': 20,
        'V': 21,
        'W': 22,
        'X': 23,
        'Y': 24,
        'Z': 25
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


def decoder_mot_cle(texte_encode, mot_cle):

    # Dictionnaire de correspondance entre les lettres et les chiffres

    correspondance = {

        'A': 0,

        'B': 1,

        'C': 2,

        'D': 3,

        'E': 4,

        'F': 5,

        'G': 6,

        'H': 7,

        'I': 8,

        'J': 9,

        'K': 10,

        'L': 11,

        'M': 12,

        'N': 13,

        'O': 14,

        'P': 15,

        'Q': 16,

        'R': 17,

        'S': 18,

        'T': 19,

        'U': 20,

        'V': 21,

        'W': 22,

        'X': 23,

        'Y': 24,

        'Z': 25

    }

    alphabet="abcdefghijklmnopqrstuvwxyz"

    i=0

    for el in ["0","1","2","3","4","5","6","7","8","9","*","$","ç","!","?",";",",","."]:

        mot_cle=mot_cle.replace(el,alphabet[i])

        i+=1

    # Convertir le mot-clé en une clé numérique

    key_num = sum([correspondance[lettre.upper()] for lettre in mot_cle])



    # Décoder chaque caractère du texte encodé

    texte_decode = ''

    for caractere in texte_encode:

        if caractere.isalpha():

            # Convertir la lettre encodée en un nombre

            lettre_encodee_num = correspondance[caractere.upper()]



            # Soustraire la clé numérique à la lettre encodée

            lettre_decodee_num = (lettre_encodee_num - key_num) % 26



            # Convertir le nombre en lettre

            lettre_decodee = list(correspondance.keys())[list(correspondance.values()).index(lettre_decodee_num)]



            # Ajouter la lettre décodée au texte décodé

            texte_decode += lettre_decodee

        else:

            # Ajouter les caractères spéciaux tels quels au texte décodé

            texte_decode += caractere



    return texte_decode





class command_interpreter():



    def search(query,dictionnary_lang,importation_manager):



        """



        prend 3 variables:



            query:liste des commandes de l'utilisateur



            dictionnary_lang: dictionnaire contentant les phrases a écrire dans la langue de l'utilisateur



            importation_manager: module comprenant toutes les bibliotèques disponibles







            fait les modifications nécessaires aux variables et appelle les fonctions adequates pour renvoyer une



            chaine de charactère avec le résultat de la recherche







        """



        accent=[("é","e"),("è","e"),("à","a"),("ë","e"),("ê","e")]



        if(len(query)==1):



            user=""



            while(len(user)==0):#permet d'enlever les enters trop long pour selection le choix dans le module graphic qui pourrait être interpetré comme un enter pour l'input



                user=input("user:")



            query.append(user)



        for element in accent:



            query[1]=query[1].replace(element[0],element[1])



       



        data,might_interest=importation_manager.proposition.get_search_users(query[1].replace("_"," "),importation_manager)



        data=data.replace("<p>","\n")







        return data+"\n"+dictionnary_lang["might_interest"]+"\n"+might_interest



    def change(query,dictionnary_lang,importation_manager):



        """



        prend



            une variable query: liste de la commande de l'utilisateur



            dictionnary_lang: dictionnaire comprenant tous les textes dans la langue



            importation_manager: module comprenant toutes les bibliotèques disponibles











            retourne une erreur ou si il y a était possible de changer l'argument d'un utilisateur



        """



        



        if(len(query)==1):



            phone=""



            while(len(phone)==0):



                phone=input("phone number:")



            query.append(phone)



        



        if(len(query)<3):



            importation_manager.interface.show_manager(dictionnary_lang["changement_info"],importation_manager)



            query.append(input("argument:"))



        



        if(len(query)<4):







            query.append(input("nouvelle info:"))







        



        argument_changed=""



        for argument in ["username","lastname","email","address","comment"]:



            if(query[2]==argument):



                argument_changed=argument



       



        if(argument_changed!=""):



           



            try:







                user_data=importation_manager.database_com.Registry.get_user_data(query[1],importation_manager)



            except:



                return dictionnary_lang["KeyError"]



            user_data[argument_changed]=query[3]



            print(user_data)



            importation_manager.database_com.Registry.add(query[1],user_data,dictionnary_lang,importation_manager)



            



            return dictionnary_lang["change_information"].format(query[1])



        print("return")



        return ""



    def add(query,importation_manager,dictionnary_lang):



        """



        prend 3 variables:



            query:liste comprenant la commande de l'utilisateur



            dictionnary_lang: dictionnaire comprenant tous les textes dans la langue



            importation_manager: module comprenant toutes les bibliotèques disponibles



        renvoi une chaine de charactère de si l'action est réussite dans la langue paramètrée











        """



        



      
        
        username=query[2].replace("_"," ");print(query)



        lastname=query[3].replace("_"," ")



        email=query[4].replace("_","")



        address=query[5].replace("_"," ")



        description=query[6].replace("_"," ");print(address);print(description)



        



        description_w_def=importation_manager.database_com.external_data.text_w_definition_manager(description,importation_manager)



        importation_manager.database_com.Registry.add(query[1],{"username":username,"lastname":lastname,"email":email,



            "address":address,"comment":description,



            "comment_w_def":description_w_def,"time":[],"day":[]},dictionnary_lang,importation_manager)



        



        return dictionnary_lang["add_successfully"]



    def delete(query,dictionnary_lang,importation_manager):



        """



        prend 2 variables:



                query:liste des commandes de l'utilisateur



                dictionnary_lang:dictionnaire des messages à afficher dans la bonne langue







        """



        if(len(query)==1):



           



            user=""



            while(len(user)==0):



                user=input("user:")



            query.append(user)



        return importation_manager.database_com.Registry.delete(query[1],dictionnary_lang,importation_manager)



        











        















def command(query,dictionnary_instruction,dictionnary_lang,settings,importation_manager,token):



    """



    prend en charge 4 variables:



    query:chaine de charactère contenant les données rentrées données par l'utilisateur



    dictionnary_instruction:dictionnaire contenant les differentes commandes possible dans la langue de l'utilisateur



    dictionnary_lang:dictionnaire contenant les differents textes à afficher dans la langue de l'utilisateur



    importation_manager: module comprenant toutes les bibliotèques disponibles



    la fonction s'occupe de voir qu'elle fonctionnalité à été demander par l'utilisateur et d'appeler la fonction en charge



    renvoi le texte renvoyer par les fonction demandé par l'utilisateur







    """



    accent=[("é","e"),("è","e"),("à","a"),("ë","e"),("ê","e")]



    query=query.split(" ")



    print(query[0])



    if(query[0]==dictionnary_instruction["change"] or query[0]=="2"):



        return command_interpreter.change(query,dictionnary_lang,importation_manager)



        



            







            



    if(query[0]==dictionnary_instruction["add"] or query[0]=="1"):



        return command_interpreter.add(query,importation_manager,dictionnary_lang)







    elif(query[0]==dictionnary_instruction["search"] or query[0]=="0"):



        return command_interpreter.search(query,dictionnary_lang,importation_manager)



    elif(query[0]==dictionnary_instruction["exit"]  or query[0]=="4"):



        return "stop" #retourne stop pour que le programme qui à appelez la fonction agisse en conséquence



    elif(query[0]==dictionnary_instruction["delete"] or query[0]=="3"):



        return command_interpreter.delete(query,dictionnary_lang,importation_manager)



    elif(query[0]==dictionnary_instruction["settings"] or query[0]=="5"):



        if(len(query)==4):



            lang_=query[1]



            option_=query[2]



            mode_=query[3]  



        else:



            lang_=""



            option_=""



            mode_=""







        importation_manager.settings.create_settings(importation_manager,settings=settings,lang=lang_,mode=mode_,option=option_)



        settings=importation_manager.settings.main(importation_manager)



        return "stop"



    

    elif(query[0]=="6"):

        file_=open("user.json","r")

        data_user=json.load(file_)

        try:
            print(data_user[query[1]]["password"])
            print(encoder_mot_cle(query[2],query[2][:2]))

            if(data_user[query[1]]["password"]==encoder_mot_cle(query[2],query[2][:2])):

                return '{"message":"bienvenue","token":"'+str(token)+'"}'

            else:

                return '{"message":"mot de passe incorrect","token":""}'

        except Exception as e:
            print(e)

            return '{"message":"nom d\'utilisateur incorrect","token":""}'

    

    elif(query[0]=="7"):

        importation_manager.database_com.Registry.creat_account(query[1],query[2],importation_manager,"user.json")
        return '{"message":"bienvenue","token":"'+str(token)+'"}'

    elif(query[0]=="8"):
        f=open("data.json")
        users_json=importation_manager.json.load(f)
        f.close()
        re_text=""
        for key,value in users_json.items():
            re_text+=value["username"]+" "+value["lastname"]+'<br><a href="tel:'+key+'">'+key+"</a><br>"+value["email"]+"<br><p>"+value["address"]+"<p>"+value["comment"]+"<p>--------<p>"
        return re_text
    else:



        return dictionnary_lang["no_command"].format(query[0])



