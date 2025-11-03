# [AI-Search-Engine](https://github.com/saiAravind-1104/AI-Search-Engine)

# 🤖 Langchain Multi-Source Search Engine with AI Agent

A **powerful AI-powered search engine** built using **LangChain**, **Streamlit**, and **Groq LLM** that intelligently queries **Wikipedia**, **Arxiv**, and **DuckDuckGo** through an interactive conversational interface.

This app allows you to **ask questions about any topic**, the **AI agent decides which sources to query**, retrieves relevant information, and generates **intelligent, context-aware answers** from your **LLM**.

---

## 🚀 Features

✅ Multi-Source Search (Wikipedia, Arxiv, DuckDuckGo)  
✅ Intelligent AI Agent with ReAct Pattern  
✅ Zero-Shot Tool Selection  
✅ Interactive Streamlit Chat Interface  
✅ Conversation History Management  
✅ Environment Variables with `.env`  
✅ Package Management using `uv`  
✅ Error Handling and Timeout Management  

---

## 🧱 Project Structure

```
AI-Search-Engine/
│
├── src/
│   └── app.py                  # Main Streamlit application
│
├── .env                        # API keys (GROQ_API_KEY)
├── .gitignore                  # Git ignore rules
├── requirements.txt            # Python dependencies
├── pyproject.toml              # Project metadata (optional)
└── README.md                   # Project documentation
```

---

## ⚙️ Prerequisites

Make sure you have the following installed:

- **Python ≥ 3.10**
- **uv** (modern Python package manager)
- **Git**

---

## 🧩 Installation Steps

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/saiAravind-1104/AI-Search-Engine.git
cd AI-Search-Engine
```

### 2️⃣ Install uv (if not already installed)

**On macOS/Linux:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**On Windows:**
```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### 3️⃣ Create Virtual Environment and Install Dependencies

```bash
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
uv pip install -r requirements.txt
```

**OR** if using `pyproject.toml`:

```bash
uv sync
```

This installs all required libraries with the correct versions:
- `streamlit` - Web interface
- `langchain` - LLM framework
- `langchain-groq` - Groq LLM integration
- `langchain-community` - Community tools and utilities
- `python-dotenv` - Environment variable management
- `wikipedia` - Wikipedia API
- `arxiv` - Arxiv research papers API
- `duckduckgo-search` - Web search engine

### 4️⃣ Setup Environment Variables

Create a `.env` file in your project root:

```bash
touch .env
```

Add your Groq API key:

```env
GROQ_API_KEY=your_groq_api_key_here
```

