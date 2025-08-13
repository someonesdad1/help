'''
Print out examples of bit manipulations
'''
if 1:   # Header
    from color import t
    t.title = t.ornl
    t.topic = t.purl
    t.bin = t.trql
if 1:   # Functions
    def GetByte(value=0):
        a = bytearray(1)
        a[0] = value
        return a
    def Show(a, name="a"):
        t.print(f"{ind}{name} is {t.bin}{fbin(a)}")

if __name__ == "__main__":  
    ind, n = " "*2, 1
    fbin = lambda x: f"{t.bin}0b{int(x[0]):08b}"
    if 1:   # Intro
        t.print(f"{t.title}Examples of python bit manipulations")
        print(f"{ind}Bit indexes in a byte go from 0 to 7 with 0 the rightmost bit")
        print()
    if 1:   # Setting a bit
        t.print(f"{t.topic}Setting a bit:  set bit 2 to 1")
        print(f"{ind}Method:  shift a 1 appropriately and OR with the byte")
        a = GetByte()
        t.print(f"{ind}a = bytearray({n}) --> {a} = {t.bin}{fbin(a)}")
        a[0] |= (1 << 2)
        t.print(f"{ind}a[0] |= (1 << 2)) --> {fbin(a)}")
    if 1:   # Getting a bit
        t.print(f"{t.topic}Getting a bit:  get bit 2")
        print(f"{ind}Method:  shift a 1 appropriately and AND with the byte, then use bool() of result ")
        Show(a)
        a[0] &= (1 << 2)
        t.print(f"{ind}bool(a[0] &= (1 << 2)) --> {bool(a[0])}")
        print(f"{ind}Note bit 0 is False:")
        a = GetByte(4)
        Show(a)
        a[0] &= (1 << 0)
        t.print(f"{ind}bool(a[0] &= (1 << 0)) --> {bool(a[0])}")
    if 1:   # Clearing a bit
        t.print(f"{t.topic}Clearing a bit:  set bit 2 to 0")
        print(f"{ind}Method:  shift a 1 appropriately, invert, and AND with the byte")
        a = GetByte(4)
        Show(a)
        a[0] &= ~(1 << 2)
        t.print(f"{ind}a[0] &= ~(1 << 2) --> {fbin(a)}")
    if 1:   # Toggling a bit
        t.print(f"{t.topic}Toggling a bit:  toggle bit 2")
        print(f"{ind}Method:  shift a 1 appropriately and XOR with the byte")
        a = GetByte(4)
        Show(a)
        a[0] ^= (1 << 2)
        t.print(f"{ind}a[0] ^= (1 << 2) --> {fbin(a)}")
        print(f"{ind}Do it again")
        Show(a)
        a[0] ^= (1 << 2)
        t.print(f"{ind}a[0] ^= (1 << 2) --> {fbin(a)}")
