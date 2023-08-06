# uname2

Print certain system information. With no OPTION, same as -s.

## Install


```shell
pip install uname2
```

## Usage


```shell
    PS E:\code\uname2> uname2 --help
    Usage: uname2 [OPTIONS]

    Print certain system information.  With no OPTION, same as -s.

    Options:
    -a, --all             print all information
    -s, --kernel-name     print the kernel name
    -n, --nodename        print the network node hostname
    -r, --kernel-release  print the kernel release
    -v, --kernel-version  print the kernel version
    -m, --machine         print the machine hardware name
    -p, --processor       print the hardware platform or "unknown"
    --help                Show this message and exit.
    PS E:\code\uname2>
```

## Example

```
    PS E:\code\uname2> uname2
    Windows
    PS E:\code\uname2> uname2 -a
    Windows DESKTOP-OR9GS4G 10 10.0.16299 AMD64 Intel64 Family 6 Model 60 Stepping 3, GenuineIntel
    PS E:\code\uname2> uname2 -snrvmp
    Windows DESKTOP-OR9GS4G 10 10.0.16299 AMD64 Intel64 Family 6 Model 60 Stepping 3, GenuineIntel
    PS E:\code\uname2>
```

## Releases


### 0.1.3 2019/12/10

- Fix document.

### 0.1.1 2019/08/08

- Fix package strcture and remove src folder.

### 0.1.0 2019/04/04

- First release.