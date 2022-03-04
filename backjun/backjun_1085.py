x,y,w,h = map(int,input().split())


new_h = h-y
new_w = w-x
print(min(x,y,new_h,new_w))