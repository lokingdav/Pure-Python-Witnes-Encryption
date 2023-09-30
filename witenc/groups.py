import random
from .chianetbls import ec
from .chianetbls import pairing

def random_Zq():
    # sample random scalar
    return random.randint(1, ec.default_ec.n - 1)

def random_G1():
    # sample random G1 element
    r = random_Zq()
    # multiply by random scalar
    return r * ec.G1Generator()

def random_G2():
    # sample random G2 element
    r = random_Zq()
    # multiply by random scalar
    return r * ec.G2Generator()

def random_GT():
    # sample random G1 and G2 elements
    g1 = random_G1()
    g2 = random_G2()

    # compute pairing gt = e(G1, G2)
    gt = pairing.ate_pairing(g1, g2)

    return gt