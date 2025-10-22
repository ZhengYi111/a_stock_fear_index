"""
恐慌指数计算核心成分股清单
使用字典列表格式，便于前端展示和数据管理
"""

# 重点A股清单 - 恐慌指数计算核心成分
IMPORTANT_STOCKS = [
    # ==================== 金融板块 ====================
    {"ts_code": "601318.SH", "name": "中国平安", "sector": "保险", "weight": 0.15, "description": "保险龙头，金融板块风向标"},
    {"ts_code": "600036.SH", "name": "招商银行", "sector": "银行", "weight": 0.12, "description": "银行股代表，机构重仓股"},
    {"ts_code": "601166.SH", "name": "兴业银行", "sector": "银行", "weight": 0.08, "description": "股份制银行重要代表"},
    {"ts_code": "600030.SH", "name": "中信证券", "sector": "证券", "weight": 0.10, "description": "券商龙头，市场情绪放大器"},
    {"ts_code": "000001.SZ", "name": "平安银行", "sector": "银行", "weight": 0.05, "description": "零售银行代表"},
    
    # ==================== 消费板块 ====================
    {"ts_code": "600519.SH", "name": "贵州茅台", "sector": "白酒", "weight": 0.15, "description": "A股股王，价值投资标杆"},
    {"ts_code": "000858.SZ", "name": "五粮液", "sector": "白酒", "weight": 0.08, "description": "白酒第二龙头，消费情绪指标"},
    {"ts_code": "601888.SH", "name": "中国中免", "sector": "旅游零售", "weight": 0.07, "description": "免税龙头，消费复苏晴雨表"},
    {"ts_code": "000333.SZ", "name": "美的集团", "sector": "家电", "weight": 0.06, "description": "家电龙头，内需代表"},
    {"ts_code": "603288.SH", "name": "海天味业", "sector": "食品饮料", "weight": 0.04, "description": "调味品龙头，必需消费品"},
    
    # ==================== 科技成长板块 ====================
    {"ts_code": "300750.SZ", "name": "宁德时代", "sector": "新能源", "weight": 0.12, "description": "新能源绝对龙头，成长股旗帜"},
    {"ts_code": "002594.SZ", "name": "比亚迪", "sector": "新能源", "weight": 0.09, "description": "新能源汽车龙头，技术领先"},
    {"ts_code": "002475.SZ", "name": "立讯精密", "sector": "消费电子", "weight": 0.06, "description": "消费电子龙头，科技制造代表"},
    {"ts_code": "603986.SH", "name": "兆易创新", "sector": "半导体", "weight": 0.05, "description": "芯片设计龙头，科技自主可控"},
    {"ts_code": "688981.SH", "name": "中芯国际", "sector": "半导体", "weight": 0.05, "description": "半导体制造龙头，科技战略标的"},
    
    # ==================== 资源周期板块 ====================
    {"ts_code": "601857.SH", "name": "中国石油", "sector": "能源", "weight": 0.08, "description": "能源战略，通胀预期指标"},
    {"ts_code": "601088.SH", "name": "中国神华", "sector": "煤炭", "weight": 0.06, "description": "煤炭龙头，周期股代表"},
    {"ts_code": "600019.SH", "name": "宝钢股份", "sector": "钢铁", "weight": 0.04, "description": "钢铁龙头，工业需求指标"},
    {"ts_code": "600309.SH", "name": "万华化学", "sector": "化工", "weight": 0.05, "description": "化工龙头，制造业需求"},
    
    # ==================== 医药健康板块 ====================
    {"ts_code": "600276.SH", "name": "恒瑞医药", "sector": "医药", "weight": 0.08, "description": "创新药龙头，医药板块标杆"},
    {"ts_code": "300759.SZ", "name": "康龙化成", "sector": "医药研发", "weight": 0.04, "description": "CXO龙头，医药研发情绪指标"},
    {"ts_code": "300015.SZ", "name": "爱尔眼科", "sector": "医疗服务", "weight": 0.04, "description": "医疗服务龙头，成长性代表"},
    
    # ==================== 其他重要股票 ====================
    {"ts_code": "601012.SH", "name": "隆基绿能", "sector": "光伏", "weight": 0.05, "description": "光伏龙头，新能源代表"},
    {"ts_code": "600900.SH", "name": "长江电力", "sector": "电力", "weight": 0.04, "description": "水电龙头，防御性资产"},
]