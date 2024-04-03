from pathlib import Path
from argparse import ArgumentParser

def main(args):
    # Open the file for reading
    with open(args.file, 'r') as file:
        # Read the content of the file
        content = file.read()
        # Replace the old word with the new word in the content
        new_content = content.replace(args.old_word, args.new_word)

    # Open the file for writing
    with open(args.file, 'w') as file:
        # Write the modified content back to the file
        file.write(new_content)

if __name__ == '__main__':
    # Create an argument parser with description
    parser = ArgumentParser(description="Enter word to replace and new word")
    
    # Add arguments for the file, old word, and new word
    parser.add_argument('file', help='Enter the path of the file')
    parser.add_argument('old_word', type=str, help='Enter the word to replace')
    parser.add_argument('new_word', type=str, help='Enter the new word to replace with')

    # Parse the arguments provided through the command line
    args = parser.parse_args()
    
    print(args)
    
    main(args)
