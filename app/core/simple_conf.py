# Security projects configure
# => Make sure added conf.py in .gitignore file
HOST= '0.0.0.0'
PORT= 8888

class ConfigDB:
    SECRET_KEY = 'your_secret_key'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///sqlite.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

GOFTINO_BASE_URL = "https://api.goftino.com/v1"
GOFTINO_API_KEY = "YOUR_API_KEY"

OPEN_AI_BASE_URL = "https://api.openai.com/v1"
OPEN_AI_API_KEY = "YOUR_API_KEY"