import os
import numpy as np

dirname = os.path.dirname(os.path.abspath(__file__))
headline = os.path.join(dirname, 'hosking_headlines.txt')
comments = os.path.join(dirname, 'hosking_comments.txt')

with open('hosking_headlines.txt', 'r') as corpus:
    data=corpus.read().replace('\n', '')


def build_transition_matrix(corpus):
    corpus = corpus.split(' ')
    transitions = {}

    for k in range(0, len(corpus)):
        word = corpus[k]
        if k != len(corpus) - 1:  # Deal with the last word
            next_word = corpus[k + 1]
        else:
            next_word = corpus[0]  # loop back

        if word not in transitions:
            transitions[word] = []

        transitions[word].append(next_word)
    return transitions


def sample_headline(corpus, sentence_length, burn_in=1000):
    corpus = corpus
    sentence = []

    transitions = build_transition_matrix(corpus)

    # make a sentence 50 words long
    # we sample the sentence after running through the chain 1000 times
    current_word = np.random.choice(corpus.split(' '), size=1)[0]
    for k in range(0, burn_in + sentence_length):
        # sample from the lists with an equal chance for each entry
        # this chooses a word with a correct probability distribution in the matrix
        current_word = np.random.choice(transitions[current_word], size=1)[0]

        if k >= burn_in:
            sentence.append(current_word)

    return ' '.join(sentence)


print(sample_headline(corpus, 50, 1000))
