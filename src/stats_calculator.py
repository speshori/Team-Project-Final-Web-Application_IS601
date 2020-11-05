from calculator import calculator
import random

class stats_calculator:

    def __init__(self):
        pass

    def random_generator(self):
        # 1. Generate a random number without a seed between a range of two numbers - Both Integer and Decimal
        rand_num_int = random.randint(1, 10)
        rand_num_float = random.uniform(1.0, 10.0)

        # 2. Generate a random number with a seed between a range of two numbers - Both Integer and Decimal
        random.seed(9001)
        rand_num_int_seed = random.randint(1, 10)
        random.seed(9001)
        rand_num_float_seed = random.uniform(1.0, 10.0)
        random.seed(9002)

        # 3. Generate a list of N random numbers with a seed and between a range of numbers - Both Integer and Decimal
        lst_int = []
        lst_float = []
        for i in range(rand_num_int):
            lst_int.append(random.randint(1, 20))
        for j in range(rand_num_int):
            lst_float.append(random.uniform(1.0, 20.0))

        # 4. Select a random item from a list

        random.seed(30)
        rand_item = lst_int[random.randint(0, rand_num_int-1)]

        # 5. Set a seed and randomly.select the same value from a list
        random.seed(30)
        rand_item_same = lst_int[random.randint(0, rand_num_int-1)]

        # 6. Select N number of items from a list without a seed
        select = random.randint(0, rand_num_int-1)
        select_list = []
        for i in range(select):
            select_list.append(lst_int[i])

        # 7. Select N number of items from a list with a seed
        random.seed(20)
        select = random.randint(0, rand_num_int - 1)
        select_list_seed = []
        for j in range(select):
            select_list_seed.append(lst_int[j])

