import string

from nlpaug.util import Method
from nlpaug import Augmenter
from nlpaug.util import WarningException, WarningName, WarningCode, WarningMessage


class WordAugmenter(Augmenter):
    def __init__(self, action, name='Word_Aug', aug_min=1, aug_max=10, aug_p=0.3, stopwords=None,
                 tokenizer=None, reverse_tokenizer=None, device='cpu', verbose=0):
        super().__init__(
            name=name, method=Method.WORD, action=action, aug_min=aug_min, aug_max=aug_max, device=device,
            verbose=verbose)
        self.aug_p = aug_p
        self.tokenizer = tokenizer or self._tokenizer
        self.reverse_tokenizer = reverse_tokenizer or self._reverse_tokenizer
        self.stopwords = stopwords

    @classmethod
    def _tokenizer(cls, text):
        return [t for t in text.split(' ') if len(t) > 0]
        # return text.split(' ')

    @classmethod
    def _reverse_tokenizer(cls, tokens):
        return ' '.join(tokens)

    @classmethod
    def clean(cls, data):
        return data.strip()

    def skip_aug(self, token_idxes, tokens):
        return token_idxes

    def pre_skip_aug(self, tokens, tuple_idx=None):
        results = []
        for token_idx, token in enumerate(tokens):
            if tuple_idx is not None:
                _token = token[tuple_idx]
            else:
                _token = token
            # skip punctuation
            if _token in string.punctuation:
                continue
            # skip stopwords
            if self.stopwords is not None and _token in self.stopwords:
                continue

            results.append(token_idx)

        return results

    @classmethod
    def is_duplicate(cls, dataset, data):
        for d in dataset:
            if d == data:
                return True
        return False

    @classmethod
    def align_capitalization(cls, src_token, dest_token):
        # For whole word is upper case
        if src_token.isupper():
            return dest_token.upper()
        # For capitalize word
        elif src_token and src_token[0].isupper():
            return dest_token.capitalize()
        else:
            return dest_token

    def _get_aug_idxes(self, tokens):
        aug_cnt = self.generate_aug_cnt(len(tokens))
        word_idxes = self.pre_skip_aug(tokens)
        word_idxes = self.skip_aug(word_idxes, tokens)
        if len(word_idxes) == 0:
            if self.verbose > 0:
                exception = WarningException(name=WarningName.OUT_OF_VOCABULARY,
                                             code=WarningCode.WARNING_CODE_002, msg=WarningMessage.NO_WORD)
                exception.output()
            return []
        if len(word_idxes) < aug_cnt:
            aug_cnt = len(word_idxes)
        aug_idexes = self.sample(word_idxes, aug_cnt)
        return aug_idexes

    def _get_random_aug_idxes(self, tokens):
        aug_cnt = self.generate_aug_cnt(len(tokens))
        word_idxes = self.pre_skip_aug(tokens)
        if len(word_idxes) < aug_cnt:
            aug_cnt = len(word_idxes)

        aug_idxes = self.sample(word_idxes, aug_cnt)

        return aug_idxes
