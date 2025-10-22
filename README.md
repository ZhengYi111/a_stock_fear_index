📈 A股恐慌指数（A-share Panic Index）

🧠 一个端到端（End-to-End）的 AI 驱动金融数据管道项目
使用 Tushare API + Airflow + PostgreSQL + Streamlit 构建
—— 展示数据采集、清洗、调度、分析、AI总结与可视化的完整流程

🧩 项目简介

本项目旨在构建一个 自动化的A股市场“恐慌指数”分析系统，
通过富途牛牛 API 获取实时市场数据，结合 AI 模型进行舆情与情绪分析，
最终计算每日“市场恐慌指数”，并在可视化界面中展示趋势与总结。

🔍 目标：复现企业级 Data Engineer + Data Scientist 的完整工作流
🪶 展示数据采集 → 清洗 → 存储 → 调度 → AI总结 → 可视化 全链条能力

🧠 核心功能
模块	说明
📊 数据采集	使用 Tushare API 获取上证指数等市场行情数据
🧹 数据清洗	Pandas 清洗结构化数据，AI 模型处理新闻/文本情绪
🗄️ 数据存储	PostgreSQL 数据库保存原始与清洗数据
⏰ 任务调度	Airflow 自动化运行 ETL Pipeline（每日更新）
🧮 恐慌指数计算	基于成交量、跌幅、舆情权重的自定义指标
🤖 AI总结	LLM 模型生成 “今日恐慌原因总结”
📈 可视化	Streamlit 仪表盘展示趋势图与AI总结报告


🏗️ 技术栈
技术	用途	理由
Python 3.11	主语言	数据工程标准语言
Tushare API	数据源	提供合法实时A股行情
PostgreSQL	数据存储	支持复杂查询，工业标准
Airflow	调度	企业级任务编排框架
Pandas / NumPy	数据处理	高效清洗、特征计算
OpenAI / Llama API	AI总结	自动生成市场情绪洞察
Streamlit / Plotly	可视化	快速构建交互式仪表盘
Docker（可选）	部署	实现一键启动的生产环境


🧱 项目结构
a_share_panic_index/
│
├── dags/                          # Airflow DAGs 调度任务
│   ├── fetch_data_dag.py
│   ├── clean_store_dag.py
│   ├── panic_index_dag.py
│   └── summarize_report_dag.py
│
├── src/                           # 核心逻辑代码
│   ├── fetch/                     # 数据采集模块（Tushare API）
│   │   └── Tushare_api_fetcher.py
│   ├── clean/                     # 数据清洗与AI处理
│   │   └── ai_cleaner.py
│   ├── compute/                   # 恐慌指数计算
│   │   └── panic_index_calculator.py
│   ├── summarize/                 # AI总结模块
│   │   └── reason_summarizer.py
│   └── utils/                     # 数据库/配置工具
│       └── db_utils.py
│
├── database/
│   ├── init_db.sql                # 初始化数据库表结构
│   └── db_config.yaml
│
├── webapp/                        # Streamlit 可视化前端
│   └── app.py
│
├── notebooks/                     # 实验笔记与探索
│   └── feature_exploration.ipynb
│
├── tests/                         # 单元测试
│
├── requirements.txt
├── airflow_setup.sh
├── README.md
└── .env.example


🧭 系统架构图
graph TD
A[Tushare API 数据源] --> B[数据采集 fetch_data_dag]
B --> C[AI清洗 clean_store_dag]
C --> D[PostgreSQL 数据库]
D --> E[计算 panic_index_dag]
E --> F[AI总结 summarize_report_dag]
F --> G[Streamlit 可视化 Dashboard]
subgraph Airflow Pipeline
B --> C --> D --> E --> F
end


⚙️ 环境配置与运行方法

1️⃣ 创建环境
conda create -n panic_index python=3.11 -y
conda activate panic_index
pip install -r requirements.txt

2️⃣ 配置数据库

在 PostgreSQL 中创建数据库：

CREATE DATABASE a_stock_fear_index;
CREATE USER panic_user WITH PASSWORD 'your_code';
GRANT ALL PRIVILEGES ON DATABASE a_stock_fear_index TO panic_user;


执行初始化 SQL：

psql -U panic_user -d a_stock_fear_index -f database/init_db.sql

3️⃣ 配置环境变量

复制 .env.example → .env 并填写：

DB_HOST=localhost
DB_NAME=a_stock_fear_index
DB_USER=panic_user
DB_PASS=your_code
Tushare_API_KEY=your_Tushare_api_key
OPENAI_API_KEY=your_openai_key

4️⃣ 启动 Airflow 调度
export AIRFLOW_HOME=$(pwd)/airflow
airflow db init
airflow users create --username admin --password admin --role Admin --firstname Data --lastname Engineer --email you@example.com
airflow webserver -p 8080
airflow scheduler

5️⃣ 运行数据采集脚本（单独测试）
python src/fetch/Tushare_api_fetcher.py

6️⃣ 启动 Streamlit 前端
streamlit run webapp/app.py

🧩 项目路线图（Roadmap）
阶段	内容	状态
阶段1	环境搭建与DB初始化	✅ 完成
阶段2	Tushare API 数据采集	✅ 完成
阶段3	AI清洗 + 入库管道	🔄 进行中
阶段4	Airflow 调度整合	⏳ 待实现
阶段5	恐慌指数计算逻辑	⏳ 待实现
阶段6	AI总结模块	⏳ 待实现
阶段7	Streamlit 可视化	⏳ 待实现
阶段8	Docker 部署 & README完善	⏳ 待实现


 ✨ 作者

Vive

🎯Data Analyst → Data Engineer in progress
📍 技术标签：Python · SQL · Airflow · AI Integration · Streamlit
📍 Shanghai / Remote
