"""
Client MCP - Count R - using Qwen Hugging Face LLM
-------------------------------------------
This client:
1️. Connects to a MCP Server.
2. Uses tools to count the letter 'R'.
3. Integrates Hugging Face's API to demonstrate tool usage.
"""
import os
import json
import httpx
from fastmcp import Client

MCP_SERVER_URL = os.environ.get("MCP_URL", "http://localhost:8000/mcp")
FASTMCP_API_KEY = os.environ.get("FASTMCP_API_KEY")
HF_API_TOKEN = os.environ.get("HF_API_TOKEN")
HF_MODEL = os.environ.get("HF_MODEL", "Qwen/Qwen3-4B-Instruct-2507")  
HF_INFERENCE_URL = f"https://api-inference.huggingface.co/models/{HF_MODEL}"

async def main():
    # Connect to the MCP server. If the API key is available, pass it.
    if FASTMCP_API_KEY:
        client_mcp = Client(MCP_SERVER_URL, auth=FASTMCP_API_KEY)
        print("Using FastMCP API key for authentication.")
    else:
        client_mcp = Client(MCP_SERVER_URL)

    async with client_mcp:
        print(" Connected to the MCP Count R server")
        text_test = "Rapidly running rabbits rapidly run."
        
        # Call the tool `count_r` directly (same as before)
        response = await client_mcp.call_tool(
            "count_r",
            {"text": text_test}
        )
        print(f"Direct TEST - Response from count_r tool: {response}\n")

        # --- Hugging Face approach (orquestado manualmente) ---
        if not HF_API_TOKEN:
            print("HF_API_TOKEN not set — skipping Hugging Face demo.")
            return

        prompt = (
            "Return a JSON with the form {\"tool\":\"count_r\",\"args\":{\"text\":\"...\"}} "
            "when you want to invoke the count_r tool. "
            f"Text: \"{text_test}\""
        )

        async with httpx.AsyncClient() as hc:
            headers = {"Authorization": f"Bearer {HF_API_TOKEN}"}
            payload = {"inputs": prompt, "options": {"use_cache": False}}
            r = await hc.post(HF_INFERENCE_URL, headers=headers, json=payload, timeout=60.0)
            r.raise_for_status()
            # La Inference API puede devolver distintos formatos; asumimos texto en r.json() o r.text
            resp_json = r.json()
            # Muchos modelos devuelven [{'generated_text': '...'}]
            if isinstance(resp_json, list) and "generated_text" in resp_json[0]:
                generated = resp_json[0]["generated_text"]
            else:
                generated = r.text

        print("\nRespuesta del modelo HF (raw):", generated)

        # Intentar parsear JSON que indica la llamada al tool
        try:
            parsed = json.loads(generated.strip())
            if parsed.get("tool") == "count_r" and "args" in parsed:
                tool_args = parsed["args"]
                tool_resp = await client_mcp.call_tool("count_r", tool_args)
                print("Resultado de count_r (desde HF-driven flow):", tool_resp)
            else:
                print("El modelo no solicitó la herramienta 'count_r' en el formato esperado.")
        except json.JSONDecodeError:
            print("No se pudo parsear la salida del modelo como JSON. Salida cruda:", generated)

if __name__ == "__main__":
    asyncio.run(main())