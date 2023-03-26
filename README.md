
##################################################################################################################################################################################################################################################################|RÉPERTOIRE TÉLÉPHONIQUE WEB|#########################################################################################
############################################################################################################################################################################################


  Le programme est un site web (HTML, CSS, JS) qui a la fonction d'un répertoire téléphonique. La partie serveur est gérée par un programme en Python (flask), et elle permet d'enregistrer les numéros, noms et informations des contacts enregistrés par les utilisateurs.

#######################################################################|CONTENU|############################################################################################################

	Lors de la première ouverture, le site demande de se connecter à un compte, ou bien d'en créer un. Cela permet d'éviter que n'importe qui puisse rajouter ou modifier des contacts de manière anonyme. L'utilisateur n'aura pas accès au site tant que le compte n'est pas créé ou que l'utilisateur n'est pas connecté. Le site fait usage du storage local pour enregistrer un token.

   Une fois connecté, le menu déroulant sur la gauche (bouton en haut à gauche) permet de sélectionner les multiples fonctionnalités du site web en appuyant sur des boutons:

- "Rechercher" : Le site web revient à la page d'accueil, affichant la liste entiere des contacts enregistrés dans le répertoire. La barre de recherche permet de rentrer un nom ou suite de mots, et l'algorithme de recherche essaiera de trouver des similitudes avec la liste de contacts de la base de données. Si l'algorithme ne trouve rien, il fera alors des suggestions.

- "Ajouter" : L'utilisateur peut rentrer les informations d'un contact telles que: Prénom, Nom, Courriel, Adresse Postale, Description, Numéro de téléphone. Lors de la validation, le serveur enregistrera le contact dans la base de données.

- "Modifier" : L'utilisateur rentre le numéro exact du contact qu'il souhaite modifier. Il selectionne ensuite dans le menu déroulant l'information du contact qu'il souhaite modifier. Si le changement est effectué, il y a confirmation, sinon il y a un message d'erreur.

- "Supprimer" : L'utilisateur rentre le numéro exact du contact qu'il souhaite supprimer. Si le numéro du contact existe bel et bien, le programme supprimera toutes les informations du contact de la base de données.

N.B. : La barre de recherche est tout le temps présente peu importe la fonction selectionnée par l'utilisateur. Si celui-ci décide de faire une recherche, il peut à tout moment utiliser la barre de recherche et cela le conduira directement à la page de recherche des résultats trouvés par l'algorithme de recherche.

#########################################################################|DÉMARRAGE|########################################################################################################


Pour démarrer le site web, il suffit de démarrer le fichier python "web.py". Le site web sera donc initialisé, et il sera disponible à l'adresse 127.0.0.1 au port 5000, ou plus facilement, "localhost:5000".

##########################################################################|CREDITS|#########################################################################################################

Diego FRAUEL CASTRO
Raphaël SCOTT 
(1ere NSI)
