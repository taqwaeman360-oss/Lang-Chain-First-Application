A simple, modular AI assistant built using LangChain. This project demonstrates how to use Prompt Templates and LCEL (LangChain Expression Language) to create dynamic, persona-based AI interactions.

🚀 Features
Persona-based responses: Easily switch between different expert roles (Teacher, Career Advisor, Code Reviewer).

Modular Architecture: Prompt templates are separated from application logic for better maintainability.

LCEL Implementation: Uses LangChain's modern piping (|) syntax to chain components.

Secure: Uses .env files to manage API credentials.

🛠 Prerequisites
Python 3.10+

An OpenAI API Key

pip installed

⚙️ Setup Instructions
Clone the repository:

Bash
git clone https://github.com/taqwaeman360
cd your-repo-name
Install dependencies:

Bash
pip install langchain langchain-openai python-dotenv
Configure environment variables:
Create a file named .env in the root directory and add your API key:

Plaintext
OPENAI_API_KEY=your_openai_api_key_here
Run the application:

Bash
python main.py
📂 Project Structure
Plaintext
├── .env              # API keys (Do not commit this to GitHub!)
├── .gitignore        # Files to exclude from Git (includes .env)
├── main.py           # Core application entry point
├── prompts.py        # Prompt template definitions
└── README.md         # Project documentation
💡 How it Works
prompts.py: Contains a dictionary of personas and the logic to inject user input into a ChatPromptTemplate.

main.py: Initializes the ChatOpenAI model and creates a chain using the pipe (|) operator to connect the prompt and the model.


