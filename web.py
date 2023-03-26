from flask import Flask, render_template, request
import json
import __main__
import random

token=random.randint(0,99999999999999)
import importation_manager# import le module importation manager qui se charge d'importer les modules disponibles sur l'ordinateur

settings={'lang': 'fr_FR', 'fonction': 'server', 'mode': 'smart'}
dictionnary_lang={"menu":"Bienvenue tapez .... pour faire ...","no_command":"Désolé, il n'y a aucune command pour {} \n voici les commandes qui existes \n cherche \n quitter() \n changer \n ajoute","add_successfully":"Ajout réussi.","change_information":"Changement réussi.","might_interest":"Cela pourrait vous intéresser...","KeyError":"Il n'existe aucun utilisateur {}","add_error_command":"La fonction ajoute doit être appellé de la manière suivante: ajoute <numéro de téléphone>","input_importation":"Voulez vous installer le(s) {} module(s)\n pour bénificier de toutes les fonctionalités \n répondre avec y(pour oui) ou n(pour non):","changement_info":'parmi les instructions suivantes, laquelle voulez-vous changer ?\n"nom dutilisateur","nom","email","adresse","commentaire"'}

dictionnary_instruction={"add":"ajoute","search":"cherche","exit":"quitter()","change":"changer","delete":"supprime","all_instuction":["cherche","changer","ajoute","supprime","paramètres"],"settings":"paramètres"}

importation_dictionnary=importation_manager.creat_importation_list()#recupère la liste des librairies qui peuvent être importé


app = Flask(__name__)

@app.route('/')
def index():
 return render_template('main.html')

@app.route('/post-data', methods=['POST'])
def post_data():
    # Code to handle POST request
    data = json.loads(request.data)
   
    re_data=importation_manager.command.command(data["data"],dictionnary_instruction,dictionnary_lang,settings,importation_manager,token)
    re_data=re_data.replace("\n","<br>")
    
    re_data=re_data.replace("<br><br>","<br>")
    re_data=re_data.replace("<p></p>","")
    return re_data.replace("%20"," ")

app.run(debug=False,host="0.0.0.0", port=911)
