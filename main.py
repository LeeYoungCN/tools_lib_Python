#!/usr/bin/env python3
# coding=utf-8

from main_cli import MainCli
from tools.can_frame.can_frame_cli import CanFrameCli


def main() -> None:
    main_cli = MainCli()
    main_cli.AddSubCli(CanFrameCli())
    main_cli.RunCli()


if __name__ == '__main__':
    main()
