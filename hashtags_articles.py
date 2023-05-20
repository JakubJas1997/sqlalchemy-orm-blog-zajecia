from session import session
from models import Hashtag, Article


def main():
    hashtag = session.query(Hashtag).get(1)
    print(f"Articles with #{hashtag.name}:")
    for article in hashtag.articles:
        print(article.title)

    print("-" * 20)
    for article in session.query(Article):
        print(article.title)
        for hashtag in article.hashtags:
            print(f"  #{hashtag.name}")


if __name__ == "__main__":
    main()
