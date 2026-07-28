from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from schemas import AssistantResponse
from config import settings

# 1. Initialize the model
llm = ChatOpenAI(model=settings.MODEL_NAME)

# 2. Bind the schema for Structured Output
# This forces the model to return a JSON object matching the AssistantResponse schema
structured_llm = llm.with_structured_output(AssistantResponse)

def build_chain(persona_prompt):
    """
    Creates a chain that takes user input and returns a structured object.
    """
    prompt = ChatPromptTemplate.from_messages([
        ("system", persona_prompt),
        ("human", "{user_input}")
    ])
    
    # Return the runnable chain
    return prompt | structured_llm
