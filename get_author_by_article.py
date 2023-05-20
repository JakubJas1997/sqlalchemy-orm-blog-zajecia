from models import Article
from session import session


def main():
    article = session.query(Article).get(1)
    print(article, article.author)


if __name__ == "__main__":
    main()
