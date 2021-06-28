import os
import sys
import asyncio
import argparse

from bgpd import metadata

def main(argv):
    print(metadata.description + ' ' + metadata.version)

    parser = argparse.ArgumentParser(description=metadata.description)

    parser.add_argument('config',
                        help='Configuration file')
    args = parser.parse_args()

    args.config = os.path.abspath(args.config)



def entry_point():
    """Zero-argument entry point for use with setuptools/distribute."""
    raise SystemExit(main(sys.argv))


if __name__ == '__main__':
    entry_point()
