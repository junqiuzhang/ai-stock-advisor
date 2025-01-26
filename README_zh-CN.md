# ai-stock-advisor
[English Version](README.md)
基于LLM的股票分析顾问

## 信息分析员
使用LLM模型分析最新新闻。分析员会先将新闻分类为：
- 公司新闻
- 行业新闻
- 市场新闻
- 指标新闻
- 政策新闻
- 未知新闻

随后针对不同类型的新闻进行深入解读，再从股票主营介绍向量数据库中搜索与分析结果最相关的股票，并提供最终报告。

### 工作流程
![alt text](images/workflow.png)