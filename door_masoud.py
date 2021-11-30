w, h = map(int, input().split())
wm, hm = map (int, input().split())

if w >= wm and h >= hm:
    print("yes")
elif w != wm or h != hm:
    print("no")