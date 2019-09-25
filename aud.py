import argparse
parser = argparse.ArgumentParser(description='Make your adofai level to straight', allow_abbrev=True)
parser.add_argument('-v', '--version', action='version', version='%(prog)s : Alpha build 1')
parser.add_argument('-o', '--output', action='store', type=str, help='Output file that saves unfolded level')
parser.add_argument('level', action='store', type=str, help='Input file that has original map file')

args = parser.parse_args()
if not args.output:
    args.output = args.level.replace('.adofai','-aud.adofai')