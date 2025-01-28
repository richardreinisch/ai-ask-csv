
# AI Ask CSV

A local tool powered by Ollama, LangChain, and llama3.2 to query CSV data using advanced embeddings and a large language model. Designed for efficiency, it utilizes an NVIDIA GPU with 12 GB VRAM.

---

## How It Works

1. **CSV Reading**: The script reads the data from a specified CSV file.
2. **Embedding Selection**: Relevant data is selected using embeddings.
3. **LLM Query**: The language model generates responses based on your questions.

---

## Example Output using Testdata `main_hugging.py`

`Question: Please find a company related to sports equipment for athletes, add all details?`

````
Based on the context provided, the company related to sports equipment for athletes is FitGear (FG).

Here are the details:

* id: 6
* company: FitGear
* short: FG
* text: High-performance sports equipment
* meta: Athletes endorsed: 30

This information provides a brief overview of FitGear as a company that specializes in high-quality sports equipment for athletes, with 30 endorsements from prominent athletes. 
````

## Preparation

### Install Ollama

Download and install Ollama from [their official website](https://ollama.com/).

### Create a Virtual Environment

In the root directory of the project:
```bash
python -m venv .venv
source .venv/bin/activate  # For Linux/macOS
.venv\Scripts\activate   # For Windows
```

### Install Dependencies

Run the following command to install the required Python packages:
```bash
pip install -r requirements.txt
```

---

## Usage

### Start the Ollama Server

Ensure the Ollama server is running. You can start it with:
```bash
ollama serve
```

Download Model:
```bash
ollama pull llama3.2
```

### Run the Script

Execute the main script to use the tool:
```bash
python main.py
```

Alternatively, you can run the Hugging Face Embeddings version:
```bash
python main_hugging.py
```

**Important Notes:**
- The used Ollama embedding model could lead to unexpected results, in that case use different embedding models or try the HuggingFace solution    
- For HuggingFace: on the first run, the embedding model will be downloaded and stored in the `.cache` folder.
- The HuggingFace embedding uses `all-MiniLM-L6-v2`, which is effective but continuously improving. For optimal performance, consider updating the model as newer versions are released.

---

## Legal Information

- This tool uses open-source models and embeddings. Refer to their respective licenses for compliance.
- Ensure your use case complies with data protection regulations, particularly when handling sensitive or personal information.
- The authors provide no warranty and assume no liability for any issues arising from the use of this tool.

---