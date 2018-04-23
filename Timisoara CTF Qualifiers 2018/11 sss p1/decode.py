points = ((1, 0x4612c90f5d8cd5d616193257336d92af1f66df92443b4ee69f5c885f0173ad80113844e393d194e3),
          (2, 0x8c25921e46b03e48b7cbe94c3267f41adf618abd16422f660b59df6fae81e8aff2242852be33db49),
          (3, 0xd2385b2d2fd3a6bb597ea041316255869f5c35e7e8490fe5775736805b9023dfd3100bc1e89621af))

m = points[1][1] - points[0][1]
s = points[0][1] - m
d = bytearray.fromhex(hex(s)[2:]).decode()
print(d)