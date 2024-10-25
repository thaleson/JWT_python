from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Defina uma chave secreta para as sessões

# Simulando um "banco de dados" simples com um dicionário
users = {}

# Página principal
@app.route('/')
def index():
    return render_template('index.html')

# Página de Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Verifica se o usuário existe e se a senha está correta
        if username in users and users[username] == password:
            session['username'] = username  # Armazena o usuário na sessão
            flash("✅ Login feito com sucesso, {}! Você agora tem acesso à nossa plataforma.".format(username), "success")
            return redirect(url_for('user_page', username=username))
        else:
            flash("⚠️ Credenciais inválidas. Por favor, verifique seu nome de usuário e senha e tente novamente.", "error")
            return redirect(url_for('login'))
    return render_template('login.html')

# Página de Registro
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Verifica se o usuário já existe
        if username in users:
            flash("⚠️ O nome de usuário '{}' já está registrado. Por favor, escolha outro.".format(username), "error")
            return redirect(url_for('register'))
        else:
            # Registra o novo usuário
            users[username] = password
            flash("✅ Registrado com sucesso! Agora faça login.", "success")
            return redirect(url_for('login'))
    return render_template('register.html')

# Página de Logout
@app.route('/logout')
def logout():
    session.pop('username', None)  # Remove o usuário da sessão
    flash("✅ Você saiu da plataforma com sucesso.", "success")
    return redirect(url_for('index'))

# Página do usuário comum
@app.route('/user/<username>')
def user_page(username):
    if 'username' not in session or session['username'] != username:
        flash("⚠️ Você precisa fazer login para acessar esta página.", "error")
        return redirect(url_for('login'))
    return render_template('user.html', username=username)

if __name__ == '__main__':
    app.run(debug=True)
