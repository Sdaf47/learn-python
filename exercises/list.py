import os

import sys

import itertools


class FileList:
    lst = list()

    def __init__(self, dir=str(), ):
        self.dir = '' if dir == str() else dir
        self.current_index = 0

    def get_list(self):
        if len(self.lst) <= 0:
            self.lst = os.listdir(self.dir)
        return self.lst

    def create_file(self):
        file_name = input('Введите имя файла с расширением .lst, либо программа сама его добавит. Тут жу вам решать: ')
        if len(file_name) <= 0:
            print("Не понял?!")
            return self.create_file()
        if len(file_name) < 5 or file_name[-4:] != '.lst':
            print('Ну ок!')
            file_name += '.lst'
        return file_name

    def choose_file(self):
        self.get_list()

        for i in range(len(self.lst)):
            print("{}. {}".format(i + 1, self.lst[i]))

        self.current_index = int(input("Введите номер желаемого файла или 0 для создания нового: ")) - 1
        if self.current_index == -1:
            return self.create_file()
        return self.dir + self.lst[self.current_index]

    def show_list(self):
        pass


class ListParser:
    lines = dict()
    key = int(1)

    def __init__(self, file_name):
        with open(file_name) as file:
            self.lines = dict([(self.inc(), line.strip()) for line in file])

    def inc(self):
        self.key += 1
        return self.key

    def show(self):
        print(self.lines)
        for key in self.lines:
            print("{}. {}".format(key, self.lines[key]))


def main():
    try:
        file_list = FileList(sys.argv[1])
        file_name = file_list.choose_file()
        list_parser = ListParser(file_name)
        list_parser.show()

    except IndexError:
        print("usage: please get the fucking directory")
    except ValueError:
        print("usage: what wrong?")


if __name__ == '__main__':
    main()
