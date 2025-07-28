# Aiven OLAP Selector

This is an application that helps you choose between Aiven for PostgreSQL with TimescaleDB or Aiven for ClickHouse based on your specific use case requirements.

## Features

- Interactive questionnaire with 5 key questions
- Scoring system based on your responses
- Detailed recommendations with explanations
- Next steps guidance for implementation

## Questions Asked

3. **Real-time Requirements** - Latency and processing speed needs
4. **Data Retention** - How long you need to keep data
5. **Team Expertise** - Your team's database experience level

## Installation

This project uses [uv](https://github.com/astral-sh/uv) for dependency management.

```bash
# Install dependencies
uv sync

# Run the application
uv run streamlit run database_selector.py
```

## Usage

1. Launch the application
2. Answer the questions about your use case
4. Review the recommendation and reasoning
5. Follow the suggested next steps

Each recommendation includes detailed explanations and confidence scores to help you make an informed decision.
