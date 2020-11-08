from calculator import calculator
import random
import collections

class stats_calculator:

    def __init__(self):
        pass

    # RANDOM FUNCTIONS
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

    # DESCRIPTIVE STATISTICS FUNCTIONS

    # mean
    def mean(self, lst):
        sum = 0
        for i in lst:
            sum = calculator().add(sum, i)
        mean_value = calculator().divide(sum, len(lst))
        return mean_value

    # median
    def median(self, lst):
        middle = int(len(lst)/2)
        if len(lst) % 2 == 0:
            other_num = calculator().subtract(middle, 1)
            return (calculator().add(lst[middle], lst[other_num])/2)
        else:
            return lst[middle]

    # mode
    def mode(self, lst):
        data = collections.Counter(lst)
        data_list = dict(data)
        max_value = max(list(data.values()))
        mode_val = [num for num, freq in data_list.items() if freq == max_value]
        if len(mode_val) == len(lst):
            return 0
        else:
            return int(mode_val[0])
    # variance
    def variance(self, lst):
        sum = 0
        for i in lst:
            sum = calculator().add(sum, i)
        sq = calculator().square(sum)
        div = calculator().divide(sq, len(lst)) #20,533.5
        sqsum = 0
        for j in lst:
            tempsq = calculator().square(j)
            sqsum = sqsum + tempsq #51,633
        sub = sqsum - div #31,099.5
        newnum = calculator().subtract(len(lst), 1)
        variance_result = calculator().divide(sub, newnum)
        return variance_result

    # standard deviation
    def standard_deviation(self, lst):
        var = stats_calculator().variance(lst)
        sd = calculator().squareroot(var)
        return sd

    # z-score
    def z_score(self, lst):
        mean = stats_calculator().mean(lst)
        sd = stats_calculator().standard_deviation(lst)
        zlist = []
        for i in lst:
            diff = calculator().subtract(i, mean)
            zscore = calculator().divide(diff, sd)
            zlist.append(zscore)
        return zlist

'''
lst = [3, 9, 17, 21, 98, 203]
print(stats_calculator().z_score(9, lst))
'''

