from typing import Dict
import re
from collections import Counter
from n_gram_counter import count_ngrams
from scan_the_web import get_random_wikipedia_articles


def compute_difficulty(text: str, n: int, num_articles: int) -> Dict[int, float]:
    """
    Computes the difficulty of a given text based on n-gram statistics from Wikipedia articles.

    Args:
        text (str): The input text to analyze
        n (int): The maximum size of n-grams to consider
        num_articles (int): The number of Wikipedia articles to use for statistics

    Returns:
        Dict[int, float]: A dictionary mapping k (1 to n) to the difficulty score for k-grams
    """
    # Generate statistics for each k from 1 to n
    stats = {}
    for k in range(1, n + 1):
        articles_gen = get_random_wikipedia_articles("fr", num_articles)
        stats[k] = count_ngrams(articles_gen, k, threshold=0.0)

    # Compute difficulty scores for the input text
    difficulty_scores = {}
    words = re.findall(r"\b\w+\b", text.lower())

    for k in range(1, n + 1):
        text_ngrams = [" ".join(words[i : i + k]) for i in range(len(words) - k + 1)]
        ngram_counts = Counter(text_ngrams)

        difficulty_score = sum(
            count * stats[k].get(ngram, 0) for ngram, count in ngram_counts.items()
        )
        difficulty_scores[k] = difficulty_score

    return difficulty_scores


if __name__ == "__main__":
    sample_text = "Ceci est un exemple de texte en français pour tester la fonction de calcul de difficulté."
    difficulty = compute_difficulty(sample_text, n=3, num_articles=100)
    print("Difficulty scores:")
    for k, score in difficulty.items():
        print(f"{k}-grams: {score}")
