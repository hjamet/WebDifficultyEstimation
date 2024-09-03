import wikipedia
from typing import Set
from tqdm import tqdm
import logging
from utils.logger import configure_logger

configure_logger()
logger = logging.getLogger(__name__)


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

    with tqdm(
        total=num_articles, desc=f"Retrieving {target_language} Wikipedia articles"
    ) as pbar:
        while len(articles) < num_articles:
            remaining = num_articles - len(articles)
            random_titles = wikipedia.random(remaining)

            for title in random_titles:
                if len(articles) >= num_articles:
                    break
                try:
                    page_content = wikipedia.page(title).content
                    if page_content not in articles:
                        articles.add(page_content)
                        pbar.update(1)
                except Exception as e:
                    logger.error(f"Error retrieving content for {title}: {str(e)}")

    logger.info(f"Number of articles retrieved: {len(articles)}")
    return articles


if __name__ == "__main__":
    articles = get_random_wikipedia_articles("fr", 10)
    print(articles)
