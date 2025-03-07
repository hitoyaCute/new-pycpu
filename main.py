import os
import json
import display
import assembler
import emulator


def main(program):
    # assemble and get the program
    with open(program, "r") as file:
        program, conf = assembler.assemble(file.read() )

    # create ram file
    with open("ram", "r") as file:
        json.dump([0]*256, file)

    # runs display 
    display.Display(conf["display-size"], conf["map"],)

    # emulates
    emulator.run((program))


if __name__ == "__main__":
    ss = os.listdir("./program/") 
    inp = int(input(f"choose what program to run (0 to {len(ss)-1})\n\n{ss}"))

    main("./program/"+ss[inp])

