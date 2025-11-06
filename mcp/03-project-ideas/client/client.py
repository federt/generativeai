"""
Client MCP - Project Ideas Management
-------------------------------------------
This client:
1️. Connects to a MCP Server.
2. Uses tools to add and list ideas.
3. Uses resources (guides, examples).
4. Uses prompts to generate analysis with GPT-4o-mini.
"""

import os
import asyncio
from openai import OpenAI
from fastmcp import Client

# os.environ["OPENAI_API_KEY"] = ""
OPENAI_MODEL = "gpt-4o-mini"
MCP_SERVER_URL = os.environ.get("MCP_URL", "http://localhost:8000/mcp")


async def main():
    # Connect to the MCP server
    client_mcp = Client(MCP_SERVER_URL)

    async with client_mcp:
        print(" Connected to the MCP Project Ideas Management server")

        # Create an idea with the tool `add_idea`
        response_add = await client_mcp.call_tool(
            "add_idea",
            {"title": "App Verde", "description": "Una app que incentiva el reciclaje con recompensas.", "author": "Danilo"}
        )
        print(f" {response_add}\n")

        # List registered ideas
        ideas = await client_mcp.call_tool("list_ideas")
        print(" Registered ideas:")
        print(ideas.content)

        # Get a resource (guide)
        guide = await client_mcp.read_resource("ideas://guide")
        print(" Guide to evaluate ideas:\n", guide, "\n")

        # Get a resource (examples)
        examples = await client_mcp.read_resource("ideas://examples")
        print(" Inspiring examples:\n", examples, "\n")

        # Get a prompt (for example, "analyze_idea")
        prompt_template = await client_mcp.get_prompt("analyze_idea")
        prompt_text = prompt_template.messages[0].content.text

        # Replace template variable with a concrete idea
        idea_description = "Una aplicación móvil que conecta turistas con guías locales según sus intereses culturales y gastronómicos."
        final_prompt = prompt_text.replace("{{idea_description}}", idea_description)

        print("\n Final prompt to be sent to the model:\n")
        print(final_prompt)

        # Crear cliente OpenAI
        client_openai = OpenAI()

        # Send the prompt to the GPT-4o-mini model
        print("\n Generating analysis with GPT-4o-mini...")
        response = client_openai.responses.create(
            model=OPENAI_MODEL,
            input=final_prompt,
        )

        print("\n Model response:\n")
        print(response.output_text)


if __name__ == "__main__":
    asyncio.run(main())