"""Core Python analysis for Project 01.

Paths are intentionally relative so the project can be moved between machines.
The original MSc notebook remains in notebooks/ for full provenance.
"""
from pathlib import Path
import re
import pandas as pd
from gensim import corpora, models
from gensim.models.coherencemodel import CoherenceModel

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"

CUSTOM_STOPWORDS = {
    "covid", "coronavirus", "covidtesting", "covidpandemic", "covidvaccine",
    "covidupdate", "coronavirusupdates", "coronaviruspandemic", "covid19",
    "covid_19", "link", "https", "bio", "india", "pandemic", "update"
}


def preprocess(text, stop_words):
    tokens = re.findall(r"\b[a-z]{3,}\b", str(text).lower())
    return [word for word in tokens if word not in stop_words]


def load_translated_data(path):
    df = pd.read_csv(path)
    df = df.dropna(subset=["post"]).copy()
    return df


def select_topic_model(tokens, dictionary, corpus, min_topics=2, max_topics=10):
    scores = []
    for k in range(min_topics, max_topics + 1):
        model = models.LdaModel(
            corpus=corpus,
            id2word=dictionary,
            num_topics=k,
            random_state=123,
            update_every=1,
            passes=10,
            per_word_topics=True,
        )
        coherence = CoherenceModel(
            model=model, texts=tokens, dictionary=dictionary, coherence="c_v"
        ).get_coherence()
        scores.append((k, coherence))
    return scores


def fit_three_topic_model(df):
    stop_words = set(__import__("nltk").corpus.stopwords.words("english")) | CUSTOM_STOPWORDS
    df = df.copy()
    df["tokens"] = df["post"].apply(lambda x: preprocess(x, stop_words))
    dictionary = corpora.Dictionary(df["tokens"])
    corpus = [dictionary.doc2bow(tokens) for tokens in df["tokens"]]
    model = models.LdaModel(
        corpus=corpus,
        id2word=dictionary,
        num_topics=3,
        random_state=123,
        passes=10,
        per_word_topics=True,
    )
    return model, dictionary, corpus, df


if __name__ == "__main__":
    print("Use the original notebook in notebooks/ for the full MSc workflow.")
