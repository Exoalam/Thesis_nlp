# import csv

# # Path to your CSV file
# csv_file_path = 'complete_dataset.csv'
# # The column name you want to extract
# column_name = 'answer_translated'
# # Variable to hold the concatenated string


# # Open the CSV file for reading
# with open(csv_file_path, mode='r', encoding='utf-8') as csvfile:
#     # Create a DictReader to read the CSV
#     reader = csv.DictReader(csvfile)
    
#     # Iterate over the rows in the CSV
#     for row in reader:
#         # Extract the desired column's value and append it to the string
#         concatenated_string += row[column_name] + ' '  # Adding a space for separation

# # Print or use the concatenated string

class Tokenzier:
    def get_stats(self,vocab):
        pairs = {}
        for word, freq in vocab.items():
            symbols = word.split()
            for i in range(len(symbols) - 1):
                pair = (symbols[i], symbols[i + 1])
                if pair in pairs:
                    pairs[pair] += freq
                else:
                    pairs[pair] = freq
        return pairs

    def merge_vocab(self,pair, v_in):
        v_out = {}
        bigram = ' '.join(pair)
        replacement = ''.join(pair)
        for word in v_in:
            w_out = word.replace(bigram, replacement)
            v_out[w_out] = v_in[word]
        return v_out
        
    def byte_pair_encode_bangla(self,text, num_merges):
        vocab = {}
        for word in text.split():
            word = ' '.join(word) + ' </w>'  
            if word in vocab:
                vocab[word] += 1
            else:
                vocab[word] = 1
        
        for i in range(num_merges):
            pairs = self.get_stats(vocab)
            if not pairs:
                break
            best = max(pairs, key=pairs.get)
            vocab = self.merge_vocab(best, vocab)
        
        bpe_tokens = set()
        for word in vocab.keys():
            bpe_tokens.update(word.split())
        
        return bpe_tokens

# with open("dataset.txt") as f:
#     data = f.read()
#     data = concatenated_string
#     tokens = []
#     for i in range(100):
#         token = byte_pair_encode_bangla(data, i)
#         for x in token:
#             if x not in tokens:
#                 tokens.append(x)

#     text_file = open("token.txt", "w")
#     n = text_file.write(str(tokens))
#     text_file.close()