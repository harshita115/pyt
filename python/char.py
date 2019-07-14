n = input()
strig = input()
queryc = int(input())
for a in range(queryc):
  pos = int(input())
  count = 0
  sstrin = list(strig)
  element = sstrin[pos-1]
  i = (pos-1)-1
  type(i)
  while i>=0:
    if sstrin[i] == element:
      count = count + 1
    i=i-1
  print (count)
