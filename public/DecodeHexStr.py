# -*- coding: utf-8 -*-

import re
from numpy import character

from sqlalchemy import false


class DecodeInfo:
    def __init__(self, name: str = "", start: int = 0, end: int = 0) -> None:
        self._name:str  = name
        self._start:int = start
        self._end:int   = end

    @property
    def name(self) -> str:
        return self._name

    @property
    def start(self) -> int:
        return self._start

    @property
    def end(self) -> int:
        return self._end

class DecodeHexStr:
    def __init__(self, input:str) -> None:
        self._m_hexStr: str = input[::-1]
        self._m_decode_item: list[DecodeInfo] = {}

    def Decode(self, hexStr: str) -> None:
        pass

    def Decode2Bit(self) -> list[int] or None:
        if self.__JudgeStrValid() is False:
            print ("input is invalid\n")
            return None
        retStr = ""
        for char in self._m_hexStr:
            retStr += self.Hex2FullBitStr(char)
        return retStr
    
    def Hex2FullBitStr(cls, char: character) -> str:
        """
        将字符转换为4位bit位
        """
        retStr: str = "0000"
        bitStr: str =  bin(int(char, 16))[2:]
        retStr = retStr[0: len(retStr) - len(bitStr)] + bitStr
        return retStr

    def __JudgeStrValid(self) -> bool:
        """
        检查输入字符串是否合理
        """
        pattern = re.compile(r'^[0-9a-fA-F]+$', re.I)
        if pattern.match(self._m_hexStr) is None:
            return False
        return True


if __name__ == "__main__":
    a = DecodeHexStr("123456789aAbBcCdDeEfF")
    a.Decode2Bit()
    # a = "123"
    # print("%d, %#hx" %(1, 10))