import argparse
import string

# Argument parsing
aparser = argparse.ArgumentParser(prog='myxxd',
                                  description='xxd clone not fully featured')

_ = aparser.add_argument('infile')
arg_cols_action = aparser.add_argument('-c', '--cols', default=16, type=int)

args = aparser.parse_args()

LINE_LENGTH: int = args.cols #pyright: ignore[reportAny]
if LINE_LENGTH > 256:
    raise argparse.ArgumentError(arg_cols_action, 'Maximum number bytes per line is 256')


if __name__ == '__main__':
    infile: str = args.infile #pyright: ignore[reportAny]

    class Line:
        def __init__(self, offset: int, data: bytes) -> None:
            self.offset: int = offset
            self.data: bytes = data
            self.len = len(data)

        def __str__(self) -> str: #pyright: ignore[reportImplicitOverride]
            assert self.len <= LINE_LENGTH or LINE_LENGTH == 0 # data must be up to LINE_LENGTH bytes per line or LINE_LENGTH == 0 (no limit)

            # offset
            out = f'{self.offset:08x}' + ":"
            offset_len = len(out)
            # hex dump
            for idx in range(self.len):
                if idx % 2 == 0:
                    out += ' '
                out += f'{int(self.data[idx]):02x}'

            # padding
            if (LINE_LENGTH == 0 or LINE_LENGTH == self.len):
                pass
            else:
                out = out.ljust(LINE_LENGTH * 2 + offset_len + LINE_LENGTH // 2)
            out += '  '

            # ascii dump
            for c in self.data:
                if chr(c) == '\n':
                    out += '.'
                elif chr(c).isspace():
                    out += ' '
                elif chr(c) in string.printable:
                    out += chr(c)
                else:
                    out += '.'
            return out


    with open(infile, 'rb') as f:
        offset: int = 0
        read_count: int = -1
        data: bytes = b''
        while True:
            if LINE_LENGTH == 0:
                data = f.read()
            else:
                data = f.read(LINE_LENGTH)
            read_count = len(data)
            if read_count == 0:
                break
            line = Line(offset, data)
            print(line)
            offset += read_count
