from pydantic import BaseModel, Field

class AssistantResponse(BaseModel):
    """Schema for structured AI output."""
    answer: str = Field(description="The primary answer to the user's question.")
    tone: str = Field(description="The tone used by the AI (e.g., professional, friendly).")
    confidence_score: float = Field(description="The AI's confidence level between 0 and 1.")
