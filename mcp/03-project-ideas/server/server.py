"""
MCP Server: Project Ideas Management
-----------------------------------------
This MCP server allows managing project ideas.
It exposes:
 - Tools: create, list, and search ideas.
 - Resources: static or dynamic guides.
 - Prompts: templates for idea analysis and expansion.
Typical usage:
An MCP agent can query registered ideas, analyze them,
or propose improvements based on the exposed guides and prompts.
"""

from fastmcp import FastMCP
from typing import List
import datetime

mcp = FastMCP("MCP Server - Manage Project Ideas")

IDEAS_DB = []

@mcp.tool
def add_idea(title: str, description: str, author: str) -> str:
    """
    Registers a new project idea in memory.
    """
    idea = {
        "title": title,
        "description": description,
        "author": author,
        "created_at": datetime.datetime.now().isoformat(),
    }
    IDEAS_DB.append(idea)
    return f"Idea registered: '{title}' by {author}"


@mcp.tool
def list_ideas() -> List[dict]:
    """
    Lists all registered project ideas.
    """
    return IDEAS_DB


@mcp.tool
def find_idea(keyword: str) -> List[dict]:
    """
    Searches for ideas containing a keyword in the title or description.
    """
    results = [
        idea for idea in IDEAS_DB
        if keyword.lower() in idea["title"].lower() or keyword.lower() in idea["description"].lower()
    ]
    return results


@mcp.resource("ideas://guide")
def ideas_guide() -> str:
    """
    Guide to evaluate or create project ideas.
    """
    return (
        "Guide to generating and evaluating project ideas:\n"
        "- Must solve a real problem or improve an existing process.\n"
        "- Consider technical, economic, and environmental feasibility.\n"
        "- Define the social or educational impact you seek to achieve.\n"
        "- Include possible data sources or technologies to be used."
    )


@mcp.resource("ideas://examples")
def ideas_examples() -> str:
    """
    Inspirational examples of previous project ideas.
    """
    return (
        "Examples of previous projects:\n"
        "1. Platform for sharing urban ecological routes.\n"
        "2. Recommendation system for educational materials using AI.\n"
        "3. App for monitoring domestic energy consumption.\n"
        "4. Dashboard for analyzing open public transport data."
    )


@mcp.resource("ideas://{title}")
def idea_detail(title: str) -> str:
    """
    Dynamic resource: returns details of a registered idea.
    Example: GET ideas://App Eco
    """
    for idea in IDEAS_DB:
        if idea["title"].lower() == title.lower():
            return (
                f"Idea: {idea['title']}\n"
                f"Description: {idea['description']}\n"
                f"Author: {idea['author']}\n"
                f"Date: {idea['created_at']}"
            )
    return f"No idea found with title '{title}'."


@mcp.prompt("analyze_idea")
def analyze_idea_prompt(idea_description: str) -> str:
    """
    Prompt for the model to analyze an idea according to innovation criteria.
    """
    return (
        "Analyze the following project idea considering these criteria:\n"
        "1. Originality and innovation.\n"
        "2. Potential impact (social, environmental, or economic).\n"
        "3. Technical feasibility.\n"
        "4. Clarity of purpose.\n\n"
        "Return a brief evaluation and a score from 1 to 5 for each criterion.\n\n"
        f"Idea:\n{idea_description}"
    )


@mcp.prompt("expand_idea")
def expand_idea_prompt() -> str:
    """
    Prompt for the model to propose improvements or extensions to an idea.
    """
    return (
        "You are a creative consultant. Based on the following idea, "
        "propose improvements or new possible directions, specifying:\n"
        "- What problem it solves.\n"
        "- Who it benefits.\n"
        "- What technologies or approaches could be used.\n\n"
        "Idea:\n{{idea_description}}"
    )


@mcp.prompt("summarize_ideas")
def summarize_ideas_prompt() -> str:
    """
    Prompt for the model to generate an executive summary
    of the current ideas in the database.
    """
    return (
        "Summarize the registered ideas executive, highlighting:\n"
        "- Main areas of interest.\n"
        "- Problems they address.\n"
        "- Common patterns.\n\n"
        "List of ideas:\n{{ideas_list}}"
    )