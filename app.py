from flask import Flask, render_template

app = Flask(__name__)
# Renderizamos el login
@app.route('/')
def Login():
    return render_template('index.html')

# Redirigimos al apartado de recuperacion de cuenta
@app.route('/recover')
def Recuperar():
    return render_template('recover-account.html')

# Redirigimos al apartado de si se le olvido la contraseña
@app.route('/forgot')
def Olvide():
    return render_template('forgot-password.html')

if __name__ == '__main__':
    app.run(debug=True)