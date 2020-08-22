import argparse

from src.tips import PyBitesTips


def main():
    parser = argparse.ArgumentParser(description='Search term')
    parser.add_argument("-s", "--search", type=str,
                        help='Search PyBites Python tips')

    args = parser.parse_args()

    pb_tips = PyBitesTips()
    if args.search:
        tips = pb_tips.filter_tips(args.search)
        pb_tips.show_tips(tips)
    else:
        pb_tips()


if __name__ == '__main__':
    main()
