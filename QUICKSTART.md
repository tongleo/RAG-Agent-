# 快速启动（QUICKSTART）

本快速启动提供两条可复制的路线：

A) 本地原型（推荐） — LangChain + Chroma + sentence-transformers

1. 克隆仓库并进入 starter 目录：

   git clone https://github.com/tongleo/RAG-Agent-.git
   cd RAG-Agent-/starter

2. 复制环境文件并安装依赖：

   cp .env.template .env
   python -m venv .venv && source .venv/bin/activate
   pip install -r requirements.txt

   在 .env 中填写 OPENAI_API_KEY（可选）。如果没有 OpenAI Key，demo 仍会展示检索到的文档片段。

3. 运行 demo：

   python demo.py

   该 demo 会：
   - 读取 starter/data 里的文本文件
   - 通过 sentence-transformers 生成 embeddings，写入 Chroma（默认持久化到 starter/chroma_db）
   - 用简单检索找到 top-k 文档并（如果配置了 OPENAI_API_KEY）将检索结果拼到 prompt 里调用 OpenAI 生成回答


B) 生产化参考（Haystack + Milvus） — 高级/部署路径

- 生产化通常会把向量存储换成 Milvus/Weaviate，并通过容器化部署检索服务与模型服务。这里给出参考：
  - Milvus 官方：https://github.com/milvus-io/milvus
  - Haystack 官方：https://github.com/deepset-ai/haystack

- 推荐在生产环境使用 docker-compose / Kubernetes + 负载均衡与监控。


更多细节请参见 starter/README.md（包含逐步运行说明与可扩展建议）。
