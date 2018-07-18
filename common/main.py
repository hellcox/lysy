import config
from common.NetworkRequest import NetworkRequest
from tool.Tool import Tool


class Main:
    def __init__(self):
        self.r = NetworkRequest()
        self.interface = Tool.read_json('interface')
        self.api = Tool.read_json('api')
        self.token = self.r.request_token()

    def run(self):
        for interface in self.interface['interfaces']:
            action_file = Tool.read_json(interface['addr'])
            actions = action_file['actions']
            datas = action_file['data']
            for action in actions:
                print(action)



if __name__ == '__main__':
    main = Main()
    main.run()
