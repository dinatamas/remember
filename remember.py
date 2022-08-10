#!/usr/bin/env python3
from argparse import ArgumentParser


def main():
    args = parse_args()

    print(args)


def parse_args():
    main_help = 'store values and recall them sorted by the frecency of their use'
    parser = ArgumentParser(description=main_help)
    subparsers = parser.add_subparsers(dest='command', required=True)

    use_help = 'increase the frecency score of a value'
    use_parser = subparsers.add_parser('use', description=use_help, help=use_help)
    use_parser.add_argument('collection', help='named group of values')
    use_parser.add_argument('value', help='the string to add/refresh')

    recall_help = 'list the stored values sorted by frecency'
    recall_parser = subparsers.add_parser('recall', description=recall_help, help=recall_help)
    recall_parser.add_argument('collection', help='named group of values')

    return parser.parse_args()


if __name__ == '__main__':
    main()
