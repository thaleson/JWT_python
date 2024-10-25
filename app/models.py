from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    role = db.Column(db.String(20), nullable=False)  # SUPERUSER ou USER

    def __repr__(self):
        return f'<User {self.username}>'

# Cria as tabelas no banco de dados
db.create_all()
