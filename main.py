
from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import build_retriever

# Initialize retriever on transcript
retriever = build_retriever("artifacts/transcript/Llamacon 2025 - Conversation with Mark Zuckerberg and Satya Nadella_transcript.txt")

# Set up the Ollama-based LLM and prompt template
model = OllamaLLM(model="llama3.1:8b", temperature=0.3)

template = """
You are PanelAgent, an expert panelist in a keynote discussion.
Use the provided transcript snippets to answer thoughtfully.

Transcript snippets:
{reviews}

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
    answer = chain.invoke({"reviews": snippets, "question": question})
    print("\n")
    print("A:", answer)
    print("\n\n\n------------------")