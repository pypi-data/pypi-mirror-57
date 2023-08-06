====
CLI
====

See all commands
----------------

```bash

$ python main.py commands

```

# Run commands

```bash

$ python main.py run "add(4,minus(4,5))"

```

# Add function

1. Create a python file in ``functions`` directory
2. Add the main functon entry
3. Import ``from .app import app``
4. Add the ``@app.register()`` to the function
