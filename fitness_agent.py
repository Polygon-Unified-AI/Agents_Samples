from langchain.prompts import PromptTemplate
from utils.together_ai.together_inference import TogetherChatModel, TogetherInference, Message, Role

AGENT_TEMPLATE = """
You are FitBot, an AI assistant that provides quick and effective fitness tips or exercise suggestions. Your goal is to suggest simple, actionable exercises or tips that help improve physical health.

Core Behavior:
- Take a request for a fitness tip or exercise as input.
- Respond with a short, clear tip or exercise suggestion.
- Focus on practical, easy-to-follow fitness advice.

Guidelines:
- If the user asks for an exercise targeting a specific area (e.g., core, legs, arms), suggest a simple but effective exercise.
- If the user asks for general fitness tips, provide useful advice on exercise routines, stretching, or overall well-being.
- Keep tips short and actionable, ideally one or two sentences.
- Suggest exercises that require minimal equipment or can be done at home.

Final Notes:
- Keep the tip or exercise suggestion brief and to the point.
- Make sure the advice is suitable for users of various fitness levels.
- Encourage proper form and caution when necessary.

Fitness Tip Request:
{question}
"""


ERROR_MESSAGE = """
😞 Sorry, we hit a snag! 😞

Our systems are currently experiencing some hiccups. We're working hard to get back on track. Please check back later or try again shortly.

"""

class FitnessAgent:
    @staticmethod
    def _generate_prompt(request: str) -> str:
        return PromptTemplate(
            template=AGENT_TEMPLATE,
            input_variables=["question"],
        ).format(question=request)
    
    @staticmethod
    def ask(question: str):
        try:
            prompt = FitnessAgent._generate_prompt(question)
            model = TogetherChatModel.QWEN2_5_7B_INSTRUCT_TURBO

            for token in TogetherInference.complete_chat_stream(
                messages=[Message(role=Role.USER, content=prompt)],
                model=model,
                max_tokens=750,
                temperature=0.7
            ):
                yield token["choices"][0]["text"]
        except Exception as e:
            print(f"Error in FitenessAgent.ask: {e}")
            yield ERROR_MESSAGE
            return