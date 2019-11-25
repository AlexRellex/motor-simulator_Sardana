from sardana.pool.pool import Pool

class CreatePool():
    def __init__(self):
        self.pool = Pool('tango//localhost/10000/Sardana/test01/Pool/pool/test01/1')
        #self.pool.init(tango//localhost/10000)

    def get_pool_name(self):
        self.pool.get_full_name()


def main():
    swimmingpool = CreatePool()
    print(swimmingpool.get_pool_name())

if __name__ == '__main__':
    main()