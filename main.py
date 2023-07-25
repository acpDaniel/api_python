from flask import Flask
from module import module_bp

app = Flask(__name__)

# Registrar os blueprints dos recursos
app.register_blueprint(module_bp, url_prefix="/api")

if __name__ == "__main__":
    app.run(debug=True)
