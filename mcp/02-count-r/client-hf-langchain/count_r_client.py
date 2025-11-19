"""
Client MCP - Count R - Using LLM QWen Hugging Face  & LangChain
-------------------------------------------
This client:
1️. Connects to a MCP Server.
2. Uses tools to count the letter 'R'.
3. Integrates Hugging Face's API to demonstrate tool usage.
4. Utilizes LangChain for streamlined interactions with Hugging Face models.
"""

import asyncio
import os
import json
import httpx
from fastmcp import Client
from langchain.prompts import ChatPromptTemplate
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.output_parsers import StrOutputParser

MCP_SERVER_URL = os.environ.get("MCP_URL", "http://localhost:8000/mcp")
FASTMCP_API_KEY = os.environ.get("FASTMCP_API_KEY")
HF_API_TOKEN = os.environ.get("HF_API_TOKEN")
HF_MODEL = os.environ.get("HF_MODEL", "Qwen/Qwen3-4B-Instruct-2507")  

async def main():
    text_test = "Rapidly running rabbits rapidly run."
    
    # Connect to the MCP server. If the API key is available, pass it.
    if FASTMCP_API_KEY:
        client_mcp = Client(MCP_SERVER_URL, auth=FASTMCP_API_KEY)
        print("Using FastMCP API key for authentication.")
    else:
        client_mcp = Client(MCP_SERVER_URL)
    
    async with client_mcp:
        print(" Connected to the MCP Count R server")

        # Call the tool `count_r` directly (same as before)
        response = await client_mcp.call_tool(
            "count_r",
            {"text": text_test}
        )
        print(f"Direct TEST - Response from count_r tool: {response}\n")

    
        print("-----------------------------------------------------")
        print(f"Hugging Face Integration with LangChain and model {HF_MODEL}:")
        
        # --- Hugging Face approach (using LangChain HuggingFaceHub) ---
        if not HF_API_TOKEN:
            print("HF_API_TOKEN not set — skipping Hugging Face demo.")
            return

        # Create LangChain LLM backed by Hugging Face Inference
        hf_endpoint = HuggingFaceEndpoint(
            repo_id=HF_MODEL, 
            task="conversational",
            huggingfacehub_api_token=HF_API_TOKEN,
            temperature=0.7,
            max_new_tokens=256)
        
        llm = ChatHuggingFace(llm=hf_endpoint)

        prompt = ChatPromptTemplate.from_messages([
            ("system", "You are a helpful and concise assistant."),
            ("human", 'Return only a JSON object like {{"tool":"count_r","args":{{"text":"{text}"}}}}'),
        ])
        
        chain = prompt | llm | StrOutputParser()
        generated = chain.invoke({"text": text_test})
        print("\nResponse from HF model (raw):", generated)

        # Attempt to parse JSON indicating the tool call
        try:
            parsed = json.loads(generated.strip())
            if parsed.get("tool") == "count_r" and "args" in parsed:
                tool_args = parsed["args"]
                tool_resp = await client_mcp.call_tool("count_r", tool_args)
                print("Result of count_r (from HF-driven flow):", tool_resp)
            else:
                print("The model did not request the 'count_r' tool in the expected format.")
        except json.JSONDecodeError:
            print("Failed to parse the model output as JSON. Raw output:", generated)


if __name__ == "__main__":
    asyncio.run(main())