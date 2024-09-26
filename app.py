from flask import Flask, session, send_from_directory
from datetime import timedelta
from dotenv import load_dotenv
from werkzeug.middleware.proxy_fix import ProxyFix  # Importando ProxyFix
import os


# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

from mod_site.mod_site import bp_home
#from mod_admin.admin import bp_admin


app = Flask(__name__)

# Carregar chave secreta do arquivo .env
app.secret_key = os.getenv("SECRET_KEY", os.urandom(12).hex())

# Adicionar o ProxyFix para garantir que o Flask lide corretamente com o proxy reverso
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_port=1, x_prefix=1)


# Registro dos Blueprints
app.register_blueprint(bp_home)
#app.register_blueprint(bp_admin)


@app.before_request
def before_request():
    session.permanent = True

    # Carregar tempo de sessão do arquivo .env (padrão para 30 minutos se não estiver definido)
    session_lifetime = int(os.getenv("SESSION_LIFETIME", "30").split()[0])
    session['tempo'] = session_lifetime
    app.permanent_session_lifetime = timedelta(minutes=session_lifetime)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
