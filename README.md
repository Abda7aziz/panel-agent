# PanelAgent
##### TODO: An agent that parse the transcript as a talk, panel discussion or an interview.
##### TODO: A script or an agent to split the transcript according to its type as chunks of docs.


PanelAgent is a Q&A system that uses AI to answer questions based on panel discussion transcripts. It leverages LangChain, Ollama, and ChromaDB to provide context-aware responses from transcript data.

## ✅ Features

- Interactive Q&A interface for panel discussion transcripts
- Vector-based semantic search using ChromaDB
- Local LLM integration via Ollama
- Context-aware responses based on transcript content
- Support for large language models (LLaMA 3.1 8B)

### BONUS

##### TODO: add argparse for download.py for runnin on CLI

The downloader file let you download from youtube, use the cc or just the audio and whisper from OPENAI to create the transcript and burn the subtitle into the video:

- YouTube video downloader
- CC and CC language selector
- pull transcript using openai whisper (in case of no CC)
- subtitle burner (optional)

to use downloader.py you will need ffmpeg installed:
```bash
brew install ffmpeg
```


## 🔧 Requirements

- Python 3.8+
- Ollama installed and running locally
- Required Python packages (see Installation)

## 📦 Installation

1. First, install and run Ollama:
   ```bash
   # Install Ollama
   brew install ollama  # For macOS
   
   # Start the Ollama server
   ollama serve
   
   # Pull the LLaMA 3.1 8B model
   ollama pull llama3.1:8b
   ```

2. Clone the repository and install dependencies:
   ```bash
   git clone https://github.com/your-username/panel-agent.git
   cd panel-agent
   pip install -r requirements.txt #might be missing some packages 
   ```

## 🚀 Quick Start

1. Prepare your transcript file in the `artifacts/transcript/` directory.
   The file should be a plain text file with one line per speaker turn.
   
2. Run the application:
   ```bash
   python main.py
   ```

3. The application will:
   - Load and process the transcript (embedding)
   - Create a vector store for semantic search
   - Start an interactive Q&A session

4. Type your questions about the panel discussion and press Enter to get answers.

## 🛠️ Project Structure

- `main.py`: Main application entry point
- `vector.py`: Handles document processing and vector store operations
- `downloader.py`: Utility for downloading and processing YouTube videos (optional)
- `artifacts/transcript/`: Directory for storing transcript files
- `chromadb_langchain/`: Directory for the ChromaDB vector store (created on first run)

## ⚠️ Note

- Ensure you have sufficient system resources to run the LLaMA 3.1 8B model
- The first run will take longer as it processes the transcript and builds the vector store
- For best results, use high-quality transcripts with clear speaker turns

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
