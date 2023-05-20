from session import session
from models import Author, Article
from faker import Faker


def main():
    author = session.query(Author).filter_by(
        user_name="sammy"
    ).one()

    fake = Faker()
    article = Article(
        title=fake.sentence(),
        content="New article content"
    )

    author.articles.append(article)
    session.commit()


if __name__ == "__main__":
    main()
