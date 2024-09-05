import re
from collections import Counter
from typing import Dict, Iterator
import os
import csv
from utils.git import get_repo_root

from scan_the_web import get_random_wikipedia_articles


def count_ngrams(
    articles_generator: Iterator[str], n: int, threshold: float = 0.0
) -> Dict[str, float]:
    """
    Counts n-grams from the articles generator and returns their proportions.
    Saves statistics every 10 articles.

    Args:
        articles_generator (Iterator[str]): Generator yielding article contents
        n (int): Size of n-grams to count
        threshold (float): Minimum proportion for an n-gram to be included in the output

    Returns:
        Dict[str, float]: Dictionary with n-grams as keys and their proportions as values
    """
    ngram_counter = Counter()
    total_ngrams = 0
    total_words = 0
    articles_processed = 0
    repo_root = get_repo_root()
    stats_file = os.path.join(repo_root, "scratch", f"stats_{n}.csv")

    for article in articles_generator:
        words = re.findall(r"\b\w+\b", article.lower())
        total_words += len(words)
        ngrams = [" ".join(words[i : i + n]) for i in range(len(words) - n + 1)]
        ngram_counter.update(ngrams)
        total_ngrams += len(ngrams)
        articles_processed += 1

        if articles_processed % 10 == 0:
            save_stats(ngram_counter, total_ngrams, total_words, threshold, stats_file)

    ngram_proportions = {
        ngram: count / total_ngrams
        for ngram, count in ngram_counter.items()
        if count / total_ngrams >= threshold
    }

    save_stats(ngram_counter, total_ngrams, total_words, threshold, stats_file)
    return ngram_proportions


def save_stats(
    ngram_counter: Counter,
    total_ngrams: int,
    total_words: int,
    threshold: float,
    file_path: str,
):
    """
    Saves current n-gram statistics to a CSV file with metadata.

    Args:
        ngram_counter (Counter): Counter object with n-gram counts
        total_ngrams (int): Total number of n-grams processed
        total_words (int): Total number of words processed
        threshold (float): Minimum proportion for an n-gram to be included
        file_path (str): Path to the CSV file
    """
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([f"# Total words processed: {total_words}"])
        writer.writerow([f"# Total n-grams processed: {total_ngrams}"])
        writer.writerow(["n-gram", "proportion"])
        for ngram, count in ngram_counter.items():
            proportion = count / total_ngrams
            if proportion >= threshold:
                writer.writerow([ngram, proportion])


if __name__ == "__main__":
    articles_gen = get_random_wikipedia_articles("fr", 10)
    ngram_stats = count_ngrams(articles_gen, n=1, threshold=0.001)
    print(ngram_stats)
