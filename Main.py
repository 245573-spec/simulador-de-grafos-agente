from flask import Flask
from flask_cors import CORS
from Controller.Endpoint import ChatBot

# Inicializamos Flask como API pura (sin plantillas ni archivos estáticos)
main = Flask(__name__)

# Habilitamos CORS para que tu frontend en GitHub Pages pueda hacer peticiones
CORS(main, resources={r"/*": {"origins": "https://245573-spec.github.io"}})

# Cargamos las rutas/endpoints del agente
main.register_blueprint(ChatBot)

if __name__ == "__main__":
    main.run(debug=True)