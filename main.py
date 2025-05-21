
from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import build_retriever

# TODO: update main to take be a function that takes an arg for the transcript path

# Initialize retriever on transcript
retriever = build_retriever("artifacts/transcript/OpenAI’s Sam Altman Talks ChatGPT, AI Agents and Superintelligence — Live at TED2025.mp4_transcript.txt")

# Set up the Ollama-based LLM and prompt template
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

# REPL loop
print("=== PanelAgent Q&A ===")
print("Type 'q' to quit.")
while True:
    question = input("Q: ")
    if question.lower() == 'q':
        break
    snippets = retriever.invoke(question)
    answer = chain.invoke({"snippets": snippets, "question": question})
    print("\n")
    print("A:", answer)
    print("\n\n\n------------------")