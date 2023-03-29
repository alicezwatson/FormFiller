from faker import Faker
from random import choice

fake = Faker()


def make_email(uname):
    sep = choice(['', '-', '_', '.'])
    uname = sep.join(uname.lower().split(' '))
    dom = fake.free_email_domain()

    return '@'.join([uname, dom])


def make_phone(area_codes=None):

    if area_codes:
        area_code = choice(area_codes)

    else:
        area_code = str(fake.pyint(min_value=200, max_value=790))

    prefix = str(fake.pyint(min_value=200, max_value=999))
    suffix = str(fake.pyint(min_value=1000, max_value=9999))
    sep = choice(['', ' ', '-', '.'])
    phone = sep.join([area_code, prefix, suffix])

    return phone


def make_address(cities=None, post_codes=None, states=None):

    street_address = fake.street_address()

    if cities:
        city = choice(cities)

    else:
        city = fake.city()

    if post_codes:
        post_code = str(choice(post_codes))

    else:
        post_code = fake.postcode()

    if states:
        state = choice(states)

    else:
        state = 'MO'

    return f"{street_address}\n{city} {state}, {post_code}"


if __name__ == '__main__':

    area_codes = ['314', '417', '573', '636', '660', '816']  # Missouri area codes

    cities = [
        'Kansas City', 'St. Louis', 'Springfield', 'Columbia', 'Independence',
        'St. Joseph', 'Joplin', 'Jefferson City', 'St. Charles', "O'Fallon"
    ]  # Missouri cities

    post_codes = [
        63001, 63002, 63003, 63004, 63005, 63006, 63007, 63008, 63009, 63010, 63011, 63012,
        63013, 63014, 63015, 63016, 63017, 63018, 63019, 63020, 63021, 63022, 63023, 63024,
        63025, 63026, 63027, 63028, 63029, 63030, 63031, 63032, 63033, 63034, 63035, 63036,
        63037, 63038, 63039, 63040, 63041, 63042, 63043, 63044, 63045, 63046, 63047, 63048,
        63049, 63050
    ]  # Missouri post codes

    quit = False

    while not quit:
        name = fake.name()
        address = make_address(cities=cities, post_codes=post_codes, states=['MO'])
        email = make_email(name)
        phone = make_phone(area_codes=area_codes)

        print(f"{name}\n{email}\n{phone}\n{address}\n")

        quit = input('Continue? [Y/n] ') == 'n'
