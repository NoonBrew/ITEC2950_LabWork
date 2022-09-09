from ast import excepthandler


def get_random_cat_and_pattern():
    return 'tiger', 'stripes' # returns a tuple

cat, pattern = get_random_cat_and_pattern()

data = get_random_cat_and_pattern()

try:
    print(data[10])
except:
    print('oops that does not exist.')