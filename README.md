# LinkedIn Post Generator (LangChain + Groq)

A Python project that uses LangChain and Groq LLM to generate professional LinkedIn posts based on a user-provided topic and language.

The system uses a **Router Agent** to classify topics as **Tech** or **General**, then conditionally selects the appropriate Writer Agent.

## Features

- Generates technology-focused LinkedIn posts.
- Generates general-topic posts (education, business, career, leadership, productivity, etc.).
- Uses a Router Agent for topic classification.
- Includes two Writer Agents: Tech Writer and General Writer.
- Supports multiple languages, including English and Bengali.
- Generates engaging posts with 2–4 short paragraphs.
- Uses Groq API through LangChain.

## Requirements

- Python 3.10 or newer
- Groq API key
- Visual Studio Code (recommended)

## Project Structure

```text
LinkedIn-Post-Generator/
│
├── Untitled20.ipynb
├── requirements.txt
├── .env.example
├── .env
├── .gitignore
└── README.md
```

## Setup in VS Code

### 1. Open the Project

Open the project folder in Visual Studio Code.

### 2. Create a Virtual Environment

**Windows (PowerShell):**

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, use Command Prompt:

```bat
.venv\Scripts\activate.bat
```

**macOS/Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

Create `requirements.txt` with:

```text
langchain-core
langchain-groq
python-dotenv
```

Install the packages:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Configure Groq API Key

Get your API key from:

https://console.groq.com/keys

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_actual_groq_api_key
```

You can also create `.env.example`:

```env
GROQ_API_KEY=your_groq_api_key_here
```

**Important:** Never upload your actual `.env` file or API key to GitHub.

### 5. Run the Notebook

1. Open `Untitled20.ipynb` in VS Code.
2. Select the Python interpreter from `.venv`.
3. Run the notebook cells from top to bottom.
4. Enter your API key if the notebook prompts you using `getpass()`.

Alternatively, to load the key from `.env`, use:

```python
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY not found.")
```

Pass `api_key` when initializing `ChatGroq`.

## Model Configuration

The project uses the following Groq model:

```python
llm = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0.7
)
```

Model availability depends on your Groq account and API access.

## Demonstration

### Example 1: Tech Topic (English)

```python
post = linkedin_post_generator(
    topic="Artificial Intelligence in Healthcare",
    language="English"
)

print(post)
```

**Selected Agent:** Tech Writer Agent

### Example 2: General Topic (Bengali)

```python
post = linkedin_post_generator(
    topic="Importance of Education",
    language="Bengali"
)

print(post)
```

**Selected Agent:** General Writer Agent

## Workflow

```text
User Input (Topic + Language)
             |
             v
         Router Agent
             |
       Topic Classification
             |
       +-----+------+
       |            |
      Tech        General
       |            |
       v            v
  Tech Writer   General Writer
       |            |
       +-----+------+
             |
             v
     LinkedIn Post
```

## Notes

- The project uses `ChatGroq` for LLM integration.
- `ChatOpenAI` is imported in the original notebook but is not required because it is not used.
- The notebook may make API calls when example cells are executed.
- API usage is subject to your Groq account's applicable limits and terms.