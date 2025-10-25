# Analytics Requirements AI Agent

This Python-based AI agent automatically generates **analytics requirements** using a **Retrieval-Augmented Generation (RAG)** approach.  
By leveraging historical requirements as context, it produces more accurate, consistent, and contextually relevant outputs for analytics projects.

---

## ✨ Features

- 🧠 **Context-Aware Generation** — uses historical requirements as a retrieval base to enrich new outputs  
- 💾 **Separation of Data** — keeps generated requirements and source data stored independently  
- 🧩 **Prompt Templates** — ensures consistent phrasing and formatting across generated requirements  
- 🔌 **Extendable Design** — can integrate easily with analytics, BI, or data engineering workflows  
- ⚙️ **Configurable Retrieval** — supports modular vector stores (e.g., FAISS, Chroma, Pinecone)

---

## 🗂 Project Structure

```
analytics-requirements-ai-agent/
│
├── data/
│   ├── historical_requirements/     # Existing reference documents
│   └── generated_requirements/      # Newly generated output
│
├── src/
│   ├── retriever.py                 # Handles vector database and document retrieval
│   ├── generator.py                 # LLM-based text generation logic
│   ├── prompts.py                   # Prompt templates for RAG generation
│   └── main.py                      # Entry point for the AI agent
│
├── config/
│   └── settings.yaml                # Model parameters and paths
│
├── requirements.txt                 # Python dependencies
└── README.md                        # Project documentation
```

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/analytics-requirements-ai-agent.git
cd analytics-requirements-ai-agent
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure Settings
Update `config/settings.yaml` with your preferred:
- LLM provider (e.g., OpenAI, Anthropic, or local model)
- Vector store backend (FAISS, Chroma, etc.)
- Paths to your historical and generated requirements

### 4. Run the Agent
```bash
python src/main.py
```

---

## 🧩 Example Workflow

1. Load historical analytics requirements into the `data/historical_requirements/` folder.  
2. The agent indexes these using a vector database.  
3. You provide a prompt (e.g., *“Generate analytics requirements for a new marketing campaign dashboard.”*).  
4. The model retrieves relevant past requirements and generates a new, context-aware spec.  
5. The new output is stored under `data/generated_requirements/`.

---

## ⚙️ Tech Stack

- **Python 3.9+**
- **LangChain** for orchestration  
- **OpenAI / Azure OpenAI / Local LLMs** for generation  
- **FAISS or Chroma** for retrieval  
- **YAML + JSON** for configuration and data handling  

---

## 🧠 Future Enhancements

- Add semantic search UI  
- Integrate with Jira or Confluence for auto-documentation  
- Implement evaluation metrics for generated requirement quality  
- Support fine-tuning on domain-specific datasets  

---

## 📄 License

MIT License © 2025 [Your Name]

---

## 🤝 Contributing

Contributions are welcome!  
Please open an issue or submit a pull request for improvements or new features.

---

## 💬 Example Prompt

```text
Generate analytics requirements for an e-commerce sales performance dashboard.
```

**Example Output:**
```yaml
title: E-Commerce Sales Performance Dashboard
description: Provides real-time insights into sales performance by category, region, and marketing channel.
requirements:
  - Enable daily data refresh via ETL pipeline
  - Display sales KPIs (Revenue, Orders, AOV)
  - Include filters for date, category, and region
  - Integrate with Google Analytics and internal CRM
```
