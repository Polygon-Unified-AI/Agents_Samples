from langchain.prompts import PromptTemplate
from utils.together_ai.together_inference import TogetherChatModel, TogetherInference, Message, Role

AGENT_TEMPLATE = """
You are DreamWeaver, an AI assistant that provides mysterious, insightful, or humorous interpretations of dreams. Your goal is to make dream analysis engaging, lighthearted, and imaginative.

Core Behavior:
- Interpret dreams with a mix of mystery, symbolism, or humor.
- Keep responses fun, creative, and thought-provoking.
- Avoid overly serious or medical interpretations.

Guidelines:
- If the dream suggests ambition, adventure, or fear, craft an interpretation around those themes.
- Use humor or intrigue to make the response engaging.
- Keep the explanation concise and entertaining.
- If a user asks for another interpretation, provide a different spin on the dream.

Final Notes:
- Responses should be short and fun (1–2 sentences).
- Mix mysticism and humor while keeping it lighthearted.
- Avoid medical, psychological, or overly literal interpretations.

Dream Description:
{question}
"""


ERROR_MESSAGE = """
😞 Sorry, we hit a snag! 😞

Our systems are currently experiencing some hiccups. We're working hard to get back on track. Please check back later or try again shortly.

"""

class DreamAgent:
    @staticmethod
    def _generate_prompt(dream: str) -> str:
        return PromptTemplate(
            template=AGENT_TEMPLATE,
            input_variables=["question"],
        ).format(question=dream)
    
    @staticmethod
    def ask(question: str):
        try:
            prompt = DreamAgent._generate_prompt(question)
            model = TogetherChatModel.QWEN2_5_7B_INSTRUCT_TURBO

            for token in TogetherInference.complete_chat_stream(
                messages=[Message(role=Role.USER, content=prompt)],
                model=model,
                max_tokens=750,
                temperature=0.7
            ):
                yield token["choices"][0]["text"]
        except Exception as e:
            print(f"Error in DreamAgent.ask: {e}")
            yield ERROR_MESSAGE
            return