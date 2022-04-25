#!/usr/bin/env python3
# coding=utf-8

import sys

from main_cli import MainCli
from tools.can_frame_cli import CanFrameCli


def main() -> None:
    main_cli = MainCli()
    main_cli.RegCli(CanFrameCli())
    main_cli.RunCli()


if __name__ == '__main__':
    main()
