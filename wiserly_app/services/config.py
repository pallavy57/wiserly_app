import os
import multiprocessing

PORT = int(os.getenv("PORT", 5000))
DEBUG_MODE = int(os.getenv("DEBUG_MODE", 0))

# Gunicorn config
bind = ":" + str(PORT)
workers = multiprocessing.cpu_count() * 2 + 1
threads = 2 * multiprocessing.cpu_count()


class DefaultConfig(object):
    PROJECT = "Wiserly Count for Shopify"
    DB_SCHEMA = "inventory_planner"
    PROJECT_ROOT = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    DEBUG = True
    TESTING = False
    SECRET_KEY = os.getenv("SECRET_KEY", "super-random-key")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    SHOPIFY_API_KEY = os.getenv("SHOPIFY_API_KEY")
    SHOPIFY_SHARED_SECRET = os.getenv("SHOPIFY_SHARED_SECRET")
    SHOPIFY_API_VERSION = os.getenv("SHOPIFY_API_VERSION")
    HOSTNAME = os.getenv("HOSTNAME_FOR_SHOPIFY", None)
    # WEBHOOK_TEST_MODE = os.getenv("WEBHOOK_TEST_MODE", False) is (True)


class TestingConfig(object):
    PROJECT = "Wiserly Count for Shopify"
    DB_SCHEMA = "testing_inventory_planner"
    PROJECT_ROOT = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    DEBUG = True
    TESTING = True
    SECRET_KEY = os.getenv("SECRET_KEY", "super-random-key")
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://wiserly_test:123456@test-db/wiserlydb_test"
    SHOPIFY_API_KEY = os.getenv("SHOPIFY_API_KEY")
    SHOPIFY_SHARED_SECRET = os.getenv("SHOPIFY_SHARED_SECRET")#change this
    SHOPIFY_API_VERSION = os.getenv("SHOPIFY_API_VERSION")
    HOSTNAME = os.getenv("HOSTNAME_FOR_SHOPIFY", None) #change this
    # WEBHOOK_TEST_MODE = os.getenv("WEBHOOK_TEST_MODE", False) is (True)#change this


