# Text-Preporcessing-MCP-server

A Model Context Protocol (MCP) server that provides automated comprehensive text preprocessing capabilities for CSV datasets. This server enables AI assistants to perform various text cleaning and transformation tasks on text data stored in CSV files.

## Core Functionalities

### 🧹 Basic Text Cleaning

- Lowercasing: Convert text to lowercase
- Punctuation Removal: Strip punctuation marks from text
- Emoji Removal: Clean out emoji characters
- Emoticon Removal: Remove text-based emoticons (:), :(, etc.)

### 🔤 Advanced Text Processing

- Stopword Removal: Filter out common stopwords ("the", "and", "is", etc.)
- Stemming: Reduce words to their root form using Porter Stemmer
- Lemmatization: Convert words to their dictionary base form using WordNet Lemmatizer

## Installation

### Prerequisites

- Python 3.11 or higher (required)
- uv (recommended) or pip package manager

### From Source with uv (Recommended)
```bash
# Clone the repository
git clone https://github.com/ayyu-ssh/text-preprocessing-MCP-server.git
cd text-preprocessing-MCP-server

# Install with uv
uv sync

# Or install in development mode
uv pip install -e .
```

### Development Setup with uv
```bash
# Clone and set up for development
git clone https://github.com/yourusername/pandas-mcp.git
cd pandas-mcp

# Create project with uv (if starting from scratch)
# uv init pandas-mcp

# Sync dependencies (creates venv automatically)
uv sync

# Activate the virtual environment
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Download required NLTK data
uv run python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords'); nltk.download('wordnet')"
```

## Dependencies
This package automatically installs the following dependencies:

- **anthropic≥0.57.1** - Anthropic API client integration
- **fastmcp≥2.8.1** - Fast MCP server implementation
- **mcp-server≥0.1.4** - Core MCP server components
- **mcp[cli,fastmcp]≥1.9.4** - MCP with CLI and FastMCP support
- **nltk≥3.9.1** - Natural Language Toolkit for text processing
- **pandas≥2.3.0** - Data manipulation and analysis
- **python-dotenv≥1.1.0** - Environment variable management
- **scikit-learn≥1.7.0** - Machine learning utilities

## 🚀 Usage
### Starting the server
#### Using uv
```bash
# Run the MCP server directly
uv run server.py
```
The server will start and expose the three main tools to connected LLMs.

### Using the CLI
#### Interactive Mode
```bash
# using custom client
uv run client.py
```
#### 🔧 Client Configuration
```json
{
  "mcpServers": {
    "TextPreprocessingMCP": {
      "command": "uv",
      "args": [
        "--directory",
        "path/to/server.py",
        "run",
        "server.py"
      ]
    }
  }
}
```
Above configuration can also be used as configuration to Claude Desktop.
 
## File Structure
```bash
text-preprocessing-mcp/
├── server.py             # Main MCP server implementation with tools
├── functions.py          # Preprocessing functions source code
├── client.py             # Implementation of custom client
├── requirements.txt      # Python dependencies
├── pyproject.toml        # Configutation file
└── README.md             # This file
```

## Available Functions

### 1. CSV Operations

- read_csv(file_path) - Read CSV file and return basic information
- use_cols(file_path, cols) - Select specific columns and save to temp.csv

### 2. Text Cleaning Functions

- lowercasing(col, file_path) - Convert text to lowercase
- remove_punctuation(col, file_path) - Remove punctuation
- remove_emojis(col, file_path) - Remove emoji characters
- remove_emoticons(col, file_path) - Remove text emoticons

### 3. Text Processing Functions

- remove_stopwords(col, file_path) - Remove common stopwords
- stemming(col, file_path) - Apply stemming to words
- lemmatize(col, file_path) - Lemmatize words

### 4. Analysis Functions

- get_words_count(col, file_path) - Get word frequency counts

## 📄 License
This project is licensed under the MIT License - see the LICENSE file for details.
