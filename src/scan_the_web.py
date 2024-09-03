import wikipedia
from langdetect import detect


def get_random_text_content(target_language, num_attempts=10):
    """
    Récupère le contenu textuel d'un article Wikipedia aléatoire dans la langue cible.

    Args:
    target_language (str): Code de langue cible (ex: 'fr' pour français)
    num_attempts (int): Nombre maximal de tentatives pour trouver un article dans la langue cible

    Returns:
    str: Contenu textuel de l'article dans la langue cible, ou None si aucun article trouvé
    """
    wikipedia.set_lang(target_language)

    for _ in range(num_attempts):
        try:
            random_page = wikipedia.random(1)
            page_content = wikipedia.page(random_page).content

            if detect(page_content) == target_language:
                return page_content
        except Exception as e:
            print(f"Erreur lors de la récupération du contenu: {e}")

    return None


# Exemple d'utilisation
french_content = get_random_text_content("fr")
if french_content:
    print("Contenu en français trouvé:", french_content[:200] + "...")
else:
    print("Aucun contenu en français trouvé après plusieurs tentatives.")
