from flask import Flask , render_template

app = Flask(__name__)
@app.route('/')
def home ():
    mon_nom = 'Falou,badiane,badji'
    return render_template("Page_d'accueil.html", m=mon_nom)