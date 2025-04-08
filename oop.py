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
        r"""
        # 🧱 Introduction to OOP

        Python supports object-oriented programming. Here's how you define a class and create objects.
        """
    )
    return


@app.cell
def _():
    # code
    class Dog:
        def __init__(self, name):
            self.name = name

        def bark(self):
            print(f"{self.name} says woof!")

    # Try it out
    my_dog = Dog("Buddy")
    my_dog.bark()
    return Dog, my_dog


@app.cell
def _(mo):
    mo.md(
        """
        ## 🧠 Functions in Python
        #
        Functions help you organize and reuse code. Here's a basic example:
        """
    )
    return


@app.cell
def _():
    def greet(name):
        return f"Hello, {name}!"

    print(greet("Alicia"))
    return (greet,)


@app.cell
def _(mo):
    mo.md(
        """
        ## 🧰 Methods in Classes

        Methods are functions defined inside classes. They usually act on instance data.
        """
    )
    return


@app.cell
def _():
    class Counter:
        def __init__(self):
            self.count = 0

        def increment(self):
            self.count += 1

        def show(self):
            print(f"Current count is {self.count}")

    c = Counter()
    c.increment()
    c.increment()
    c.show()
    return Counter, c


if __name__ == "__main__":
    app.run()
