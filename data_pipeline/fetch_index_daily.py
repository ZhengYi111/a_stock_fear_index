#从 Tushare 获取重点A股最近一年日线数据并存储为 CSV 文件
import tushare as ts
import pandas as pd
from pathlib import Path
from datetime import datetime,timedelta
from utils.config_loader import load_env # 加载环境变量
from utils.logger import get_logger # 日志记录
from .stock_universe import IMPORTANT_STOCKS #重点A股清单


config = load_env() #从 .env文件读取 TUSHARE_TOKEN和 LOG_PATH
logger = get_logger(__name__, config["LOG_PATH"])#自动获取当前模块的名称，创建一个与当前模块关联的日志记录器

ts.set_token(config["TUSHARE_TOKEN"])
pro = ts.pro_api()#创建一个 Tushare 的 API 对象


def fetch_daily_data(ts_codes=None):
    """
    从Tushare获取A股日线数据
    """

    end_date = datetime.now().strftime("%Y%m%d")
    start_date = (datetime.now() - timedelta(days=365)).strftime("%Y%m%d")

    # 确定要获取的股票代码列表
    if ts_codes is None:
        # 从IMPORTANT_STOCKS中提取所有股票代码
        ts_codes = [stock["ts_code"] for stock in IMPORTANT_STOCKS]
    elif isinstance(ts_codes, str):
        ts_codes = [ts_codes]
    
    # 创建数据存储目录
    Path("data/raw").mkdir(parents=True, exist_ok=True)
    
    all_data = []  # 存储所有获取的数据
    
    for idx, ts_code in enumerate(ts_codes, 1):
        try:

            logger.info(f"正在获取 {ts_code} 数据 ({idx}/{len(ts_codes)})...")
            print(f"🔄 正在获取 {ts_code} 数据 ({idx}/{len(ts_codes)})...")
            
            df = pro.daily(ts_code=ts_code, start_date=start_date, end_date=end_date)
            
            if df.empty:
                logger.warning(f"{ts_code} 未获取到数据")
                print(f"⚠️  {ts_code} 未获取到数据")
                continue
            
            all_data.append(df)
            
            logger.info(f"{ts_code} 数据保存成功，共 {len(df)} 行。")
            print(f"✅ {ts_code} 数据保存成功，共 {len(df)} 行。")
            
        except Exception as e:
            logger.error(f"获取 {ts_code} 数据失败: {e}")
            print(f"❌ 获取 {ts_code} 数据失败: {e}")
    
    # 合并所有数据
    if all_data:
        combined_df = pd.concat(all_data, ignore_index=True)
        
        # 保存合并后的数据
        combined_path = f"data/raw/all_stocks_daily_{end_date}.csv"
        combined_df.to_csv(combined_path, index=False, encoding='utf-8-sig')
        
        logger.info(f"所有股票数据已合并保存，共 {len(combined_df)} 行。")
        print(f"🎉 所有股票数据已合并保存，共 {len(combined_df)} 行。")
        
        return combined_df
    else:
        logger.warning("未获取到任何数据")
        return None


if __name__ == "__main__":
    # 获取所有重要A股数据
    fetch_daily_data()
