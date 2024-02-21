class Tokenizer:
    def load_tokens(filename):
        with open(filename, "r", encoding="utf-8") as f:
            tokens = [line.strip() for line in f]
        # Sort tokens by length in descending order to prioritize longer tokens during matching
        tokens.sort(key=len, reverse=True)
        return tokens

    def tokenize_text(self, text, tokens=load_tokens("tokens.txt")):
        # Initialize an empty list to hold the tokenized text
        tokenized_text = []
        # Scan through the text, attempting to match the longest tokens first
        while text:
            match = None
            for token in tokens:
                if text.startswith(token):
                    match = token
                    break
            if match:
                tokenized_text.append(match)
                text = text[len(match):]  # Move past the matched token
            else:
                tokenized_text.append(text[0])  # No match found, default to the first character
                text = text[1:]  # Move past the unmatched character
        return tokenized_text
