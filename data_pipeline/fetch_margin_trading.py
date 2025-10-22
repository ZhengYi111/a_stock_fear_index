import tushare as ts
import pandas as pd
from pathlib import Path
from utils.config_loader import load_env
from utils.logger import get_logger

config = load_env()
logger = get_logger(__name__, config["LOG_PATH"])

ts.set_token(config["TUSHARE_TOKEN"])
pro = ts.pro_api()

def fetch_margin_trading(start_date="20240101", end_date="20260101"):
    """
    获取融资融券汇总数据
    """
    try:
        Path("data/raw").mkdir(parents=True, exist_ok=True)
        df = pro.margin(start_date=start_date, end_date=end_date)
        path = "data/raw/margin_trading.csv"
        df.to_csv(path, index=False)
        logger.info(f"融资融券数据保存成功，共 {len(df)} 行。")
        print(f"✅ 融资融券数据保存成功，共 {len(df)} 行。")
        return df
    except Exception as e:
        logger.error(f"获取融资融券数据失败: {e}")
        print(f"❌ 获取融资融券数据失败: {e}")

if __name__ == "__main__":
    fetch_margin_trading()
