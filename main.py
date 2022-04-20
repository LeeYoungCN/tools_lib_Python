import sys
from tools.can_frame import CanFrame

def main():
    input_str = ""
    for i in range(1, len(sys.argv)):
        input_str += sys.argv[i]
    can_frame_decode = CanFrame(input_str)
    can_frame_decode.Print()

# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    main()

