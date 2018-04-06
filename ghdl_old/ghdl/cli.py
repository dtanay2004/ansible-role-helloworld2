# -*- coding: utf-8 -*-

"""Console script for ghdl."""
import sys
import click

from ghdl import ghdl

@click.command()
@click.option('--loglevel', default='DEBUG', prompt='Log level = DEBUG/INFO/WARNING', help='Set your log level')

def main(loglevel):
    """Console script for ghdl."""
    print('ABClevel {}'.format(loglevel))
    ghdl.download(loglevel)

    #click.echo("Replace this message by putting your code into "
      #         "ghdl.cli.main")
    #click.echo("See click documentation at http://click.pocoo.org/")
    #return 0


if __name__ == "__main__":
    sys.exit(main(loglevel))  # pragma: no cover
