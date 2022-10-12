from collections import defaultdict

class Dictionary:
    def __init__(self, doc=None):
        self.vocab_size = 0
        self.idx2word = defaultdict(str)
        self.word2idx = defaultdict(int)
        self.update(doc)

    def update(self, doc: list):
        if doc is None:
            return
        vocab_size, word2idx, idx2word = self.vocab_size, self.word2idx, self.idx2word
        tokens = set()
        for line in doc:
            tokens.update(line)
        for token in tokens:
            if token not in word2idx:
                word2idx[token] = vocab_size
                idx2word[vocab_size] = token
                vocab_size += 1
        self.vocab_size = vocab_size

    def corpus(self, doc: list) -> list:
        word2idx = self.word2idx
        return [[word2idx[word] for word in line if word in word2idx] for line in doc]