import streamlit as st
import subprocess

# ClawForge: Local AI Agent for Creative Workflows
st.set_page_config(page_title="ClawForge Agent", page_icon="🤖", layout="wide")

st.title("🤖 ClawForge: Local AI Assistant")
st.markdown("Automate your local creative workflows using DGX Spark & OpenClaw.")

# Sidebar configuration
st.sidebar.header("Agent Configuration")
model_choice = st.sidebar.selectbox("Local LLM Backend", ["gpt-oss-20b (Ollama)", "Nemotron-3-Nano", "LM Studio"])
st.sidebar.success(f"Connected to locally hosted {model_choice} on DGX.")

# Main Agent Interface
st.subheader("Send a command to your local agent:")
user_command = st.text_area("Example: 'Organize all loose images in my downloads folder by extension.'", height=100)

if st.button("Execute Command"):
    if user_command:
        with st.spinner(f"Agent reasoning via {model_choice}..."):
            # Mock execution for demo purposes
            st.success("Command parsed successfully.")
            st.info("Generated Python execution script:")
            
            mock_script = """
import os
import shutil

# Agent generated script to organize files
target_dir = './mock_workspace'
print(f"Agent executing cleanup in {target_dir}...")
# ... file operation logic ...
print("Task completed successfully in 0.4 seconds.")
            """
            st.code(mock_script, language='python')
            
            st.success("✅ Execution complete! Your workspace has been updated safely.")
    else:
        st.warning("Please enter a command for the agent.")

st.markdown("---")
st.caption("Powered by NVIDIA DGX Spark Playbooks & OpenClaw")
