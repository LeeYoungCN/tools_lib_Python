#!/usr/bin/env python3
# coding=utf-8

import math
import re
from enum import Enum
from pyclbr import Function
from typing import Dict


class NumStrFmtEnum(Enum):
    BIN = 2,
    OCT = 8,
    DEC = 10,
    HEX = 16,


class __NumFmtInfo__:
    def __init__(self, decimal: int, trans_f, prefix: str, pattern: re.Pattern) -> None:
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


class NumStringFormatManager:
    _NumFmtInfoDict_: Dict[NumStrFmtEnum, __NumFmtInfo__] = {
        NumStrFmtEnum.BIN: __NumFmtInfo__(2, bin, "0b", re.compile(r'^(0b)?[0-1]+$', re.I)),
        NumStrFmtEnum.OCT: __NumFmtInfo__(8, oct, "0o", re.compile(r'^(0o)?[0-7]+$', re.I)),
        NumStrFmtEnum.DEC: __NumFmtInfo__(10, int, "", re.compile(r'^[\d]+$', re.I)),
        NumStrFmtEnum.HEX: __NumFmtInfo__(16, hex, "0x", re.compile(r'^(0x)?[\da-f]+$', re.I)),
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
        return NumStrFmtEnum.Num2Str(self._num_, NumStrFmtEnum.BIN, min_len)

    def ToOctStr(self, min_len: int = 0) -> str:
        """
        输入数字的八进制字符串
        :param min_len: 字符串数字部分最小长度
        :return: 带前缀八进制字符串
        """
        return NumStrFmtEnum.Num2Str(self._num_, NumStrFmtEnum.OCT, min_len)

    def ToDecStr(self, min_len: int = 0) -> str:
        """
        输入数字的十进制字符串
        :param min_len: 字符串数字部分最小长度
        :return: 十进制字符串
        """
        return NumStrFmtEnum.Num2Str(self._num_, NumStrFmtEnum.DEC, min_len)

    def ToHexStr(self, min_len: int = 0) -> str:
        """
        输入数字的十六进制字符串
        :param min_len: 字符串数字部分最小长度
        :return: 带前缀十六进制字符串
        """
        return NumStrFmtEnum.Num2Str(self._num_, NumStrFmtEnum.HEX, min_len)

    @classmethod
    def GetNumStrZeros(cls, str_fmt: NumStrFmtEnum, str_len: int) -> str:
        return cls._NumFmtInfoDict_[str_fmt].prefix + "0" * str_len

    @classmethod
    def IsBinStr(cls, bin_str: str) -> bool:
        """
        判断输入字符串是否为二进制形式字符串
        :param bin_str: 输入字符串
        :return: True or False
        """
        return cls.IsRightFmt(bin_str, NumStrFmtEnum.BIN)

    @classmethod
    def IsOctStr(cls, oct_str: str) -> bool:
        """
        判断输入字符串是否为八进制形式字符串
        :param oct_str: 输入字符串
        :return: True or False
        """
        return cls.IsRightFmt(oct_str, NumStrFmtEnum.OCT)

    @classmethod
    def IsDecStr(cls, dec_str: str) -> bool:
        """
        判断输入字符串是否为十进制形式字符串
        :param dec_str: 输入字符串
        :return: True or False
        """
        return cls.IsRightFmt(dec_str, NumStrFmtEnum.DEC)

    @classmethod
    def IsHexStr(cls, hex_str: str) -> bool:
        """
        判断输入字符串是否为十六进制形式字符串
        :param hex_str: 输入字符串
        :return: True or False
        """
        return cls.IsRightFmt(hex_str, NumStrFmtEnum.HEX)

    @classmethod
    def IsRightFmt(cls, num_str: str, src_fmt: NumStrFmtEnum) -> bool:
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
    def Str2Num(cls, src_str: str, src_fmt: NumStrFmtEnum) -> int or None:
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
    def Num2Str(cls, src_num: int, str_fmt: NumStrFmtEnum, min_len: int = 0) -> str:
        """
        数字转为指定格式的字符串
        :param src_num: 输入数字
        :param str_fmt: 字符串格式
        :param min_len: 字符串数字部分最小长度
        :return: 带前缀的字符串
        """
        ret_str: str = cls._NumFmtInfoDict_[str_fmt].prefix
        dst_str: str = str(cls._NumFmtInfoDict_[str_fmt].trans_f(src_num))

        if str_fmt is not NumStrFmtEnum.DEC:
            pre_len = len(cls._NumFmtInfoDict_[str_fmt].prefix)
            dst_str = dst_str[pre_len:]
        dst_str_len = len(dst_str)
        if min_len > dst_str_len:
            ret_str += "0" * (min_len - dst_str_len)
        ret_str += dst_str
        return ret_str

    @classmethod
    def StrFmtTrans(cls, src_str: str, src_fmt: NumStrFmtEnum, dst_fmt: NumStrFmtEnum, min_len: int = 0) -> str:
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

        min_len = max(min_len, cls.CalDstMinLen(src_str, src_fmt, dst_fmt))
        return cls.Num2Str(dec_num, dst_fmt, min_len)

    @classmethod
    def CalDstMinLen(cls, src_str: str, src_fmt: NumStrFmtEnum, dst_fmt: NumStrFmtEnum) -> int:
        if cls.IsRightFmt(src_str, src_fmt) is False:
            return 0

        if dst_fmt == NumStrFmtEnum.DEC:
            return 0

        src_times = math.log2(cls._NumFmtInfoDict_[src_fmt].decimal)
        dst_times = math.log2(cls._NumFmtInfoDict_[dst_fmt].decimal)

        return math.ceil(cls.GetNumPartLen(src_str, src_fmt) * src_times / dst_times)

    @classmethod
    def GetNumPartLen(cls, num_str: str, num_fmt: NumStrFmtEnum) -> int:
        """
        计算数字部分的长度
        :param num_str: 输入数字字符串
        :param num_fmt: 输入数字字符串格式
        :return 数字部分的长度
        """
        if cls.IsRightFmt(num_str, num_fmt) is False:
            return 0

        if cls.HasPrefix(num_str, num_fmt) is True:
            prefix_len = len(cls._NumFmtInfoDict_[num_fmt].prefix)
            return len(num_str) - prefix_len
        return len(num_str)

    @classmethod
    def DelPrefix(cls, src_str: str, src_fmt: NumStrFmtEnum) -> str:
        """
        删除数字字符串前缀
        :param src_str: 输入字符串
        :param src_fmt: 输入字符串格式
        :return: 格式正确则返回对应字符串, 否则返回原字符串
        """
        if cls.IsRightFmt(src_str, src_fmt) is False:
            return src_str

        if cls.HasPrefix(src_str, src_fmt) is True:
            prefix_len = len(cls._NumFmtInfoDict_[src_fmt].prefix)
            return src_str[prefix_len:]

        return src_str

    @classmethod
    def HasPrefix(cls, src_str: str, src_fmt: NumStrFmtEnum) -> bool:
        if len(src_str) > 2 and src_str[:2] == cls._NumFmtInfoDict_[src_fmt].prefix:
            return True
        return False
