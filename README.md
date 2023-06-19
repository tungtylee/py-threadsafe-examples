# py-threadsafe-examples
python examples for thread safety

## An object example

A simple class contains two lists and a process function. The time for waiting for lock is recorded in the internal list waitTime.

```bash
    python run_objop.py
```

## A joint example for an dictionary of objects

A dictionary class is used for keeping a list of objects and handle multiple threading for getting and deleting objects.

```bash
    python run_objdict.py
```

