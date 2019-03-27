x = ''
y = ''
with open('v.zip', 'rb') as f:
    x = f.read()
    y = [x]
print(repr(x))
# for i in range(len(y) / 20 + 1):
#     print([y[i * 20:(i + 1) * 20]])
# sys.exit(0)
