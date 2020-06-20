#!/usr/bin/env python3

import binascii
import struct
import sys


def main():
    if len(sys.argv) > 1:
        file = sys.argv[1]
    else:
        print("No file specified. Assuming 'param.sfo' in current directory.")
        file = 'param.sfo'

    try:
        with open(file, 'rb') as f:
            data = f.read()
    except FileNotFoundError:
        sys.exit("No 'param.sfo' file provided.")

    # read HEADER_BYTES=20
    HEADER_BYTES=20
    header_raw = data[0:20]
    header = struct.unpack('<4s4BIII', header_raw)
#    print(header)

    # Variable and data references
    name_table_start = header[5]
    data_table_start = header[6]
    n_params = header[7]

    # Addressing
    def_table_bytes = 16 * n_params
    name_table_bytes = data_table_start - name_table_start
    def_table_padding = name_table_start - HEADER_BYTES - def_table_bytes

    # Ensure sufficient space for the parameter definition data
    assert def_table_padding >= 0

    #---
    # Parse definition table
    def_table = []

    file_seek_index = HEADER_BYTES

    for e in range(n_params):
        def_rec_raw = data[file_seek_index:file_seek_index+16]
        def_record = struct.unpack('<HHIII', def_rec_raw)
        def_table.append(def_record)
        file_seek_index += 16

    # Read past any padded space between the definition and name tables
    # TODO: May be able to eliminate this
    data[file_seek_index:file_seek_index+def_table_padding]
    file_seek_index += def_table_padding

    #---
    # Parse parameter names
    param_names = []
    for e in range(n_params):
        try:
            p_name_bytes = def_table[e+1][0] - def_table[e][0]
        except IndexError:
            p_name_bytes = name_table_bytes - def_table[e][0]
        p_name = data[file_seek_index:file_seek_index+p_name_bytes]
        file_seek_index += p_name_bytes
        param_names.append(p_name.rstrip(b'\x00'))


    #---
    # Parse parameter values
    param_values = []
    for e in range(n_params):
        # TODO: Maybe use def_table[4] (addressing) rather than byte size
        v_type  = def_table[e][1]
        v_bytes = def_table[e][2]
        v_total = def_table[e][3]

        value_raw = data[file_seek_index:file_seek_index+v_total]
        file_seek_index += v_total

        if v_type in (0x0204, 0x0004):
            value = value_raw.rstrip(b'\x00')
        elif v_type == 0x0404:
            # Reverse index to read as little-endian
            # NOTE: Method for raw string to int?
            value_ascii = binascii.hexlify(value_raw[::-1])
            value = int(value_ascii, 16)
        else:
            print('unknown format')

        param_values.append(value)

    params = dict(zip(param_names, param_values))

    for k, v in params.items():
        if k.startswith(b"TITLE") and k != b"TITLE_ID":
            print("{}: {}".format(k.decode("utf-8"), v.decode("utf-8")))

    lang_map = {
        b"00": "Japanese",
        b"01": "English",
        b"02": "French",
        b"03": "Spanish",
        b"04": "German",
        b"05": "Italian",
        b"06": "Dutch",
        b"07": "Portuguese",
        b"08": "Russian",
        b"09": "Korean",
        b"10": "Chinese (Traditional)",
        b"11": "Chinese (Simplified)",
        b"12": "Finnish",
        b"13": "Swedish",
        b"14": "Danish",
        b"15": "Norwegian",
        b"16": "Polish",
        b"17": "Portuguese",
        b"18": "English",
        b"19": "Turkish",
        b"20": "Spanish",
        b"21": "Arabic",
        b"22": "French",
        b"23": "Czech",
        b"24": "Hungarian",
        b"25": "Greek",
        b"26": "Romanian",
        b"27": "Thai",
        b"28": "Vietnamese",
        b"29": "Indonesian",
    }

    langs = set(["English"])
    for key in params:
        _, _, lang_code = key.partition(b'_')
        if lang_code and lang_code.isdigit():
            try:
                langs.add(lang_map[lang_code])
            except KeyError:
                print("Unsupported language code: {}".format(lang_code))

    print("\n\nLanguages: {}".format(", ".join(sorted(langs))))

if __name__ == '__main__':
    main()
