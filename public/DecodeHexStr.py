# -*- coding: utf-8 -*-

from sqlalchemy import false, true

class DecodeInfo:
    def __init__(self, name:str = "", start:int = 0, end:int = 0) -> None:
        self._name  = name
        self._start = start
        self._end   = end

    @property
    def name(self) -> str:
        return self._name

    @property
    def start(self) -> int:
        return self._start

    @property
    def end(self) -> int:
        return self._end

class ReadCfgFile:
    def __init__(self, fileName: str) -> None:
        self._fileName = ""
        pass

class DecodeHexStr:
    def __init__(self) -> None:
        self._m_hexStr:str = ""
        self._m_decode_item:dict[str, tuple(int, int)] = {}

    def Decode(self, hexStr : str) -> None:
        pass

    def __JudgeStrValid(self) -> bool:
        """
        检查输入字符串是否合理
        """
        if self._m_hexStr is None:
            return false
        for c in self._inputStr:
            if (c >= '0' and c <= '9') :
                continue
            elif c >= 'A' and c <= 'Z' :
                continue
            elif c >= 'a' and c <= 'z':
                continue
            else:
                return false

        return true


if __name__ == "__main__" :
    a = DecodeInfo("123", 1, 2)
    print(a.start)
    print("Hello world")