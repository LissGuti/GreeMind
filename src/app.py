from flask import Flask, render_template, request, redirect
import sqlite3
import os

#Aqui esta la ruta correcta 
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))


app = Flask(__name__,
    template_folder=os.path.join(BASE_DIR, 'templates'),
    static_folder=os.path.join(BASE_DIR, 'static'))

DB_PATH = os.path.join(BASE_DIR, 'db', 'usuarios.db')

# Renderizamos el login
@app.route('/', methods=['GET', 'POST'])
def Login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Conectar a la base de datos
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        # Buscar usuario con email y password
        cursor.execute('SELECT * FROM usuarios WHERE email=? AND password=?', (email, password))
        usuario = cursor.fetchone()
        conn.close()

        if usuario:
            return f"<h1> Login exitoso. ¡Bienvenido, {email}!</h1>"
        else:
            return "<h2> Credenciales incorrectas</h2>"
    return render_template('index.html')

# Redirigimos al apartado de recuperacion de cuenta
@app.route('/recover')
def Recuperar():
    return render_template('recover-account.html')

# Redirigimos al apartado de si se le olvido la contraseña
@app.route('/forgot')
def Olvide():
    return render_template('forgot-password.html')

@app.route('/pas')
def Pasaste():
    return render_template('menu.html')

if __name__ == '__main__':
    app.run(debug=True)