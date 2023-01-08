#!/usr/bin/env python3

import os
import sys

from base import CorbotRunner

# invoked as corbot todo "message"
# appends message to todo.txt


class Todo(CorbotRunner):
    @property
    def todofile(self) -> str:
        return os.path.join(self.corbot_dir, "todo.txt")

    def already_exists(self, todoline: str) -> bool:
        with open(self.todofile, "r") as f:
            for line in f:
                if line == todoline:
                    return True
        return False

    def todoline(self, *args) -> str:
        return f"TODO {' '.join(args)}"

    def print(self, highlight=False) -> None:
        with open(self.todofile, "r") as f:
            lines = f.readlines()
            for line in lines[:-1]:
                print(line, end="")
            if highlight:
                # last line in green
                print(f"\033[92m{lines[-1]}\033[00m", end="")
            else:
                print(lines[-1], end="")
        print()

    def run(self, *args) -> None:
        # if no args, print todofile
        if len(args) == 0:
            self.print()
            return

        # todoline should be unique
        todoline: str = self.todoline(*args)
        if self.already_exists(todoline):
            print(f"\033[91m Already exists: {todoline} \033[00m")
            sys.exit(1)

        # search for todoline in todofile
        with open(self.todofile, "a") as f:
            f.write(f"{todoline}\n")

        # print todofile to console
        self.print(highlight=True)


def main() -> None:
    Todo().run(*sys.argv[1:])


if __name__ == "__main__":
    main()
