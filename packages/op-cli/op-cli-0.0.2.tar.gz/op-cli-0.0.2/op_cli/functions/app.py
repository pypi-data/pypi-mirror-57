import sys

import requests
class CLI():
    def __init__(self):
        self.func_map = {}

    def register(self, name=None):
        def func_wrapper(func):
            _name = name if name else func.__name__
            self.func_map[_name] = func
            return func

        return func_wrapper

    def call_command(self):
        command = sys.argv[1]
        command = self.call_registered(command)
        return command

    def run_command(self, command):
        try:
            res = eval(command, self.func_map)
        except NameError as e:
            print("No such command is found: {} ".format(str(e)))
            return
        except SyntaxError as e:
            print("Command SyntaxError: {} ".format(str(e)))
            return

        return res

    def get_command(self, name=None):
        func = self.func_map.get(name, None)
        if func is None:
            print("No such command is found: {} ".format(str(e)))
            
        return func


app = CLI()

@app.register()
def add(x, y):
    """Add values"""
    # call api
    return x + y

@app.register()
def minus(x, y):
    return x-y

@app.register()
def grte(x, y):
    return x > y

@app.register()
def lste(x, y):
    return x < y


@app.register()
def pretify(json):
    return json.keys()

@app.register()
def jobs(q):
    url = f"https://indreed.herokuapp.com/api/jobs/?q={q}"
    req = requests.get(url)
    if req.status_code == 200:
        return req.json()

@app.register()
def rand(min=100, max=1000):
    """
    rand()
    """
    url = f"https://jvnyl60l6b.execute-api.eu-west-2.amazonaws.com/prod/add-number-generator?min={min}&max={max}"
    req = requests.get(url)
    return int(req.content.decode("utf-8"))
