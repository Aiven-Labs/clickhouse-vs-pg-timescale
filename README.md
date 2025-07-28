# Aiven OLAP Selector

A Streamlit application that helps you choose between PostgreSQL with TimescaleDB and ClickHouse based on your specific use case requirements.

## Features

- Interactive questionnaire with 5 key questions
- Intelligent scoring system based on your responses
- Detailed recommendations with explanations
- Next steps guidance for implementation

## Questions Asked

1. **Data Volume** - Expected daily data ingestion volume
2. **Query Patterns** - OLTP, OLAP, mixed, or time-series analytics
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
2. Answer the 5 questions about your use case
3. Click "Get Recommendation" 
4. Review the recommendation and reasoning
5. Follow the suggested next steps

## Recommendations

The app will recommend either:

- **PostgreSQL with TimescaleDB** - Best for transactional workloads, real-time ingestion, and teams with PostgreSQL experience
- **ClickHouse** - Best for large-scale analytics, high-volume data, and complex analytical queries

Each recommendation includes detailed explanations and confidence scores to help you make an informed decision.