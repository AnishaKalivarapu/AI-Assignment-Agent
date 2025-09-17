# AI Assignment Assistant Agent – System Architecture

This document describes the design, components, and workflow of the **AI Assignment Assistant Agent**, which automates academic assignment drafting.

---

## 1. Overview

The AI Agent system automates drafting high-quality reports from a topic prompt. It combines **planning, content generation, and review** into a modular pipeline.

**Core Agents:**
1. **Planner Agent:** Generates structured outlines and sub-tasks.
2. **Writer Agent:** Uses a **fine-tuned LLM (LoRA)** to generate draft content.
3. **Reviewer Agent:** Evaluates the draft for coherence, relevance, style, and grammar.

**Optional Extensions:**
- Multi-agent collaboration (Planner + Writer + Reviewer in parallel)
- Retrieval-Augmented Generation (RAG) for integrating external knowledge
- Custom tools for dataset integration or external document access

---

## 2. High-Level Architecture

```text
+-------------------+
|     User Input    |
|  (Topic / Prompt) |
+--------+----------+
         |
         v
+-------------------+
|   Planner Agent   |
| - Generates outline|
| - Plans sections  |
+--------+----------+
         |
         v
+-------------------+
|   Writer Agent    |
| - Fine-tuned LLM  |
| - Generates draft |
+--------+----------+
         |
         v
+-------------------+
|  Reviewer Agent   |
| - Multi-metric eval|
| - Feedback report |
+--------+----------+
         |
         v
+-------------------+
|  Final Output     |
|  (Reviewed Draft) |
+-------------------+

3. Component Details
3.1 Planner Agent

Converts user topic into structured sections and points.

Input: Topic or prompt.

Output: Outline (Introduction, Methodology, Results, Conclusion).

Logic: Predefined templates + reasoning.

Optional: Can use a lightweight LLM for dynamic outline generation.

3.2 Writer Agent

Generates detailed draft content based on the outline.

Input: Outline from Planner Agent.

Output: Draft content.

Model: Fine-tuned LLM (LoRA) for academic style and reliability.

Features: Section-wise generation, iterative refinement, modular design.

3.3 Reviewer Agent

Evaluates draft quality for coherence, relevance, style, and grammar.

Input: Draft from Writer Agent.

Output: Evaluation report with scores and feedback.

Metrics: Coherence, Relevance, Style, Grammar.

Optional: Can integrate a separate LLM or grammar-checking tool for advanced evaluation.

4. Interaction Flow
