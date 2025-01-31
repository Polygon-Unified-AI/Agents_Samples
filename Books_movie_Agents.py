from langchain.prompts import PromptTemplate
from utils.together_ai.together_inference import TogetherChatModel, TogetherInference, Message, Role

AGENT_TEMPLATE = """
You are RecoBot, an AI assistant that recommends books or movies based on the user's genre or mood. Your goal is to provide tailored suggestions that match the user's preferences.

Core Behavior:
- Take a genre or mood as input (e.g., sci-fi, romantic, adventurous, etc.).
- Respond with a book or movie recommendation and a brief description.
- Keep the recommendation relevant and engaging.

Guidelines:
- If the user specifies a genre, provide a recommendation for a book or movie that fits that genre.
- If the user specifies a mood (e.g., uplifting, intense, relaxing), recommend a book or movie that aligns with the mood.
- Offer a brief, enticing description to help the user decide if the recommendation fits their taste.

Final Notes:
- Keep recommendations relevant to the genre or mood.
- Provide a brief description of why the book or movie is a great fit.
- Avoid giving too many details to avoid spoilers.

Genre or Mood:
{question}
"""


ERROR_MESSAGE = """
😞 Sorry, we hit a snag! 😞

Our systems are currently experiencing some hiccups. We're working hard to get back on track. Please check back later or try again shortly.
"""

class BooksMovieAgent:
    @staticmethod
    def _generate_prompt(request: str) -> str:
        return PromptTemplate(
            template=AGENT_TEMPLATE,
            input_variables=["question"],
        ).format(question=request)
    
    @staticmethod
    def ask(question: str):
        try:
            prompt = BooksMovieAgent._generate_prompt(question)
            model = TogetherChatModel.QWEN2_5_7B_INSTRUCT_TURBO

            for token in TogetherInference.complete_chat_stream(
                messages=[Message(role=Role.USER, content=prompt)],
                model=model,
                max_tokens=750,
                temperature=0.7
            ):
                yield token["choices"][0]["text"]
        except Exception as e:
            print(f"Error in BookMovieAgent.ask: {e}")
            yield ERROR_MESSAGE
            return