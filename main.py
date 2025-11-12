import sys
from colorama import Fore, Back, Style, init
import utils.switch as methods
from utils.tools import cli
from utils.help import help_commands
import numpy as np

mat1=[[1,2], [3,4]]
mat2=[[6,9], [7,8]]
vect=[1,2,4,3,7,5]
n=3

print(np.arange(8, 15, 2))

args=sys.argv[1:]

# print(cli(args))
# print(help_commands["linspace"])