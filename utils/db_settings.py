import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    TUSHARE_TOKEN = os.getenv("TUSHARE_TOKEN")
    LOG_PATH = os.getenv("LOG_PATH")
    
    # 数据库配置
    DB_NAME = os.getenv("DB_NAME")
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_PORT = os.getenv("DB_PORT", "5432")
    