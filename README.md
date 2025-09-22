# Multi-Agent Blog Post Generator

## Overview

This project implements a multi-agent workflow using the CrewAI framework to automate the generation of blog posts. Leveraging large language models via Groq's API, the system orchestrates three specialized agents—Content Planner, Content Writer, and Editor—to produce structured, SEO-optimized Markdown articles on user-specified topics. The workflow ensures factual accuracy, engaging narrative, and polished output suitable for publication.

Key capabilities include:
- Dynamic topic-based content planning with trend analysis and keyword research.
- Expansion into full drafts with insightful analysis.
- Final editing for clarity, style, and error correction.

This tool is designed for content creators, educators, and developers seeking efficient, AI-assisted writing assistance.

## Features

- **Modular Agent Design**: Three agents collaborate sequentially for comprehensive content lifecycle management.
- **Groq LLM Integration**: Utilizes high-performance models (e.g., `llama-3.3-70b-versatile`) for rapid inference.
- **Command-Line Interface**: Accepts topics via arguments for seamless execution.
- **Output Persistence**: Generates clean Markdown files for easy archiving or deployment.
- **Verbose Logging**: Provides detailed execution traces for debugging and monitoring.

## Prerequisites

- Python 3.10 or higher.
- A valid Groq API key (obtainable from [console.groq.com](https://console.groq.com)).
- Required libraries: `crewai`, `langchain-groq`, `python-dotenv`.

## Installation

1. Clone or download the project repository.

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install crewai langchain-groq python-dotenv
   ```

4. Create a `.env` file in the project root with your Groq API key:
   ```
   GROQ_API_KEY=your_groq_api_key_here
   ```

## Usage

Execute the script with a topic as a command-line argument:

```
python main.py "Your Topic Here"
```

- **Example**:
  ```
  python main.py "Artificial Intelligence in Education"
  ```
  This generates a blog post saved as `blog_post_artificial_intelligence_in_education.md`.

- **Output**: The script prints the result to the console and saves it to a Markdown file. For production use, redirect output or integrate with a CI/CD pipeline.

### Customization

- **Agents and Tasks**: Modify `main.py` to adjust agent roles, goals, or task descriptions for specialized workflows (e.g., adding SEO tools).
- **LLM Model**: Update the `model` parameter in `ChatGroq` to alternative Groq-supported models, such as `groq/gemma2-27b-it`.
- **Default Topic**: Uncomment or set a default in `argparse` for non-interactive runs.

## Configuration

The workflow relies on environment variables loaded via `dotenv`. Ensure the `.env` file is git-ignored for security.

Agent backstories and goals are placeholders; refine them in `main.py` to align with your brand voice.

## Troubleshooting

- **LLM Errors**: Verify your Groq API key and model availability. Deprecated models (e.g., `mixtral-8x7b-32768`) will fail; refer to [Groq's deprecations](https://console.groq.com/docs/deprecations).
- **Provider Prefix**: Model names must include the `groq/` prefix for LiteLLM compatibility.
- **Rate Limits**: Monitor Groq usage quotas; implement retries if needed.
- **Verbose Output**: Set `verbose=False` in agents or crew for concise logging.

For persistent issues, consult CrewAI documentation at [docs.crewai.com](https://docs.crewai.com) or Groq's API reference.


*Last Updated: September 23, 2025*
