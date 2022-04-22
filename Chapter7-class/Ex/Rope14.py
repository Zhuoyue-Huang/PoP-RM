"""Implement an addition operator."""


class Rope:
    def __init__(self, nodes):
        self.nodes = nodes

    def __add__(self, other):
        total_nodes = self.nodes + other.nodes + 1
        return Rope(total_nodes)

    def __str__(self):
        return f"{self.nodes}"
