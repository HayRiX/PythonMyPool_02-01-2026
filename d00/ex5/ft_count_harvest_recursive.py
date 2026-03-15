def ft_count_harvest_recursive():
    count = int(input("Days until harvest: "))
    i = 1

    def recursive(count, i):
        if i > count:
            return
        print("Day", i)
        i += 1
        recursive(count, i)
    recursive(count, i)
    print("Harvest time!")