**To get your Groq API key:**
1. Visit [https://console.groq.com](https://console.groq.com)
2. Sign up for a free account
3. Generate an API key from the dashboard
4. Copy and paste it into your `.env` file

### 5️⃣ Run the Application

```bash
streamlit run src/app.py
```

Then open the URL shown in your terminal (usually `http://localhost:8501`) in your browser.

---

## 🧠 How It Works: The AI Agent Pipeline

### 1. User Query
You ask a question through the Streamlit chat interface.

### 2. Agent Analysis
The LangChain Agent (ZERO_SHOT_REACT_DESCRIPTION) reads your question and analyzes:
- **Should I search Wikipedia for general knowledge?**
- **Should I search Arxiv for academic papers?**
- **Should I use DuckDuckGo for web search?**
- **Or should I combine multiple sources?**

### 3. Tool Selection & Execution
Based on the ReAct pattern:
- **Reasoning**: Agent decides which tool(s) to use
- **Acting**: Agent calls the selected tool(s)

**Available Tools:**
- **Wikipedia** - General knowledge (200 char limit, 1 result)
- **Arxiv** - Academic papers and research (200 char limit, 1 result)
- **DuckDuckGo** - Web search for current information

### 4. Information Retrieval
Each tool retrieves relevant information from its source.

### 5. LLM Processing
Groq's LLaMA-3.1-8B-instant model processes the retrieved information and generates a natural, coherent response.

### 6. Response Generation
The synthesized answer is displayed in the chat interface and stored in session memory.

---

## 🧪 Example Interactions

### Example 1: Academic Query
**User:**
> What are transformer models?

**Agent Action:** Queries Arxiv for recent research papers on transformers

**Assistant:**
> Transformer models are a type of neural network architecture... [synthesized from Arxiv papers]

### Example 2: General Knowledge
**User:**
> Tell me about artificial intelligence

**Agent Action:** Queries Wikipedia for comprehensive information

**Assistant:**
> Artificial intelligence (AI) refers to... [sourced from Wikipedia]

### Example 3: Current Events
**User:**
> What's happening in AI research today?

**Agent Action:** Combines multiple sources (DuckDuckGo for latest news, Arxiv for papers)

**Assistant:**
> Recent developments in AI include... [synthesized from multiple sources]

---

## 📦 Key Dependencies & Explanations

| Package | Purpose |
|---------|---------|
| **LangChain** | Framework for building LLM applications and agents |
| **Streamlit** | Interactive web interface for chat |
| **langchain-groq** | Integration with Groq's fast LLM inference |
| **langchain-community** | Community tools (Wikipedia, Arxiv, DuckDuckGo) |
| **FAISS** | Vector similarity search (optional, for future enhancements) |
| **python-dotenv** | Secure environment variable management |
| **Wikipedia** | Wikipedia API for knowledge retrieval |
| **Arxiv** | Academic paper search and retrieval |
| **duckduckgo-search** | Privacy-focused web search |

---

## 🧑‍🏫 Code Deep Dive (Gen AI Tutor Mode)

### Understanding the Agent Architecture

```python
agent = initialize_agent(
    llm=llm,
    tools=[wikipedia, arxiv, web_search],
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    handling_parsing_errors=True
)
```

**Breaking It Down:**

- **`llm`**: The Groq LLaMA model - the "brain" that understands queries
- **`tools`**: List of available tools the agent can choose from
- **`agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION`**:
  - **Zero-Shot**: No training examples needed, agent learns from tool descriptions
  - **ReAct**: Reasoning + Acting pattern (thinks before acting)
  - **Description**: Agent uses text descriptions to understand tools

### The ReAct Pattern (Reasoning + Acting)

```
[Thought] → [Action] → [Observation] → [Thought] → ... → [Final Answer]
```

Example for "What is machine learning?":
1. **Thought**: "This is a general knowledge question, I should use Wikipedia"
2. **Action**: Call WikipediaQueryRun with query "machine learning"
3. **Observation**: Receive summary from Wikipedia
4. **Final Answer**: Generate comprehensive response for user

### Session State Management

```python
if "message" not in st.session_state:
    st.session_state["message"] = [...]
```

**Why this matters:**
- Streamlit reruns the entire script on every interaction
- Without `session_state`, chat history would disappear
- `session_state` persists data across reruns
- All messages are stored as objects: `{"role": "user"/"ai", "content": "..."}`

### Error Handling

```python
handling_parsing_errors=True
```

- Gracefully handles cases where agent gets confused
- Prevents crashes from malformed responses
- Automatically retries with better formatting

---

## 🛠️ Troubleshooting

### Issue: `ModuleNotFoundError`
**Solution:** 
```bash
uv pip install --force-reinstall streamlit langchain langchain-groq langchain-community
```

### Issue: API Key Error
**Solution:** 
- Verify `.env` file exists in root directory
- Check format: `GROQ_API_KEY=gsk_...` (no quotes needed)
- Ensure no extra spaces or special characters

### Issue: DuckDuckGo Search Fails
**Solution:**
```bash
uv pip install --upgrade duckduckgo-search
```

### Issue: Agent Timeout
**Solution:**
- Try simpler queries first
- Check internet connection
- Groq API might be rate-limited (wait a moment and retry)

### Issue: Streamlit Caching Error
**Solution:**
```bash
streamlit run src/app.py --logger.level=debug
```

---

## 🚀 Advanced Usage

### Customize Tool Parameters

To retrieve more context, modify in `src/app.py`:

```python
# Increase character limit from 200 to 500
wikipedia_api_wrapper = WikipediaAPIWrapper(
    doc_content_chars_max=500,  # More content
    top_k_results=3              # More results
)
```

### Add New Tools

To extend with custom tools:

```python
from langchain.tools import Tool

def custom_tool_func(query):
    # Your implementation
    return result

custom_tool = Tool(
    name="CustomTool",
    func=custom_tool_func,
    description="Description of what this tool does"
)

tools = [wikipedia, arxiv, web_search, custom_tool]
```

### Use Different LLM Models

```python
# Instead of LLaMA 3.1 8B
llm = ChatGroq(model="mixtral-8x7b-32768")  # More powerful
llm = ChatGroq(model="gemma-7b-it")          # Lightweight
```

---

## 📚 Learning Resources

### LangChain & Agents
- [LangChain Documentation](https://python.langchain.com/)
- [LangChain Agents Guide](https://python.langchain.com/docs/modules/agents/)
- [ReAct Pattern Paper](https://arxiv.org/abs/2210.03629)

### Groq API
- [Groq Console](https://console.groq.com)
- [Groq Python SDK](https://github.com/groq/groq-python)

### Tools & Frameworks
- [Streamlit Documentation](https://docs.streamlit.io/)
- [uv Package Manager](https://docs.astral.sh/uv/)

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---


## 👨‍💻 Author

Created with ❤️ by **Sai Aravind**

- GitHub: [@saiAravind-1104](https://github.com/saiAravind-1104)
- Project: [AI-Search-Engine](https://github.com/saiAravind-1104/AI-Search-Engine)

---

## 🙏 Acknowledgments

- **LangChain** for the powerful agent framework
- **Groq** for ultra-fast LLM inference
- **Streamlit** for the intuitive UI framework
- **HuggingFace** for embeddings and model hosting
- **Wikipedia, Arxiv, DuckDuckGo** for data sources

---

## 📞 Support

For issues, questions, or suggestions, please:
1. Check the [Troubleshooting](#-troubleshooting) section
2. Open an [Issue](https://github.com/saiAravind-1104/AI-Search-Engine/issues) on GitHub
3. Contact the maintainer

---

**Happy Searching! 🔍🤖**