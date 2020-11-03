import os
import sys
import argparse
import json
from prettytable import PrettyTable


def main():
    args = createArgSetting()
    createHistory()

    if args.cmd == 'add':
        print('add exec')
    if args.cmd == 'ls':
        getStashList()
    if args.cmd == 'rm':
        print('rm exec')


def createHistory():
    stashPath = os.environ['HOME'] + '/.cstash'
    stashFilename = 'stash.json'

    if not os.path.exists(stashPath):
        os.makedirs(stashPath, exist_ok=True)
    if not os.path.exists(stashPath + '/' + stashFilename):
        f = open(stashPath + '/' + stashFilename, 'w')
        f.write('[]')
        f.close()


def createArgSetting():
    cmdList = ['add', 'ls', 'rm']

    p = argparse.ArgumentParser()
    p.add_argument('cmd', help='ls, rm, add', choices=cmdList)
    # p.add_argument('-a', '--opt_a', help='option')
    return p.parse_args()


def getStashList():
    stashJsonPath = os.environ['HOME'] + '/.cstash/stash.json'
    with open(stashJsonPath) as f:
        loadStash = json.load(f)

        x = PrettyTable()
        x.field_names = ['INDEX', 'COMMAND']
        for i in range(len(loadStash)):
            x.add_row([i, loadStash[i]])

        print(x.get_string())
