#!/usr/bin/env python3
# coding=utf-8
import math
from typing import Dict, List
from NumStringFormatManager import NumStringFormatManager as NumStrFmtMng
from NumStringFormatManager import NumStrFmtEnum

class CodeStruct:
    def __init__(self, title: str = "", start: int = 0, end: int = 0) -> None:
        self.title: str = title
        self.start: int = start
        self.end:   int = end
        self.val:   int = 0

    def __str__(self) -> str:
        min_len = math.ceil((self.end - self.start) / 4)
        hex_str = NumStrFmtMng.Num2Str(self.val, NumStrFmtEnum.HEX, min_len)
        return self.title + ": " + hex_str


class NumStrEncodeAndDecode:
    """
    数字型字符串编码与解码
    """
    def __init__(self, num_str: str, str_fmt: NumStrFmtEnum, data_st_list: List[CodeStruct]) -> None:
        """
        构造函数
        :param num_str: 数字型字符串
        :param str_fmt: 字符串格式类型
        :param data_st_list: 编码解码结构体数组
        """
        self._bin_str: str = NumStrFmtMng.StrFmtTrans(num_str, str_fmt, NumStrFmtEnum.BIN)
        self._data_dict: Dict[str, CodeStruct] = {}

        for data_st in data_st_list:
            if self._data_dict.get(data_st.title) is not None:
                continue
            if NumStrEncodeAndDecode.Decode(self._bin_str, data_st) is False:
                continue
            self._data_dict[data_st.title] = data_st


    def GetVal(self, key: str) -> int or None:
        if self._data_dict.get(key) is None:
            return None
        return self._data_dict.get(key).val

    def SetVal(self, key: str, val: int) -> bool:
        if self._data_dict.get(key) is None:
            return False
        self._data_dict.get(key).val = val
        return True

    @classmethod
    def Decode(cls, bin_str: str, data: CodeStruct) -> bool:
        bin_str: str = NumStrFmtMng.DelPrefix(bin_str, NumStrFmtEnum.BIN)
        str_len: int = len(bin_str)
        [start, end] = cls.GetRange(data, str_len)
        if start is None or end is None:
            return False
        data.val = NumStrFmtMng.Str2Num(bin_str[start: end], NumStrFmtEnum.BIN)
        return True

    @classmethod
    def Encode(cls, data: CodeStruct, dst_bin_str: str) -> str or None:
        src_len = data.end - data.start
        src_str = NumStrFmtMng.Num2Str(data.val, NumStrFmtEnum.BIN, src_len)[2:]
        if src_len != len(src_str):
            return None
        dst_len: int = len(dst_bin_str)
        [start, end] = cls.GetRange(data, dst_len)
        if start is None or end is None:
            return None
        ret_str = dst_bin_str[0: start] + src_str + dst_bin_str[end:]
        return ret_str

    @classmethod
    def GetRange(cls, data: CodeStruct, str_len: int) -> int or None:
        return cls.IndexConvert(data.end, str_len), cls.IndexConvert(data.start, str_len)

    @classmethod
    def IndexConvert(cls, index: int, str_len: int) -> int or None:
        if index > str_len:
            return None
        return str_len - index
