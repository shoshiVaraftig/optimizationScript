

from pathlib import Path

from argparse import ArgumentParser

def main(args):
    
   
    path=Path(args.folder_name)
    path.rename(args.new_name)
    print(f"Renaming folder '{args.folder_name}' to '{args.new_name}'.")



if __name__=='__main__':
   
    parser = ArgumentParser(description="Enter folder name and new name to replace it")
    parser.add_argument('folder_name', type=str, help='Enter the folder name to be renamed')
    parser.add_argument('new_name', type=str, help='Enter the new name to replace the folder name')
 
    
    args=parser.parse_args()
    print(args)
    main(args)