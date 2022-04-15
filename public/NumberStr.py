import re
from enum import Enum

class NumFormat:
    BIN = 2,
    DEC = 10,
    HEX = 16

class NumFmtInfo:
    def __init__(self, prefix, pattern) -> None:
        self._prefix = prefix
        self._pattern = pattern

    @property
    def prefix(self):
        return self._prefix

    @property
    def pattern(self):
        return self._pattern

NumFmtInfoDict = {
    NumFormat.BIN : NumFmtInfo("0b", re.compile(r'^(0b)?[0-1]+$', re.I)),
    NumFormat.DEC : NumFmtInfo("",   re.compile(r'^[\d]+$', re.I)),
    NumFormat.HEX : NumFmtInfo("0x", re.compile(r'^(0x)?[\da-f]+$', re.I)),
}

class NumberStr:
    @classmethod
    def Hex2Bin(cls, hex_str: str, min_len: int = 0) -> str:
        """
        将字符转换为4位bit位
        """
        return cls.FmtTrans(hex_str, NumFormat.HEX, NumFormat.BIN, min_len)

    @classmethod
    def IsHexStr(cls, hex_str: str) -> bool:
        """
        判断是否为16进制字符串
        """
        return cls.IsRightFmt(hex_str, NumFormat.HEX)
    
    @classmethod
    def IsBinStr(cls, bin_str: str) -> bool:
        """
        判断是否为2进制字符串
        """
        return cls.IsRightFmt(bin_str, NumFormat.BIN)

    @classmethod
    def IsRightFmt(cls, num_str: str, fmt: NumFormat) -> bool:
        if NumFmtInfoDict[fmt].pattern.match(num_str) is None:
            return False
        return True
    
    @classmethod
    def FmtTrans(cls, src_str, src_fmt, dst_fmt, min_len) -> str:
        if cls.IsRightFmt(src_str, src_fmt) is False:
            return ""

        ret_str = NumFmtInfoDict[dst_fmt].prefix
        if dst_fmt == NumFormat.BIN:
           dst_str = bin(int(src_str, src_fmt))[2:] 
        elif dst_fmt == NumFormat.DEC:
            dst_str = "%d"%(int(src_str, src_fmt))
        elif dst_fmt == NumFormat.HEX:
            dst_str = "%lx"%(int(src_str, src_fmt))
        else:
            return ""
        
        for i in range(len(dst_str), min_len):
            ret_str += '0'
        ret_str += dst_str
        return ret_str


    @classmethod
    def IsDecStr(cls, dec: str) -> bool:
       return True
 
if __name__ == "__main__":
    a = '0x0a'
    print(NumberStr.Hex2Bin(a))