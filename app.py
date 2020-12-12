import os
import sys
import argparse
import json
import subprocess
from prettytable import PrettyTable


def main():
    parser = createParseSetting()
    args = parser.parse_args()

    createHistory()
    if args.COMMAND == 'add':
        addStash(parser, args.command)
    elif args.COMMAND == 'ls':
        getStashList()
    elif args.COMMAND == 'rm':
        deleteStash(parser, args.index)
    elif args.COMMAND == 'exec':
        execStash(parser, args.index)
    else:
        if parser.print_help() != None:
            showHelp(parser)


def showHelp(parser):
    print(parser.print_help())


def createHistory():
    stashPath = os.environ['HOME'] + '/.cstash'
    stashFilename = 'stash.json'

    if not os.path.exists(stashPath):
        os.makedirs(stashPath, exist_ok=True)
    if not os.path.exists(stashPath + '/' + stashFilename):
        f = open(stashPath + '/' + stashFilename, 'w')
        f.write('[]')
        f.close()


def createParseSetting():
    p = argparse.ArgumentParser()
    p.add_argument('COMMAND', help='')
    p.add_argument('-c', '--command', help='')
    p.add_argument('-i', '--index', help='')
    return p


def getStashList():
    stashJsonPath = os.environ['HOME'] + '/.cstash/stash.json'
    with open(stashJsonPath) as f:
        loadStash = json.load(f)
        x = PrettyTable()
        x.field_names = ['INDEX', 'COMMAND']
        for i in range(len(loadStash)):
            x.add_row([i, loadStash[i]])

        print(x.get_string())


def addStash(parser, cmd):
    if cmd == None:
        showHelp(parser)
        sys.exit()

    stashJsonPath = os.environ['HOME'] + '/.cstash/stash.json'
    with open(stashJsonPath) as f:
        loadStash = json.load(f)
        loadStash.append(cmd)
        addStash = json.dumps(loadStash)

        f = open(stashJsonPath, 'w')
        f.write(addStash)
        f.close()


def deleteStash(parser, index):
    stashJsonPath = os.environ['HOME'] + '/.cstash/stash.json'
    with open(stashJsonPath) as f:
        loadStash = json.load(f)
        if index == None or int(index) > len(loadStash) - 1 or int(index) < 0:
            showHelp(parser)
            sys.exit()

        del loadStash[int(index)]
        deleteStash = json.dumps(loadStash)

        f = open(stashJsonPath, 'w')
        f.write(deleteStash)
        f.close()


def execStash(parser, index):
    stashJsonPath = os.environ['HOME'] + '/.cstash/stash.json'
    with open(stashJsonPath) as f:
        loadStash = json.load(f)
        if index == None or int(index) > len(loadStash) - 1 or int(index) < 0:
            showHelp(parser)
            sys.exit()
        print(loadStash[int(index)])
        subprocess.call(loadStash[int(index)].split())