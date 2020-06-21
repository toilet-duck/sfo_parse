# sfo_parse
Quick and dirty PSV SFO parser


# Usage:
```
# Assumes 'param.sfo' in same directory as sfo_parse.py
./sfo_parse.py
# Alternatively specify path to param.sfo
./sfo_parse.py /path/to/param.sfo
# Optional --all argument to print parameters aside from TITLExxx
./sfo_parse.py --all
```

# Example output:
```
TITLE: LEGO® MARVEL Super Heroes: Universe in Peril
TITLE_01: LEGO® MARVEL Super Heroes: Universe in Peril
TITLE_02: LEGO® MARVEL Super Heroes : L'Univers en Péril
TITLE_03: LEGO® MARVELl Super Heroes: Universo en peligro
TITLE_04: LEGO® MARVEL Super Heroes: Universum in Gefahr
TITLE_05: LEGO® MARVEL Super Heroes: l'Universo in pericolo
TITLE_06: LEGO® MARVELl Super Heroes: Universe in Peril
TITLE_08: LEGO® MARVEL: Вселенная в опасности
TITLE_14: LEGO® MARVEL Super Heroes: Universe in Peril
TITLE_16: LEGO® MARVEL Super Heroes: Świat w opałach


Languages: Danish, Dutch, English, French, German, Italian, Polish, Russian, Spanish
```

```
# Output with --all
APP_VER: 01.00
ATTRIBUTE: 2097152
ATTRIBUTE2: 0
ATTRIBUTE_MINOR: 18
CATEGORY: gd
CONTENT_ID: EP2475-PCSB01257_00-PERSONA5DEU00000
GC_RO_SIZE: 0
GC_RW_SIZE: 0
PARENTAL_LEVEL: 5
PSP2_DISP_VER: 03.680
PSP2_SYSTEM_VER: 57147392
PUBTOOLINFO: c_date=20180922,sdk_ver=03570000
REGION_DENY: 0
SAVEDATA_MAX_SIZE: 8192
STITLE: P5D
TITLE: Persona 5: Dancing in Starlight
TITLE_ID: PCSB01257
VERSION: 01.01
```
