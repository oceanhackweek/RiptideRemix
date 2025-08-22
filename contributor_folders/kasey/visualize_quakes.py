import marimo

__generated_with = "0.14.17"
app = marimo.App(
    width="columns",
    app_title="RiptideRemix_mixer",
    layout_file="layouts/visualize_quakes.grid.json",
)


@app.cell(column=0)
def _():
    import platform
    from pathlib import Path

    # Detect OS and set project root accordingly
    if platform.system() == "Windows":
        basePath = Path("C:/Users/kasey/Desktop/ohw25_proj_RiptideRemix")
    else:
        basePath = Path("/home/jovyan/ohw25_proj_RiptideRemix")
    return (basePath,)


@app.cell
def _(basePath):
    import marimo as mo
    mo.image(
        src= basePath / "Images" / "logo_flat.jpg",
        alt="placeholder",
        width=1200,
        height=100,
        rounded=True,
        caption=""
    )
    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Hey there! Welcome to your data playground! Here, you can dive into different datasets and discover how researchers pick the perfect spots to study. Check out the “Seismic” and “Hydrophone” sections below to start exploring our data.""")
    return


@app.cell
def _(mo):
    mo.md("""---""")
    return


@app.cell
def _(basePath, mo):
    mo.image(
        src= basePath / "Images" /  "ArtGifs" / "placeholder.gif",
        alt="placeholder",
        width=900,
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
def _(basePath, mo):
    mo.image(
        src= basePath / "Images" / "welcome.png",
        alt="placeholder",
        width=115,
        height=115,
        rounded=False,
        caption=""
    )
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
    nav_menu = mo.nav_menu({
        "/": "Mix Sounds",  # internal
        "/learn": "Learn More",  # internal
        "/about": "About the Team",  # internal
        "/quake": "Gather More Data"
    })
    nav_menu
    return


@app.cell(column=2)
def _(mo):
    mo.md(r"""## LIBRARY""")
    return


@app.cell
def _(mo):
    mo.md(r"""Scientists use Ocean Bottom Seismometers (OBS) to measure vibrations in the seafloor, monitor earthquakes, and study the movement of Earth beneath the ocean. This helps researchers understand geological processes in ways that aren’t visible from the surface. In this interface, anyone can look at the data through these seismic waveforms produced from different Earthquakes.""")
    return


@app.cell
def _(mo):
    category_dropdown = mo.ui.dropdown(options={'Seismic Event': 1, 'Cetacean Call': 2, 'Anthropogenic': 3, 'Other': 3}, value = 'Cetacean Call')
    return (category_dropdown,)


@app.cell
def _(mo):
    mo.md(r"""### Choose Your Clip:""")
    return


@app.cell
def _(mo):
    mo.md(r"""Earthquake:""")
    return


@app.cell
def _(mo):
    mo.md(r"""Network:""")
    return


@app.cell
def _(mo):
    mo.md(r"""Sensor:""")
    return


@app.cell
def _(mo):
    mo.md(r"""Clip:""")
    return


@app.cell
def _(category_dropdown):
    category_dropdown
    return


@app.cell
def _(category_dropdown, mo):
    if category_dropdown.selected_key == 'Seismic Event':
        labelopts = {'Japan2011': 1, 'Alaska2021': 2, 'Russia2025': 3}
    elif category_dropdown.selected_key == 'Cetacean Call':
        labelopts = {'Mysticetes': 1, 'Odontocetes': 2} # replace with available_wavs/cetacean
    elif category_dropdown.selected_key == 'Anthropogenic':
        labelopts = {"All": 1}
    else:
        labelopts = {"All": 1} # replace with available_wavs/other

    class_dropdown = mo.ui.dropdown(options=labelopts)
    class_dropdown
    return (class_dropdown,)


@app.cell
def _(basePath, category_dropdown, class_dropdown, mo, os):
    if category_dropdown.selected_key == 'Cetacean Call':
        sc_path = basePath / "Library" / "Cetacean" / class_dropdown.selected_key
        sc_list = os.listdir(sc_path)
        sc_dict = {sc_list[i]: i for i in range(len(sc_list))}
    elif category_dropdown.selected_key == 'Seismic Event':
        sc_dict = {"All": 1}
    else:
        sc_dict = {"All": 1}
    sc_dropdown = mo.ui.dropdown(options=sc_dict)
    return (sc_dropdown,)


@app.cell
def _(sc_dropdown):
    sc_dropdown
    return


@app.cell
def _(basePath, category_dropdown, class_dropdown, os, sc_dropdown):
    if category_dropdown.selected_key == 'Cetacean Call':
        clips_path = basePath / "Library" / "Cetacean" / class_dropdown.selected_key / sc_dropdown.selected_key
        clip_list = os.listdir(clips_path)
    elif category_dropdown.selected_key == 'Seismic Event':
        clips_path = basePath / "Library" / "Seismic" / class_dropdown.selected_key
        clip_list = os.listdir(clips_path)
    elif category_dropdown.selected_key == 'Anthropogenic':
        clips_path = basePath / "Library" / "Anthropogenic" 
        clip_list = os.listdir(clips_path)
    else:
        clips_path = basePath / "Library" / "Other"
        clip_list = os.listdir(clips_path)
    return clip_list, clips_path


