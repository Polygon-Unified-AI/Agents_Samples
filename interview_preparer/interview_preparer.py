from langchain.prompts import PromptTemplate
from langchain.output_parsers import PydanticOutputParser

from utils.together_ai.together_inference import TogetherChatModel, TogetherInference, Message, Role
from .models.interview_questions import InterviewQuestions
from .models.answers_evaluation import AnswersEvaluation
from .models.question_and_answer import QuestionAndAnswer
from .prompts.interview_preparer_template import INTERVIEW_PREPARER_TEMPLATE
from .prompts.interview_evaluation_template import INTERVIEW_EVALUATION_TEMPLATE

# Output parser for InterviewQuestions
INTERVIEW_QUESTIONS_OUTPUT_PARSER = PydanticOutputParser(
    pydantic_object=InterviewQuestions
)

# Output parser for AnswersEvaluation
ANSWERS_EVALUATION_OUTPUT_PARSER = PydanticOutputParser(
    pydantic_object=AnswersEvaluation
)


class InterviewPreparer:
    # ----- Questions Generation ----- #
    @staticmethod
    def _generate_generation_prompt_template() -> str:
        return PromptTemplate(
            template=INTERVIEW_PREPARER_TEMPLATE,
            input_variables=[
                "job_title",
                "job_description",
                "job_duties",
                "job_type",
                "interview_mode",
                "number_of_questions",
            ],
            partial_variables={
                "format_instructions": INTERVIEW_QUESTIONS_OUTPUT_PARSER.get_format_instructions()
            },
        )

    @staticmethod
    def generate_questions(
        job_title: str,
        job_description: str,
        job_duties: str,
        job_type: str,
        interview_mode: str,
        number_of_questions: int,
        model: TogetherChatModel = TogetherChatModel.QWEN2_5_72B_INSTRUCT_TURBO,
    ) -> InterviewQuestions:
        # generate prompt
        prompt = InterviewPreparer._generate_generation_prompt_template().format(
            job_title=job_title,
            job_description=job_description,
            job_duties=job_duties,
            job_type=job_type,
            interview_mode=interview_mode,
            number_of_questions=number_of_questions,
        )

        # start inference
        response = TogetherInference.complete_chat(
            [
                Message(
                    role=Role.USER,
                    content=prompt,
                )
            ],
            model,
            max_tokens=750,
        )

        return INTERVIEW_QUESTIONS_OUTPUT_PARSER.parse(response)

    # ----- Evaluations ----- #
    @staticmethod
    def _generate_evaluation_prompt_template() -> str:
        return PromptTemplate(
            template=INTERVIEW_EVALUATION_TEMPLATE,
            input_variables=["question_answers"],
            partial_variables={
                "format_instructions": ANSWERS_EVALUATION_OUTPUT_PARSER.get_format_instructions()
            },
        )

    @staticmethod
    def evaluate_answers(
        answers: list[QuestionAndAnswer],
        model: TogetherChatModel = TogetherChatModel.QWEN2_5_72B_INSTRUCT_TURBO,
    ) -> AnswersEvaluation:
        # generate prompt
        prompt = InterviewPreparer._generate_evaluation_prompt_template().format(
            questions_answers=answers
        )

        # start inference
        response = TogetherInference.complete_chat(
            [
                Message(
                    role=Role.USER,
                    content=prompt,
                )
            ],
            model,
            max_tokens=1000,
        )

        return ANSWERS_EVALUATION_OUTPUT_PARSER.parse(response)
