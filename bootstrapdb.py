import random

from faker import Faker
from sqlalchemy.exc import IntegrityError

from models import Base, Author, Article, Hashtag
from session import session


def generate_authors(session, count=50):
    fake = Faker()
    session.add_all([
        Author(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            user_name=fake.user_name(),
            email=fake.email(),
        )
        for _ in range(count)
    ])
    session.commit()


def generate_articles(session, count=10):
    fake = Faker()
    for author in session.query(Author):
        author.articles.extend([
            Article(
                title=fake.sentence(),
                content=fake.text(),
            )
            for _ in range(count)
        ])
    session.commit()


def generate_hashtags(session, count=10):
    fake = Faker()
    total_hashtags = 0
    while total_hashtags < count:
        hashtag = Hashtag(name=fake.word())
        try:
            session.add(hashtag)
            total_hashtags += 1
        except IntegrityError:
            session.rollback()


def assign_hashtags(session):
    all_hashtags = session.query(Hashtag).all()
    for article in session.query(Article):
        hashtags = random.choices(
            all_hashtags, k=random.randint(1, 5)
        )
        article.hashtags.extend(set(hashtags))
    session.commit()


def main():
    print("Creating database tables...")
    Base.metadata.create_all()

    print("Generating authors...")

    generate_authors(session)

    print("Generating articles...")
    generate_articles(session)

    print("Generating hashtags...")
    generate_hashtags(session)

    print("Assigning hashtags to articles...")
    assign_hashtags(session)

    print("Done!")


if __name__ == "__main__":
    main()
