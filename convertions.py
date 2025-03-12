

# parameters

"""
imr = immediate and value

"""
opParams = {
        "nop":None,
        "hlt":None,
        # letts the bit size
        "bws":{"regA":3,"regB":3,"reOps":3,"regRes":3},
        "amt":{"regA":3,"regB":3,"reOps":3,"regRes":3},
        # imrs 1 if immediate store 0 for ram page
        "dla":{"imr":8, "imrs"1, "regAdrs":3},
        "dmv":{"regSrcs":3,"regDes":3},
        "rds":{"ramDes":8,"regDes":3},


        "flg":{"regA":3,"regB":3},
        "beef":{"address":8,"condition":4}

        }

atm_names = {
        # amt sub ops
        "add":0,
        "sub":1,
        "addim":2,
        "subim":3,
        # bws sub ops
        "not":0,
        "and":1,
        "xor":2,
        }



alias = {
        "bif":{"beef",opParams["beef"]},
        "shiftUp":{"atm",{}}
        }







 
