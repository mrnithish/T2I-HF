from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM


class PromptEnhancer:
    def __init__(self, model_checkpoint="gokaygokay/Flux-Prompt-Enhance", device="cpu"):
        """Initialize the Prompt Enhancer class with model and tokenizer."""
        self.device = device
        self.tokenizer = AutoTokenizer.from_pretrained(model_checkpoint)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(model_checkpoint)
        self.enhancer = pipeline(
            'text2text-generation',
            model=self.model,
            tokenizer=self.tokenizer,
            repetition_penalty=1.2,
            device=0 if device == "cuda" else -1
        )
        self.prefix = "enhance Image prompt: "
        self.max_target_length = 256

    def enhance(self, short_prompt):
        """Enhance a short prompt into a detailed one."""
        input_text = self.prefix + short_prompt
        try:
            answer = self.enhancer(input_text, max_length=self.max_target_length)
            return answer[0]['generated_text']
        except Exception as e:
            raise RuntimeError(f"Error enhancing prompt: {e}")


