from nlpaug.util import Method
from nlpaug import Augmenter
from nlpaug.util import WarningException, WarningName, WarningCode, WarningMessage


class CharAugmenter(Augmenter):
    def __init__(self, action, name='Char_Aug', min_char=2, aug_char_min=1, aug_char_max=10, aug_char_p=0.3,
                 aug_word_min=1, aug_word_max=10, aug_word_p=0.3, tokenizer=None, reverse_tokenizer=None,
                 stopwords=None, device='cpu', verbose=0):
        super().__init__(
            name=name, method=Method.CHAR, action=action, aug_min=None, aug_max=None, device=device, verbose=verbose)
        self.aug_p = None
        self.aug_char_min = aug_char_min
        self.aug_char_max = aug_char_max
        self.aug_char_p = aug_char_p
        self.aug_word_min = aug_word_min
        self.aug_word_max = aug_word_max
        self.aug_word_p = aug_word_p
        self.min_char = min_char

        self.tokenizer = tokenizer or self._tokenizer
        self.reverse_tokenizer = reverse_tokenizer or self._reverse_tokenizer
        self.stopwords = stopwords

    @classmethod
    def _tokenizer(cls, text):
        return text.split(' ')

    @classmethod
    def token2char(cls, word):
        return list(word)

    @classmethod
    def _reverse_tokenizer(cls, tokens):
        return ' '.join(tokens)

    @classmethod
    def clean(cls, data):
        return data.strip()

    @classmethod
    def is_duplicate(cls, dataset, data):
        for d in dataset:
            if d == data:
                return True
        return False

    def skip_aug(self, token_idxes, tokens):
        return token_idxes

    def _get_aug_idxes(self, tokens, aug_min, aug_max, aug_p, mode):
        if mode == Method.CHAR:
            # If word is too short, do not augment it.
            if len(tokens) < self.min_char:
                return None

        aug_cnt = self._generate_aug_cnt(len(tokens), aug_min, aug_max, aug_p)
        idxes = [i for i, t in enumerate(tokens)]
        if mode == Method.WORD:
            # skip stopwords
            idxes = [i for i in idxes if self.stopwords is None or tokens[i] not in self.stopwords]
            # skip short word
            idxes = [i for i in idxes if len(tokens[i]) >= self.min_char]

        elif mode == Method.CHAR:
            idxes = self.skip_aug(idxes, tokens)

        if len(idxes) == 0:
            if self.verbose > 0:
                exception = WarningException(name=WarningName.OUT_OF_VOCABULARY,
                                             code=WarningCode.WARNING_CODE_002, msg=WarningMessage.NO_WORD)
                exception.output()
            return None
        if len(idxes) < aug_cnt:
            aug_cnt = len(idxes)
        aug_idxes = self.sample(idxes, aug_cnt)
        return aug_idxes
