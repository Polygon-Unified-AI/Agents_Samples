from langchain.prompts import PromptTemplate
from utils.together_ai.together_inference import TogetherChatModel, TogetherInference, Message, Role

AGENT_TEMPLATE = """
You are RapMaster, an AI assistant that crafts creative and rhythmic rap verses based on a given word. Your goal is to drop bars that flow smoothly and capture the essence of the word provided.

Core Behavior:
- Generate short, punchy rap verses (2–4 lines).
- Keep it rhythmic, catchy, and true to rap culture.
- Use clever wordplay and rhyme schemes.

Guidelines:
- Focus on the given word and build the verse around it.
- Keep the language fresh and engaging, suitable for a rap battle vibe.
- Avoid explicit language, offensive themes, or inappropriate content.
- Ensure all responses are inclusive and free from racism, stereotypes, or harmful language.
- Make sure each verse has a clear flow and rhyme.

Final Notes:
- Keep it short—2 to 4 lines maximum.
- Ensure the rap has a good rhythm and rhymes well.
- If asked for another verse, switch up the style or approach for variety.

Word:
{question}
"""


ERROR_MESSAGE = """
😞 Sorry, we hit a snag! 😞

Our systems are currently experiencing some hiccups. We're working hard to get back on track. Please check back later or try again shortly.

"""

class RapAgent:
    @staticmethod
    def _generate_prompt(request: str) -> str:
        return PromptTemplate(
            template=AGENT_TEMPLATE,
            input_variables=["question"],
        ).format(question=request)
    
    @staticmethod
    def ask(question: str):
        try:
            prompt = RapAgent._generate_prompt(question)
            model = TogetherChatModel.QWEN2_5_7B_INSTRUCT_TURBO

            for token in TogetherInference.complete_chat_stream(
                messages=[Message(role=Role.USER, content=prompt)],
                model=model,
                max_tokens=750,
                temperature=0.7
            ):
                yield token["choices"][0]["text"]
        except Exception as e:
            print(f"Error in RapAgent.ask: {e}")
            yield ERROR_MESSAGE
            return