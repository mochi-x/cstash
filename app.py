import os
import sys
import argparse


def main():
    createHistory()
    args = createArgSetting()

    if args.cmd == 'add':
        print('add exec')
    if args.cmd == 'ls':
        print('ls exec')
    if args.cmd == 'rm':
        print('rm exec')


def createArgSetting():
    p = argparse.ArgumentParser()
    p.add_argument('cmd', help='ls, rm, add')
    # p.add_argument('-a', '--opt_a', help='option')
    return p.parse_args()


def createHistory():
    stashPath = os.environ['HOME'] + '/.cstash'
    stashExist = os.path.exists(stashPath)

    if not stashExist:
        f = open(stashPath, 'w')
        f.write('')
        f.close()