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
    mo.md(r"""---""")
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
    mo.md(r"""---""")
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


@app.cell(column=2)
def _(mo):
    mo.md(r"""## LIBRARY""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    Ahoy, explorer! 
    You’ve stumbled upon the Ocean Sound Library, a treasure chest of the sea’s secrets. Here you’ll hear glaciers groaning, icebergs cracking, whales singing their heart out, and even the occasional crocodile making mischief.

    Ready to set sail? Just click “Explore this sound” to dive deeper into any recording and uncover the stories hidden in the waves.
    """
    )
    return


@app.cell
def _(mo):
    soundclass_dropdown = mo.ui.dropdown(options={'Seismic Event': 1, 'Cetacean Call': 2}, value='Seismic Event')
    return (soundclass_dropdown,)


@app.cell
def _(soundclass_dropdown):
    soundclass_dropdown
    return


@app.cell
def _(mo):
    mo.md(r"""### Choose Your Clip:""")
    return


@app.cell
def _(mo):
    mo.md(r"""Category:""")
    return


@app.cell
def _(mo):
    mo.md(r"""Class:""")
    return


@app.cell
def _(mo):
    mo.md(r"""Subclass/Network:""")
    return


@app.cell
def _(mo):
    mo.md(r"""Station:""")
    return


@app.cell
def _(mo):
    mo.md(r"""Clip:""")
    return


@app.cell
def _(mo, soundclass_dropdown):
    if soundclass_dropdown.selected_key == 'Seismic Event':
        labelopts = {'Japan Earthquake, 2011': 1, 'Russia Earthquake, 2019': 2, 'Other Seismic Event, Year': 3}
    elif soundclass_dropdown.selected_key == 'Cetacean Call':
        labelopts = {'Mysticetes': 1, 'Odontocetes': 2}
    else:
        labelopts = {'Beans': 1, 'Toast': 2}

    class_dropdown = mo.ui.dropdown(options=labelopts)
    class_dropdown
    return (class_dropdown,)


@app.cell
def _(class_dropdown, mo, soundclass_dropdown):
    if soundclass_dropdown.selected_key == 'Seismic Event':
        labelopts_sc = {'P-Wave': 1, 'S-Wave': 2, 'Love Wave': 3, 'Raliegh Wave': 4}
    elif soundclass_dropdown.selected_key == 'Cetacean Call' and class_dropdown.selected_key == 'Mysticetes':
        labelopts_sc = {'Blue Whale': 1, 'Humpback Whale': 2}
    elif soundclass_dropdown.selected_key == 'Cetacean Call' and class_dropdown.selected_key == 'Odontocetes':
        labelopts_sc = {'Orca': 1, 'Sperm Whale': 2}
    else:
        labelopts_sc = {'Beans': 1, 'Toast': 2}

    subclass_dropdown = mo.ui.dropdown(options=labelopts_sc)
    subclass_dropdown
    return (subclass_dropdown,)


@app.cell
def _(class_dropdown, mo, soundclass_dropdown, subclass_dropdown):
    if soundclass_dropdown.selected_key == 'Seismic Event' and subclass_dropdown.selected_key == 'P-Wave':
        labelopts_sites = {'Site1': 1, 'Site2': 2}
    if soundclass_dropdown.selected_key == 'Seismic Event' and subclass_dropdown.selected_key == 'S-Wave':
        labelopts_sites = {'Site1': 1, 'Site2': 2}
    elif soundclass_dropdown.selected_key == 'Cetacean Call' and class_dropdown.selected_key == 'Mysticetes' and subclass_dropdown.selected_key == 'Blue Whale':
        labelopts_sites = {'Site1': 1, 'Site2': 2}
    elif soundclass_dropdown.selected_key == 'Cetacean Call' and class_dropdown.selected_key == 'Odontocetes':
        labelopts_sites = {'Site1': 1, 'Site2': 2}
    else:
        labelopts_sites = {'Beans': 1, 'Toast': 2}

    site_dropdown = mo.ui.dropdown(options=labelopts_sites)
    site_dropdown
    return


@app.cell
def _(mo):
    clip_dropdown = mo.ui.dropdown(options={'Clip1': 1, 'Clip2': 2}, value='Clip1')
    clip_dropdown
    return


@app.cell
def _(mo):
    button_libraryplay = mo.ui.run_button(label='Play')
    button_libraryplay
    return


@app.cell
def _(mo):
    button_libraryadd = mo.ui.run_button(label='Explore this sound')
    button_libraryadd
    return


@app.cell
def _(mo):
    library_loop = mo.ui.checkbox(label="Loop audio")
    library_loop
    return


@app.cell(column=3)
def _(mo):
    slider_t = mo.ui.slider(1.0, 60.0, label='Time in Song (s)')
    slider_t
    return


@app.cell
def _(mo):
    slider_speed = mo.ui.slider(1, 10, label='Speed')
    slider_speed
    return


@app.cell
def _(mo):
    slider_f = mo.ui.slider(1, 10, label='Central Frequency (Hz)')
    slider_f
    return


@app.cell
def _(mo):
    slider_amp = mo.ui.slider(1, 10, label='Amplitude (dB)')
    slider_amp
    return


@app.cell
def _(mo):
    editor_loop = mo.ui.checkbox(label="Loop audio")
    editor_loop
    return


@app.cell
def _(mo):
    # a button that when clicked will have its value set to True;
    # any cells referencing that button will automatically run.
    button_addclip = mo.ui.run_button(label='Add to Symphony')
    button_addclip
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    Each clip is yours to play with—speed it up to make it race, slow it down to let it drift, shift the frequency to soar into the skies or rumble in the deep, and adjust the amplitude to whisper or roar.

    When you’ve crafted the sound just the way you like, click “Add to Song” to weave it into your grand ocean symphony.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""### Acoustic Modifiers""")
    return


@app.cell(column=4)
def _(mo):
    mo.md(r"""## MIXER""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    Here’s where your ocean symphony comes together. Watch your creation take shape through the waveform (the rolling tides of your song) and the spectrogram (a colorful map of its hidden patterns).

    Listen, layer, and fine-tune until your piece feels just right. When you’re ready to set it free, click Export to send your song sailing off into the world.
    """
    )
    return


if __name__ == "__main__":
    app.run()
