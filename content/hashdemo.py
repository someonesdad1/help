import hashlib
from color import t

d = (hashlib.md5, hashlib.sha1, hashlib.sha224, hashlib.sha256, hashlib.sha384,
     hashlib.sha512, hashlib.sha3_224, hashlib.sha3_256, hashlib.sha3_384,
     hashlib.sha3_512, hashlib.shake_128, hashlib.shake_256, hashlib.blake2b,
     hashlib.blake2s)
if 1:
    t.alg = t.sky
    t.hd1 = t.ornl
    t.hd2 = t.redl
if 1:
    print('Hashlib hashes of b"a", showing size of the hex digest\n')
    t.print(f"{t.alg}Hash name")
    nbytes = 32
    t.print(f"Number of hex digits:  {t.hd1} normal{t.n}, {t.hd2}shake ({2*nbytes} chosen)")
    print("For shake, you can choose a bytes length of 0 to 255\n")
for alg in d:
    m = alg()
    m.update(b"a")
    # Get algorithm name
    s = str(alg)
    if "<built-in" in s:
        s = s.replace("<built-in function openssl_", "").replace(">", "")
    else:
        s = s.replace("<class '_blake2.", "").replace("'>", "")
    t.print(f"{t.sky}{s}", end=" ")
    try:
        hd = m.hexdigest()
        t.print(hd, f"{t.hd1}<{len(hd)}>")
    except Exception:
        hd = m.hexdigest(nbytes)
        t.print(hd, f"{t.hd2}<{len(hd)}>")
