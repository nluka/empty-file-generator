# empty-file-generator

A simple Python script for generating empty files with specific sizes. Created as a utility for [Ctructure](https://github.com/nluka/Ctructure).

## Usage

`python genfile.py [<fpathname> <fsize>]...`

### fsize

File size is specified by a summation of components. A component can have a [modifier](#component-modifiers) applied to it.

#### Component Modifiers

| Modifier | Description |
| -------- | ----------- |
| g\|G     | Gigabyte    |
| m\|M     | Megabyte    |
| k\|K     | Kilobyte    |

#### Examples

- `1` = 1 byte
- `1K` = 1 kilobyte
- `1m` = 1 megabyte
- `1G` = 1 gigabyte
- `100+2k` = 100 bytes + 2 kilobytes
- `1G+1M+3` = 1 gigabyte + 1 megabyte + 3 bytes
