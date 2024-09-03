import wikipedia
from typing import Set
from tqdm import tqdm
import logging
from utils.logger import configure_logger

configure_logger()
logger = logging.getLogger(__name__)


def get_random_wikipedia_articles(target_language: str, num_articles: int = 1000):
    """
    Yields text content of random Wikipedia articles in the target language.

    Args:
        target_language (str): Target language code (e.g., 'fr' for French)
        num_articles (int): Number of articles to retrieve

    Yields:
        str: Text content of an article in the target language
    """
    wikipedia.set_lang(target_language)
    articles_yielded = 0

    with tqdm(
        total=num_articles, desc=f"Retrieving {target_language} Wikipedia articles"
    ) as pbar:
        while articles_yielded < num_articles:
            random_titles = wikipedia.random(num_articles - articles_yielded)

            for title in random_titles:
                if articles_yielded >= num_articles:
                    break
                try:
                    page_content = wikipedia.page(title).content
                    yield page_content
                    articles_yielded += 1
                    pbar.update(1)
                except Exception as e:
                    logger.warning(f"Error retrieving content for {title}")

    logger.info(f"Number of articles retrieved: {articles_yielded}")


if __name__ == "__main__":
    articles = get_random_wikipedia_articles("fr", 10)
    print(len([article for article in articles]))
