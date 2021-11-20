import requests as requests
from flask import Flask, render_template, request, redirect, session, flash

from Classes import User
from Classes.Jogo import Jogo

app = Flask(__name__)

jogo1 = Jogo('Mega Man 10(2010)', 'https://media.rawg.io/media/screenshots/b87/b876d9664840d7e2f53cf5c649476935.jpg',
             '2')
jogo2 = Jogo('Valorant', 'https://media.rawg.io/media/games/b11/b11127b9ee3c3701bd15b9af3286d20e.jpg', '4')
jogo3 = Jogo('The Sims 4', 'https://media.rawg.io/media/games/e44/e445335e611b4ccf03af71fffcbd30a4.jpg', '10')
jogo4 = Jogo('ARK: Survival Evolved', 'https://media.rawg.io/media/games/58a/58ac7f6569259dcc0b60b921869b19fc.jpg',
             '10')
jogo5 = Jogo('Grand Theft Auto V', 'https://media.rawg.io/media/games/456/456dea5e1c7e3cd07060c14e96612001.jpg',
             '7')
jogo6 = Jogo('Sub Nautica', 'https://media.rawg.io/media/games/739/73990e3ec9f43a9e8ecafe207fa4f368.jpg', '4')
jogo7 = Jogo('Dystopian', 'https://media.rawg.io/media/games/6c0/6c00ee85d1344f58c469e8e47fd8ae7c.jpg', '10')
jogo8 = Jogo('Zombies', 'https://media.rawg.io/media/games/f6f/f6f39c5b56413f7f4513b25989a1b747.jpg',
             '10')
jogo9 = Jogo('Blood', 'https://media.rawg.io/media/screenshots/ca8/ca840f2a8ebfc74aac1688367dc1f903.jpg',
             'Jogo Sem Nota')
jogo10 = Jogo('Shooter', 'https://media.rawg.io/media/games/34b/34b1f1850a1c06fd971bc6ab3ac0ce0e.jpg', 'Jogo Sem Nota')
jogo11 = Jogo('darkness', 'https://media.rawg.io/media/screenshots/a68/a6841923b21d6cfe1197722a6b8a6eb1.jpg',
              'Jogo Sem Nota')
jogo12 = Jogo('Tactical', 'https://media.rawg.io/media/games/16b/16b1b7b36e2042d1128d5a3e852b3b2f.jpg', 'Jogo Sem Nota')

apikey = 'f3463a88067a455892363f8ead0bd700'
app.secret_key = 'secretKey'

url = f'https://api.rawg.io/api/games?key={apikey}'
requestapi = requests.get(url)

Listconcluido = [jogo1, jogo2, jogo3, jogo4]
Listjogando = [jogo5, jogo6, jogo7, jogo8]
Listfila = [jogo9, jogo10, jogo11, jogo12]
ListJogosIndex = []
Listteste = []


@app.route('/')
def hello_world():  # put application's code here
    return index()


@app.route('/index')
def index():  # put application's code here
    datajson = requestapi.json()['results']

    return render_template("index.html", datajson=datajson, concluido=Listconcluido, jogando=Listjogando,
                           fila=Listteste)


@app.route('/editar', methods=['POST', ])
def telaEditar():  # put application's code here
    name_jogo = request.form['nomeJogo']
    for jogo in Listconcluido:
        if (name_jogo == jogo.nomeJogo):
            return render_template("editar.html", jName=jogo.nomeJogo, jImg=jogo.imgJogo)

    for jogo in Listjogando:
        if (name_jogo == jogo.nomeJogo):
            return render_template("editar.html", jName=jogo.nomeJogo, jImg=jogo.imgJogo)

    for jogo in Listfila:
        if (name_jogo == jogo.nomeJogo):
            return render_template("editar.html", jName=jogo.nomeJogo, jImg=jogo.imgJogo)


@app.route('/editarJogo', methods=['POST', ])
def editarJogo():  # put application's code here
    name_jogo = request.form['nomeJogo']
    nota_jogo = request.form['notaJogo']
    for jogo in Listconcluido:
        if (name_jogo == jogo.nomeJogo):
            if not nota_jogo == 'Nota':
                jogo.notaJogo = nota_jogo
                flash('Editado com sucesso!')

    for jogo in Listjogando:
        if (name_jogo == jogo.nomeJogo):
            if not nota_jogo == 'Nota':
                jogo.notaJogo = nota_jogo
                flash('Editado com sucesso!')

    for jogo in Listfila:
        if (name_jogo == jogo.nomeJogo):
            if not nota_jogo == 'Nota':
                jogo.notaJogo = nota_jogo
                flash('Editado com sucesso!')

    return redirect('/index')


@app.route('/deletar/<string:name>')
def deletar(name):
    # for jogo in ListJogo:
    # if jogo.nomeJogo == name:
    # ListJogo.remove(jogo)
    return redirect('/index')


@app.route('/addJogo', methods=['POST', ])
def addJogo():
    name_jogo = request.form['nomeJogo']
    nota_jogo = request.form['notaJogo']
    search = f'&search={name_jogo}'
    url = f'https://api.rawg.io/api/games?key={apikey}{search}'
    requestapi = requests.get(url)
    data = requestapi.json()
    img_jogo = data['results'][0]['background_image']
    name_jogo = data['results'][0]['name']

    for jogo in Listconcluido:
        if (name_jogo != jogo.nomeJogo):
            jogo.notaJogo = 'Jogo Sem Nota'
            flash('Adicionado com sucesso!')
            jogoEncontrado = Jogo(name_jogo, img_jogo, nota_jogo)
            Listfila.append(jogoEncontrado)
            return redirect('/index')

    for jogo in Listjogando:
        if (name_jogo != jogo.nomeJogo):
            jogo.notaJogo = 'Jogo Sem Nota'
            flash('Adicionado com sucesso!')
            jogoEncontrado = Jogo(name_jogo, img_jogo, nota_jogo)
            Listfila.append(jogoEncontrado)
            return redirect('/index')

    for jogo in Listfila:
        if (name_jogo != jogo.nomeJogo):
            jogo.notaJogo = 'Jogo Sem Nota'
            flash('Adicionado com sucesso!')
            jogoEncontrado = Jogo(name_jogo, img_jogo, nota_jogo)
            Listfila.append(jogoEncontrado)
            return redirect('/index')

    return flash('Já possui esse jogo adicionado!')


@app.route('/teste', methods=['POST', ])
def teste():
    name_jogo = request.form['nomeJogo']
    nota_jogo = request.form['notaJogo']
    search = f'&search={name_jogo}'
    url = f'https://api.rawg.io/api/games?key={apikey}{search}'
    requestapi = requests.get(url)
    data = requestapi.json()
    img_jogo = data['results'][0]['background_image']
    name_jogo = data['results'][0]['name']

    for jogo in Listteste:
        if (name_jogo != jogo.nomeJogo):
            jogo.notaJogo = 'Jogo Sem Nota'
            flash('Adicionado com sucesso!')
            jogoEncontrado = Jogo(name_jogo, img_jogo, nota_jogo)
            Listteste.append(jogoEncontrado)
            return redirect('/index')

    return flash('nao foi')


if __name__ == '__main__':
    app.run()
