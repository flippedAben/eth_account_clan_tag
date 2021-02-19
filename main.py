import argparse
import generate

parser = argparse.ArgumentParser()
parser.add_argument('tag', help='The desired clan tag')

if __name__ == '__main__':
    args = parser.parse_args()
    generate.generate(args.tag)
