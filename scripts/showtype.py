#!/usr/bin/env python

import argparse

import six.moves.cPickle as pickle

import pickletype as pt


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('file')
    args = parser.parse_args()

    with open(args.file, 'rb') as f:
        data = pickle.load(f)
    t = pt.get_type(data)
    print(t)
