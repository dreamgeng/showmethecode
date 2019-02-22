# 0001:
# 做为 Apple Store App 独立开发者，你要搞限时促销，
# 为你的应用生成激活码（或者优惠券），
# 使用 Python 如何生成 200 个激活码（或者优惠券）
import random
import string


forSelect = string.ascii_letters + string.digits


def generate_code(count, length):
    for x in range(count):
        Re = ""
        for y in range(length):
            Re += random.choice(forSelect)
        print(Re)


if __name__ == '__main__':
    generate_code(200, 10)
