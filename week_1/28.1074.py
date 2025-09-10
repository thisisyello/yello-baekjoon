def zzz(n, row, col, count):
    half_point = 2 ** (n - 1)

    if n == 0:
        return count
    else:
        if row < half_point and col < half_point:
            qudra = 1
        elif row < half_point and col >= half_point:
            qudra = 2
            col = col - half_point
        elif row >= half_point and col < half_point:
            qudra = 3
            row = row - half_point
        elif row >= half_point and col >= half_point:
            qudra = 4
            row = row - half_point
            col = col - half_point
    count += (qudra - 1) * (half_point ** 2)

    return zzz(n-1, row, col, count)
    
n, row, col = map(int, input().split())
    
print(zzz(n, row, col, 0))