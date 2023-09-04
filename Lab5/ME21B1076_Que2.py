import numpy as np
from sklearn.feature_extraction.text import CountVectorizer

def file_text(Path):
    with open(Path, 'r') as f:
        text = f.read()
    return text

def cosine_similarity(vec1, vec2):
    # Calculate cosine similarity
    dot_product = np.dot(vec1, vec2)
    norm1 = np.linalg.norm(vec1)
    norm2 = np.linalg.norm(vec2)
    similarity = dot_product / (norm1 * norm2)
    return similarity

doc1 = file_text('Lab5\doc1.txt')
doc2 = file_text('Lab5\doc2.txt')

wrds1 = doc1.split()
wrds2 = doc2.split()

Vectorizer = CountVectorizer()
X = Vectorizer.fit_transform([doc1, doc2])

vec1 = X.toarray()[0]
vec2 = X.toarray()[1]

sim_score = cosine_similarity(vec1, vec2)

print("Cosine similarity between the documents are ", sim_score)