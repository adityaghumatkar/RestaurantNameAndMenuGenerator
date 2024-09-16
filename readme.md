# Restaurant Name Generator

This is a simple web application that generates fancy restaurant names and corresponding menu items for various cuisines using LangChain, OpenAI, and Streamlit. The app leverages LangChain's SequentialChain, agents, and custom prompts to generate creative restaurant names and menu items based on a selected cuisine.

## Table of Contents
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [How It Works](#how-it-works)
  - [LangChain Sequential Chains](#langchain-sequential-chains)
  - [Prompt Engineering](#prompt-engineering)
- [Streamlit Integration](#streamlit-integration)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)

## Features
- Select a cuisine type from the Streamlit sidebar.
- Generate a unique restaurant name based on the selected cuisine.
- Generate fancy menu items for the selected cuisine.
- User-friendly interface built with Streamlit.
- Backend powered by LangChain, using SequentialChain and custom prompts to interact with OpenAI's language model.

## Tech Stack
- **LangChain**: Framework for building applications powered by large language models (LLMs).
- **OpenAI**: LLM provider used for generating restaurant names and menu items.
- **Streamlit**: Framework for building web applications in Python.
- **Python**: Core language for the app's backend.

## Installation
1. Clone this repository:
    ```bash
    git clone https://github.com/yourusername/restaurant-name-generator.git
    cd restaurant-name-generator
    ```
2. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```
3. Set up your OpenAI API key in the environment. You can create a `.env` file and add your OpenAI key:
    ```makefile
    OPENAI_API_KEY=your_openai_api_key
    ```
4. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

## Usage
1. Open your browser and navigate to `http://localhost:8501/` to access the app.
2. Select a cuisine from the sidebar dropdown menu.
3. Click the "Generate Restaurant Name & Menu" button.
4. The app will display a fancy restaurant name and corresponding menu items for the selected cuisine.

## Project Structure
```bash
restaurant-name-generator/
  ├── app.py                 # Main Streamlit app
  ├── langchain_helper.py    # LangChain logic (sequential chains, prompts)
  ├── data/
  │   └── cuisine.py         # List of available cuisines
  ├── requirements.txt       # Python dependencies
  └── README.md              # This README file
