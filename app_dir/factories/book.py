import factory
from faker import Factory
from ..core.loading import get_model
from app_dir.factories import AuthorFactory
faker = Factory.create()


class BookFactory(factory.DjangoModelFactory):
    class Meta:
        model = get_model('book', 'Book')

    title = factory.Faker('sentence', nb_words=4) # generate a 4 word sentence
    author = AuthorFactory.create() # Authorfactory create a new author and return new author id