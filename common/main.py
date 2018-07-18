import config
from common.NetworkRequest import NetworkRequest
from tool.Tool import Tool


class Main:
    def __init__(self):
        self.r = NetworkRequest()
        self.interface = Tool.read_json('interface')
        self.api = Tool.read_json('api')
        pass

    def read(self):
        pass

    def run(self):
        print(self.interface)
        print(self.interface)
        pass


if __name__ == '__main__':
    main = Main()
    main.run()
