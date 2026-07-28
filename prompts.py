from langchain_core.prompts import ChatPromptTemplate

# Define different personas here
personas = {
    "teacher": "You are a patient and knowledgeable teacher who explains complex topics simply.",
    "career_advisor": "You are a professional career coach who gives practical, actionable advice.",
    "code_reviewer": "You are a senior software engineer who focuses on clean code, performance, and best practices."
}

def get_prompt_template(persona_type):
    system_instruction = personas.get(persona_type, "You are a helpful AI assistant.")
    
    template = ChatPromptTemplate.from_messages([
        ("system", system_instruction),
        ("user", "{user_input}")
    ])
    return template
