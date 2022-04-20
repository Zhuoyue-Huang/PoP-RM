"""Deduce a class implementation."""


class Hello:
    def __init__(self):
        self.name = "World"

    def __call__(self, args):
        if args:
            self.name = args
        return f"Hello, {self.name}!"

    def __str__(self):
        return f"Hello, {self.name}!"
