# ClawForge: Local AI Agent for Creative Workflows

**Harnessing the power of DGX Spark and the intelligence of OpenClaw for seamless local automation.**

## Overview

ClawForge is an autonomous local AI agent designed specifically for creators—from game developers to technical artists. It bridges the gap between high-level creative intent and complex file/system operations. Instead of manually managing directories, writing glue scripts, and switching context, creators can simply ask ClawForge to handle the tedious work, ensuring faster iteration, zero data privacy risks, and maximum use of local compute power.

This project was built during the **DGX Spark Hackathon** utilizing the official [NVIDIA DGX Spark Playbooks](https://github.com/NVIDIA/dgx-spark-playbooks).

## The Problem
Creative workflows are plagued by manual friction. Creators lose hours on boilerplate automation, directory restructuring, and setting up development environments. This context-switching kills creative momentum and slows down product delivery.

## Our Solution
ClawForge provides an intuitive natural language interface (via OpenClaw) that communicates with a local LLM (served via Ollama) on a powerful NVIDIA DGX instance. The agent can write, debug, and execute Python/Bash scripts directly on the secure host machine to automate any workflow.

### The "Multiplier" Effect
ClawForge transforms hours of manual labor into seconds of automated execution. It doesn't just suggest code; it executes it, giving creators back their most valuable asset: **time**.

## Technical Execution
ClawForge utilizes a robust, 100% local architecture:
- **Compute Instance:** NVIDIA DGX Spark.
- **Agent Framework:** OpenClaw.
- **Local LLM Backend:** Ollama.
- **Model Used:** gpt-oss-20b (optimized for local inference via quantization).

## High-Level Architecture
1. **Creator User Input:** Types natural language command into the OpenClaw Web UI.
2. **OpenClaw Agent:** Analyzes request and queries the local LLM.
3. **Local LLM (via Ollama):** Generates the necessary Python/Bash script.
4. **Secured Execution:** OpenClaw executes the script directly on the DGX host.
5. **Real-time Result:** The workspace is immediately updated and summarized for the creator.

## Quick Start (Theoretical Workflow)

### Prerequisites
- [NVIDIA DGX Spark environment](https://github.com/NVIDIA/dgx-spark-playbooks).
- [OpenClaw installed and running](https://github.com/NVIDIA/dgx-spark-playbooks/tree/main/nvidia/openclaw).
- [Ollama installed and running locally](https://ollama.com/install.sh).

### Step-by-Step

**1. Pull the Model:**
In the DGX terminal, run:
`ollama pull gpt-oss:20b`

**2. Configure OpenClaw:**
In the OpenClaw Config UI, set the Local Endpoint to `http://localhost:11434` and select the `gpt-oss:20b` model.

**3. Start Creating:**
Use the OpenClaw chat to issue commands.
> **Example:** "Create a standard Python package structure for a project named 'AssetPipeline'."

*(Note: Actual code generation will be automated by OpenClaw after Ollama finishes installation.)*

## Contribution & License
This project is licensed under the MIT License. Contributions are welcome!

## Team
- **Jack Yingjie Zhao:** yzhao9426@gmail.com/ yjack@upenn.edu


---
Built with pride at the **DGX Spark Hackathon**, San Jose, CA.
