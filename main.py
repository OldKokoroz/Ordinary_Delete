import os
from time import sleep

attack = ""  # full path of the directory you want to delete things
# Just keep it default like C:\\ and just enter file or directory names you want to delete !"with extensions"!

to_del = ["delete1.txt", "delete2.txt"]


def mass_del():
    try:
        print("\nBot Started")
        os.chdir(attack)

        dirs = []
        dirs.clear()  # clear everything from last use
        deleted = 0
        total_files = 0

        for _ in os.listdir():
            print(os.listdir())
            if _ in to_del:
                os.remove(f"{os.getcwd()}/{_}")
                deleted += 1

            elif os.path.isdir(_):
                os.chdir(f"{os.getcwd()}/{_}")

                print(os.getcwd())
                sleep(1)
                print(os.listdir())

                total_files += len(os.listdir())

                for i in os.listdir():
                    if _ in to_del:
                        if os.path.isfile(_):
                            os.remove(f"{os.getcwd()}/{_}")
                            deleted += 1

                    elif os.path.isdir(i):
                        os.chdir(f"{os.getcwd()}/{i}")

            else:
                continue

        print(f"""\n
            Searched Directories : {len(dirs)}
            Searched Files       : {total_files + deleted} 
            Deleted  Files       : {deleted}
            Left     Files       : {total_files}
            """)

    except KeyboardInterrupt:
        print("Exiting")
        exit()


mass_del()