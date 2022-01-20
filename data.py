import mysql.connector as msql

bdd = None
cursor = None

def connexion():
    global bdd
    global cursor

    bdd = msql.connect(user='hichem', password='hichem', host='localhost', port="8889", database='dons')
    cursor = bdd.cursor()

def deconnexion():
    global bdd
    global cursor

    cursor.close()
    bdd.close()

def get_users() : # récupère les informations de la table dans la BDD
    global cursor

    connexion()
    query = "SELECT * FROM utilisateur"
    cursor.execute(query)
    utilisateurs = []

    for enregistrement in cursor :
        utilisateur = {}
        utilisateur['id_Utilisateur'] = enregistrement[0]
        utilisateur['nom'] = enregistrement[1]
        utilisateur['prenom'] = enregistrement[2]
        utilisateur['adresse'] = enregistrement[3]
        utilisateur['email'] = enregistrement[4]
        utilisateur['somme'] = enregistrement[5]
        
        utilisateurs.append(utilisateur)

    print(utilisateurs)
    deconnexion()
    return utilisateurs
    
def somme():
    connexion()
    total=0
    query="SELECT * FROM utilisateur"
    cursor.execute(query)
    for enregistrement in cursor:
        total +=enregistrement[5]
    deconnexion()
    return (total)
    
def set_utilisateur(nom, prenom, adresse, email, somme): # récupère les infos et les inscrit dans la BDD
    global bdd
    global cursor

    connexion()

    query="INSERT INTO utilisateur(nom, prenom, adresse, email, somme) VALUES ('"+nom+"','"+prenom+"','"+adresse+"','"+email+"','"+somme+"');"
    cursor.execute(query)
    bdd.commit()

    deconnexion()


