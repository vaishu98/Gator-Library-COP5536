from GatorHelper import GatorLibrary
import sys

if __name__ == "__main__":
    
    # Extracting file name from the command line arguments
    inputFilename = str(sys.argv[1])

    # Initializing the output file name
    outputFileName = inputFilename.split('.')[0]+"_output_file.txt"

    # Initializing the Gator Helper object along with the output filename
    lib = GatorLibrary(outputFileName)

    # Reading operations from the file
    with open(inputFilename, 'r') as file:
        commands = file.readlines()

    # Iterating through the commands
    for command in commands:

        # Removing trailing spaces
        commandStripped = command.strip()
        # Removing trailing semi-colons
        commandStripped = commandStripped.strip(';')
        # Extracting operation name
        command_parts = commandStripped.strip().split('(')
        command_name = command_parts[0]
        # Ignoring commands after Quit command
        if command_name=='Quit':
            commandExecute = "lib."+commandStripped
            # Executing Quit command
            eval(commandExecute)
            break
        commandExecute = "lib."+commandStripped
        # Execting command using the initialized lib object
        eval(commandExecute)
