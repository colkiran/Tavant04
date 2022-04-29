"""
the name of the current module will be __main__ if executed as a file (__name__ = __main__)
if the file is imported as a module then __name__ will be the name of the file

"""


class HDFC:

    def withdraw(self):
        print("You can withdraw upto 75k per day")

# print(__name__)

if __name__ =='__main__':
    hdfc = HDFC()
    hdfc.withdraw()
