import factory
from faker import Factory
from ..core.loading import get_model
from app_dir.factories import AuthorFactory, UserFactory, BookFactory
from ...core.common import REQUEST_CHOICES, STATUS_CHOICES

faker = Factory.create()


class LoanFactory(factory.DjangoModelFactory):
    class Meta:
        model = get_model('loan', 'loan')

    request = factory.Faker('random_element', elements=[choice[0] for choice in REQUEST_CHOICES])
    status = factory.Faker('random_element', elements=[choice[0] for choice in STATUS_CHOICES])
    book = BookFactory.create() # BookFactory create a new book and return new author id
    user = UserFactory.create() # UserFactory create a new user and return new author id