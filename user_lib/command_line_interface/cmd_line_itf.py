#!/usr/bin/env python3
# coding=utf-8
from typing import Dict


class CmdLineItf:
    """
    命令行类
    """
    def __init__(self, name: str, info: str) -> None:
        self._name: str = name
        self._description: str = info
        self._sub_cli: Dict[str, CmdLineItf] = {}
        self._prefix: str = ""

    def RunCli(self) -> None:
        """
        运行命令行
        """
        while True:
            input_str = input("%s/%s-> :" % (self._prefix, self._name))

            if input_str == "":
                continue
            elif input_str == "quit" or input_str == "exit":
                return
            elif input_str == "--help" or input_str == "?":
                self._ShowInfo()
            elif self._sub_cli.get(input_str) is not None:
                self._sub_cli.get(input_str).RunCli()
            elif self.ProcInput(input_str) is False:
                print("input error: %s" % input_str)

    def SetPrefix(self, prefix: str) -> None:
        """
        设置显示前缀
        """
        self._prefix = prefix

    def AddSubCli(self, sub_cli):
        """
        添加子命令行
        """
        self._sub_cli[sub_cli.Name] = sub_cli
        sub_cli.SetPrefix(self._prefix + "/" + self._name)

    def _ShowInfo(self):
        """
        打印信息
        """
        print(self._name, self._description)
        for sub_cli in self._sub_cli.values():
            print(sub_cli.Name, sub_cli.Description)

    @property
    def Name(self):
        """
        类名称
        """
        return self._name

    @property
    def Description(self) -> str:
        """
        类描述
        """
        return self._description

    def ProcInput(self, input_str: str) -> bool:
        """
        输入处理函数, 自行实现
        """
        return False
