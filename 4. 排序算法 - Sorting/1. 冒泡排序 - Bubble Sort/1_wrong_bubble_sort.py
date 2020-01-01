def bubbLe_sort(L):
    '''演示错误的冒泡算法'''
    n = len(L)
    if n <= 1:
        return

    for i in range(n-1):  # 共需要n-1次冒泡操作

        # 每次冒泡操作都遍历整个列表的元素，即使后面已经排序好的元素也会比较，完全是在浪费时间
        for j in range(n-1):  # j 表示列表的下标，j不能取值n-1，否则L[j+1]会下标越界
            if L[j] > L[j+1]:
                L[j], L[j+1] = L[j+1], L[j]


if __name__ == '__main__':
    L1 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print('Before: ', L1)
    bubbLe_sort(L1)
    print('After: ', L1)

    # Output:
    # Before:  [54, 26, 93, 17, 77, 31, 44, 55, 20]
    # After:  [17, 20, 26, 31, 44, 54, 55, 77, 93]

    '''
    压力测试，timeit.timeit() 如果from __main__ import L，结果好像不对，所以在函数内初始化相同的L：

    from timeit import timeit

    def bubbLe_sort():
        # import random
        # gen = (random.randint(1, 100) for i in range(100))  # 产生100个 1-99 范围内的随机整数
        # L = list(gen)
        L = [96, 2, 65, 23, 47, 58, 8, 48, 69, 92, 34, 83, 93, 47, 45, 55, 95, 15, 92, 24, 64, 19, 29, 55, 35, 48, 39, 29, 63, 94, 99, 38, 50, 10, 10, 93, 74, 27, 74, 44, 29, 81, 85, 86, 74, 30, 50, 50, 12, 12, 38, 75, 41, 87, 80, 97, 16, 48, 65, 69, 83, 71, 28, 9, 64, 69, 27, 74, 74, 86, 40, 69, 79, 79, 77, 100, 53, 72, 77, 16, 8, 36, 41, 58, 59, 29, 46, 79, 81, 66, 8, 35, 60, 52, 2, 82, 2, 36, 79, 66]

        n = len(L)
        for i in range(n-1):
            for j in range(n-1):
                if L[j] > L[j+1]:
                    L[j], L[j+1] = L[j+1], L[j]

        return L


    print('Bubble sort function run 1000 times, cost: ', timeit('bubbLe_sort()', 'from __main__ import bubbLe_sort', number=1000), 'seconds.')


    # Output:
    # Bubble sort function run 1000 times, cost:  2.900782099 seconds.
    '''