@app.cell
def _(clip_list, mo):
    clip_dict = {clip_list[i]: i for i in range(len(clip_list))}
    clip_dropdown = mo.ui.dropdown(options=clip_dict)
    clip_dropdown
    return (clip_dropdown,)


@app.cell
def _(clip_dropdown, clips_path, os):
    selected_audio = os.path.join(clips_path, clip_dropdown.selected_key)
    return


@app.cell
def _(mo):
    button_preview = mo.ui.run_button(label="Update preview")
    button_preview
    return (button_preview,)


@app.cell
def _(
    audio_selected,
    button_preview,
    ipd,
    np,
    process_one_clip_to_add,
    slider_amp,
    slider_loops,
    slider_pitch,
    slider_speed,
    slider_t,
):
    if button_preview.value and audio_selected:
        print(
            audio_selected,
            slider_t.value,
            slider_loops.value,
            slider_amp.value,
            slider_pitch.value,
            slider_speed.value
        )
        sr_clip, d_clip = process_one_clip_to_add(
            audio_selected,
            slider_t.value,
            slider_loops.value,
            slider_amp.value,
            slider_pitch.value,
            slider_speed.value
        )
        if np.max(np.abs(d_clip)) > 0:
            d_clip = d_clip / np.max(np.abs(d_clip))

        ipd.display(ipd.Audio(data=d_clip, rate=sr_clip))
    return


@app.cell
def _():
    # Keep this for displaying wave form, spectrogram, and explanation of clip
    # stretch goal for educational piece
    # button_libraryadd = mo.ui.run_button(label='Explore this sound')
    # button_libraryadd
    return


@app.cell
def _(d_final, plot_waveform, sr_resampled):
    fig = plot_waveform(d_final, sr_resampled)
    fig
    return


@app.cell
def _(d_final, plot_spectrogram, sr_selected):
    fig2 = plot_spectrogram(d_final, sr_selected)
    fig2
    return


@app.cell(column=3)
def _(mo):
    mo.md(r"""## Seismogram from Ocean Bottom Seismometers (OBS)""")
    return


@app.cell
def _(slider_amp, slider_loops, slider_pitch, slider_speed, slider_t):
    start_time = slider_t.value
    ptch = slider_pitch.value
    spd = slider_speed.value
    # ptch_speed = slider_speed.value
    loops = slider_loops.value # slider_f.value
    loudness = slider_amp.value

    return


@app.cell
def _(mo):
    # start time
    slider_t = mo.ui.slider(0, 20.0, label='Time in Song (s)')
    slider_t 
    return (slider_t,)


@app.cell
def _(mo):
    # ptch_spd
    slider_speed = mo.ui.slider(0, 2, .1, label='Speed', value=1)
    slider_speed
    return (slider_speed,)


@app.cell
def _(mo):
    # reporpoise
    slider_pitch = mo.ui.slider(0, 2, .1, label='Pitch', value=1)
    slider_pitch
    return (slider_pitch,)


@app.cell
def _(mo):
    # loudness
    slider_amp = mo.ui.slider(0, 2, .1, label='Amplitude (dB)', value=1)
    slider_amp
    return (slider_amp,)


@app.cell
def _(mo):
    # loops
    slider_loops = mo.ui.slider(0, 15, 1, label='Loops', value=1)
    slider_loops
    return (slider_loops,)


@app.cell(column=4)
def _(mo):
    mo.md(r"""## HYDROPHONES""")
    return


@app.cell
def _(mo):
    mo.md(r"""This section isn't quite ready yet. Come back later to see how ecologists can use hydrophones to understand biological populations.""")
    return


@app.cell(column=5)
def _(basePath, mo):
    mo.image(
        src=  basePath / "Images" / "logo.png",
        alt="Logo",
        width=100,
        height=100,
        rounded=True,
        caption=""
    )
    return


@app.cell
def _(mo):
    mo.md(r"""Thanks for your RiptideRemix! Your journey through sound has brought together whispers, rumbles, and songs of the sea. We’re so glad you set sail with us. Now take your creation, share it, and let it ripple out into the world.""")
    return


@app.cell
def _(mo):
    mo.md(r"""Derya""")
    return


@app.cell
def _(mo):
    mo.md(r"""Mattie""")
    return


@app.cell
def _(mo):
    mo.md(r"""Isabelle""")
    return


@app.cell
def _(mo):
    mo.md(r"""Kasey""")
    return


@app.cell
def _(mo):
    mo.md(r"""Oluwatofunmi""")
    return


@app.cell
def _(mo):
    mo.md(r"""Dwight""")
    return


@app.cell(column=6)
def _(mo):
    mo.md(r"""# Underlying Python functions""")
    return


if __name__ == "__main__":
    app.run()
