from calculator import calculator
import random

class stats_calculator:

    def __init__(self):
        pass

    # 1. Generate a random number without a seed between a range of two numbers - Both Integer and Decimal
    def random_num_int_generator(self):

        rand_num_int = random.randint(1, 10)
        return rand_num_int

    def random_num_float_generator(self):
        rand_num_float = random.uniform(1.0, 10.0)
        return rand_num_float

    # 2. Generate a random number with a seed between a range of two numbers - Both Integer and Decimal
    def random_num_seed_int_generator(self):
        random.seed(9001)
        rand_num_int_seed = random.randint(1, 10)
        return rand_num_int_seed

    def random_num_seed_float_generator(self):
        random.seed(9001)
        rand_num_float_seed = random.uniform(1.0, 10.0)
        return rand_num_float_seed

    # 3. Generate a list of N random numbers with a seed and between a range of numbers - Both Integer and Decimal
    def list_seed_int_generator(self):
        rand_num_int_seed = random.randint(1, 10)
        random.seed(9002)
        lst_int = []
        for i in range(rand_num_int_seed):
            lst_int.append(random.randint(1, 20))
        return lst_int

    def list_seed_float_generator(self):
        rand_num_int_seed = random.randint(1, 10)
        random.seed(9002)
        lst_float = []
        for j in range(rand_num_int_seed):
            lst_float.append(random.uniform(1.0, 20.0))
        return lst_float

    # 4. Select a random item from a list
    def random_item_generator(self, lst):
        rand_item = lst[random.randint(0, len(lst)-1)]
        return rand_item

    # 5. Set a seed and randomly select the same value from a list
    def random_seed_item_generator(self, lst):
        random.seed(30)
        rand_item_same = lst[random.randint(0, len(lst)-1)]
        return rand_item_same

    # 6. Select N number of items from a list without a seed
    def select_range_generator(self, lst):
        select = random.randint(0, len(lst)-1)
        select_list = []
        for i in range(select):
            select_list.append(lst[i])
        return select_list

    # 7. Select N number of items from a list with a seed
    def select_seed_range_generator(self, lst):
        random.seed(20)
        select = random.randint(0, len(lst) - 1)
        select_list_seed = []
        for j in range(select):
            select_list_seed.append(lst[j])
        return select_list_seed

'''
lst = [0, 1, 2, 3, 4, 5, 6]
print(stats_calculator().random_seed_item_generator(lst))
'''