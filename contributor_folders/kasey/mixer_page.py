import marimo

__generated_with = "0.14.17"
app = marimo.App(
    width="columns",
    app_title="RiptideRemix_mixer",
    layout_file="layouts/mixer_page.grid.json",
)


@app.cell(column=0)
def _():
    import marimo as mo
    mo.image(
        src="/home/jovyan/ohw25_proj_RiptideRemix/Images/logo_flat.jpg",
        alt="placeholder",
        width=1200,
        height=100,
        rounded=True,
        caption=""
    )
    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Welcome to RipTide Remix! {WRITE BLURB ABOUT WHAT THIS IS AND HOW TO INTERACT WITH IT}""")
    return


@app.cell
def _(mo):
    mo.md("""---""")
    return


@app.cell
def _(mo):
    mo.image(
        src="/home/jovyan/ohw25_proj_RiptideRemix/Images/ArtGifs/placeholder.gif",
        alt="placeholder",
        width=1200,
        height=200,
        rounded=False,
        caption=""
    )
    return


@app.cell
def _(mo):
    mo.md("""---""")
    return


@app.cell
def _(mo):
    mo.md(r"""---""")
    return


@app.cell
def _(mo):
    mo.md(r"""---""")
    return


@app.cell
def _(mo):
    checkbox = mo.ui.checkbox(label="Loop audio")
    return (checkbox,)


@app.cell
def _(checkbox, mo):
    mo.hstack([checkbox, mo.md(f"Has value: {checkbox.value}")])
    return


@app.cell
def _(checkbox):
    if checkbox.value:
        print('check!')
    return


@app.cell
def _(mo):
    # a button that when clicked will have its value set to True;
    # any cells referencing that button will automatically run.
    button_addclip = mo.ui.run_button(label='Add to Song')
    button_addclip
    return


@app.cell
def _(mo):
    slider_t = mo.ui.slider(1.0, 60.0, label='Time in Song (s)')
    slider_t
    return


@app.cell
def _(mo):
    slider_f = mo.ui.slider(1, 10, label='Cent. Frequency')
    slider_f
    return


@app.cell
def _(mo):
    slider_amp = mo.ui.slider(1, 10, label='Amplitude (dB)')
    slider_amp
    return


@app.cell
def _(mo):
    dropdown = mo.ui.dropdown(options={'Seismic activity': 1, 'Whale song': 2}, value='Seismic activity')
    return (dropdown,)


@app.cell
def _(dropdown):
    dropdown
    return


@app.cell
def _(dropdown):
    if dropdown.selected_key == 'Seismic activity':
        display = 'seismic event recordings'
    elif dropdown.selected_key == 'Whale song':
        display = 'whale song recordings'
    else:
        display = 'ERROR'

    print(f'Currently displaying {display}')
    return


@app.cell
def _(mo):
    mo.md(r"""What if users had the option to save their song when they were happy with it?""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""asdf""")
    return


@app.cell
def _(mo):
    mo.image(
        src="/home/jovyan/ohw25_proj_RiptideRemix/Images/squirrel.JPG",
        alt="placeholder",
        width=200,
        height=200,
        rounded=False,
        caption=""
    )
    return


@app.cell
def _(mo):
    file_browser = mo.ui.file_browser(
        initial_path="/home/jovyan/ohw25_proj_RiptideRemix/data", multiple=True)
    return (file_browser,)


@app.cell
def _(file_browser):
    file_browser
    return


@app.cell
def _(mo):
    mo.md(r"""## LIBRARY""")
    return


@app.cell
def _(mo):
    mo.md(r"""## -----------------------------------------SOUND MIXER -----------------------------------------------""")
    return


@app.cell
def _(mo):
    mo.md(r"""## CLIP EDITOR""")
    return


