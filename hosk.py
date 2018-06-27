import numpy as np
import string as st

class Bot:
    def __init__(self,
                 documents,
                 max_document_length = 1000,
                 burn_in = 250,):
        self._documents = documents
        self._corpus = {}
        self._max_sentence_length = max_document_length
        self._burn_in = burn_in

    def _line_to_array(self, line):
        if len(line) < 1:
            return [], False
        line = line.strip()
        line = line.split()
        return line, True

    def _add_to_corpus(self, parsed, key, k, next_key):
        if next_key is None:
            addition = 2
        else:
            addition = 0

        word = parsed[k + addition]

        if key in self._corpus:
            self._corpus[key].append(word)
        else:
            self._corpus[key] = [word]

    def _load_data(self):
        next_key = None
        for doc in self._documents:
            with open(doc, "r") as f:
                for line in f.readlines():
                    parsed, add = self._line_to_array(line)
                    if add:
                        if next_key is None:
                            a = -2
                        else:
                            a = 0
                        for k in range(0, (len(parsed) + a)):
                            if next_key is not None:
                                key = next_key
                                next_key = (next_key[1], parsed[k])
                            else:
                                key = (parsed[k], parsed[k + 1])

                            self._add_to_corpus(parsed, key, k, next_key)
                        if k == len(parsed) - 3 and next_key is None:
                            next_key = (parsed[k + 1], parsed[k + 2])
        self.last_key = next_key

    def _generate_text(self, size=10000):
        size += self._burn_in # for a burn of 250 words
        start_word = self._grab_two_random_words()
        text = ['']*size
        cap = [False]*size
        cap[0] = True
        text[0] = start_word[0]
        text[1] = start_word[1]

        punc = set(st.punctuation)

        # create sample
        i = 2
        while i < size:
            if any ([True if k in punc and k != ',' else False for k in text[i-1]]):
                cap[i] = True
            key = (text[i-2], text[i-1])
            if key == self.last_key:
                # restart if last key is chosen
                new_key = self._grab_two_random_words()
                text[i] = new_key[0]
                if i+1 < size:
                    text[i+1] = new_key[1]
                key = new_key
                i+=2
            choice = np.random.choice(self._corpus[key])
            if i < size:
                text[i] = choice
                i += 1

        # capitalise

        for k in range(0, size):
            if cap[k]:
                text[k] = text[k].capitalize()

            if k == size-1:
                if not any([True if j in punc and j != '\'' else False for j in text[k]]):
                    text[k] =  text[k] + '.'

        # find the first period after burn in
        for first_period in range(self._burn_in, size):
            if '.' in text[first_period]:
                break

        return ' '.join(text[(first_period+1):]).strip()

    def _grab_two_random_words(self):
        start = np.random.randint(0, len(self._corpus))
        start_word = list(self._corpus.keys())[start]
        return start_word

    def _get_headline(self):
        headline = ''
        while headline == '':
            num_words = np.random.randint(2, self._max_sentence_length)
            temp = self._generate_text(num_words).split(".")

            k = 0
            for k in range(0, len(temp)):
                if len(temp[k]) > 20:
                    break

            for i in range(len(temp), -1, -1):
                pos_headline = '.'.join(temp[k:(i + 1)])
                if len(pos_headline) < 50 and len(temp) > 20:
                    headline = pos_headline + "."
                    break

        return headline.strip().replace("\"","")

    def run(self):
        self._load_data()
        headline = self._get_headline()
        print("Mike Hosking: %s".format(headline))

def main():

    documents = ["hosking_headlines.txt"]
    bot = Bot(documents)

    bot.run()

if __name__ == "__main__":
    main()