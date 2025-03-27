# from inspect import signature
from random import randint
 
from faker import Faker
 
def rand_ratio():
     return randint(840, 900), randint(473, 573)
 
 
fake = Faker('pt_BR')
 # print(signature(fake.random_number))
 
 
def make_permission():
     return {
         'i': fake.random_number(digits=1, fix_len=True),
         'id': fake.random_number(digits=2, fix_len=True),
         'location': fake.text(50),
         'description': fake.text(70),
         'order': fake.sentence(nb_words=2),
         'author': {
             'first_name': fake.first_name(),
             'last_name': fake.last_name(),
         },
         'date_today': fake.date_time(),
         'reason': fake.sentence(nb_words=2),
         'date_start': fake.date_time().strftime('%Y-%m-%d %H:%M:%S'),
         'date_end': fake.date_time().strftime('%Y-%m-%d %H:%M:%S'),
     }
 
 
if __name__ == '__main__':
     from pprint import pprint
     pprint(make_permission())