
from pathlib import Path

from argparse import ArgumentParser

def main(args):
    
    
    path=Path(args.path)
    for file in path.rglob(f'*.{args.end}'):

        file.rename(file.with_suffix('.txt'))

if __name__=='__main__':
   
    parser = ArgumentParser(description="Enter end folder to change")

    parser.add_argument('path',type=str)
    parser.add_argument('end',type=str)

    args=parser.parse_args()
    print(args)
    main(args) 