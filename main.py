import os


def get_last_day():
    folder = "./"
    folders = [name for name in os.listdir(folder) if
               os.path.isdir(os.path.join(folder, name)) and name.startswith("day")]
    return int(folders[-1:][0][-2:])


def run_by_day(day):
    day = "0" + str(day) if day < 10 else str(day)
    # very hacky
    path = f"./day{day}/"
    script = [name for name in os.listdir(path) if name.endswith(".py")][0]
    main_dir = os.getcwd()
    os.chdir(main_dir + path)
    compiled = compile(open(script).read(), script, "exec")
    exec(compiled)
    print("")
    os.chdir(main_dir)


# TODO: Fix classes not being interpreted causing errors
if __name__ == '__main__':
    last = get_last_day()
    while True:
        print("Advent of Code 2022's janky python solutions\n")
        sel = int(input(f"Select a day (1-{str(last)}) or run all answers (0):\n"))
        if 0 < sel <= last:
            try:
                run_by_day(sel)
            except Exception as e:
                print("An error has occurred.\n")
                print(str(e) + "\n")
        else:
            for i in range(1, last, 1):
                print(f"DAY {str(i)}\n")
                try:
                    run_by_day(i)
                except Exception as e:
                    print("An error has occurred.\n")
                    print(str(e) + "\n")
        input()
