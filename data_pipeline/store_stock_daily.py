#重点A股最近一年日线数据入数据库
import sys
import os
import pandas as pd
from pathlib import Path
import psycopg2#PostgreSQL 数据库适配器
from psycopg2.extras import execute_values 
from dotenv import load_dotenv
from datetime import datetime
from utils.config_loader import load_env # 加载环境变量
from utils.logger import get_logger # 日志记录

#获取数据
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from data_pipeline.fetch_daily_data import fetch_daily_data


# 加载环境变量
load_dotenv()

# 初始化日志
config = load_env()
logger = get_logger(__name__, config["LOG_PATH"])#自动获取当前模块的名称，创建一个与当前模块关联的日志记录器

# 获取数据库配置
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")


def store_stock_daily(df, table_name="ods_stock_daily"):
    """将DataFrame写入PostgreSQL的ODS层"""
    conn = psycopg2.connect(
        dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD,
        host=DB_HOST, port=DB_PORT
    )

    current_date = datetime.now().strftime("%Y%m%d")

    try:
        cur = conn.cursor()   # 创建游标

        records = [tuple(x) for x in df.to_numpy()]

        insert_query = f"""
            INSERT INTO {table_name} (
                ts_code, trade_date, open, high, low, close, pre_close,
                change, pct_chg, vol, amount
            ) VALUES %s
            ON CONFLICT (ts_code, trade_date)
            DO NOTHING
        """

        execute_values(cur, insert_query, records)

        conn.commit()   # 提交事务
        cur.close()  # 关闭游标
        conn.close()
        print(f"✅ {current_date}成功写入 {len(df)} 条记录到表 {table_name}")
    
    except Exception as e:
        logger.error(f"{current_date}数据入库失败: {e}")
        print(f"❌ {current_date}数据入库失败: {e}")


if __name__ == "__main__":
    df = fetch_daily_data()
    
    if df is not None:
        store_stock_daily(df)  
    else:
        print("❌ 未能获取到数据，无法执行存储操作")