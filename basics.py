import marimo

__generated_with = "0.12.4"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md(
        """

        # 🐍 Welcome to Python Basics!
        # In this notebook, we'll cover:
        # - Basic data types
        # - Control flow (conditionals and loops)
        # - Intro to object-oriented programming (OOP)

        """
    )
    return


@app.cell
def _():
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        ## 🔢 Data Types in Python

        Python has several built-in data types. The most commonly used are:

        - Integers: `int`
        - Floating point numbers: `float`
        - Text: `str`
        - Boolean: `bool`
        - Lists: `list`
        - Dictionaries: `dict`

        """
    )
    return


@app.cell
def _():
    # code
    # Try editing and running this cell!
    my_int = 42
    my_float = 3.14
    my_str = "Hello, world!"
    my_bool = True
    my_list = [1, 2, 3, 4]
    my_dict = {"name": "Alice", "age": 30}

    print(type(my_int))
    print(type(my_float))
    print(type(my_str))
    print(type(my_bool))
    print(type(my_list))
    print(type(my_dict))

    return my_bool, my_dict, my_float, my_int, my_list, my_str


@app.cell
def _(mo):
    mo.md(
        r"""
        ## ⚙️ Control Flow

        Python uses `if`, `elif`, and `else` for decision making.
        Try changing the value of `number` below and running the cell.

        """
    )
    return


@app.cell
def _():
    # code
    number = 15

    if number > 20:
        print("Greater than 20")
    elif number == 20:
        print("Exactly 20")
    else:
        print("Less than 20")

    return (number,)


@app.cell
def _(mo):
    mo.md(
        r"""
        ## 🔁 Loops

        Python supports `for` and `while` loops.
        Here's a simple `for` loop to print items in a list:

        """
    )
    return


@app.cell
def _():
    items = ["apple", "banana", "cherry"]

    for item in items:
        print(f"I like {item}")

    return item, items


@app.cell
def _():
    # Try a while loop!
    count = 0
    while count < 5:
        print("Counting:", count)
        count += 1

    return (count,)


if __name__ == "__main__":
    app.run()
