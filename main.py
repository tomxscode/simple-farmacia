from flask import Flask

app = Flask(__name__)
app.secret_key = 'secret'

# Rutas
from routes.admin import admin_bp

app.register_blueprint(admin_bp)

if __name__ == '__main__':
    app.run(debug=True)