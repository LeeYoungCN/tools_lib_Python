#!/usr/bin/env python3
#coding=utf-8

import re
from enum   import Enum
from pyclbr import Function

class NumFormat(Enum):
    BIN = 2,
    OCT = 8,
    DEC = 10,
    HEX = 16

class NumFmtInfo:
    def __init__(self, decimal: int, trans_f: Function , prefix: str, pattern: re.Pattern) -> None:
        self._decimal: int        = decimal
        self._trans_f: Function   = trans_f
        self._prefix:  str        = prefix
        self._pattern: re.Pattern = pattern
    
    @property
    def decimal(self) -> int:
        return self._decimal
    
    @property
    def trans_f(self) -> Function:
        return self._trans_f

    @property
    def prefix(self) -> str:
        return self._prefix

    @property
    def pattern(self) -> re.Pattern:
        return self._pattern


class NumberStrTrans:
    _NumFmtInfoDict_: dict = {
        NumFormat.BIN : NumFmtInfo(2,  bin, "0b", re.compile(r'^(0b)?[0-1]+$',   re.I)),
        NumFormat.OCT : NumFmtInfo(8,  oct, "0o", re.compile(r'^(0o)?[0-7]+$',   re.I)),
        NumFormat.DEC : NumFmtInfo(10, int, "",   re.compile(r'^[\d]+$',         re.I)),
        NumFormat.HEX : NumFmtInfo(16, hex, "0x", re.compile(r'^(0x)?[\da-f]+$', re.I)),
    }

    @classmethod
    def IsBinStr(cls, bin_str: str) -> bool:
        return cls.IsRightFmt(bin_str, NumFormat.BIN)

    @classmethod
    def IsOctStr(cls, oct_str: str) -> bool:
        return cls.IsRightFmt(oct_str, NumFormat.OCT)

    @classmethod
    def IsDecStr(cls, dec_str: str) -> bool:
        return cls.IsRightFmt(dec_str, NumFormat.DEC)

    @classmethod
    def IsHexStr(cls, hex_str: str) -> bool:
        return cls.IsRightFmt(hex_str, NumFormat.HEX)

    @classmethod
    def IsRightFmt(cls, num_str: str, fmt: NumFormat) -> bool:
        if cls._NumFmtInfoDict_[fmt].pattern.match(num_str) is None:
            return False
        return True

    @classmethod
    def Str2Num(cls, src_str: str, src_fmt: NumFormat) -> int or None:
        if cls.IsRightFmt(src_str, src_fmt) is False:
            return None
        
        if len(src_str) > 2 and src_str[:2] == cls._NumFmtInfoDict_[src_fmt].prefix:
            src_str = src_str[2:]

        src_dec: int = cls._NumFmtInfoDict_[src_fmt].decimal
        dec_num: int = int(src_str, src_dec)
        return dec_num
    
    @classmethod
    def Num2Str(cls, num: int, str_fmt: NumFormat, min_len: int) -> str:
        ret_str: str = cls._NumFmtInfoDict_[str_fmt].prefix
        dst_str: str = str(cls._NumFmtInfoDict_[str_fmt].trans_f(num))

        if str_fmt is not NumFormat.DEC:
            dst_str = dst_str[2:]

        for i in range(len(dst_str), min_len):
            ret_str += '0'
        ret_str += dst_str
        return ret_str

    @classmethod
    def StrFmtTrans(cls, src_str: str, src_fmt: NumFormat, dst_fmt: NumFormat, min_len: int = 0) -> str:
        dec_num: int or None = cls.Str2Num(src_str, src_fmt)
        if dec_num is None:
            return ""

        return cls.Num2Str(dec_num, dst_fmt, min_len)

 
if __name__ == "__main__":
    a: str = "a01"
    print(NumberStrTrans.StrFmtTrans(a, NumFormat.HEX, NumFormat.OCT))
