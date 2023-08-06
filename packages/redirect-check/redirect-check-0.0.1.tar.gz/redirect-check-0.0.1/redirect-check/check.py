#!/usr/bin/env python3

import sys, os, argparse, array
import subprocess
import requests

def main():
    # arguments parser set up
    parser = argparse.ArgumentParser(description='Check response code of websites',
                                     add_help=False)
    # create mutually exclusive group of Arguments for files or domains
    mutually_exclusive = parser.add_mutually_exclusive_group()
    mutually_exclusive.add_argument("-af", "--address_file", action='store', dest='address_file', type=argparse.FileType('r'), help="file filled with internal ip address to test for ssrf")
    mutually_exclusive.add_argument("-u", "--url", action='store', dest='url', help="a single url that is vuln to open redirect")
    parser.add_argument("-o", "--output", action='store', dest='output_file', help="output file path (by default, the script will print to stdout)")
    parser.add_argument("-h", "--help", action="help", help="Show this help message and exit.")
    args = parser.parse_args()
    print(args.url)

    ports = [80, 443, 5601]
    print(ports[0])
if __name__ == '__main__':
    SystemExit(main())
