from dotenv import load_dotenv
import os
from pathlib import Path

def load_env():
    """加载环境变量"""
    # 获取项目根目录路径（utils目录的上一级）
    project_root = Path(__file__).parent.parent
    env_path = project_root / '.env'
    
    # 加载指定路径的.env文件
    load_dotenv(env_path)
    
    config = {
        "TUSHARE_TOKEN": os.getenv("TUSHARE_TOKEN"),
        "LOG_PATH": os.getenv("LOG_PATH", "./logs/app.log"),
        "DB_HOST":os.getenv("DB_HOST"),
        "DB_PORT":os.getenv("DB_PORT"),
        "DB_NAME":os.getenv("DB_NAME"),
        "DB_USER":os.getenv("DB_USER"),
        "DB_PASSWORD":os.getenv("DB_PASSWORD")
    }
    return config