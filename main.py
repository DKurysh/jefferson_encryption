from encryptor import Encryptor
from disks import Disks
from constants import SHIFT

if __name__ == '__main__':

    text = 'Some encrypted tex'
    discs = Disks().discs

    out = Encryptor().jefferson_encryption(text, discs, SHIFT, reverse=False)
    print(out)

