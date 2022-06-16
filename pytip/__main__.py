import argparse

from pytip.tips import PyBitesTips


def main():
    parser = argparse.ArgumentParser(description='Search term')
    parser.add_argument("-s", "--search", type=str,
                        help='Search PyBites Python tips')
    parser.add_argument("-p", "--pager", action='store_true',
                        help='Go through the resulting tips one by one')
    parser.add_argument("-c", "--colors", action='store_true',
                        help='Do syntax highlighting on the snippets')

    args = parser.parse_args()

    pb_tips = PyBitesTips(use_pager=args.pager, use_colors=args.colors)
    if args.search:
        tips = pb_tips.filter_tips(args.search)
        pb_tips.show_tips(tips)
    else:
        pb_tips()


if __name__ == '__main__':
    main()
