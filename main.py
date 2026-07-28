import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

# Load your API key from .env
load_dotenv()

# 1. Initialize the Chat Model
llm = ChatOpenAI(model="gpt-4o-mini")

# 2. Define the Prompt Template
# The system message sets the persona, the user message takes dynamic input
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a {persona}. Provide short, helpful answers."),
    ("human", "{user_input}")
])

# 3. Create and Invoke the Chain
# We use the '|' operator to pipe the prompt into the model
chain = prompt | llm

# Run the application
persona = "helpful career advisor"
user_input = "How do I prepare for a technical interview?"

response = chain.invoke({"persona": persona, "user_input": user_input})

print(response.content)
