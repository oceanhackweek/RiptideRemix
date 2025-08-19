import marimo

__generated_with = "0.14.17"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # Welcome to Riptide Remix

    The goal of this project is to create a web interface where users can combine marine soundscape audio clips (e.g. whale calls, earthquakes, ships) to create music. Think GarageBand, but with marine science!
    """
    )
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
