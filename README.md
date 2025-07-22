# Text-Preporcessing-MCP-server

A Model Context Protocol (MCP) server that provides automated comprehensive text preprocessing capabilities for CSV datasets. This server enables AI assistants to perform various text cleaning and transformation tasks on text data stored in CSV files.

## 🧹 Basic Text Cleaning

Lowercasing: Convert text to lowercase
Punctuation Removal: Strip punctuation marks from text
Emoji Removal: Clean out emoji characters
Emoticon Removal: Remove text-based emoticons (:), :(, etc.)

## 🔤 Advanced Text Processing

Stopword Removal: Filter out common stopwords ("the", "and", "is", etc.)
Stemming: Reduce words to their root form using Porter Stemmer
Lemmatization: Convert words to their dictionary base form using WordNet Lemmatizer

## File Structure

text-preprocessing-mcp/
├── server.py             # Main MCP server implementation with tools
├── functions.py          # Preprocessing functions source code
├── requirements.txt      # Python dependencies
├── pyproject.toml        # Configutation file
└── README.md             # This file

## Client Configuration

{
  "mcpServers": {
    "text-preprocessing": {
      "command": "uv",
      "args": ["path/to/server.py"]
    }
  }
}
