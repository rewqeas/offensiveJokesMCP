def build_mcp_prompt(system, tools, query, memory=[]):
    prompt = ""

    prompt += f"System: {system}\n\n"
    prompt += f"Available Tools:\n{tools}\n\n"

    if memory:
        prompt += "Memory:\n" + "\n".join(memory) + "\n\n"

    prompt += f"Query:\n{query}\n\n"

    prompt += (
        "Instructions:\n"
        "- Use the user's input topic to fetch a relevant joke using available APIs.\n"
        "- If no joke is found, fallback to a random joke.\n"
        "- Translate the joke into the requested language using a translation API.\n"
        "- Return both the original English joke and the translated version.\n"
        "- Be polite, concise, and humorous in tone when returning results.\n"
    )

    return prompt
