# AI Assignment Assistant Agent

This repository contains a **modular AI agent system** designed to automate drafting university assignments from a given topic prompt. The system uses **fine-tuned LLMs (LoRA)** and multi-agent workflows for planning, content generation, and review.

---

## 🚀 Features

### Core Features (Mandatory)
- **Planner Agent:** Generates structured outlines and sub-tasks from a topic.
- **Writer Agent:** Generates draft content using a **fine-tuned LLM (LoRA)**.
- **Reviewer Agent:** Evaluates draft quality based on coherence, relevance, style, and grammar.
- **Interaction Logs:** Capture all prompts, outputs, and feedback for reproducibility.

### Optional Features (Bonus)
- Multi-agent collaboration (Planner + Writer + Reviewer in parallel).
- External integrations:
  - Retrieval-Augmented Generation (RAG) for external knowledge.
  - Custom tools or APIs for additional resources.
- User interface (CLI, web app, or desktop app).

---

## 📁 Repository Structure

├── agent/ # Python code for Planner, Writer, and Reviewer agents
│ ├── planner.py
│ ├── writer.py
│ ├── reviewer.py
│ └── utils.py # Helper functions
├── logs/ # Interaction logs
│ ├── sample_prompts.json
│ └── sample_feedback.json
├── architecture.md # Detailed architecture and component maps
├── report.md # Project report with fine-tuning details and evaluation
├── requirements.txt # Python dependencies
└── README.md # This file


---

## 🏗️ System Architecture

The system is composed of three main agents:

1. **Planner Agent:** Converts a topic into structured sections and sub-tasks.  
2. **Writer Agent:** Uses a **fine-tuned LoRA model** to generate draft content for each section.  
3. **Reviewer Agent:** Evaluates draft quality using multi-metric evaluation (coherence, relevance, style, grammar).  

**Workflow:**
User Input → Planner Agent → Writer Agent → Reviewer Agent → Final Draft

Refer to `architecture.md` for detailed diagrams and interaction flow.

---

## ⚙️ Installation

1. Clone the repository:
```bash
git clone https://github.com/<your-username>/AI-Assignment-Agent.git
cd AI-Assignment-Agent

2.Create a virtual environment and activate it
 python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

3.Install dependencies:
pip install -r requirements.txt


💻 Usage

1.Run the Planner Agent:
python agent/planner.py --topic "Automating University Assignments using AI Agents"

2.Generate draft content using Writer Agent:
python agent/writer.py --outline "logs/sample_outline.json"

3.Evaluate draft using Reviewer Agent:
python agent/reviewer.py --draft "logs/sample_draft.json"

4.Check final reviewed draft in logs/.
📊 Evaluation Metrics

Coherence: Logical structure across sections.

Relevance: Matches outline and topic.

Style: Academic tone and clarity.

Grammar: Correct language usage.

📜 Fine-Tuning

Model: Base LLM fine-tuned using LoRA.

Purpose: Specialize the model for academic writing with reliable structure and style.

Data: Collection of academic assignments and reports.

Method: Parameter-efficient tuning with LoRA; reduced hallucinations and improved output quality.

📂 Deliverables

Source code: agent/ folder

Architecture diagrams: architecture.md

Project report: report.md

Interaction logs: logs/ folder

📝 Acknowledgements

Developed as part of the AI Agents Assignment.
Inspired by Anthropic’s “Building Effective Agents” and modern LLM architectures.

📌 License

This project is for educational purposes only.
