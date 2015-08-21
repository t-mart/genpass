import sys
import string
import itertools
import random
import enum

import click

from . import __version__

def rand_string(pool, length):
    return "".join(random.choice(pool) for _ in range(length))

@click.command()
@click.option('-l', '--length', default=20, type=click.INT, help="the length "
              "of the generated password.")
@click.option('-u', '--upper', default=False, is_flag=True, help="include "
              "upper case letters in the pool.")
@click.option('-l', '--lower', default=False, is_flag=True, help="include "
              "lower case letters in the pool.")
@click.option('-d', '--digit', default=False, is_flag=True, help="include "
              "digits in the pool.")
@click.option('-p', '--punct', default=False, is_flag=True, help="include "
              "punctuation in the pool.")
@click.option('-e', '--exclude', default="", help="exclude the characters set "
              "in this option from the pool.")
@click.option('-P', '--only-punct', default="", help="if punctuation is "
              "is in the character pool, only use the punctuation listed by "
              "this option. useful when requirements allow only certain "
              "punctuation. for example --only-punct #*%$")
@click.option('-r', '--repeat', default=False, is_flag=True, help="print an "
              "appropriate password repeatedly after Enter is pressed. Ctrl-C "
              "to exit. good for scanning through many passwords.")
@click.option('-v', '--version', default=False, is_flag=True, help="print "
              "the version and then quit")
def genpass(length, upper, lower, digit, punct, exclude, only_punct, repeat,
            version):
    if version:
        click.echo(__version__)
        sys.exit(0)

    classes = (upper, lower, digit, punct)
    pool = set()
    # add classes if present
    if upper:
        pool |= set(string.ascii_uppercase)
    if lower:
        pool |= set(string.ascii_lowercase)
    if digit:
        pool |= set(string.digits)
    if only_punct:
        # override punctuation
        pool |= set(only_punct)
    elif punct:
        pool |= set(string.punctuation)

    # if nothing added to pool explicitly, add everything
    if not pool:
        pool |= set(string.ascii_lowercase) | set(string.ascii_uppercase) | set(string.digits) | set(string.punctuation)

    # remove these if you see 'em.
    if exclude:
        pool -= set(exclude)

    pool = list(pool)

    if repeat == False:
        iterator = itertools.repeat("",1)
        click.echo(rand_string(pool, length), nl=True)
    else:
        for _ in itertools.repeat(""):
            click.echo(rand_string(pool, length), nl=False)
            input()
