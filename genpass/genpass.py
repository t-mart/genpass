import string
import itertools
import random

import click

def rand_string(pool, length):
    return "".join(random.choice(pool) for _ in range(length))

@click.command()
@click.option('-l', '--length', default=20, type=click.INT, help="the length "
              "of the generated password.")
@click.option('-t', '--types', 'example', default='aA0!',
              help="include characters like these in the character pool. for "
              "example 'a1?' includes the lower case letters, digits and "
              "punctuation. make sure to escape any punctuation that has "
              "special shell meaning.")
@click.option('-e', '--exclude', default="", help="remove these characters"
              "from the character pool.")
@click.option('-p', '--only-punct', default="", help="if punctuation is "
              "is in the character pool, only use the punctuation defined by "
              "this option." "useful when requirements allow only certain "
              "punctuation.")
@click.option('-r', '--repeat', default=False, help="print an appropriate "
              "password repeatedly after Enter is pressed. Ctrl-C to exit. good"
              "for scanning through many passwords.")
def genpass(length, example, exclude, only_punct, repeat):
    punct = only_punct if only_punct else string.punctuation
    types = {string.ascii_lowercase,
             string.ascii_uppercase,
             string.digits,
             punct}
    selected = set()
    for char in example:
        for type in types:
            if char in type:
                selected = selected.union(type)
                break
        else:
            raise click.ClickException("unrecognized character '%s'" %
                                       (char))
    pool = []
    for chars in types:
        for char in chars:
            pool.append(char)
    pool = set(pool)

    for exclusion in exclude:
        pool = pool - {exclusion}

    pool = list(pool)

    if repeat:
        try:
            while True:
                click.echo(rand_string(pool, length))
                input()
        except KeyboardInterrupt:
            click.abort()
    else:
        click.echo(rand_string(pool, length))

