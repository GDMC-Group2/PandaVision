
def sort(centers):
    new_centers = []
    min_dis = 1e6
    i = 0
    min_index = -1
    for one_c in centers:
        x = one_c[0]
        y = one_c[1]
        dis = x**2 + y**2
        if dis < min_dis:
            min_dis = dis
            min_index = i
        i += 1

    min_center = centers[min_index]
    new_centers.append(min_center)
    centers[min_index] = []

    for i in range(len(centers)-1):
        min_dis = 1e6
        min_index = -1
        for j in range(len(centers)):
            if len(centers[j]) == 0:
                continue
            dis = (new_centers[i][0]-centers[j][0])**2 + (new_centers[i][1]-centers[j][1])**2
            if dis < min_dis:
                min_dis = dis
                min_index = j

        new_centers.append(centers[min_index])
        centers[min_index] = []

    return new_centers


# if __name__ == '__main__':
#     m = [(300, 80), (120, 90), (10, 29)]
#     print(sort(m))