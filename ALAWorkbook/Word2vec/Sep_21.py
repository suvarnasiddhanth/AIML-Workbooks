tag_list = ["research", "innovation", "education", "university", "students", "faculty", "campus", "engineering", "medicine", "technology", "curriculum", "collaboration", "publication", "laboratory", "scholarship", "mentorship", "internship", "entrepreneurship", "sololeveling", "higher education"]
from builtins import Exception
import os
import numpy as np
from gensim.models import KeyedVectors

def load_model(word2vec_model_path:str) -> KeyedVectors:
    try:
        fast_model_path = os.path.expanduser(word2vec_model_path)
        return KeyedVectors.load(fast_model_path, mmap='r')
    except Exception as e:
        print(f"Failed to load model in word2vec format: {e}")
    return None

def get_word_vector_single(model, word:str):
    try:
        v = model[word]
        assert len(v) == 50
        return v
    except KeyError:
        print(f"Word '{word}' not in the model vocabulary.")
    return None

def get_word_vector_multiple(model, word:str):
    try:
        mult_word = word.split()
        word_size = len(mult_word)
        mult_word_vec = []
        for i in mult_word:
            v = model[i]
            assert len(v) == 50
            mult_word_vec.append(v)
        return np.sum(mult_word_vec)/word_size
    except KeyError:
        print(f"Word '{word}' not in the model vocabulary.")
    return None

def main():
    word2vec_model_path = "./glove50/glove_50_fast.wordvectors"
    model = load_model(word2vec_model_path)
    assert model is not None, "Model loading failed."
    tag_vec = []
    error_tag = []
    for t in tag_list:
        v_temp = get_word_vector_multiple(model, t) if any(char.isspace() for char in t) else get_word_vector_single(model,t)
        tag_vec.append(v_temp)
        if v_temp is None: error_tag.append(t)
    print(error_tag)
    print(len(tag_vec))

if __name__ == "__main__":
    main()
