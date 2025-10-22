import tushare as ts
import pandas as pd
from pathlib import Path
from utils.config_loader import load_env
from utils.logger import get_logger

config = load_env()
logger = get_logger(__name__, config["LOG_PATH"])

ts.set_token(config["TUSHARE_TOKEN"])
pro = ts.pro_api()

def fetch_north_moneyflow(start_date="20240101", end_date="20260101"):
    """
    获取北向资金每日流入流出数据
    """
    try:
        Path("data/raw").mkdir(parents=True, exist_ok=True)
        df = pro.moneyflow_hsgt(start_date=start_date, end_date=end_date)
        df["north_money"] = df["north_money"].astype(float)
        path = "data/raw/north_moneyflow.csv"
        df.to_csv(path, index=False)
        logger.info(f"北向资金数据保存成功，共 {len(df)} 行。路径：{path}")
        print(f"✅ 北向资金数据保存成功，共 {len(df)} 行。")
        return df
    except Exception as e:
        logger.error(f"获取北向资金数据失败: {e}")
        print(f"❌ 获取北向资金数据失败: {e}")

if __name__ == "__main__":
    fetch_north_moneyflow()
