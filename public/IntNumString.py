#!/usr/bin/env python3
# coding=utf-8

import re
from enum import Enum
from pyclbr import Function


class NumStrFmt(Enum):
    BIN = 2,
    OCT = 8,
    DEC = 10,
    HEX = 16


class __NumFmtInfo__:
    def __init__(self, decimal: int, trans_f: Function, prefix: str, pattern: re.Pattern) -> None:
        self._decimal: int = decimal  # 进制
        self._trans_f: Function = trans_f  # 装换公式
        self._prefix: str = prefix  # 前缀
        self._pattern: re.Pattern = pattern  # 匹配模式

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


class IntNumString:
    _NumFmtInfoDict_: dict = {
        NumStrFmt.BIN: __NumFmtInfo__(2,  bin, "0b", re.compile(r'^(0b)?[0-1]+$',   re.I)),
        NumStrFmt.OCT: __NumFmtInfo__(8,  oct, "0o", re.compile(r'^(0o)?[0-7]+$',   re.I)),
        NumStrFmt.DEC: __NumFmtInfo__(10, int, "",   re.compile(r'^[\d]+$',         re.I)),
        NumStrFmt.HEX: __NumFmtInfo__(16, hex, "0x", re.compile(r'^(0x)?[\da-f]+$', re.I)),
    }

    def __init__(self, num: int) -> None:
        """
        构造函数
        :param num: 原始输入整形数字
        """
        self._num_ = num

    def ToBinStr(self, min_len: int = 0) -> str:
        """
        输入数字的二进制字符串
        :param min_len: 字符串数字部分最小长度
        :return: 带前缀二进制字符串
        """
        return IntNumString.Num2Str(self._num_, NumStrFmt.BIN, min_len)

    def ToOctStr(self, min_len: int = 0) -> str:
        """
        输入数字的八进制字符串
        :param min_len: 字符串数字部分最小长度
        :return: 带前缀八进制字符串
        """
        return IntNumString.Num2Str(self._num_, NumStrFmt.OCT, min_len)

    def ToDecStr(self, min_len: int = 0) -> str:
        """
        输入数字的十进制字符串
        :param min_len: 字符串数字部分最小长度
        :return: 十进制字符串
        """
        return IntNumString.Num2Str(self._num_, NumStrFmt.DEC, min_len)

    def ToHexStr(self, min_len: int = 0) -> str:
        """
        输入数字的十六进制字符串
        :param min_len: 字符串数字部分最小长度
        :return: 带前缀十六进制字符串
        """
        return IntNumString.Num2Str(self._num_, NumStrFmt.HEX, min_len)

    @classmethod
    def IsBinStr(cls, bin_str: str) -> bool:
        """
        判断输入字符串是否为二进制形式字符串
        :param bin_str: 输入字符串
        :return: True or False
        """
        return cls.IsRightFmt(bin_str, NumStrFmt.BIN)

    @classmethod
    def IsOctStr(cls, oct_str: str) -> bool:
        """
        判断输入字符串是否为八进制形式字符串
        :param oct_str: 输入字符串
        :return: True or False
        """
        return cls.IsRightFmt(oct_str, NumStrFmt.OCT)

    @classmethod
    def IsDecStr(cls, dec_str: str) -> bool:
        """
        判断输入字符串是否为十进制形式字符串
        :param dec_str: 输入字符串
        :return: True or False
        """
        return cls.IsRightFmt(dec_str, NumStrFmt.DEC)

    @classmethod
    def IsHexStr(cls, hex_str: str) -> bool:
        """
        判断输入字符串是否为十六进制形式字符串
        :param hex_str: 输入字符串
        :return: True or False
        """
        return cls.IsRightFmt(hex_str, NumStrFmt.HEX)

    @classmethod
    def IsRightFmt(cls, num_str: str, src_fmt: NumStrFmt) -> bool:
        """
        判断输入的字符串是否为指定形式
        :param num_str: 数字字符串
        :param src_fmt: 字符串类型
        :return: True or False
        """
        if cls._NumFmtInfoDict_[src_fmt].pattern.match(num_str) is None:
            return False
        return True

    @classmethod
    def Str2Num(cls, src_str: str, src_fmt: NumStrFmt) -> int or None:
        """
        字符串转整形数字
        :param src_str: 源字符串
        :param src_fmt: 字符串格式
        :return: 字符串格式正确, 返回数字, 不正确, 返回 None
        """
        if cls.IsRightFmt(src_str, src_fmt) is False:
            return None

        src_cpy = cls.DelPrefix(src_str, src_fmt)

        src_dec: int = cls._NumFmtInfoDict_[src_fmt].decimal
        dec_num: int = int(src_cpy, src_dec)
        return dec_num

    @classmethod
    def Num2Str(cls, src_num: int, str_fmt: NumStrFmt, min_len: int = 0) -> str:
        """
        数字转为指定格式的字符串
        :param src_num: 输入数字
        :param str_fmt: 字符串格式
        :param min_len: 字符串数字部分最小长度
        :return: 带前缀的字符串
        """
        ret_str: str = cls._NumFmtInfoDict_[str_fmt].prefix
        dst_str: str = str(cls._NumFmtInfoDict_[str_fmt].trans_f(src_num))

        if str_fmt is not NumStrFmt.DEC:
            dst_str = dst_str[2:]

        for i in range(len(dst_str), min_len):
            ret_str += '0'
        ret_str += dst_str
        return ret_str

    @classmethod
    def StrFmtTrans(cls, src_str: str, src_fmt: NumStrFmt, dst_fmt: NumStrFmt, min_len: int = 0) -> str:
        """
        字符串格式装换
        :param src_str: 输入数字字符串
        :param src_fmt: 输入数字字符串格式
        :param dst_fmt: 目标数字字符串格式
        :param min_len: 字符串数字部分最小长度
        :return: 目标数字字符串或空字符串
        """
        dec_num: int or None = cls.Str2Num(src_str, src_fmt)
        if dec_num is None:
            return ""

        return cls.Num2Str(dec_num, dst_fmt, min_len)

    @classmethod
    def DelPrefix(cls, src_str: str, src_fmt: NumStrFmt) -> str:
        """
        删除数字字符串前缀
        :param src_str: 输入字符串
        :param src_fmt: 输入字符串格式
        :return: 格式正确则返回
        """
        if cls.IsRightFmt(src_str, src_fmt) is False:
            return src_str

        if cls.HasPrefix(src_str, src_fmt) is True:
            return src_str[2:]
        return src_str
    
    @classmethod
    def HasPrefix(cls, src_str: str, src_fmt: NumStrFmt) -> bool:
        if len(src_str) > 2 and src_str[:2] == cls._NumFmtInfoDict_[src_fmt].prefix:
            return True
        return False


if __name__ == "__main__":
    s = IntNumString(100)
    print(s.ToBinStr())
