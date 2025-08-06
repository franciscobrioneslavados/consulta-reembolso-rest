from flask import Flask
from config import Config
from models import db
from routes import bp as boleta_routes
from errors import register_error_handlers
import logging

# Setup Logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
register_error_handlers(app)
app.register_blueprint(boleta_routes)

def create_tables():
    db.create_all()
    logging.info("Tablas creadas o ya existentes")

if __name__ == '__main__':
    with app.app_context():
        try:
            db.create_all()
            logging.info("Tablas creadas o ya existentes")
        except Exception as e:
            logging.error(f"Error creando tablas: {e}")
    app.run(host='0.0.0.0', port=8080)