"""starter/demo.py

最小可运行的 RAG 演示：
- 从 starter/data 读取文本文件
- 用 sentence-transformers 生成 embeddings
- 用 chromadb 持久化向量并检索 top-k
- 若配置了 OPENAI_API_KEY，会把检索到的上下文拼入 prompt 并调用 OpenAI
"""

import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
PERSIST_DIR = os.getenv("CHROMA_PERSIST_DIR", "./chroma_db")

# 小依赖导入
try:
    from sentence_transformers import SentenceTransformer
    import chromadb
    from chromadb.config import Settings
except Exception as e:
    print("缺少依赖，请先运行: pip install -r requirements.txt")
    raise

# 读取示例文档
DATA_DIR = Path(__file__).parent / "data"
files = sorted(DATA_DIR.glob("*.txt"))
if not files:
    print(f"未在 {DATA_DIR} 找到示例文档，请至少放置一个 .txt 文件。")
    exit(1)

documents = [f.read_text(encoding='utf-8') for f in files]
ids = [f.name for f in files]

# 生成 embeddings
print("加载 embedding 模型 (all-MiniLM-L6-v2)...")
model = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = model.encode(documents, convert_to_numpy=True).tolist()

# 初始化 Chroma 客户端并写入 collection
print(f"初始化 Chroma，持久化目录: {PERSIST_DIR}")
client = chromadb.Client(Settings(chroma_db_impl="duckdb+parquet", persist_directory=PERSIST_DIR))
collection = None
try:
    collection = client.get_collection("rag_demo")
except Exception:
    collection = client.create_collection("rag_demo")

print("写入文档与 embeddings 到 Chroma...")
collection.add(ids=ids, documents=documents, embeddings=embeddings)

# 简单查询流程
query = input("输入查询 (或直接回车使用默认示例): ")
if not query:
    query = "什么是 RAG (检索增强生成) 的核心思想?"

q_emb = model.encode([query], convert_to_numpy=True).tolist()[0]
res = collection.query(query_embeddings=[q_emb], n_results=3, include=['documents', 'distances'])

retrieved = res.get('documents', [[]])[0]
print("\n检索到的 top-k 文档：\n")
for i, doc in enumerate(retrieved, 1):
    print(f"--- 文档 {i} ---")
    print(doc[:800])
    print()

# 可选：调用 OpenAI
if OPENAI_API_KEY:
    try:
        import openai
        openai.api_key = OPENAI_API_KEY
        prompt = "根据以下检索到的文档，简洁回答用户问题:\n\n"
        for i, doc in enumerate(retrieved, 1):
            prompt += f"[来源 {i}] " + doc + "\n---\n"
        prompt += f"问题: {query}\n回答："

        print("调用 OpenAI 生成答案...")
        resp = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role":"user", "content": prompt}],
            max_tokens=300,
            temperature=0.0,
        )
        ans = resp['choices'][0]['message']['content']
        print("\n=== 生成回答 ===\n")
        print(ans)
    except Exception as e:
        print("调用 OpenAI 失败：", e)
else:
    print("\n未配置 OPENAI_API_KEY，已展示检索结果。如需 LLM 输出，请在 .env 中设置 OPENAI_API_KEY。")
