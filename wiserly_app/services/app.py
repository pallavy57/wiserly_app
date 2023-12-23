from sqlalchemy.sql import text
import os
from flask import Flask
from flask import jsonify
from flask_cors import CORS
import logging
from flask_migrate import Migrate
from wiserly_app.services.shopify_bp import shopify_bp
from wiserly_app.services.config import DefaultConfig, TestingConfig
from flask import request, jsonify
from wiserly_app.services.extensions import db

logging.basicConfig(
    format="%(asctime)s %(levelname)s %(name)s:%(lineno)d %(threadName)s : %(message)s")

log_level = {
    'DEBUG': logging.DEBUG,
    'WARNING': logging.WARNING,
    'INFO': logging.INFO,
    'ERROR': logging.ERROR
}

logging.getLogger('werkzeug').setLevel(log_level[os.getenv('LOG_LEVEL',                                                        'ERROR')])
log = logging.getLogger('werkzeug')

db_schema = None
app = Flask(__name__, instance_relative_config=False)

# print(DefaultConfig)

if os.environ["FLASK_ENV"] == "prod":
    app.config.from_object(DefaultConfig)

else:
    app.config.from_object(TestingConfig)

CORS(app)
# Blueprints
app.register_blueprint(shopify_bp)


# Liveness probe


@app.route('/health')
def health():
    return jsonify({"status": 200, "message": "It's alive!"})


# Database
with app.app_context():
    db.init_app(app)
    Migrate(app, db)
    # db.session.execute(text("CREATE SCHEMA IF NOT EXISTS inventory_planner"))
    db.session.commit()
    # db.create_all()


if __name__ == "__main__":
    app.run(use_reloader=True, debug=True)
