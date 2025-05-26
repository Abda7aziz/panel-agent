# main.py
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from agent.runner import run_agent

print("=== PanelAgent Q&A ===")
print("Type 'q' to quit.")

while True:
    question = input("Q: ")
    if question.lower() == 'q':
        break
    answer = run_agent(question)
    print("\nA:", answer)
    print("\n------------------")