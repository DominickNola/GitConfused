"""import stack.py"""
import stack
# These 63 methods will eventually Implement all the opcode commands.
# ONLY BUILD THE METHODS NOT COMMENTED OUT.
# pylint: disable = W0603, C0330
S = stack.Stack()

# According to the JVPM documentation Zach posted to Slack,
# we need to use a local arrays'[] index values when using MATH for iload and istore.
# Therefore, I transitioned the VARIABLES_0-4 to the VARIABLES[] array.
VARIABLES = [0]

# ****************************************************************************************

def opcode_methods(argument):
    """DICTIONARY OF METHODS, FOR SPRINT 3 ONLY BUILD THE METHODS NOT COMMENTED OUT."""
    # Array of arguments from the main for istore and iload
    # arguments = []
    token_dict = {
#         "91": i2b,              # convert an int into a byte
#         "92": i2c,              # convert an int into a character
#         "87": i2d,              # convert an int into a double
#         "86": i2f,              # convert an int into a float
#         "85": i2l,              # convert an int into a long
#         "93": i2s,              # convert an int into a short
        "60": iadd,              # add two ints
#         "2e": method11, #iaload          # load an int from an array
        "7e": iand,          # perform a bitwise AND on two integers
#         "4f": iastore,         # store an int into an array
        "02": iconst_m1,    # load the int value -1 onto the stack
        "03": iconst_0,      # load the int value 0 onto the stack
        "04": iconst_1,      # load the int value 1 onto the stack
        "05": iconst_2,      # load the int value 2 onto the stack
        "06": iconst_3,      # load the int value 3 onto the stack
        "07": iconst_4,      # load the int value 4 onto the stack
        "08": iconst_5,      # load the int value 5 onto the stack
        "6c": idiv,              # divide two integers
#         "a5": if_acmpeq,       # if references are equal branch to instruction
#         "a6": if_acmpene,      # if references are not equal branch to instruction
#         "9f": if_icmpeq,       # if ints are equal, branch
#         "a2": if_icmpge,       # if value1 >= value2, branch
#         "a3": if_icmpgt,       # if value1 > value2, branch
#         "a4": if_icmple,       # if value1 <= value 2, branch
#         "a1": if_icmplt,       # if value1 < value2, branch
#         "a0": if_icmpne,       # if value1 != value2, branch
#         "99": ifeq,            # if value is 0, branch
#         "9c": ifge,            # if value >= 0, branch
#         "9d": ifgt,            # if value > 0, branch
#         "9e": ifle,            # if value <= 0, branch
#         "9b": iflt,            # if value < 0, branch
#         "9a": ifne,            # if value != 0 , branch
#         "c7": ifnonnull,   # if value is not null, branch
#         "c6": ifnull,         # if value is null, branch
#         "84": iinc,              # increment local variable #index by signed byte const
#         "15": iload,           # load an int value from a local variabl #index
         "1a": iload_0,       # load an int value from local array variable[0]
         "1b": iload_1,       # load an int value from local array variable[1]
         "1c": iload_2,       # load an int value from local variable[2]
         "1d": iload_3,       # load an int value from local variable[3]
#         "fe": impdep1,       # reserved for implementation dependent operations,
#         "ff": impdep2,       # reserved for implementation dependent operations,
#                                   # should not appear
        "68": imul,              # multiply two integers
        "74": ineg,  #ineg        # negate int
#         "c1": instanceof,      # determines if objectref is of a given type
#         "ba": invokedynamic,   # invoke a dynamic method and put the result on Stack
#         "b9": invokeinterface, # invoke an interface method on object object ref and
#                                      # puts results on the stack
#         "b7": invokespecial,   # invoke instance method on objectref and
#                                      # puts result on the stack
#         "b8": invokestatic,    # invoke static method and puts result on the stack
#         "b6": invokevirtual,   # invoke virtual method on objectref and
#                                      # puts result on the stack
        "80": ior,           # bitwise int OR
        "70": irem,          # logical in remainder
#         "ac": ireturn,       # returner an integer from a method
        "78": ishl,          # int shift left
        "7a": ishr,          # int arithmetic shift right
        #"36": istore,        # store int value into variable #index
        "3b": istore_0,      # store int value into VARIABLE[0]
        "3c": istore_1,      # store int value into VARIABLE[1]
        "3d": istore_2,      # store int value into VARIABLE[2]
        "3e": istore_3,      # store int value into VARIABLE[3]
        "64": isub,              # int subtract
        "7c": iushr,         # int logical shift right
        "82": ixor          # xor
    }
    # get the method name from the token_dict dictionary
    method = token_dict.get(argument, lambda: "Invalid opcode")

    # trying to figure out how to recieve arguments from main for istore and iload
    # if arguments == []
    #     method()
    # else
    #     method(arguments[0])

    # Call the Method.
    method()


# ****************************************************************************************

