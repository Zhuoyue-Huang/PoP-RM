class Polynomial:
    def __init__(self, coeff_dict):
        self.coeff = coeff_dict

    def __call__(self, x):
        coeff_dict = self.coeff
        s = 0
        for (power, coeff) in coeff_dict.items():
            s += coeff * x**power
        return s

    def __add__(self, other):
        result = self.coeff.copy()
        for power in other.coeff:
            if power in self.coeff:
                result[power] += other.coeff[power]
            else:
                result[power] = other.coeff[power]
        return Polynomial(result)

    def __sub__(self, other):
        result = self.coeff.copy()
        for power in other.coeff:
            if power in self.coeff:
                result[power] -= other.coeff[power]
            else:
                result[power] = -other.coeff[power]
        return Polynomial(result)

    def __mul__(self, other):
        c = self.coeff
        d = other.coeff
        result = {}
        for cpower in c:
            for dpower in d:
                if cpower+dpower in result:
                    result[cpower+dpower] += c[cpower] * d[dpower]
                else:
                    result[cpower+dpower] = c[cpower] * d[dpower]
        return Polynomial(result)
