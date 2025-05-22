from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/primeiro')
def primeiro():
    return render_template('primeiro.html') 

@app.route('/segundo')
def segundo():
    return render_template('segundo.html') 

@app.route('/terceiro')
def terceiro():
    return render_template('terceiro.html')

@app.route('/quarto')
def quarto():
    return render_template('quarto.html') 

@app.route('/recebedados', methods=['POST'])
def recebedados():
    nome = request.form['nome']
    email = request.form['email']
        #nome = request.args['nome']
        #email = request.args["email"]
		#nome = request.args.get("nome")
    return "{} e {}".format(nome,email)

if __name__ == '__main__':
    app.run(debug=True)
