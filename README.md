# Termibot

A simple terminal-based chatbot using `langchain_ollama` and `OllamaLLM`.  

## Installation & Setup  

### 1. Clone the Repository  
```bash
git clone https://github.com/yourusername/repository-name.git
cd repository-name
```

### 2. Install Dependencies  
Create a virtual environment (optional but recommended):  
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```  

Then install dependencies:  
```bash
pip install -r requirements.txt
```

### 3. Install Ollama  
Since the chatbot uses `OllamaLLM`, install Ollama from [ollama.ai](https://ollama.ai/) and pull the required model:  
```bash
ollama pull llama3.2
```

### 4. Run the Chatbot  
```bash
python main.py
```

## Usage  
- Type your message and press **Enter** to chat with the bot.  
- Type **exit** to quit.  

## Contributing  
Feel free to fork this repository, submit issues, or contribute with pull requests!  

## License  
This project is licensed under the MIT License.  
