⚙️ 二、研发设计文档（RDD）		
		
项目名称：A股恐慌指数系统		
版本：v1.0		
作者：Yi Zheng		
目标读者：技术团队 / 面试官		
		
		
		
1. 系统架构总览		
		
                      ┌──────────────────────┐		
                      │        Airflow        │		
                      │  fetch → clean → NLP  │		
                      │  → calc → store → vis │		
                      └──────────────────────┘		
                                   │		
                                   ▼		
      ┌─────────────────────────────────────────────┐		
      │                 Data Pipeline               │		
      │ 1. fetch_data.py  | 调 Tushare、爬舆情网站 │		
      │ 2. clean_data.py  | 数据清洗 & 格式化      │		
      │ 3. store_data.py  | 入 PostgreSQL           │		
      └─────────────────────────────────────────────┘		
                                   │		
                                   ▼		
               ┌──────────────────────────────┐		
               │     PostgreSQL 数据库         │		
               │ raw_data / clean_data / fear_index / news_sentiment │		
               └──────────────────────────────┘		
                                   │		
                                   ▼		
               ┌──────────────────────────────┐		
               │ NLP 模块（DeepSeek API）     │		
               │ 舆情分析 + 情绪量化 + 关键字抽取 │		
               └──────────────────────────────┘		
                                   │		
                                   ▼		
               ┌──────────────────────────────┐		
               │ Streamlit Dashboard          │		
               │ 左表格 + 搜索 + 折线 + AI总结 │		
               └──────────────────────────────┘		
		
		
		
2. 模块设计		
		
(1) 数据采集模块		
		
文件路径：data_pipeline/fetch_data.py		
		
来源	技术	数据类型
Tushare	API	A股每日行情数据（open, close, high, low, volume）;北向资金每日流入流出数据；
新闻网站：东方财富网	requests + BeautifulSoup	财经新闻标题、正文、发布时间
		
		
(2) 数据清洗模块（ETL任务）		
		
文件路径：data_pipeline/clean_data.py		
		
执行方式：由 Airflow DAG 定时执行		
		
去除重复行、空值；		
		
统一日期格式；		
		
检测并修正价格异常；		
		
使用停用词表清洗舆情文本；		
		
提取情感关键词（为后续NLP分析准备）。		
		
		
		
(3) 舆情分析模块（NLP）		
		
文件路径：analysis/nlp_sentiment.py		
		
功能：		
		
传入清洗后的舆情文本；		
		
调用 DeepSeek API，返回：		
		
情绪倾向（正向 / 负向 / 中性）		
		
恐慌关键词列表		
		
恐慌度评分（0–1）		
		
输出存入数据库表 news_sentiment。		
		
		
		
(4) 恐慌指数计算模块		
		
文件路径：analysis/calculate_fear_index.py		
		
计算逻辑示例：		
		
fear_index = (		
    normalized_volatility * 0.5 +      # 波动率因子 (权重50%)		
    sentiment_score * 0.3 +            # 情绪因子 (权重30%)  		
    abnormal_volume_ratio * 0.2        # 成交量异常因子 (权重20%)		
) * 100		
		
1. normalized_volatility（标准化波动率，权重50%）​​		
		
数据来源​：Tushare Pro API的日线行情数据		
金融意义​：波动率是衡量市场恐慌的核心指标。价格波动越大，市场不确定性越高。		
		
2. sentiment_score（情绪得分，权重30%）​​		
		
数据来源​：网络爬虫获取的舆情数据 + NLP情感分析		
		
3. abnormal_volume_ratio（异常成交量比率，权重20%）​​		
		
数据来源​：Tushare成交量数据 + 历史统计		
金融意义​：异常高成交量通常伴随恐慌性抛售或抄底行为，是情绪极端化的信号。		
		
		
		
(5) 可视化模块		
		
文件路径：dashboard/app.py		
		
框架：Streamlit		
		
左侧表格：pandas DataFrame 显示（名称、代码、板块、价格、恐慌指数）		
		
搜索框：输入股票代码过滤数据		
		
折线图：st.line_chart 显示历史恐慌指数		
		
AI总结：从 ai_summary 表读取最新生成内容		
		
		
		
3. 数据库设计		
		
表名	说明	
raw_stock_data	从 Tushare 抓取的原始行情	
clean_stock_data	清洗后的行情数据	
news_sentiment	舆情情绪数据（来自DeepSeek分析）	
fear_index	综合计算后的恐慌指数	
ai_summary	DeepSeek生成的市场恐慌文字总结	
		
		
4. 技术栈说明		
		
模块	技术	理由
调度系统	Airflow	可视化任务编排、容错
数据采集	requests + aiohttp + Tushare	异步爬取 & 官方API
清洗处理	pandas + numpy	高效ETL
数据库	PostgreSQL	结构化管理
NLP		
	DeepSeek API	舆情理解
Web框架	Streamlit	快速交互展示
日志监控	logging + Airflow UI	任务可追踪性
环境	conda + .env	环境隔离与安全性
		
		
5. Airflow DAG 任务流（核心）		
		
# airflow_dags/fear_index_pipeline.py		
task_fetch = PythonOperator(task_id='fetch_data', python_callable=fetch_all_data)		
task_clean = PythonOperator(task_id='clean_data', python_callable=clean_data)		
task_nlp = PythonOperator(task_id='nlp_sentiment', python_callable=analyze_sentiment)		
task_calc = PythonOperator(task_id='calculate_fear_index', python_callable=calculate_fear_index)		
task_store = PythonOperator(task_id='store_to_db', python_callable=store_data)		
task_vis = PythonOperator(task_id='generate_ai_summary', python_callable=generate_ai_summary)		
		
task_fetch >> task_clean >> task_nlp >> task_calc >> task_store >> task_vis		
		
		
		
6. 日志与错误处理		
		
所有任务写入统一日志 utils/logger.py		
		
任务失败时 Airflow 自动重试 1 次		
		
每日任务状态邮件通知（Airflow内置）		
		
		
		
7. 项目结构		
		
a_stock_fear_index/		
├── airflow_dags/		
│   └── fear_index_pipeline.py		
├── data_pipeline/		
│   ├── fetch_data.py		
│   ├── clean_data.py		
│   └── store_data.py		
├── analysis/		
│   ├── calculate_fear_index.py		
│   ├── nlp_sentiment.py		
│   └── ai_summary.py		
├── dashboard/		
│   └── app.py		
├── db/		
│   ├── schema.sql		
│   └── config.py		
├── utils/		
│   ├── logger.py		
│   └── config_loader.py		
├── requirements.txt		
├── docker-compose.yml		
└── README.md		
		
		
		
8. 未来扩展		
		
增加板块级恐慌指数聚合；		
		
接入港股、美股；		
		
加入时间序列预测模型（Prophet或LSTM）；		
		
部署至云端（AWS Lambda + RDS + Streamlit Cloud）。		