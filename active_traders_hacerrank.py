def mostActive(customers):
    store = dict()
    res = []
    for i in customers:
        for i in store:
            store[i] += 1
        else:
            store[i] = 1

    for i in store.items():
        if (i[1] / len(customers)) * 100 > 5 or (len(customers) * 5) / 100 >= 5:
            if (i[1] / len(customers)) * 100 >= (len(customers) * 5) / 100 >= 5 or (i[1] / len(customers)) * 100 >= 5:
                res.append(i[0])
    return sorted(res)


if __name__ == '__main__':
    n = int(input())
    customers = []
    for i in range(n):
        cust_name = input()
        customers.append(cust_name)
    result = mostActive(customers)
    print(result)