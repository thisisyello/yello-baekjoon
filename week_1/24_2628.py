width, height = map(int, input().split())
line_count = int(input())

w_cut = [0, width]
h_cut = [0, height]
a = []
b = []

for i in range(line_count):
    cut_way, cut_line = map(int, input().split())
    if cut_way == 0:
       h_cut.append(cut_line)
    else:
        w_cut.append(cut_line)

w_cut.sort()
h_cut.sort()

for i in range(1, len(w_cut)):
    a.append(w_cut[i] - w_cut[i-1])


for i in range(1, len(h_cut)):
    b.append(h_cut[i] - h_cut[i-1])

print(max(a) * max(b))

