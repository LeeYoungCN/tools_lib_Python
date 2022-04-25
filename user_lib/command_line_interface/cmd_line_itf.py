#!/usr/bin/env python3
# coding=utf-8
from typing import Dict


class CmdLineItf:
    def __init__(self, name: str, info: str) -> None:
        self._name: str = name
        self._description:str = info
        self._sub_cli: Dict[str, CmdLineItf] = {}
        self._prefix: str = ""

    def RunCli(self) -> None:
        while True:
            input_str = input("%s/%s-> :" % (self._prefix, self._name))
            if input_str == "quit" or input_str == "exit":
                return
            elif self._sub_cli.get(input_str) is not None:
                self._sub_cli.get(input_str).RunCli()
            elif input_str == "--help" or input_str == "?":
                self._ShowInfo()
            else:
                if self.ProcInput(input_str) is False:
                    print("input error: %s"%(input_str))

    def SetPrefix(self, prefix: str) -> None:
        self._prefix = prefix

    def RegCli(self, sub_cli):
        self._sub_cli[sub_cli.Name] = sub_cli
        sub_cli.SetPrefix(self._prefix + "/" + self._name)

    def _ShowInfo(self):
        print(self._name, self._description)
        for sub_cli in self._sub_cli.values():
            print(sub_cli.Name, sub_cli.Description)

    @property
    def Name(self):
        return self._name

    @property
    def Description(self) -> str:
        return self._description

    def ProcInput(self, input_str: str) -> bool:
        return False
