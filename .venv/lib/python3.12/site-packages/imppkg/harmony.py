import sys
from imppkg.harmonic_mean import harmonic_mean
from termcolor import cprint

def main():
    nums = [float(arg) for arg in sys.argv[1:]]
    cprint(harmonic_mean(nums), 'red', 'on_cyan', attrs=['bold'])