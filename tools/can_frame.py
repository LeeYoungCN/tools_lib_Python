#!/usr/bin/env python3
# coding=utf-8
import sys
from os.path import dirname,abspath
project_path = dirname(dirname(abspath(__file__)))
sys.path.append(project_path)

from typing import List
from user_lib.int_num_format_str.num_str_encode_and_decode import  NumStrEncodeAndDecode as NumSreEncDec
from user_lib.int_num_format_str.num_str_encode_and_decode import CodeStruct
from user_lib.int_num_format_str.num_str_format_manager    import NumStrFmtEnum as FmtEnum

CODE_ST_LIST: List[CodeStruct] = [
    CodeStruct("协议类型", 23, 29),
    CodeStruct("目的地址" ,16, 23),
    CodeStruct("原地址",    9, 16),
    CodeStruct("QR标志位",  8,  9),
    CodeStruct("命令字",    0,  6)
]

class CanFrame:
    def __init__(self, hex_Str:str, data_list: List[CodeStruct] = CODE_ST_LIST) -> None:
        self._recv_frame = NumSreEncDec(hex_Str, FmtEnum.HEX, data_list, 32)
        self._send_farme = NumSreEncDec(hex_Str, FmtEnum.HEX, data_list, 32)
        self._Convert()
    
    def _Convert(self):
        self._send_farme.SetVal("原地址",   self._recv_frame.GetVal("目的地址"))
        self._send_farme.SetVal("目的地址", self._recv_frame.GetVal("原地址"))
        self._send_farme.SetVal("QR标志位", 1 -self._recv_frame.GetVal("QR标志位"))

    def Print(self):
        print("发送帧: ")
        self._recv_frame.PrintHexFormatStr()
        self._recv_frame.PrintList()
        print("\n回复帧: ")
        self._send_farme.PrintHexFormatStr()
        self._send_farme.PrintList()
