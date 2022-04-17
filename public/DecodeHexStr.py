#!/usr/bin/env python3
#coding=utf-8
from NumberStr import NumberStrTrans, NumFormat


class DecodeInfo:
    def __init__(self, title: str = "", start: int = 0, end: int = 0) -> None:
        self._title:str = title
        self._start:int = start
        self._end:  int = end

    @property
    def title(self) -> str:
        return self._title

    @property
    def start(self) -> int:
        return self._start

    @property
    def end(self) -> int:
        return self._end

class DecodeHexStr:
    def __init__(self, hex_str: str, decodeInfoList: list) -> None:
        self._m_hexStr: str = hex_str



if __name__ == "__main__":
    l = [
        DecodeInfo("t1", 0, 2),
        DecodeInfo("t2", 3, 4),
    ]

    print(NumberStrTrans.Str2Num("0b101", NumFormat.BIN))
