from files_sorted import *


def main():
    txt_files = file_filter()
    names_len = len_file(txt_files)
    write_file(names_len)


main()
