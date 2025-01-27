# AI股票分析师
[English Version](README.md)
基于LLM的股票分析顾问

## 信息分析师
使用LLM模型分析最新新闻。分析师会先将新闻分类为：
- 公司新闻
- 行业新闻
- 市场新闻
- 指标新闻
- 政策新闻
- 未知新闻

随后针对不同类型的新闻进行深入解读，再从股票主营介绍向量数据库中搜索与分析结果最相关的股票，并提供最终报告。

### 工作流程
![alt text](images/workflow.png)

## 特性
- [x] 多个LLM模型（GPT-4o/GPT-4o-mini/DeepSeek-V3/DeepSeek-R1）
- [x] 新闻分类
- [x] 新闻分析
- [x] 股票搜索
- [x] 报告生成