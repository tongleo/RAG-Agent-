# RAG（检索增强生成）与 Agent 推荐仓库清单

本清单面向想学习或构建 RAG/Agent 系统的开发者，按功能分类、给出简短说明、语言偏好和快速 clone 命令。

---

## 核心 RAG 框架与示例
- LangChain — 通用链/工具/Agent 框架，广泛用于把检索、提示工程和工具调用串起来。标签：RAG、Agent、Python/JS  
  https://github.com/langchain-ai/langchain  
  git clone https://github.com/langchain-ai/langchain.git

- LlamaIndex (原 GPT-Index) — 专注于文档索引与检索层，便于把大量文档转为可检索的上下文。标签：RAG、索引、Python  
  https://github.com/jerryjliu/llama_index  
  git clone https://github.com/jerryjliu/llama_index.git

- Haystack (deepset) — 面向生产的问答与 RAG 管道，支持多种检索器与部署选项。标签：RAG、生产、Python  
  https://github.com/deepset-ai/haystack  
  git clone https://github.com/deepset-ai/haystack.git

- OpenAI Cookbook — 官方示例集合，包含多个 RAG/检索示例（notebooks & scripts）。标签：示例、教学  
  https://github.com/openai/openai-cookbook  
  git clone https://github.com/openai/openai-cookbook.git

---

## Agent / Agentic orchestration（代理与编排）
- LangChain Agents（在 LangChain 仓库内） — 支持工具调用、Planner/Executor 等模式。标签：Agent、工具调用

- Microsoft AutoGen — 多 agent 协作与任务编排工具，适合复杂 agent 网络与并发场景。标签：Agent、协作  
  https://github.com/microsoft/autogen  
  git clone https://github.com/microsoft/autogen.git

- Auto-GPT — 社区示例，展示了自动化长任务和闭环 agent 的实现思路（学习/原型参考）。标签：Agent、自动化、Python  
  https://github.com/significant-gravitas/auto-gpt  
  git clone https://github.com/significant-gravitas/auto-gpt.git

- BabyAGI — 简化的 agent 流水线示例，适合入门理解 task-generation / execution / memory 循环。标签：Agent、教学  
  https://github.com/yoheinakajima/BabyAGI  
  git clone https://github.com/yoheinakajima/BabyAGI.git

---

## 向量存储 / 检索底座（RAG 常配套）
- Chroma — 轻量、本地优先的向量 DB，适合快速原型。标签：向量 DB、Python  
  https://github.com/chroma-core/chromadb  
  git clone https://github.com/chroma-core/chromadb.git

- Milvus — 企业级向量数据库，适合大规模部署与多节点扩展。标签：向量 DB、生产级  
  https://github.com/milvus-io/milvus  
  git clone https://github.com/milvus-io/milvus.git

- Weaviate — 带 semantic search 的向量 DB，支持插件与 GraphQL。标签：向量 DB、语义检索  
  https://github.com/semi-technologies/weaviate  
  git clone https://github.com/semi-technologies/weaviate.git

- FAISS — 高性能相似搜索库（ANN）由 Facebook 提供，研究与高性能部署常用。标签：ANN、库级、C++/Python  
  https://github.com/facebookresearch/faiss  
  git clone https://github.com/facebookresearch/faiss.git

- sentence-transformers — 高质量文本 embedding 库，常用于生成向量表示。标签：Embeddings、Python  
  https://github.com/UKPLab/sentence-transformers  
  git clone https://github.com/UKPLab/sentence-transformers.git

---

## 实用/整合/SDK
- semantic-kernel（Microsoft） — 支持技能/插件和 agent 式交互的 SDK，多语言支持。标签：Agent、SDK  
  https://github.com/microsoft/semantic-kernel  
  git clone https://github.com/microsoft/semantic-kernel.git

---

## 按用途的快速推荐
- 学习/入门：LangChain、LlamaIndex、OpenAI Cookbook、BabyAGI、Auto-GPT  
- 快速原型：Chroma + sentence-transformers + LangChain（或 LlamaIndex）  
- 生产化：Haystack + Milvus/Weaviate，或用 Milvus/Weaviate 做向量层并在后端部署检索服务  
- 研究/高性能：FAISS、自定义 embedding 模型、Milvus（分布式）

## 按语言偏好
- Python 优先（大多数生态、Haystack、LlamaIndex、sentence-transformers、FAISS、Milvus 等）  
- JS/TS 支持：LangChain 提供 JS SDK 与示例，部分项目有 REST/HTTP 接口可跨语言使用（例如 Milvus/Weaviate）

---

## 快速上手（建议三步）
1. 概念理解：阅读 LangChain 与 LlamaIndex 的入门示例，理解 “检索 -> 组装上下文 -> 生成” 流程。  
2. 本地原型：用 sentence-transformers 生成 embeddings，Chroma/FAISS 做本地检索，把检索结果拼进 prompt 发送给 LLM（或本地 LLM）。  
3. 加入 agent：把上一步作为工具封装，使用 LangChain agents 或 AutoGen 自动化任务与工具调用；生产化时用 Haystack + Milvus/Weaviate 作为后端。

---

如果你想要我把这份 README 直接发布为 Gist 或 新建仓库并提交其它文件（例如示例 notebook、部署脚本），我也可以继续帮你添加。