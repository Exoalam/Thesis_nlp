from transformers import T5Tokenizer, T5ForConditionalGeneration
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from normalizer import normalize 

class Generatien:
    model_g = T5ForConditionalGeneration.from_pretrained("google/flan-t5-large")
    model_b_e = AutoModelForSeq2SeqLM.from_pretrained("csebuetnlp/banglat5_nmt_bn_en")
    model_e_b = AutoModelForSeq2SeqLM.from_pretrained("csebuetnlp/banglat5_nmt_en_bn")
    tokenizer_g = T5Tokenizer.from_pretrained("google/flan-t5-large")
    tokenizer_b_e = AutoTokenizer.from_pretrained("csebuetnlp/banglat5_nmt_bn_en", use_fast=False)
    tokenizer_e_b = AutoTokenizer.from_pretrained("csebuetnlp/banglat5_nmt_en_bn", use_fast=False)

    def generate_text(self, input_sentence):
        # Normalize and translate input sentence to English
        normalized_input = normalize(input_sentence)
        input_ids = self.tokenizer_b_e(normalized_input, return_tensors="pt").input_ids
        generated_tokens = self.model_b_e.generate(input_ids)
        decoded_tokens = self.tokenizer_b_e.batch_decode(generated_tokens, skip_special_tokens=True)[0]
        input_text = decoded_tokens
        
        # Generate text with model_g
        input_ids = self.tokenizer_g(input_text, return_tensors="pt").input_ids
        outputs = self.model_g.generate(input_ids, max_length=70)
        decoded_tokens = self.tokenizer_g.decode(outputs[0], skip_special_tokens=True)
        
        # Translate the generated text back to the original language
        normalized_output = normalize(decoded_tokens)
        input_ids = self.tokenizer_e_b(normalized_output, return_tensors="pt").input_ids
        generated_tokens = self.model_e_b.generate(input_ids)
        decoded_tokens = self.tokenizer_e_b.batch_decode(generated_tokens, skip_special_tokens=True)[0]
        
        return decoded_tokens

# Debugging: Print outputs at each step to diagnose
