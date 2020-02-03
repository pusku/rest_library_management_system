import factory
from faker import Factory
from ..core.loading import get_model

faker = Factory.create()


class AuthorFactory(factory.DjangoModelFactory):
    class Meta:
        model = get_model('author', 'Author')

    name = faker.name()