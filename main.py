from translator import Translator
import wikipediaapi

def get_wikipedia_article(title, language='ru'):
    wiki = wikipediaapi.Wikipedia(
        language=language,
        extract_format=wikipediaapi.ExtractFormat.WIKI,
        user_agent='TranslationApp/1.0'
    )
    
    page = wiki.page(title)
    
    if page.exists():
        print(f"Статья найдена: {page.title}")
        print(f"Количество символов: {len(page.text)}")
        return page.text
    else:
        print(f"Статья '{title}' не найдена")
        return None

article_text = get_wikipedia_article("Россия")

trans = Translator(article_text, 500)

print("Чанки:")
for i, chunk in enumerate(trans.get_chunks()):
    print(f"Чанк {i+1}: {chunk[:100]}...")

translated_text = trans.translate_to("English")
print("\nПереведенный текст:")
print(translated_text)