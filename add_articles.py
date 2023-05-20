from session import session
from models import Author, Article
from faker import Faker


def main():
    author = session.query(Author).get(4)

    fake = Faker()
    article = Article(
        title=fake.sentence(),
        content="New article content"
    )

    author.articles.append(article)
    session.commit()


if __name__ == "__main__":
    main()
