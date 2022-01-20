from flask import Flask, render_template, request

import data

app = Flask(__name__)

@app.route('/')
def index() :
    return render_template('Association LES ENFANTS DU COEUR.html')

@app.route('/Formulaire')
def formulaire():
    return render_template('Formulaire.html')

@app.route('/add', methods=['GET'])
def add():
    nom = request.values.get('nom')
    prenom = request.values.get('prenom')
    adresse =request.values.get('adresse')
    email =request.values.get('email')
    somme =request.values.get('somme')
    
    data.set_utilisateur(nom, prenom, adresse, email, somme)

    datas = data.get_users()
    
    total = data.somme()
    
    return render_template('add.html', utilisateurs = datas, total= total)

if __name__== "__main__" :
    app.run(debug=True, port=5001)
