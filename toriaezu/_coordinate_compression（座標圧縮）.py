def coordinate_compression(A):
  rank_to_value = {v: i for i, v in enumerate(sorted(set(A)))}
  value_to_rank = {i: v for v, i in rank_to_value.items()}
  #print(value_to_rank)
  B = [0 for _ in range(len(A))]
  for i in range(len(A)):
    B[i] = rank_to_value[A[i]]
  return B, value_to_rank


A = [8, 100, 33, 33, 33, 12, 6, 1211]

# 圧縮する
B, vtor = coordinate_compression(A)
print(B)
print(vtor)
# 復元する
restored_A = [0 for _ in range(len(A))]
for i in range(len(A)):
  restored_A[i] = vtor[B[i]]
print(restored_A)