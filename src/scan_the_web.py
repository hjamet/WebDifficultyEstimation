import wikipedia
from typing import Set


def get_random_wikipedia_articles(
    target_language: str, num_articles: int = 1000
) -> Set[str]:
    """
    Retrieves the text content of random Wikipedia articles in the target language.

    Args:
        target_language (str): Target language code (e.g., 'fr' for French)
        num_articles (int): Number of articles to retrieve

    Returns:
        Set[str]: Set of text contents of articles in the target language
    """
    wikipedia.set_lang(target_language)
    articles = set()

    while len(articles) < num_articles:
        remaining = num_articles - len(articles)
        random_titles = wikipedia.random(remaining)

        for title in random_titles:
            try:
                page_content = wikipedia.page(title).content
                articles.add(page_content)
            except Exception as e:
                print(f"Error retrieving content for {title}: {e}")

    return articles


if __name__ == "__main__":
    articles = get_random_wikipedia_articles("fr", 1000)
    print(f"Number of articles retrieved: {len(articles)}")
