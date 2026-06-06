# AI-Driven Automated Bug Analysis and Code Explanation Assistant

An advanced, task-oriented agentic framework designed for undergraduate software engineering education. The system intercepts runtime syntax, structural, and logical errors in user-submitted Python code, executes them safely within an isolated environment, and provides deep, structured pedagogical feedback using a Large Language Model.

---

## 1. System Architecture & Pipeline Overview
The assistant relies on a decoupled, modular "Perception-Reasoning-Action" engineering loop to evaluate code without risks of hallucination or host system degradation:

* Presentation Layer (Frontend UI): Built with Streamlit (`app.py`), providing an interactive web interface for input ingestion, async execution tracking, and dynamic Markdown/syntax highlighting rendering.
* Perception & Action Toolkit (Execution Sandbox): An isolated runtime environment (`sandbox.py`) that uses Python's `tempfile` and `subprocess` modules to spawn standalone child processes, intercept system tracebacks, and enforce strict execution timeouts.
* Reasoning Engine (Agentic Brain): A generative AI core (`agent.py`) powered by Google Gemini 2.5 Flash via the modern `google-genai` SDK, guided by deterministic Chain-of-Thought (CoT) system prompt templates.

---

## 2. Core Features
* Trace-Driven Diagnostics: Captures real runtime outputs (`stdout`) and errors (`stderr`) rather than relying on pure static analysis.
* Infinite Loop Safeguards: Automatically terminates resource-exhausting scripts after a strict 5-second threshold to protect host system stability.
* Structured Pedagogical Reports: Enforces a rigid 4-part educational layout: Root Cause Summary, Fault Location, Step-by-Step Logic Breakdown, and Refactored Code with inline remarks.
* Secure Environment Isolations: Uses strict process boundaries and zero-cleanup footprints for dynamic script executions.

---

## 3. Prerequisites
Ensure your local environment meets the following specifications before deployment:
* Operating System: Windows 10/11, macOS, or Linux
* Python Runtime: Version 3.10 or higher
* External Access: Valid Google Gemini API Key and active internet connection

---

## 4. Detailed Installation & Environment Setup

Follow these exact steps to clone, configure, and install the application locally:

### Step A: Clone the Repository
Open your terminal or command prompt and execute:
```bash
git clone [https://github.com/AshmalShahzad/AI-Bug-Analyzer-Agent.git](https://github.com/AshmalShahzad/AI-Bug-Analyzer-Agent.git)
cd AI-Bug-Analyzer-Agent