# recursion
# 1. 상자 안을 확인한다.
# 2. 만약 상자를 발견하면 1단계로 간다.
# 3. 만약 열쇠를 발견하면 작업 종료!


def look_for_key(box):
    for item in box:
        if item.is_a_box():
            look_for_key(item)  # 재귀
        elif item.is_a_key():
            print("열쇠를 찾았어요!")


# factorial function


def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x - 1)
