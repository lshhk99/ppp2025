import math
for i in range(0,91):
    f_r=math.radians(i)
    f_s=math.sin(f_r)
    f_c = math.cos(f_r)
    f_t=math.tan(f_r)
    print("="*70)
    print(f"{i}일때 rad {f_r:.4f}, sin {f_s:.4f}, cos {f_c:.4f}, tan {f_t:.4f}")
print("="*70)
