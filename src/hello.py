#!/usr/bin/env python3

from base import CorbotRunner


class Hello(CorbotRunner):
    def run(self, *args):
        print("Hello, world!")


def main() -> None:
    Hello().run()


if __name__ == "__main__":
    main()
