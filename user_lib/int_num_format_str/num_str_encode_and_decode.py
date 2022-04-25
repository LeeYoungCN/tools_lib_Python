#!/usr/bin/env python3
# coding=utf-8
import math
from typing import Dict, List

from user_lib.int_num_format_str.num_str_format_manager import NumStrFmtEnum as FmtEnum
from user_lib.int_num_format_str.num_str_format_manager import NumStringFormatManager as NumStrFmtMng


class CodeStruct:
    def __init__(self, title: str = "", start: int = 0, end: int = 0) -> None:
        """
        编码方式结构体
        """
        self.title: str = title
        self.start: int = start
        self.end: int = end
        self.val: int = 0

    def __str__(self) -> str:
        min_len = math.ceil((self.end - self.start) / 4)
        hex_str = NumStrFmtMng.Num2Str(self.val, FmtEnum.HEX, min_len)
        return self.title + ": " + hex_str


class NumStrEncodeAndDecode:
    """
    数字型字符串编码与解码
    """
    def __init__(self, num_str: str, str_fmt: FmtEnum, data_st_list: List[CodeStruct], bit_num: int) -> None:
        """
        构造函数
        :param num_str: 数字型字符串
        :param str_fmt: 字符串格式类型
        :param data_st_list: 编码解码结构体数组
        :return: None
        """
        self._bin_str: str = NumStrFmtMng.StrFmtTrans(num_str, str_fmt, FmtEnum.BIN, bit_num)
        self._data_dict: Dict[str, CodeStruct] = {}

        for data_st in data_st_list:
            if self._data_dict.get(data_st.title) is not None:
                continue
            data_copy = CodeStruct(data_st.title, data_st.start, data_st.end)
            if NumStrEncodeAndDecode.Decode(self._bin_str, data_copy) is False:
                continue
            self._data_dict[data_st.title] = data_copy

    def GetVal(self, key: str) -> int or None:
        """
        获取关键字的值
        :param key: 关键字
        :return: 关键字数值值
        """
        if self._data_dict.get(key) is None:
            return None
        return self._data_dict.get(key).val

    def SetVal(self, key: str, val: int or str, num_fmt: FmtEnum = FmtEnum.BIN) -> bool:
        """
        设置关键字的值, 并写入字符串
        :param key: 关键字
        :param val: 要设置值, 数字或数字字符串
        :param num_fmt: 数字字符串的格式
        :return 是否设置成功
        """
        if self._data_dict.get(key) is None:
            return False

        if isinstance(val, str):
            val = NumStrFmtMng.Str2Num(val, num_fmt)

        if val is None:
            return False

        self._data_dict[key].val = val
        self._bin_str = NumStrEncodeAndDecode.Encode(self._bin_str, self._data_dict.get(key))
        return True

    def PrintList(self):
        """
        打印解码后的信息
        """
        for [_, data] in self._data_dict.items():
            print(data)

    def PrintHexFormatStr(self):
        """
        以十六进制形式打印
        """
        print(NumStrFmtMng.StrFmtTrans(self._bin_str, FmtEnum.BIN, FmtEnum.HEX))

    def PrintBinFormatStr(self):
        """
        以二进制形式打印
        """
        print(self._bin_str)

    @classmethod
    def Decode(cls, src_bin_str: str, data: CodeStruct) -> bool:
        """
        解析字符串中的内容
        :param src_bin_str: 原二进制数字字符串
        :param data: 解码信息
        :return 是否解码成功
        """
        str_len: int = len(src_bin_str)
        [start, end] = cls._ConvertRange(data, str_len)
        if start is None or end is None:
            return False
        data.val = NumStrFmtMng.Str2Num(src_bin_str[start: end], FmtEnum.BIN)
        return True

    @classmethod
    def Encode(cls, dst_bin_str: str, data: CodeStruct) -> str or None:
        """
        :param dst_bin_str: 目标二进制字符串
        :param data: 编码信息
        :return 是否设置成功
        """
        src_len = data.end - data.start
        src_str = NumStrFmtMng.Num2Str(data.val, FmtEnum.BIN, src_len)
        src_str = NumStrFmtMng.DelPrefix(src_str, FmtEnum.BIN)
        if src_len != len(src_str):
            return None
        dst_len: int = len(dst_bin_str)
        [start, end] = cls._ConvertRange(data, dst_len)
        if start is None or end is None:
            return None
        ret_str = dst_bin_str[0: start] + src_str + dst_bin_str[end:]
        return ret_str

    @classmethod
    def _ConvertRange(cls, data: CodeStruct, str_len: int) -> int or None:
        """
        范围转换
        :param data: 解码信息
        :param str_len: 字符串长度
        :return 转换后的范围
        """
        return cls._ConvertIndex(data.end, str_len), cls._ConvertIndex(data.start, str_len)

    @classmethod
    def _ConvertIndex(cls, index: int, str_len: int) -> int or None:
        """
        :param index: 待转换的位置
        :param str_len: 字符串长度
        :return 转换后的位置
        """
        if index > str_len:
            return None
        return str_len - index