# def i2b():
#     print('i2b')
#     https://www.delftstack.com/howto/python/how-to-convert-int-to-bytes-in-python-2-and-python-3/
#     temp_int = S.pop()
#     byte = bytes([temp_int])
#     S.push(byte)
#     print("i2b converts " + str(temp_int) + " to a byte: " + str(byte))

# def i2c():
#     print('i2c')

# def i2d():
#     print('i2d')

# def i2f():
#     print('i2f')

# def i2l():
#     print('i2l')

# def i2s():
#     print('i2s')

def iadd():
    """iadd: add two ints"""
    var2 = S.pop()
    var1 = S.pop()
    S.push(var1 + var2)
    print("> iadd: Popped (" + str(var1) + ") and (" + str(var2) +
          ") from the Stack, assigned to local variables, \nadded the two,"
          " and pushed result back to Stack.")
    print(">>>> Top of Stack is now " + str(S.peek()) + ".")

# def method11():
#     print('method11')

def iand():
    """iand: performed bitwise AND on two integers"""
    var2 = S.pop()
    var1 = S.pop()
    S.push(var1 & var2)
    print("> iand: Popped (" + str(var1) + ") and (" + str(var2) +
          ") from the Stack, assigned to local variables, \nperformed bitwise"
          " AND and pushed the result (" + str(var2 & var1) + ") back to Stack")
    print(">>>> Top of Stack is now " + str(S.peek()) + ".")
# def iastore():
#     print('iastore')

def iconst_m1():
    """iconst_m1: load the int value -1 onto the stack"""
    S.push(-1)
    print("iconst_m1: Pushed " + str(S.peek()) + " to Stack in jvpm_methods.py.")

def iconst_0():
    """iconst_0: load the int value 0 onto the stack"""
    S.push(0)
    print("iconst_0: Pushed " + str(S.peek()) + " to Stack in jvpm_methods.py.")

def iconst_1():
    """iconst_1: load the int value 1 onto the stack"""
    S.push(1)
    print("iconst_1: Pushed " + str(S.peek()) + " to Stack in jvpm_methods.py.")

# load the int value 2 onto the stack
def iconst_2():
    """iconst_2: load the int value 2 onto the stack"""
    S.push(2)
    print("iconst_2: Pushed " + str(S.peek()) + " to Stack in jvpm_methods.py.")

def iconst_3():
    """iconst_3: load the int value 3 onto the stack"""
    S.push(3)
    print("iconst_3: Pushed " + str(S.peek()) + " to Stack in jvpm_methods.py.")

def iconst_4():
    """iconst_4: load the int value 4 onto the stack"""
    S.push(4)
    print('"iconst_4: Pushed " + str(S.peek()) + " to Stack in jvpm_methods.py."')

def iconst_5():
    """iconst_5: load the int value 5 onto the stack"""
    S.push(5)
    print('"iconst_5: Pushed " + str(S.peek()) + " to Stack in jvpm_methods.py."')

def idiv():
    """idiv: divide two numbers"""
    var2 = S.pop()
    var1 = S.pop()
    S.push(var1 / var2)
    print("> idiv: Popped (" + str(var1) + ") and (" + str(var2) +
          ") from the Stack, assigned to local variables, \ndivided the two,"
          " and pushed result back to Stack.")
    print(">>>> Top of Stack is now " + str(S.peek()) + ".")

# def if_acmpeq():
#     print('if_acmpeq')

# def if_acmpene():
#     print('if_acmpene')

# def if_icmpeq():
#     print('if_icmpeq')

# def if_icmpge():
#     print('if_icmpge')

# def if_icmpgt():
#     print('if_icmpgt')

# def if_icmple():
#     print('if_icmple')

# def if_icmplt():
#     print('if_icmplt')

# def if_icmpne():
#     print('if_icmpne')

# def ifeq():
#     print('ifeq')

# def ifge():
#     print('ifge')

# def ifgt():
#     print('ifgt')

# def ifle():
#     print('ifle')

# def iflt():
#     print('iflt')

# def ifne():
#     print('ifne')

# def ifnonnull():
#     print('ifnonnull')

# def ifnull():
#     print('ifnull')

def iinc():
    """iinc: increment local variable #index by signed byte const"""
    print("iinc: not needed for this sprint")

# def iload():
#     print('iload')

def iload_0():
    """iload: push variable[0] to the Stack"""
    pushing = VARIABLES[0]
    S.push(pushing)
    print('iload_0: Load VARIABLES[0] on the Stack for processing.')

def iload_1():
    """iload: push variable[1] to the Stack"""
    pushing = VARIABLES[1]
    S.push(pushing)
    print('iload_1: Load VARIABLES[1] on the Stack for processing.')

def iload_2():
    """iload: push variable[2] to the Stack"""
    pushing2 = VARIABLES[2]
    S.push(pushing2)
    print('iload_2: Load VARIABLES[2] on the Stack for processing.')

