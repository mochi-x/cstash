import os
import sys
import argparse


def main():
    p = argparse.ArgumentParser()
    p.add_argument('cmd', help='ls, rm, add')
    # p.add_argument('-a', '--opt_a', help='option')
    args = p.parse_args()

    envPath = os.environ['HOME'] + '/.cstash'
    envExist = os.path.exists(envPath)

    if not envExist:
        f = open(envPath, 'w')
        f.write('')
        f.close()

    if args.cmd == 'add':
        print('add exec')
    if args.cmd == 'ls':
        print('ls exec')
    if args.cmd == 'rm':
        print('rm exec')