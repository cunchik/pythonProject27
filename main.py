def binary_search(value):
    lst = range (1,101)
    lst = sorted(lst)
    scl = False
    a = 0
    x = len(lst)-1


    while scl != True and (a <= x ):
        midl = (a+x)//2
        if value > lst[midl]:
            a = midl + 1
        elif value <  lst[midl]:
            x = midl - 1
        else:
            scl = True
            a = midl
            tor=midl
            x = a
    if scl == True:
        return f'число найдено ,{tor}'
    else:
        return F"что то не так "


print(binary_search(100))

def bubble_sort(bubble_list: list):
    bubbles_len = len(bubble_list)
    for bubbles in range(bubbles_len):
        for bubble in range(0, bubbles_len-bubbles-1):
            if bubble_list[bubble] > bubble_list[bubble + 1]:
                bubble_list[bubble], bubble_list[bubble+1] = bubble_list[bubble+1], bubble_list[bubble]
    return bubble_list

