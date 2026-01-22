import sys

print(f"--- 🔎 Searching for AgentExecutor in Python {sys.version.split()[0]} ---")

# Attempt 1: The Standard Way
try:
    from langchain.agents import AgentExecutor
    print("✅ SUCCESS: from langchain.agents import AgentExecutor")
except ImportError as e:
    print(f"❌ FAILED: from langchain.agents import AgentExecutor ({e})")

# Attempt 2: The 'agent' Submodule (Common in v0.2+)
try:
    from langchain.agents.agent import AgentExecutor
    print("✅ SUCCESS: from langchain.agents.agent import AgentExecutor")
except ImportError as e:
    print(f"❌ FAILED: from langchain.agents.agent import AgentExecutor ({e})")

# Attempt 3: The 'agent_executor' File (Old/Legacy)
try:
    from langchain.agents.agent_executor import AgentExecutor
    print("✅ SUCCESS: from langchain.agents.agent_executor import AgentExecutor")
except ImportError as e:
    print(f"❌ FAILED: from langchain.agents.agent_executor import AgentExecutor ({e})")

print("------------------------------------------------")