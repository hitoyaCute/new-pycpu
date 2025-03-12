import re
import convertions

def assemble(inp:str, default_const: dict | None = None) -> tuple[list[str],dict]:
    # step 0 split by line
    programs = inp.split("\n")

    # step 1 fetch definitions
    # step 2 search for names and create a list for render offset
    # and include tags
    # step 3 
   
    # holds tags and definitions
    names: dict[str,int] = {}

    # formated/cleaned assembly
    # list[(operation, line, in_line_start, in_line_end),..]
    asm: list[tuple[str,int,int,int]] = []
    

    # lets do it on one loop ig
    for pointer, line in enumerate(programs):
        # split the line for multi arg line
        encoding = False
        # multi line comment flag
        mlc_flag = False
        # comment flag
        cmnt_flag = False

        # read line flag
        read = True

        # remove comments
        if line.startswith("//"):
            # maybe check if its on an header
            continue
        # fetching definitions
        if line.startswith("define"):
            _, name,value = line.split(" ")
            names[name] = int(value)

        # the fun part
        for offset,char  in enumerate(line):
            if char == "/":
                encoding =True
                continue
            elif encoding:
                if char == "/":
                    cmnt_flag = True
                    break
                elif char == "*":
                    mlc_flag = True

                else:
                    raise EncodingWarning(f" error on /{char}")
                encoding = False


        # skip the line
        if cmnt_flag:
            cmnt_flag = False
            continue


#=target================state#
# definition            done
# initiazation          
# tags                  
# operation_split       
# display_index         
# comment               done
# inline_comment        done
# multi_line_comment    WIP








# input
testinp = """// stuff
// defines a constant
define constA 123

// default variables
define zero 0
define largerthan 1
define lessthan 2
define equals 3
define overflow 4

// if we define a const twice it willtrow error


tag:
// indent is just nothing
  addim @0 @12 constA // just a comment
  flag @0 @2 zero /*muli line comment
  cus whynot
  */
  // ',' is used to end the argument
  addim @0 12 constA, subim @0 12 constA
 

  /*random comment*/bif tag 
"""
# output format
## operand operands(in_order)       ; line,(row_start,row_end)
"""
addim 0 12 123   ; 18,(1,20)
flag 0 2 zero    ; 19,(1,16)
addim 0 2 123    ; 20,(1,19)
subim 0 12 123   ; 20,(21,39)
beef 0           ; 23,(19,25)
"""

print("start")
outp = assemble(testinp)



if __name__ == "__mai n__":
    with open("./program/test.asm", "r") as file:
        data = file.read()
        data = assemble(data)
        with open("./program/test.casm", "w") as outp:
            print(*data[0], sep="\n")
            print(*data[0], sep="\n",file=outp)



