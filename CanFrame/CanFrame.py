#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys

from numpy import array, unsignedinteger
class CanFrame:
    def __init__(self, inputStr:str) -> None:
        self._inputStr:str = inputStr
        self._len: int = len(inputStr)
    
    def is_valid(self) -> bool:
        

if __name__ == "__main__" :
    input:str = ""
    for i in range(1, len(sys.argv)):
        input += sys.argv[i]
    canFrameInst = CanFrame(input)