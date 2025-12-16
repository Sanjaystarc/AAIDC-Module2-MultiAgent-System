# 🤖 AAIDC Module 2 – Multi-Agent System using LangGraph & Gemini

## 🔍 Project Overview
This project is a **Multi-Agent AI System** built as part of **Module 2: Architecting Multi-Agent Systems** in the **Agentic AI Developer Certification (AAIDC)** by Ready Tensor.

The system demonstrates how multiple agents with distinct roles can collaborate, use tools, and reason with a **Large Language Model (LLM)**, coordinated through an orchestration framework.

---

## 🎯 Project Objective
The objective of this project is to demonstrate:
- Multi-agent collaboration with clearly defined roles
- Integration of **Large Language Models (LLMs)** into agent workflows
- Tool usage beyond basic text generation
- Agent orchestration using **LangGraph**

---

## 🧠 System Architecture
```
Repo Analyzer Agent
        ↓
Metadata Recommender Agent (Gemini LLM)
        ↓
Reviewer / Critic Agent
```

**Orchestration Framework:** LangGraph  
Agents communicate via a shared state object.

---

## 🧩 Agents & Responsibilities

### 1️⃣ Repo Analyzer Agent
**Role:**
- Reads and analyzes the repository README
- Extracts core project context

**Tools Used:**
- Repository README Reader

---

### 2️⃣ Metadata Recommender Agent (LLM-powered)
**Role:**
- Generates an improved project title
- Suggests relevant tags and keywords

**LLM Used:**
- Google Gemini (gemini-2.5-flash)

**Tools Used:**
- Keyword Extraction Tool
- Gemini LLM via LangChain

---

### 3️⃣ Reviewer / Critic Agent
**Role:**
- Reviews README quality
- Identifies missing or unclear sections

**Tools Used:**
- README Section Validation Tool

---

## 🛠️ Tools Used
- Repository README Reader
- Keyword Extraction Tool
- README Section Validation Tool
- Gemini LLM (via LangChain)

---

## ⚙️ Technologies Used
- Python
- LangGraph
- LangChain
- Google Gemini (gemini-2.5-flash)
- GitHub Codespaces

---

## 📂 Project Structure
```
AAIDC-Module2-MultiAgent-System/
├── main.py
├── agents/
│   ├── repo_analyzer.py
│   ├── metadata_agent.py
│   ├── reviewer_agent.py
│   └── __init__.py
├── tools/
│   ├── repo_reader.py
│   ├── keyword_extractor.py
│   ├── readme_checker.py
│   └── __init__.py
├── graph/
│   └── workflow.py
├── requirements.txt
├── .env.example
└── README.md
```

---

## ▶️ How to Run the Project

### 1️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 2️⃣ Set Environment Variable
```bash
export GEMINI_API_KEY=your_api_key_here
```

### 3️⃣ Run the Multi-Agent System
```bash
python main.py
```

---

## 💬 Sample Output
```
📘 MULTI-AGENT OUTPUT

Suggested Title: A Multi-Agent AI System for Improving Project Publications
Suggested Tags: ['agentic', 'langgraph', 'multi-agent']
Review Feedback: Missing sections: ['installation', 'usage', 'license']
```

---

## 📌 Limitations
- Uses a single LLM-powered agent
- No external web search or APIs
- No persistent memory

---

## 🚀 Future Enhancements
- Add LLM reasoning to more agents
- Introduce human-in-the-loop validation
- Support remote repository URLs
- Add evaluation metrics and observability

---

## 🎓 Certification Context
This project fulfills the requirements for **AAIDC Module 2: Architecting Multi-Agent Systems** by demonstrating:
- Multi-agent collaboration (≥3 agents)
- Tool integration
- **LLM-powered agent reasoning**
- Agent orchestration with LangGraph
- Clean, reproducible implementation

---

## 🧾 License
This project is intended for **educational purposes** as part of the Ready Tensor Agentic AI Developer Certification program.
