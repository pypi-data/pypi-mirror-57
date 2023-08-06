from op_cli.functions.app import app

@app.register()
def add(x, y):
    """Add values"""
    # call api
    return x + y

@app.register()
def minus(x, y):
    return x-y