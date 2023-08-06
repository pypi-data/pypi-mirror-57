from adlib27.autodiff import AutoDiff as AD

a = AD()

x = AD([10, -1, 3.2, 4], index=0, magnitude=2)
y = AD([-2, 0, 1, 100], index=1, magnitude=2)
z = x + y
