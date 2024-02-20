from transformers import GPT2Tokenizer
import torch
tokenizer = GPT2Tokenizer.from_pretrained("NEO",  unk_token="[UNK]")
from transformers import AutoModelForCausalLM
# tokenizer.add_special_tokens({
#     "eos_token": "</s>",
#     "bos_token": "<s>",
#     "unk_token": "<unk>",
#     "pad_token": "<pad>",
#     "mask_token": "<mask>",
# })

# config = GPT2Config()
# model = GPT2LMHeadModel(config)
# model.resize_token_embeddings(len(tokenizer))
# state_dict = torch.load('saved_model/weight.bin', map_location='cpu' if not torch.cuda.is_available() else None)
# model = load_weight(model, state_dict)
# model.eval()
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

class Generator:
    def __init__(self, model_name_or_path="NEO_old"):
        self.model = AutoModelForCausalLM.from_pretrained(model_name_or_path)
        # It's important to resize token embeddings when you've added new tokens to the tokenizer.
        #self.model.resize_token_embeddings(len(tokenizer))
        
        # Device configuration
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model.to(self.device)
    
    def generate_text(self, question, max_length=128):
        input_ids = tokenizer.encode(question, return_tensors='pt').to(self.device)
        
        # Generate text with a safeguard for the maximum length
        with torch.no_grad():
            outputs = self.model.generate(input_ids, max_length=max_length, eos_token_id=tokenizer.eos_token_id)
        
        # Decode the generated tokens to text
        generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
        return generated_text

    