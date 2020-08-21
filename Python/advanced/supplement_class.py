class My_list(object):
    my_list = ["apples", "bananas", "pears"]

    def __init__(self, snack='chocolate'):
        self.snack = snack

    def __str__(self):
        return 'My list: {}'.format(', '.join(self.my_list))

    def __repr__(self):
        return self.__str__()

    def in_my_list(self, item):
        if item in self.my_list:
            return "got it"
        else:
            return "nope"

    def snack_check(self):
        return self.snack in self.my_list


class caps_list(My_list):
    def in_my_list(self, item):
        response = super().in_my_list(item)
        return response.upper()


shouty = caps_list()
print(shouty.in_my_list('apples'))  # true
print(shouty.in_my_list('chocolate'))  # false
