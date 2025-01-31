from enum import Enum

class TogetherChatModel(Enum):
    LLAMA_3_2_11B_VISION_INSTRUCT_TURBO = (
        "meta-llama/Llama-3.2-11B-Vision-Instruct-Turbo"  # * 0.18 $ / 1M tokens
    )
    LLAMA_3_2_90B_VISION_INSTRUCT_TURBO = (
        "meta-llama/Llama-3.2-90B-Vision-Instruct-Turbo"  # * 1.20 $ / 1M tokens
    )
    QWEN2_5_72B_INSTRUCT_TURBO = (
        "Qwen/Qwen2.5-72B-Instruct-Turbo"  # * 1.20 $ / 1M tokens
    )
    QWEN2_5_7B_INSTRUCT_TURBO = "Qwen/Qwen2.5-7B-Instruct-Turbo"  # * 0.30 $ / 1M tokens
    Mixtral_8x22B_INSTRUCT_v0_1 = (
        "mistralai/Mixtral-8x22B-Instruct-v0.1"  # * 1.20 $ / 1M tokens
    )
    WIZARD_LM_2_8x22B = "microsoft/WizardLM-2-8x22B"  # * 1.20 $ / 1M tokens
    DDEPSEEK_67B = "deepseek-ai/deepseek-llm-67b-chat"  # * 0.90 $ / 1M tokens
    DDEPSEEK_V3 = "deepseek-ai/DeepSeek-V3"  # * 1.25 $ / 1M tokens
    META_LLAMA_3_1_405B = "meta-llama/Llama-3.1-405B-Instruct" # * 3.50 $ / 1M tokens
    META_LLAMA_3_1_70B = "meta-llama/Meta-Llama-3.1-70B-Instruct" # * 0.88 $ / 1M tokens
    SOLAR_10_7B_INSTRUCT = "upstage/SOLAR-10.7B-Instruct-v1.0" # * 0.30 $ / 1M tokens


class TogetherCompletionModel(Enum):
    MIXTRAL_8_7B_V0_1 = "mistralai/Mixtral-8x7B-v0.1"  # * 0.60 $ / 1M tokens
    LLAMA_2_70B = "meta-llama/Llama-2-70b-hf"  # * 0.90 $ / 1M tokens
