import os
import openai
from dotenv import load_dotenv

load_dotenv()


class LLMService:
    def __init__(self):
        self.client = openai.AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"), timeout=60)

    async def call_llm(
        self,
        prompt: str,
        max_tokens: int = 100,
        temperature: float = 0.0,
        system_prompt: str = "You are a helpful assistant.",
    ) -> dict:
        try:
            response = await self.client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": prompt},
                ],
                temperature=temperature,
                max_tokens=max_tokens,
            )
            return {"llm_answer": response.choices[0].message.content}

        except Exception as e:
            return {"error": f"An unknown error occurred: {str(e)}"}