# -*- coding: utf-8 -*-

"""Console script for pycapital."""
import sys
import click
#from pycapital.pycapital import TTY, capital
import pycapital.pycapital


@click.command()
@click.argument('country', type=str)
def main(country):
    """Console script for pycapital."""
    pycapital.pycapital.TTY = True
    pycapital.pycapital.capital(country)
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
