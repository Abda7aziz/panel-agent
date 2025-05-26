# agent/runner.py

from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from agent.vector import build_retriever

TRANSCRIPT_PATH = "artifacts/transcript/OpenAI’s Sam Altman Talks ChatGPT, AI Agents and Superintelligence — Live at TED2025.mp4_transcript.txt"

# Setup once, reuse everywhere
retriever = build_retriever(TRANSCRIPT_PATH)
model = OllamaLLM(model="llama3.1:8b", temperature=0.3)

template = """
You are PanelAgent, an expert panelist in a keynote discussion.
Use the provided transcript snippets to answer thoughtfully.

Transcript snippets:
{snippets}

Question:
{question}
"""
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

def run_agent(question: str) -> str:
    snippets = retriever.invoke(question)
    response = chain.invoke({"snippets": snippets, "question": question})
    return response