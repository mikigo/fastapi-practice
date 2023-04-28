from os import popen
from os.path import abspath
from os.path import dirname
from os.path import join

# ==================== PROJECT SETTING ====================
# Debug 模式开启
DEBUG = True
# 应用名称
APP_NAME = "FeelGood"
# 应用版本
VERSION = "0.1"
# 根目录绝对路径
ROOT_DIR = dirname(abspath(__file__))
# router目录绝对路径
ROUTER_PATH = join(ROOT_DIR, "router")
# static目录绝对路径
STATIC_PATH = join(ROOT_DIR, "static")


# ======================= DB SETTING =======================
SQLITE_FILE_NAME = "feelgood.db"
SQLITE_URL = f"sqlite:///{STATIC_PATH}/{SQLITE_FILE_NAME}"

# ====================== HOST SETTING ======================
# Debug模式开启说明是在开发环境，使用127.0.0.1，Debug模式关闭正式环境，使用真实IP
IP = popen("hostname -I").read().split(" ")[0] if not DEBUG else "127.0.0.1"
# 端口
PORT = 8000
# 热重载
RELOAD = True
