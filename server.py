from mcp.server.fastmcp import FastMCP
import pandas as pd
import os
from typing import List, Dict, Any, Optional
import string
import re

from functions import PreprocessingFunctions
fn = PreprocessingFunctions()

mcp = FastMCP("TextProcessingMCP")


def check_path(file_path):
    if not os.path.exists(file_path):
            return {
                "error": "File not found",
                "file_path": file_path
            }


@mcp.tool()
def read_csv(file_path: str) -> Dict[str, Any]:
    """
    Read a CSV file and return basic information about it.
    
    Args: 
    file_path: filepath to csv file.
     """
    check_path(file_path)    
    try:
        df = pd.read_csv(file_path)
        return {
            "success": True,
            "data": df.head(10).to_dict(orient='records'),
            "columns": df.columns.tolist(),
            "shape": list(df.shape),
            "dtypes": df.dtypes.astype(str).to_dict()
        }
    except Exception as e:
        return {
            "error": f"Error reading file: {str(e)}",
            "file_path": file_path
        }


@mcp.tool()
def use_cols(file_path: str, cols: List[str]) -> Dict[str, Any]:
    """
    Read CSV file. Generates a dataframe with provided columns and saves it in a seperate csv file.
    
    Args:
    file_path: filepath to csv file.
    cols: list of columns to be used.
    """
    check_path(file_path)
    try:
        df = pd.read_csv(file_path)
        df=df[cols]
        df.to_csv("temp.csv",index=False)
        return {
            "success": True,
            "columns used": df.columns.tolist()
        }
    except Exception as e:
        return {
            "error": f"Error reading file: {str(e)}",
            "file_path": file_path
        }

@mcp.tool()
def lowercasing(col: str, file_path:str="temp.csv") -> Dict[str, Any]:
    """
    Accesses the temp.csv file if saved previously.
    Uses this CSV file to convert the text from the column passed as parameter to lowercase.
    Saves the csv file after adding the new processed column.
    """
    check_path(file_path)
    try:
        df=pd.read_csv(file_path)
        df["processed_text"] = df[col].apply(lambda x: x.lower())   # adding new column for processed text
        df.to_csv(file_path,index=False)
        return {
            "success": True,    
            "processed text in column": "processed_text",
            "sample text before": df[col][0],
            "sample text processed": df["processed_text"][0]
        }
    except Exception as e:
        return {
            "error": f"Error in processing request: {str(e)}"
        }

        
@mcp.tool()
def remove_punctuation(col: str, file_path:str="temp.csv") -> Dict[str, Any]:
    """
    Accesses the temp.csv file if saved previously.
    Uses this CSV file to remove punctuations from the text from the column passed as parameter.
    Saves the csv file after adding the new processed column.

    Args:
    file_path: filepath to csv file saved previously.
    col: column containing text data.
    """
    check_path(file_path)
    
    try:
        df=pd.read_csv(file_path)
        df["processed_text"] = df[col].apply(lambda x: fn.remove_punc(x))   # adding new column for processed text
        df.to_csv("temp.csv",index=False)
        return {
            "success": True,
            "processed text in column": "processed_text",
            "message":"Removed punctuations using string.punctuation",
            "sample text before": df[col][0],
            "sample text processed": df["processed_text"][0]
        }
    except Exception as e:
        return {
            "error": f"Error in processing request: {str(e)}"
        }

'''
@mcp.tool()
def tokenize_text(col, file_path:str="temp.csv"):
    """
    Accesses the temp.csv file if saved previously.
    Uses this CSV file to tokenize the text from the column passes as parameter.
    Saves the csv file after adding the new processed column.
    Args:
    file_path: filepath to csv file saved previously.
    col: column containing text data.
    """
    check_path(file_path)
    try:
        df=pd.read_csv(file_path)
        df["processed_text"] = df[col].apply(lambda x: fn.tokenize(x))
        df.to_csv("temp.csv",index=False)
        return {
            "success": True,
            "processed text in column": "processed_text",   
            "sample text before": df[col][0],
            "sample text processed": df["processed_text"][0]
        }
    except Exception as e:
        return {
            "error": f"Error in processing request: {str(e)}"
        }
'''

@mcp.tool()
def remove_stopwords(col: str, file_path:str="temp.csv") -> Dict[str, Any]:
    """
    Accesses the temp.csv file if saved previously.
    Uses this CSV file to tokenize, remove stopwords and de-tokenize the text from the column passed as parameter.
    Saves the csv file after adding the new processed column.

    Args:
    file_path: filepath to csv file saved previously.
    col: column containing text data.
    """
    check_path(file_path)

    try:
        df=pd.read_csv(file_path)
        df["processed_text"] = df[col].apply(lambda x: fn.tokenize(x))
        df["processed_text"] = df[col].apply(lambda x: fn.remove_stopwords(x))
        df["processed_text"] = df[col].apply(lambda x: fn.de_tokenize(x))
        df.to_csv(file_path,index=False)
        return {
            "success": True,
            "processed text in column": "processed_text",
            "message":"Removed stopwords from using nltk.corpus",
            "sample text before": df[col][0],
            "sample text processed": df["processed_text"][0]
        }
    except Exception as e:
        return {
            "error": f"Error in processing request: {str(e)}"
        }


