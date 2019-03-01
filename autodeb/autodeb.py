#!/usr/bin/python3
import argparse

def main():
    print("Welcome to autodeb")


    parser = argparse.ArgumentParser()
    parser.add_argument('-s','--src_url', action='store',
            dest='src_url',
            help='URL where the code is stored')

    results = parser.parse_args()
    print(results.src_url)


if __name__ == '__main__':
    main()
