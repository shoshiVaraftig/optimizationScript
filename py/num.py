
from pathlib import Path

from argparse import ArgumentParser

def main(args):
    
  

    with open(args.path,'a')as file:
        file.write(f'{args.text}'*args.number)


if __name__=='__main__':
   
    parser = ArgumentParser(description="Enter folder name and string and num to write string")

    parser.add_argument('path',type=str)
    parser.add_argument('text',type=str)
    parser.add_argument('--number','-n',type=int)
    args=parser.parse_args()
    print(args)
    main(args)