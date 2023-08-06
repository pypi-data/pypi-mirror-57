from op_cli.functions.app import app

@app.register()
def grte(x, y):
    return x > y

@app.register()
def lste(x, y):
    return x < y
