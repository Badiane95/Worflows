import random
from flask import Flask, render_template, request, redirect
import json, os

DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data.json")
SENTIMENTS = ["positif", "negatif", "neutre"]

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
@app.route('/sentiment/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        with open(DATA_DIR, 'r') as f:
            messages = json.load(f)
        
        # Récupérer le message utilisateur
        message = request.form["message"]
        messages.append({"role": "user", "content": message})
        
        # Simuler l'analyse de sentiment
        sentiment = random.choice(SENTIMENTS)
        messages.append({"role": "assistant", "content": sentiment})
        
        with open(DATA_DIR, 'w') as f:
            json.dump(messages, f)  
        return redirect('/sentiment/')
        
    else:    
        with open(DATA_DIR, 'r') as f:
            messages = json.load(f)
    return render_template(
    "index.html", messages=messages)
    