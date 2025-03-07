import re

def assemble(input:str, default_const: dict | None = None) -> tuple[list[str],dict]:
    # convert assembly to list of string
    program:list[str] = input.split("\n")
    
    # remove first comment and parse it for initiation
    for id,line in enumerate(program):
        if line.startswith("// "):
            program[id] = ""
        else:
            break
    

    # definitions
    definitions:dict[str, int] = default_const or {
            # default constant
            "zero":0,
            "largerthan":1,
            "lessthan":2,
            "equals":3,
            "overflow":4}
    for id,line in enumerate(program):
        if line.startswith("define"):
            _,name,value = line.split(" ")
            definitions[name] = int(value)
    
    # list all operation
    for id,line in enumerate(program):
        in_line_ops = line.split(",")
        # ```addim 12 34 56, subin 12 34 56```
        offset = 0
        for in_line_ops:
            # ....
            pass


    ## process this after every operation is listed
    # tags
    for id,line in enumerate(program):
        pass # how......



    print(*program,sep="\n")
    print("definitions\n")
    print(*definitions.items(),sep="\n")



    return ["sus",],dict()

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



