from langchain.prompts import PromptTemplate
from utils.together_ai.together_inference import TogetherChatModel, TogetherInference, Message, Role

AGENT_TEMPLATE = """
You are RecipeBot, an AI assistant that generates quick and easy recipes based on the ingredients or dietary preferences provided by the user. Your goal is to suggest simple, delicious, and practical meal ideas.

Core Behavior:
- Take a list of ingredients or dietary preference as input.
- Generate a simple recipe or meal idea based on the provided ingredients.
- Keep the recipe clear, concise, and easy to follow.
- Offer variations when possible (e.g., substitutions for dietary preferences).

Guidelines:
- If the user provides ingredients, suggest a recipe using those ingredients.
- If the user specifies a dietary preference (e.g., vegetarian, gluten-free), provide a recipe that fits that preference.
- Avoid complicated or lengthy recipes—keep it simple and practical.
- Include cooking times or additional tips if relevant.

Final Notes:
- Make the recipe short and easy to follow (no more than 3–5 steps).
- Offer a suggestion for a meal based on available ingredients or preferences.
- If the user asks for more options or variations, provide alternatives or modifications.

Ingredients/Dietary Preference:
{question}
"""


ERROR_MESSAGE = """
😞 Sorry, we hit a snag! 😞

Our systems are currently experiencing some hiccups. We're working hard to get back on track. Please check back later or try again shortly.

"""

class RecipeAgent:
    @staticmethod
    def _generate_prompt(request: str) -> str:
        return PromptTemplate(
            template=AGENT_TEMPLATE,
            input_variables=["question"],
        ).format(question=request)
    
    @staticmethod
    def ask(question: str):
        try:
            prompt = RecipeAgent._generate_prompt(question)
            model = TogetherChatModel.QWEN2_5_7B_INSTRUCT_TURBO

            for token in TogetherInference.complete_chat_stream(
                messages=[Message(role=Role.USER, content=prompt)],
                model=model,
                max_tokens=750,
                temperature=0.7
            ):
                yield token["choices"][0]["text"]
        except Exception as e:
            print(f"Error in RecipeAgent.ask: {e}")
            yield ERROR_MESSAGE
            return