def iload_3():
    """iload: push variable[3] to the Stack"""
    pushing3 = VARIABLES[3]
    S.push(pushing3)
    print('iload_3: Load VARIABLES[3] on the Stack for processing.')

# def impdep1():
#     print('impdep1')

# def impdep2():
#     print('impdep2')

def imul():
    """imul: multiply two integers"""
    var2 = S.pop()
    var1 = S.pop()
    S.push(var1 * var2)
    print("> imul: Popped (" + str(var1) + ") and (" + str(var2) +
          ") from the Stack, assigned to local variables, \nmultiplied the two,"
          " and pushed result back to Stack.")
    print(">>>> Top of Stack is now " + str(S.peek()) + ".")

def ineg():
    """ineg: value minus zero"""
    var1 = S.pop()
    S.push(0 - var1)
    print('ineg: Popped ' + str(var1) + ' from Stack, ineg = ' + str(S.peek()) + ','
          ' and pushed back to Stack.')

# def instanceof():
#     print('instanceof')

# def invokedynamic():
#     print('invokedynamic')

# def invokeinterface():
#     print('invokeinterface')

# def invokespecial():
#     print('invokespecial')

# def invokestatic():
#     print('invokestatic')

# def invokevirtual():
#     print('invokevirtual')

def ior():
    """ior: performed bitwise OR on two integers"""
    var2 = S.pop()
    var1 = S.pop()
    S.push(var1 | var2)
    print("> ior: Popped (" + str(var1) + ") and (" + str(var2) +
          ") from the Stack, assigned to local variables, \nperformed bitwise"
          " OR and pushed the result (" + str(var2 | var1) + ") back to Stack")
    print(">>>> Top of Stack is now " + str(S.peek()) + ".")

def irem():
    """logical in remainder"""
    var2 = S.pop()
    var1 = S.pop()
    S.push(var1 % var2)
    print("irem = " + str(S.peek()))

# def ireturn():
#     print('ireturn')

def ishl():
    """int logical shift left"""
    var2 = S.pop()
    var1 = S.pop()
    S.push(var1 << var2)
    print("> ishl: Popped (" +str(var1) + ") and (" + str(var2) + ") and shifted"
          + str(var1) + " left by " + str(var2) + " bit(s) and pushed the result"
          " back to Stack.")
    print("ishl = " + str(S.peek()))


def ishr():
    """int arithmetic shift right"""
    var2 = S.pop()
    var1 = S.pop()
    S.push(var1 >> var2)
    print("ishr = " + str(S.peek()))

# def istore():
#     """istore: store int value into array[in]"""
#     print('method57')

def istore_0():
    """istore_0: store int value into VARIABLES[0]"""
    popped = S.pop()
    VARIABLES.pop(0) # remove the assigned 0 from the [0]position
    VARIABLES.insert(0, popped)
    print("istore_0: Popped " + str(popped) +
          " from Stack and stored in VARIABLES[0] in jvpm_methods.py.")

def istore_1():
    """istore_1: store int value into VARIABLES[1]"""
    popped = S.pop()
    VARIABLES.insert(1, popped)
    print("istore_1: Popped " + str(popped) +
          " from Stack and stored in VARIABLES[1] in jvpm_methods.py.")

def istore_2():
    """istore_2: store int value into VARIABLES[2]"""
    popped = S.pop()
    VARIABLES.insert(2, popped)
    print("istore_2: Popped " + str(popped) +
          " from Stack and stored in VARIABLES[2] in jvpm_methods.py.")

def istore_3():
    """istore_3: store int value into VARIABLES[3]"""
    popped = S.pop()
    VARIABLES.insert(3, popped)
    print("istore_3: Popped " + str(popped) +
          " from Stack and stored in VARIABLES[3] in jvpm_methods.py,"
          "\n>>>>>>>>>>>>>>>>>>>>>>>> c = " + str(popped) + " <<<<<<<<<<<<<<<<<<<<<<<<<<<")
    print(">>>> Top of Stack is now " + str(S.size()) + ".")

def isub():
    """isub: subtract two ints"""
    var2 = S.pop()
    var1 = S.pop()
    S.push(var1 - var2)
    print("> isub: Popped (" + str(var1) + ") and (" + str(var2) +
          ") from the Stack, assigned to local variables, \nsubtracted the two,"
          " and pushed result back to Stack.")
    print(">>>> Top of Stack is now " + str(S.peek()) + ".")

def iushr():
    """int logical shift right"""
    var2 = S.pop()
    var1 = S.pop()
    if var1 >= 0:
        S.push(var1 >> var2)
    else:
        S.push((var1 + 0x10000000) >> var2)
    print("iushr = " + str(S.peek()))

def ixor():
    """int xor"""
    variable2 = S.pop()
    variable1 = S.pop()
    S.push(variable1 ^ variable2)
    print("ixor = " + str(S.peek()))