@app.cell
def _():
    import numpy as np
    import matplotlib.pyplot as plt
    x = np.linspace(0, 10, 200)
    y = np.sin(x)

    # Create figure and plot
    fig, ax = plt.subplots(figsize=(4, 1))
    ax.plot(x, y, label="sin(x)")
    ax.set_xlabel("x")
    ax.set_ylabel("sin(x)")
    ax.set_title("Original Waveform")
    ax.legend()

    fig 
    return np, plt, x, y


@app.cell
def _(np, plt, x, y):
    x2 = np.linspace(0, 10, 200)
    y2 = np.tan(x)

    # Create figure and plot
    fig2, ax2 = plt.subplots(figsize=(4, 1))
    ax2.plot(x, y, label="sin(x)")
    ax2.set_xlabel("x")
    ax2.set_ylabel("sin(x)")
    ax2.set_title("Your New Waveform")
    ax2.legend()

    fig2
    return


@app.cell
def _(mo):
    mo.md(r"""## NEW SONG""")
    return


@app.cell
def _(plt):
    import matplotlib.patches as patches

    def plot_time_freq_boxes(boxes, 
                             time_range=(0, 60), 
                             freq_range=(0, 20000)):
        """
        Plot time-frequency boxes on a 2D plot with labels and colors.

        Parameters
        ----------
        boxes : list of tuples
            Each tuple = (t_start, t_end, f_start, f_end, label)
        time_range : tuple
            (min_time, max_time) for x-axis
        freq_range : tuple
            (min_freq, max_freq) for y-axis
        """
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.set_facecolor("black")  # black background

        for (t_start, t_end, f_start, f_end, label) in boxes:
            # Pick color based on label
            if label.lower() == "seismic":
                facecolor = "deeppink"
                edgecolor = "hotpink"
            elif label.lower() == "whale":
                facecolor = "purple"
                edgecolor = "violet"
            else:
                facecolor = "gray"
                edgecolor = "lightgray"

            # Draw box
            rect = patches.Rectangle(
                (t_start, f_start), 
                t_end - t_start, 
                f_end - f_start,
                linewidth=1.5, edgecolor=edgecolor, facecolor=facecolor, alpha=0.8
            )
            ax.add_patch(rect)

            # Add label text at the center of the box
            # ax.text(
            #     (t_start + t_end) / 2, 
            #     (f_start + f_end) / 2, 
            #     label, 
            #     color="white", ha="center", va="center", fontsize=9, weight="bold"
            # )

        # Set limits and labels
        ax.set_xlim(time_range)
        ax.set_ylim(freq_range)
        ax.set_xlabel("Time (s)", color="Purple")
        ax.set_ylabel("Frequency (Hz)", color="Purple")
        ax.set_title("MY SONG", color="Purple")

        # White ticks
        ax.tick_params(colors="white")

        return fig


    return (plot_time_freq_boxes,)


@app.cell
def _():
    boxes = [
        (5, 10, 1000, 3000, "seismic"),
        (15, 25, 5000, 7000, "whale"),
        (30, 40, 12000, 15000, "seismic"),
        (42, 50, 2000, 6000, "whale"),
    ]
    return (boxes,)


@app.cell
def _(boxes, plot_time_freq_boxes):
    fig3 = plot_time_freq_boxes(boxes)
    fig3
    return


@app.cell(column=1)
def _(mo):
    gather_button = mo.ui.button(
        value=0, on_click=lambda value: value + 1, label="Gather Data", kind='neutral'
    )
    gather_button
    return


@app.cell
def _(mo):
    mix_button = mo.ui.button(
        value=0, on_click=lambda value: value + 1, label="Mix Sounds", kind='neutral'
    )
    mix_button
    return


@app.cell
def _(mo):
    educate_button = mo.ui.button(
        value=0, on_click=lambda value: value + 1, label="Learn More", kind='neutral'
    )
    educate_button
    return


@app.cell
def _(mo):
    about_button = mo.ui.button(
        value=0, on_click=lambda value: value + 1, label="About the Team", kind='neutral'
    )
    about_button
    return


if __name__ == "__main__":
    app.run()
