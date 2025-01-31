from langchain.prompts import PromptTemplate
from langchain.output_parsers import PydanticOutputParser

from utils.together_ai.together_inference import TogetherChatModel, TogetherInference, Message, Role

from .models.cv_nfo import CvInfo
from .prompts.cv_info_extraction_template import CV_INFO_EXTRACTOR_TEMPLATE

# Output parser for CvInfo
CV_INFO_OUTPUT_PARSER = PydanticOutputParser(pydantic_object=CvInfo)


class CvInfoExtractor:
    @staticmethod
    def _generate_prompt_template() -> str:
        return PromptTemplate(
            template=CV_INFO_EXTRACTOR_TEMPLATE,
            input_variables=["cv_text"],
            partial_variables={
                "format_instructions": CV_INFO_OUTPUT_PARSER.get_format_instructions()
            },
        )

    @staticmethod
    def extract_info(
        cv_text: str,
        model: TogetherChatModel = TogetherChatModel.QWEN2_5_7B_INSTRUCT_TURBO,
    ) -> CvInfo:
        # generate prompt
        prompt = CvInfoExtractor._generate_prompt_template().format(cv_text=cv_text)

        # start inference
        response = TogetherInference.complete_chat(
            messages=[Message(role=Role.USER, content=prompt)],
            model=model,
            max_tokens=750,
            temperature=0
        )["choices"][0]["message"]["content"]

        return CV_INFO_OUTPUT_PARSER.parse(response)
