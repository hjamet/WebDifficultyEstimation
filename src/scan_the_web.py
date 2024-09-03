import requests
from bs4 import BeautifulSoup
from langdetect import detect
import random


def get_random_text_content(target_language, num_attempts=10):
    """
    Récupère le contenu textuel d'un site aléatoire dans la langue cible.

    Args:
    target_language (str): Code de langue cible (ex: 'fr' pour français)
    num_attempts (int): Nombre maximal de tentatives pour trouver un site dans la langue cible

    Returns:
    str: Contenu textuel du site dans la langue cible, ou None si aucun site trouvé
    """
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
    ]

    for _ in range(num_attempts):
        try:
            # Générer une URL aléatoire
            random_url = f"http://random.host/{random.randint(1, 1000000)}"

            # Envoyer une requête GET avec un User-Agent aléatoire
            headers = {"User-Agent": random.choice(user_agents)}
            response = requests.get(random_url, headers=headers, timeout=5)
            response.raise_for_status()

            # Parser le contenu HTML
            soup = BeautifulSoup(response.text, "html.parser")

            # Extraire le texte
            text_content = " ".join([p.get_text() for p in soup.find_all("p")])

            # Détecter la langue
            if detect(text_content) == target_language:
                return text_content
        except Exception as e:
            print(f"Erreur lors de la récupération du contenu: {e}")

    return None


# Exemple d'utilisation
french_content = get_random_text_content("fr")
if french_content:
    print("Contenu en français trouvé:", french_content[:200] + "...")
else:
    print("Aucun contenu en français trouvé après plusieurs tentatives.")
