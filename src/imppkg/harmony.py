import sys
from imppkg.harmonic_mean import harmonic_mean
from termcolor import cprint

def main():

    result = 0.0 # The result will be zero unless succesfully calculated

    try:
        nums = [float(arg) for arg in sys.argv[1:]]
    
    except ValueError:
        # If input cannot be converted to float, proceed as if there was no input
        nums = []
    
    try:
        result = harmonic_mean(nums)
    except ZeroDivisionError:
        # If there is no input or if the input is zero, rpoceed with the default result
        pass
    
    cprint(result, 'red', 'on_cyan', attrs=['bold'])