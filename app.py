from decouple import config as env_config
from flask import Flask
from views import terms_bp

SECRET_KEY = "secret_that_is_no_secret"


app = Flask(__name__)

app.secret_key = SECRET_KEY

app.register_blueprint(terms_bp)





if __name__=='__main__':
    app.run(port= 5000, debug=True)
