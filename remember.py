#!/usr/bin/env python3
from argparse import ArgumentParser
import json
import os
from pathlib import Path
from time import time

history_size = 1000


def main():
    args = parse_args()

    datadir = get_datadir()
    datafile = datadir / f'{args.collection}.json'
    if datafile.is_file():
        try:
            with open(datafile) as f:
                collection = json.load(f)
        except json.JSONDecodeError:
            collection = []
    else:
        collection = []

    if args.command == 'use':
        collection = use(collection, args.value)
        with open(datafile, 'w') as f:
            json.dump(collection, f)
    if args.command == 'recall':
        recall(collection)


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


def get_datadir():
    datadir = Path.home() / '.local' / 'share' / 'remember'
    if not datadir.is_dir():
        os.mkdir(datadir)
    return datadir


def use(collection, value):
    collection = {record['value']:record for record in collection}
    if value in collection:
        collection[value]['score'] += 1
    else:
        collection[value] = {'value': value, 'score': 1}
    collection[value]['timestamp'] = int(time())
    return sorted(collection.values(), key=lambda r: r['timestamp'])[-history_size:]


def recall(collection):
    now = time()

    def _frecency(record):
        diff = now - record['timestamp']
        if diff < 60 * 60:
            return record['score'] * 4
        if diff < 60 * 60 * 24:
            return record['score'] * 2
        if diff < 60 * 60 * 24 * 7:
            return record['score'] // 2
        return record['score'] // 4

    for record in sorted(collection, key=_frecency, reverse=True):
        print(record['value'])


if __name__ == '__main__':
    main()