@mcp.tool()
def stemming(col: str, file_path:str="temp.csv") -> Dict[str, Any]:
    """
    Accesses the temp.csv file if saved previously.
    Uses this CSV file to tokenize, remove stopwords and de-tokenize the text from the column passed as parameter.
    Saves the csv file after adding the new processed column.

    Args:
    file_path: filepath to csv file saved previously.
    col: column containing text data.
    """
    check_path(file_path)   
    try:
        df=pd.read_csv(file_path)
        df["processed_text"] = df[col].apply(lambda x: fn.tokenize(x))
        df["processed_text"] = df[col].apply(lambda x: fn.stemming(x))
        df["processed_text"] = df[col].apply(lambda x: fn.de_tokenize(x))
        df.to_csv(file_path,index=False)
        return {
            "success": True,    
            "processed text in column": "processed_text",
            "message": " Performed stemming using SnowballStemmer.",
            "sample text before": df[col][0],
            "sample text processed": df["processed_text"][0]
        }
    except Exception as e:
        return {
            "error": f"Error in processing request: {str(e)}"
        }

@mcp.tool()
def lemmatize(col: str, file_path:str="temp.csv") -> Dict[str, Any]:
    """
    Accesses the temp.csv file if saved previously.
    Uses this CSV file to tokenize, lemmatize and de-tokenize the text from the column passed as parameter.
    Saves the csv file after adding the new processed column.
    """
    check_path(file_path)
    try:
        df=pd.read_csv(file_path)
        df["processed_text"] = df[col].apply(lambda x: fn.tokenize(x))
        df["processed_text"] = df[col].apply(lambda x: fn.lemmatize(x))
        df["processed_text"] = df[col].apply(lambda x: fn.de_tokenize(x))
        df.to_csv(file_path,index=False)
        return {
            "success": True,    
            "processed text in column": "processed_text",
            "message": "Performed lemmatization using WordNetLemmatizer",
            "sample text before": df[col][0],
            "sample text processed": df["processed_text"][0]
        }
    except Exception as e:
        return {
            "error": f"Error in processing request: {str(e)}"
        }


@mcp.tool()
def remove_emojis(col: str, file_path:str="temp.csv") -> Dict[str, Any]:
    """
    Accesses the temp.csv file if saved previously.
    Uses this CSV file to remove emojis from the column passed as parameter.
    Saves the csv file after adding the new processed column.


    Args:
    file_path: filepath to csv file saved previously.
    col: column containing data.
    """
    check_file(file_path)
    try:
        df=pd.read_csv(file_path)
        df["processed_text"]=df[col].apply(lambda x: fn.remove_emojis(x))
        df.to_csv(file_path=false)
        return{
            "success": True,
            "sample text before": df[col][0],
            "sample text processed": df["processed_text"][0]
        }
    except Exception as e:
        return {
            "error": f"Error in processing request: {str(e)}"
        }


@mcp.tool()
def remove_emoticons(col: str, file_path:str="temp.csv") -> Dict[str, Any]:
    """
    Accesses the temp.csv file if saved previously.
    Uses this CSV file to remove emoticons from the column passed as parameter.
    Saves the csv file after adding the new processed column.

    Args:
    file_path: filepath to csv file saved previously.
    col: column containing data.
    """
    check_file(file_path)
    try:
        df=pd.read_csv(file_path)
        df["processed_text"]=df[col].apply(lambda x: fn.remove_emoticons(x))
        df.to_csv(file_path=false)
        return{
            "success": True,
            "sample text before": df[col][0],
            "sample text processed": df["processed_text"][0]
        }
    except Exception as e:
        return {
            "error": f"Error in processing request: {str(e)}"
        }



@mcp.tool()
def get_words_count(col: str, file_path:str="temp.csv") -> Dict[str, Any]:
    """
    Accesses the temp.csv file if saved previously.
    Uses this CSV file to get the value counts of the column passed as parameter.

    Args:
    file_path: filepath to csv file saved previously.
    col: column containing data.
    """
    check_path(file_path)
    try:
        df=pd.read_csv(file_path)
        df["word_count"]=df[col].apply(lambda x: len(x.split()))
        return {
            "success": True
        }
    except Exception as e:
        return {
            "error": f"Error in processing request: {str(e)}"
        }

        
if __name__ == "__main__":
    print("Starting MCP server...")
    mcp.run(transport='stdio')
