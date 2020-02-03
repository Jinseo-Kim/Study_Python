de_h = 6
de_m = 30
xhlrms = int(input('퇴근까지의 걸린 시간을 적어주세요(분)'))
rhdqn = int(input('공부 시간을 적어주세요(분)'))
ehrtj = int(input('독서 시간을 적어주세요(분)'))

t_h = xhlrms + de_h
t_m = xhlrms + de_m
def off_work(xhlrms):
    if 60 > xhlrms > 30:
        de_h = de_h+1
        de_m = 0
        de_m = de_m + (xhlrms - 30)
    elif xhlrms > 60:
        if t_m % 60 == 0:
            de_h = t_m // 60
        else:
            de_m = de_m + (xhlrms % 60)
            de_h = de_h + (xhlrms // 60)

    else:
        de_m = t_m
    res = "%d:%d" % (de_h,de_m)
    return res
print(off_work(xhlrms))
