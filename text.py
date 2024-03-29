from transformers import T5Tokenizer, T5ForConditionalGeneration
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from normalizer import normalize 
import openai

class Generatien:
    openai.api_key = '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'
    model_b_e = AutoModelForSeq2SeqLM.from_pretrained("csebuetnlp/banglat5_nmt_bn_en")
    model_e_b = AutoModelForSeq2SeqLM.from_pretrained("csebuetnlp/banglat5_nmt_en_bn")
    tokenizer_b_e = AutoTokenizer.from_pretrained("csebuetnlp/banglat5_nmt_bn_en", use_fast=False)
    tokenizer_e_b = AutoTokenizer.from_pretrained("csebuetnlp/banglat5_nmt_en_bn", use_fast=False)

    def generate_text(self, input_sentence):
        input_ids = self.tokenizer_b_e(normalize(input_sentence), return_tensors="pt").input_ids
        generated_tokens = self.model_b_e.generate(input_ids)
        decoded_tokens = self.tokenizer_b_e.batch_decode(generated_tokens, skip_special_tokens=True)[0]
        input_variable = decoded_tokens
        completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a friendly and knowledgeable chatbot who enjoys explaining complex topics in an easy-to-understand manner."},
            {"role": "user", "content": input_variable}
        ],
        max_tokens=20
        )
        decoded_tokens = completion.choices[0].message["content"]
        input_sentence = decoded_tokens
        input_ids = self.tokenizer_e_b(normalize(input_sentence), return_tensors="pt").input_ids
        generated_tokens = self.model_e_b.generate(input_ids)
        decoded_tokens = self.tokenizer_e_b.batch_decode(generated_tokens, skip_special_tokens=True)[0]
        return decoded_tokens
