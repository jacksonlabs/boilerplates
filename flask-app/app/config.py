from os import environ as env
import multiprocessing

ADDRESS = env.get("ADDRESS", "0.0.0.0")
PORT = int(env.get("PORT", 5000))
DEBUG_MODE = int(env.get("DEBUG_MODE", 0))

# Gunicorn config
bind = "{}:{}".format(ADDRESS, PORT)
workers = multiprocessing.cpu_count() * 2 + 1
threads = 2 * multiprocessing.cpu_count()
