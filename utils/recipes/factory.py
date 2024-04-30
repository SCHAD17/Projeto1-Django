from random import randint
from faker import Faker

def rand_ratio():
    return randint(840, 900), randint(473, 573)

fake = Faker('pt_BR')

def make_recipe():
    return {
        'title': fake.sentence(nb_words=6), # type: ignore
        'description': fake.sentence(nb_words=12), # type: ignore
        'preparation_time': fake.random_number(digits=2, fix_len=True), # type: ignore
        'preparation_time_unit': 'Minutos',
        'servings': fake.random_number(digits=2, fix_len=True), # type: ignore
        'servings_unit': 'Porção',
        'preparation_steps': fake.text(3000), # type: ignore
        'author': {
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
        },
        'category': {
            'name': fake.word()
        },
        'cover': {
            'url': 'https://loremflickr.com/%s/%s/food,cook' % rand_ratio(),
        }
    }

if __name__ == '__main__':
    from pprint import pprint
    pprint(make_recipe())