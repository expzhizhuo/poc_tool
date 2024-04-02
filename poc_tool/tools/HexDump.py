"""
@Project ：pocsuite3测试文件 
@File    ：HexDump.py
@IDE     ：PyCharm 
@Author  ：zhizhuo
@Date    ：2024/4/2 12:59 
"""


def hex_dump(file_path: str, bytes_per_line: int = 16, lines: int = None) -> str:
    """
    xxd 查看文件hex和decode数据
    :param file_path:文件路径
    :param bytes_per_line:每行显示的字节大小，默认16字节
    :param lines:显示的行数，默认全部
    :return:
    """
    try:
        with open(file_path, 'rb') as file:
            offset = 0
            lines_read = 0
            hex_data = '\n'
            while True:
                if lines is not None and lines_read >= lines:
                    break
                chunk = file.read(bytes_per_line)
                if not chunk:
                    break
                hex_values = ' '.join(f'{byte:02x}' for byte in chunk)
                printable = ''.join(chr(byte) if 32 <= byte <= 127 else '.' for byte in chunk)
                hex_data += f'{offset:08x}: {hex_values:<{bytes_per_line * 3}} {printable}\n'
                offset += bytes_per_line
                lines_read += 1
            return hex_data
    except FileNotFoundError:
        raise Exception(f"Error: File {file_path} not found. Please check whether the file path is correct.")
    except Exception as e:
        raise Exception(f"Error: {e}")
