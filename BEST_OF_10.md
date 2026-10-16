# 最值得收藏的 10 个开源项目（RAG & Agent 精选）

下面是我为你精选、值得收藏并优先关注的 10 个开源项目，适合学习、原型开发和生产化参考。

1. LangChain
- 用途：通用的链/Agent/工具调用框架，适合把检索、提示与工具组合成应用。
- 为何收藏：生态广、示例多、支持 Python/JS；是构建 RAG + Agent 的入口级库。
- 链接：https://github.com/langchain-ai/langchain

2. LlamaIndex (GPT-Index)
- 用途：构建文档索引与检索层，方便把非结构化文档转为上下文。
- 为何收藏：面向文档的大规模索引策略与示例，接入多种向量存储。
- 链接：https://github.com/jerryjliu/llama_index

3. Haystack (deepset)
- 用途：生产级问答与 RAG 管道，集成检索器、阅读器和管道组件。
- 为何收藏：关注生产化、部署与企业级需求（支持多后端）。
- 链接：https://github.com/deepset-ai/haystack

4. Microsoft AutoGen
- 用途：多 agent 协作与任务编排框架，适合复杂 agent 协同场景。
- 为何收藏：研究 agent 协作、并发与交互模式的好资料。
- 链接：https://github.com/microsoft/autogen

5. Auto-GPT
- 用途：社区级自动化 agent 示例，演示长任务闭环与自动决策。
- 为何收藏：好上手、众多社区插件和实战案例，便于理解 agent 循环。
- 链接：https://github.com/significant-gravitas/auto-gpt

6. Chroma
- 用途：本地/轻量向量数据库，适合快速原型与本地开发。
- 为何收藏：易用、部署简单，做 POC 非常方便。
- 链接：https://github.com/chroma-core/chromadb

7. Milvus
- 用途：分布式向量数据库，面向大规模向量检索场景。
- 为何收藏：生产级扩展能力强，适合需要横向扩展的检索服务。
- 链接：https://github.com/milvus-io/milvus

8. Weaviate
- 用途：带语义搜索与 GraphQL 支持的向量数据库。
- 为何收藏：易于集成多种数据源与插件，适合快速搭建语义检索服务。
- 链接：https://github.com/semi-technologies/weaviate

9. FAISS
- 用途：高性能相似搜索（ANN）库，研究与高性能检索的基石组件。
- 为何收藏：底层性能和索引策略学习的必看项目。
- 链接：https://github.com/facebookresearch/faiss

10. semantic-kernel (Microsoft)
- 用途：技能/插件系统与 agent 式交互的 SDK，支持多语言。
- 为何收藏：研究技能化、插件化 agent 的设计与实现风格。
- 链接：https://github.com/microsoft/semantic-kernel

---

使用建议：把上面 3–5 个仓库克隆到本地，先跑 README 的快速入门示例，再把其中的检索 + embedding + LLM 流程串成一个最小可运行的 demo（30–60 分钟可完成）。

需要我把这些项目各自的快速起步命令（Docker/requirements/示例脚本）也补上到仓库中吗？