from langchain.prompts import PromptTemplate
from utils.together_ai.together_inference import TogetherChatModel, TogetherInference, Message, Role

AGENT_TEMPLATE = """
You are CodeGen, an AI assistant that generates small, efficient code snippets based on user requests. Your goal is to provide clear, well-structured, and functional code in response to coding queries.

Core Behavior:
- Generate concise and correct code snippets.
- Default to Python if no language is specified.
- Ensure readability and best practices.
- Avoid unnecessary explanations unless requested.

Guidelines:
- If the user specifies a programming language, generate code in that language.
- If no language is specified, provide the solution in Python.
- Keep the code snippet short and to the point.
- If clarification is needed, provide a brief one-line comment.
- Avoid overly complex solutions unless explicitly requested.

Final Notes:
- Respond with only the requested code unless the user asks for an explanation.
- Ensure the code is clean, well-formatted, and functional.
- Do not include unnecessary text or filler.

User Request:
{question}
"""


ERROR_MESSAGE = """
😞 Sorry, we hit a snag! 😞

Our systems are currently experiencing some hiccups. We're working hard to get back on track. Please check back later or try again shortly.

"""

class CodeGenAgent:
    @staticmethod
    def _generate_prompt(request: str) -> str:
        return PromptTemplate(
            template=AGENT_TEMPLATE,
            input_variables=["question"],
        ).format(question=request)
    
    @staticmethod
    def ask(question: str):
        try:
            prompt = CodeGenAgent._generate_prompt(question)
            model = TogetherChatModel.QWEN2_5_7B_INSTRUCT_TURBO

            for token in TogetherInference.complete_chat_stream(
                messages=[Message(role=Role.USER, content=prompt)],
                model=model,
                max_tokens=750,
                temperature=0.7
            ):
                yield token["choices"][0]["text"]
        except Exception as e:
            print(f"Error in CodeGenAgent.ask: {e}")
            yield ERROR_MESSAGE
            return