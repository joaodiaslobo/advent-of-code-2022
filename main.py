import os


def get_all_days():
    folder = "./"
    folders = [name for name in os.listdir(folder) if
               os.path.isdir(os.path.join(folder, name)) and name.startswith("day")]
    last = folders[-1:]
    print(last)


if __name__ == '__main__':
    get_all_days()
