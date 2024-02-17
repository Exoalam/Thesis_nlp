from transformers import GPT2Tokenizer
import torch
tokenizer = GPT2Tokenizer.from_pretrained("vocab",  unk_token="[UNK]")
from transformers import AutoModelForCausalLM
tokenizer.add_special_tokens({
    "eos_token": "</s>",
    "bos_token": "<s>",
    "unk_token": "<unk>",
    "pad_token": "<pad>",
    "mask_token": "<mask>",
    'additional_special_tokens': ['Question:', 'Answer:']
})

# config = GPT2Config()
# model = GPT2LMHeadModel(config)
# model.resize_token_embeddings(len(tokenizer))
# state_dict = torch.load('saved_model/weight.bin', map_location='cpu' if not torch.cuda.is_available() else None)
# model = load_weight(model, state_dict)
# model.eval()
class Generator:
    model = AutoModelForCausalLM.from_pretrained("saved_model2")
    model.resize_token_embeddings(len(tokenizer))
    # Device configuration
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)

    # Encode input context
    #input_ids = tokenizer.encode("আপনি কেমন আছেন?", return_tensors='pt').to(device)
    # question = "ঢাকা বাংলাদেশ"
    def generate_text(self, question):
        #input_ids = tokenizer.encode("Question: " + question + " Answer:", return_tensors="pt").to(device)
        input_ids = tokenizer.encode(question, return_tensors='pt').to(self.device)
        # Generate text
        max_length = 128
        with torch.no_grad():
            while len(input_ids[0]) < max_length:
                outputs = self.model(input_ids)
                logits = outputs[0]  # Accessing the first element of the tuple for logits

            # Get the predicted next sub-word (greedy approach)
                predicted_id = torch.argmax(logits[:, -1, :], axis=-1)
                
                # Stop if end of sequence token is generated
                if predicted_id[0] == tokenizer.eos_token_id:
                    break

                # Append predicted token to the input sequence and continue
                input_ids = torch.cat([input_ids, predicted_id.unsqueeze(-1)], dim=-1)

        # Decode the generated tokens to text
        generated_text = tokenizer.decode(input_ids[0], skip_special_tokens=True)
        return generated_text
        # print("Generated Text:")
        # print(generated_text)
    