# python basics: calling method of a class + static/non-static


class MongoUtil:
    var1 = 10

    def start(self, param1: int):
        print('in start :: {}'.format(param1))

    def call_start(self):
        self.start(10)


obj = MongoUtil()
obj.call_start()

print(obj.var1)
