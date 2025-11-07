from utils.switch import Adv
import argparse

def number(x):
    try:
        return int(x)
    except ValueError:
        return float(x)

parser = argparse.ArgumentParser(description="Matrix Calculator")
subparsers = parser.add_subparsers(dest="cmd")

def adv_args():
    adv_parser = subparsers.add_parser("det", help="Use 'det [1,2,3,....]' to find Determinant.")
    adv_parser = subparsers.add_parser("inv", help="Use 'inv [1,2,3,....]' to find Inverse.")
    adv_parser = subparsers.add_parser("magnitude", help="Use 'magnitude [1,2,3,....]' to find Magnitude.")
    adv_parser = subparsers.add_parser("rank", help="Use 'rank [1,2,3,....]' to find Rank.")
    adv_parser = subparsers.add_parser("trace", help="Use 'trace [1,2,3,....]' to find Trace.")
    
    adv_parser.add_argument("x", type=number)
    
    args = parser.parse_args()
    if args.cmd in ("det", "inv", "magnitude", "rank", "trace"):
        print (Adv(args.cmd, args.x))
    else:
        print("No key found!")
    