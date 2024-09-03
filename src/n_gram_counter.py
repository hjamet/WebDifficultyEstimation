import re
from collections import Counter
from typing import Dict, List

from scan_the_web import get_random_wikipedia_articles


def count_ngrams(
    articles: List[str], n: int, threshold: float = 0.0
) -> Dict[str, float]:
    """
    Counts n-grams in the given articles and returns their proportions.

    Args:
        articles (List[str]): List of article contents
        n (int): Size of n-grams to count
        threshold (float): Minimum proportion for an n-gram to be included in the output

    Returns:
        Dict[str, float]: Dictionary with n-grams as keys and their proportions as values
    """
    ngram_counter = Counter()
    total_ngrams = 0

    for article in articles:
        words = re.findall(r"\b\w+\b", article.lower())
        ngrams = [" ".join(words[i : i + n]) for i in range(len(words) - n + 1)]
        ngram_counter.update(ngrams)
        total_ngrams += len(ngrams)

    ngram_proportions = {
        ngram: count / total_ngrams
        for ngram, count in ngram_counter.items()
        if count / total_ngrams >= threshold
    }

    return ngram_proportions


if __name__ == "__main__":
    articles = get_random_wikipedia_articles("fr", 10)
    ngram_stats = count_ngrams(list(articles), n=1, threshold=0.001)
    print(ngram_stats)
