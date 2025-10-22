import logging
import os

def get_logger(name, log_path="./logs/app.log"):
    os.makedirs(os.path.dirname(log_path), exist_ok=True) #提取目录路径
    logging.basicConfig(
        filename=log_path,
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    return logging.getLogger(name)
