import os
import sys
import controller
from controller import Controller
from entity import  Command
import entity
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(os.path.split(rootPath)[0])

if __name__ == "__main__":
    print(sys.argv)  # test
    con = Controller.Controller()
    con.controller(Command.parse_input(), sys.argv)