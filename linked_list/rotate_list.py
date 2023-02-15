from list_base import Slist


def main():
    slist = Slist()
    slist.build_list_from_list([1, 2, 3, 4, 5])
    slist.print_list()

    slist.rotate(4)
    slist.print_list()


if __name__ == "__main__":
    main()
