#!/usr/bin/env python3
# coding=utf-8
from tools.can_frame import CanFrame
from user_lib.command_line_interface.cmd_line_itf import CmdLineItf

class CanFrameCli(CmdLineItf):
    def __init__(self):
        super().__init__("CanFrame", "CAN帧解析")

    def ProcInput(self, input_str: str):
        tmp = CanFrame(input_str)
        tmp.Print()
