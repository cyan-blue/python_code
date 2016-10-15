def get_people_circle(path_detail):
    exist_point = []
    next_path = 0
    count = 0
    exist_index = []
    while path_detail[next_path] not in exist_point:
        current_index = next_path
        # print exist_point, "exist"
        # print next_path, "next"
        next_path = path_detail[current_index]
        exist_point.append(path_detail[current_index])
        exist_index.append(current_index)

        # print "next", next_path
        if count > 10:
            break
        count += 1
    print next_path,"nnn"
    exist_index.append(next_path)
    # print path_detail[next_path], "fff"
    return exist_index, next_path


def get_circle_num(a, i):
    result = []
    for one in a:
        if one >= i:
            result.append(one)
    return len(set(result))


print get_people_circle([1, 3, 1, 5, 2, 1])
print get_circle_num(get_people_circle([1, 3, 1, 5, 2, 1])[0], get_people_circle([1, 3, 1, 5, 2, 1])[1])
#
# print get_people_circle([1, 2, 0, 2, 3])
# print get_circle_num(get_people_circle([1, 2, 0, 2, 3])[0], get_people_circle([1, 2, 0, 2, 3])[1])
# print get_circle_num(get_people_circle([1, 2, 3, 2, 1])[0], get_people_circle([1, 2, 3, 2, 1])[1])
