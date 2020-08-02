import random
from constants import CLEAR_ALPHABET, NUMBER_OF_DISCS


class Disks:

    def __init__(self):
        random.seed(42)
        self.discs = []
        for _ in range(NUMBER_OF_DISCS):
            alp_list = list(CLEAR_ALPHABET)
            random.shuffle(alp_list)
            self.discs.append(''.join(alp_list))
