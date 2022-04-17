#!/usr/bin/env python3
# coding=utf-8
from IntNumString import IntNumString, NumStrFmt
import math


class DecData:
    def __init__(self, title: str = "", start: int = 0, end: int = 0, value: int = 0) -> None:
        self.title: str = title
        self.start: int = start
        self.end: int = end
        self.val: int = value

    def __str__(self) -> str:
        min_len = math.ceil((self.end - self.start) / 4)
        hex_str = IntNumString.Num2Str(self.val, NumStrFmt.HEX, min_len)
        return self.title + ": " + hex_str


class DecNumStr:
    @classmethod
    def DecBinStr2Num(cls, bin_str: str, data: DecData) -> bool:
        bin_str: str = IntNumString.DelPrefix(bin_str, NumStrFmt.BIN)
        str_len: int = len(bin_str)
        start, end = cls.GetRange(data, str_len)
        if start is None or end is None:
            return False
        data.val = IntNumString.Str2Num(bin_str[start: end], NumStrFmt.BIN)
        return True

    @classmethod
    def InsertToBinStr(cls, data: DecData, dst_bin_str: str) -> str or None:
        src_len = data.end - data.start
        src_str = IntNumString.Num2Str(data.val, NumStrFmt.BIN, src_len)[2:]
        if src_len != len(src_str):
            return None
        dst_len: int = len(dst_bin_str)
        start, end = cls.GetRange(data, dst_len)
        if start is None or end is None:
            return None
        ret_str = dst_bin_str[0: start] + src_str + dst_bin_str[end:]
        return ret_str

    @classmethod
    def GetRange(cls, data: DecData, str_len: int) -> int or None:
        return cls.IndexConvert(data.end, str_len), cls.IndexConvert(data.start, str_len)

    @classmethod
    def IndexConvert(cls, index: int, str_len: int) -> int or None:
        if index > str_len:
            return None
        return str_len - index


if __name__ == "__main__":
    s = "0b00000"
    w = DecData("title", 0, 4, 100)
    x = DecodeNumStr.InsertToBinStr(w, s)
    print(x)
