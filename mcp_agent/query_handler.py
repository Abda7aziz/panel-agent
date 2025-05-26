# mcp_agent/query_handler.py

from agent.runner import run_agent

def run_langgraph_agent(question: str, context: str) -> str:
    return run_agent(question)

def answer_with_context(question: str, context: str = "") -> str:
    return run_langgraph_agent(question, context)