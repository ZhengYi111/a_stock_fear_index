# 📈 A股恐慌指数（A-share Panic Index）

## 🧠 项目概述
**端到端AI驱动的金融数据管道**  
使用 Tushare API + Airflow + PostgreSQL + Streamlit 构建  
展示数据采集、清洗、调度、分析、AI总结与可视化的完整流程

---

## 🧩 项目简介
构建自动化A股市场"恐慌指数"分析系统，通过富途牛牛API获取实时数据，结合AI模型进行舆情与情绪分析，计算每日"市场恐慌指数"并可视化展示趋势。

### 🔍 核心目标
- 复现企业级Data Engineer + Data Scientist完整工作流
- 展示`数据采集 → 清洗 → 存储 → 调度 → AI总结 → 可视化`全链条能力

---

## 🧠 核心功能模块

| 模块 | 说明 |
|------|------|
| 📊 数据采集 | 使用Tushare API获取上证指数等市场行情数据 |
| 🧹 数据清洗 | Pandas清洗结构化数据，AI模型处理新闻/文本情绪 |
| 🗄️ 数据存储 | PostgreSQL数据库保存原始与清洗数据 |
| ⏰ 任务调度 | Airflow自动化运行ETL Pipeline（每日更新） |
| 🧮 恐慌指数计算 | 基于成交量、跌幅、舆情权重的自定义指标 |
| 🤖 AI总结 | LLM模型生成"今日恐慌原因总结" |
| 📈 可视化 | Streamlit仪表盘展示趋势图与AI报告 |

---

## 🏗️ 技术栈

| 技术 | 用途 | 优势 |
|------|------|------|
| Python 3.11 | 主开发语言 | 数据工程标准语言 |
| Tushare API | 数据源 | 提供合法实时A股行情 |
| PostgreSQL | 数据存储 | 支持复杂查询，工业标准 |
| Airflow | 调度 | 企业级任务编排框架 |
| Pandas/NumPy | 数据处理 | 高效清洗、特征计算 |
| OpenAI/Llama API | AI总结 | 自动生成市场情绪洞察 |
| Streamlit/Plotly | 可视化 | 快速构建交互式仪表盘 |
| Docker(可选) | 部署 | 一键启动的生产环境 |

---

## 🧱 项目结构
a_share_panic_index/

│

├── dags/                          # Airflow调度任务

│   ├── fetch_data_dag.py

│   ├── clean_store_dag.py

│   ├── panic_index_dag.py

│   └── summarize_report_dag.py

│

├── src/                           # 核心逻辑代码

│   ├── fetch/                     # 数据采集模块

│   ├── clean/                     # 数据清洗与AI处理

│   ├── compute/                   # 恐慌指数计算

│   ├── summarize/                 # AI总结模块

│   └── utils/                     # 数据库/配置工具

│

├── database/                      # 数据库配置

│   ├── init_db.sql                # 初始化表结构

│   └── db_config.yaml

│

├── webapp/                        # Streamlit前端

│   └── app.py

│

├── notebooks/                     # 实验笔记

├── tests/                         # 单元测试

├── requirements.txt

├── airflow_setup.sh

├── README.md

└── .env.example
复制
---

## 🧭 系统架构
mermaid

graph TD

A[Tushare API] --> B[数据采集]

B --> C[AI清洗]

C --> D[PostgreSQL]

D --> E[指数计算]

E --> F[AI总结]

F --> G[Streamlit可视化]

subgraph Airflow Pipeline

B --> C --> D --> E --> F

end
复制
---

## ⚙️ 环境配置

### 1️⃣ 创建环境
bash

conda create -n panic_index python=3.11 -y

conda activate panic_index

pip install -r requirements.txt
复制
### 2️⃣ 数据库配置
sql

CREATE DATABASE a_stock_fear_index;

CREATE USER panic_user WITH PASSWORD 'your_code';

GRANT ALL PRIVILEGES ON DATABASE a_stock_fear_index TO panic_user;
复制
### 3️⃣ 环境变量
复制`.env.example` → `.env`并填写：
ini

DB_HOST=localhost

DB_NAME=a_stock_fear_index

DB_USER=panic_user

Tushare_API_KEY=your_key

OPENAI_API_KEY=your_key
复制
---

## 🧩 项目路线图

| 阶段 | 内容 | 状态 |
|------|------|------|
| 阶段1 | 环境搭建与DB初始化 | ✅ 完成 |
| 阶段2 | Tushare API数据采集 | ✅ 完成 |
| 阶段3 | AI清洗+入库管道 | 🔄 进行中 |
| 阶段4 | Airflow调度整合 | ⏳ 待实现 |

---

## ✨ 作者
**Vive**  
🎯 Data Analyst → Data Engineer in progress  
📍 技术栈：Python · SQL · Airflow · AI Integration · Streamlit  
📍 Shanghai / Remote