from flask import Flask, render_template, request, redirect, url_for
import db
from models import Noticia
import pandas as pd
import requests
from bs4 import BeautifulSoup


app = Flask(__name__)



@app.route("/")
def home():
    return render_template("index.html")

# Try new one:
website = "https://www.elperiodico.cat/ca/"
result = requests.get(website)
p1 = "h2"


coverpage = result.content
soup1 = BeautifulSoup(coverpage, "html.parser")
news = soup1.find_all(p1, attrs=None)
print(f"-> There are {len(news)} news titles in {website}")



# seleccionamos el filtro

pdict = {"class": "title fs2"}

coverpage_news = soup1.find_all(p1, attrs=pdict)
print(f"-> There are {len(coverpage_news)} news titles in {website}")

list_headlines = []
list_headlines_disc = []


for item in coverpage_news:
    aux = item.get_text(strip=True)
        # aux = aux.replace("\\", "")
    if len(aux.split()) > 1:
            list_headlines.append(aux)
    else:
            list_headlines_disc.append(aux)

for n, item in enumerate(list_headlines):
    print(f"{n} {item}")
for item in list_headlines_disc:
    print(item)





if __name__ == "__main__":
    # Esta linia arranca todo el sistema de mapeo
    #db.Base.metadata.create_all(db.engine)
    app.run(debug=True)