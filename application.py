from session import session
from models import Author


def main():
    for author in session.query(Author):
        for article in author.articles:
            print(author, article)


if __name__ == "__main__":
    main()
