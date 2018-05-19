import math
# uzupełnij funkcję triangle field tak,
# aby liczyła pole trójkąta dla podanych parametrów

def triangle_field(a, h):
    """
    Args:
        a: długość podstawy
        h: wysokość
    """
    field = (a * h) / 2
    return field

# Uzupełnij funkcję circle_field tak, aby liczyła pole koła dla
# podanej długości promienia. wartość liczby pi dostępna jest w zmiennej pi
# w module math
def circle_field(r):
    """
    Args:
        r: promień okręgu
    """
    field = math.pi * ( r * r)
    return field

# Uzupełnij funkcję power tak, aby liczyła potęgi dla podanych parametrów
# W rozwiązaniu można założyć, że potęgi będą miały zawsze wykładnik naturalny.
# Pamiętaj, że a^0 = 1
def power(a, n):
    """
    Args:
        a: podstawa
        n: wykładnik
    """

    if n == 0:
        power = 1
    elif n == 1:
        power = a
    else:
        power = 1
        for x in range(n):
            power *= a
    return power

# if __name__ == '__main__':
print("Pola trójkątów")
print("a = 2, b = 3, field = {0}".format(triangle_field(2, 3)))
print("a = 5.5, b = 7, field = {0}".format(triangle_field(5.5, 7)))
print("a = 7.8, b = 8.4, field = {0}".format(triangle_field(7.8, 8.4)))
print("=" * 20)
print("Pola kół")
print("r = 2, field = {0}".format(circle_field(2)))
print("r = 99999999999999999999999999, field = {0}".format(circle_field(99999999999999999999999999)))
print("r = 7.8, field = {0}".format(circle_field(7.8)))
print("=" * 20)
print("Potęgi")
print("10^0 = {0}".format(power(10, 0)))
print("10^2 = {0}".format(power(10, 2)))
print("2^128 = {0}".format(power(2, 128)))
print("=" * 20)
