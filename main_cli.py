#!/usr/bin/env python3
# coding=utf-8

from user_lib.command_line_interface.cmd_line_itf import CmdLineItf

class MainCli(CmdLineItf):
    def __init__(self):
        super().__init__("main", "各工具命令行入口")
