# mcp_agent/app.py

import gradio as gr
from query_handler import answer_with_context

# Define the interface function that takes context and question as input
def mcp_interface(context, question):
    return answer_with_context(question, context)

# Create a Gradio Interface
iface = gr.Interface(
    fn=mcp_interface,           # The function to run when the interface is used
    inputs=["text", "text"],    # Two text inputs: context and question
    outputs="text",             # Single text output
)

# Launch the Gradio interface as a server
iface.launch(mcp_server=True)