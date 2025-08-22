import marimo

__generated_with = "0.14.17"
app = marimo.App(
    width="columns",
    app_title="RiptideRemix_mixer",
    layout_file="layouts/mixer_page.grid.json",
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
    mo.md(
        r"""
    Welcome aboard, sound adventurer! You’ve just discovered RiptideRemix, where the ocean’s voice becomes your instrument. From the haunting songs of whales to the crackle of shifting ice, every sound in our Ocean Sound Library is a piece of the sea’s secret symphony. Your journey is simple: explore, play, and create. Start by diving into any recording—listen closely, tweak it, shape it, and make it your own. Once you’ve crafted your perfect soundscape, layer your favorites together to build a song as wild and free as the ocean itself.

    Ready to make some waves? Let’s dive in.
    """
    )
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


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""asdf""")
    return


@app.cell
def _(basePath, mo):
    mo.image(
        src= basePath / "Images" / "welcome.png",
        alt="placeholder",
        width=75,
        height=75,
        rounded=False,
        caption=""
    )
    return


@app.cell
def _(basePath, mo):
    file_browser = mo.ui.file_browser(
        initial_path= basePath / "data", multiple=True)
    return


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
    Ahoy, explorer! Here lies a treasure chest of the sea’s secrets. Drift through our collection and discover glaciers groaning, icebergs cracking, whales singing their hearts out, and even the occasional mischievous crocodile.

    Click “Explore this sound” to dive deeper into any recording and uncover the stories hidden in the waves.
    """
    )
    return


@app.cell
def _(mo):
    soundclass_dropdown = mo.ui.dropdown(options={'Anthropogenic': 1, 'Cetacean Call': 2, 'Seismic Event': 3})
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
        labelopts = {'Japan 2011': 1, 'Alaska 2021': 2, 'Russia 2025': 3, 'Misc': 4}
    elif soundclass_dropdown.selected_key == 'Cetacean Call':
        labelopts = {'Mysticetes': 1, 'Odontocetes': 2} # replace with available_wavs/cetacean
    else:
        labelopts = {} # replace with available_wavs/other

    class_dropdown = mo.ui.dropdown(options=labelopts)
    class_dropdown
    return (class_dropdown,)


@app.cell
def _(class_dropdown, mo, soundclass_dropdown):
    if soundclass_dropdown.selected_key == 'Seismic Event':
        labelopts_sc = {}
    elif soundclass_dropdown.selected_key == 'Cetacean Call' and class_dropdown.selected_key == 'Mysticetes':
        labelopts_sc = {'Bowhead whale': 1, 'Humpback whale': 2}
    elif soundclass_dropdown.selected_key == 'Cetacean Call' and class_dropdown.selected_key == 'Odontocetes':
        labelopts_sc = {'Orca': 1, 'Sperm whale': 2}
    elif soundclass_dropdown.selected_key == 'Other':
        labelopts_sc = {}
    else:
        labelopts_sc = {'Beans': 1, 'Toast': 2}

    subclass_dropdown = mo.ui.dropdown(options=labelopts_sc)
    subclass_dropdown
    return (subclass_dropdown,)


@app.cell
def _(class_dropdown, os, soundclass_dropdown, subclass_dropdown):
    if soundclass_dropdown.selected_key == 'Cetacean Call':
        clips_path = os.path.join('ohw25_proj_RiptideRemix', 'Library', 'Cetacean', class_dropdown.selected_key, subclass_dropdown.selected_key)
        clip_list = os.listdir(clips_path)
    elif soundclass_dropdown.selected_key == 'Seismic Event':
        clips_path = os.path.join('ohw25_proj_RiptideRemix', 'Library', 'Seismic', class_dropdown.selected_key)
        clip_list = os.listdir(clips_path)
    else:
        clips_path = os.path.join('ohw25_proj_RiptideRemix', 'Library', soundclass_dropdown.selected_key)
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
    return (selected_audio,)


@app.cell
def _(ipd, selected_audio):
    ipd.Audio(selected_audio)
    return


@app.cell
def _():
    # Keep this for displaying wave form, spectrogram, and explanation of clip
    # stretch goal for educational piece
    # button_libraryadd = mo.ui.run_button(label='Explore this sound')
    # button_libraryadd
    return


@app.cell
def _(mo):
    library_loop = mo.ui.checkbox(label="Loop audio")
    library_loop
    return


@app.cell
def _():
    import numpy as np
    import matplotlib.pyplot as plt

    def plot_waveform(audio_data, sr):
        # Handle stereo: take first channel if needed
        if audio_data.ndim > 1:
            audio_data = audio_data[:, 0]

        # Normalize amplitude to [-1, 1]
        audio_data = audio_data.astype(np.float32)
        audio_data /= np.max(np.abs(audio_data))

        # Time axis in seconds
        duration = len(audio_data) / sr
        times = np.linspace(0, duration, len(audio_data))

        # Create the figure
        fig, ax = plt.subplots(figsize=(10, 3))
        ax.plot(times, audio_data, color="steelblue", linewidth = 0.2)
        ax.set_xlim(0, duration)
        ax.set_ylim(-1.1, 1.1)
        ax.set_xlabel("Time [s]")
        ax.set_ylabel("Amplitude")
        ax.grid(alpha=0.3)
        plt.tight_layout()

        # For Marimo / Jupyter, returning fig allows inline display
        return fig
    return np, plot_waveform, plt


@app.cell
def _(d_selected, plot_waveform, sr_selected):
    fig = plot_waveform(d_selected, sr_selected)
    fig
    return


@app.cell
def _(np, plt):
    from scipy.signal import spectrogram

    def plot_spectrogram(audio_data, sr):
        if audio_data.ndim > 1:
            audio_data = audio_data[:, 0]

        # Compute spectrogram
        frequencies, time_segments, Sxx = spectrogram( audio_data, fs=sr, nperseg=1024, noverlap=256, scaling="spectrum")

        # Convert power to dB
        Sxx_dB = 10 * np.log10(Sxx + 1e-10)

        # Create figure and plot
        fig, ax = plt.subplots(figsize=(10, 4))
        pcm = ax.pcolormesh( time_segments, frequencies, Sxx_dB, shading="gouraud", cmap="viridis", vmin=-99)
        fig.colorbar(pcm, ax=ax, label="Intensity [dB]")
        ax.set_ylabel("Frequency [Hz]")
        ax.set_xlabel("Time [s]")
        ax.set_ylim(0, sr / 2)
        plt.tight_layout()

        return fig
    return (plot_spectrogram,)


@app.cell
def _(plot_spectrogram, sample_rates, signal2):
    fig2 = plot_spectrogram(signal2, sample_rates)
    fig2
    return


@app.cell(column=3)
def _(mo):
    mo.md(r"""## Clip Editor""")
    return


@app.cell
def _(slider_amp, slider_loops, slider_pitch, slider_speed, slider_t):
    start_time = slider_t.value
    ptch = slider_pitch.value
    spd = slider_speed.value
    # ptch_speed = slider_speed.value
    loops = slider_loops.value # slider_f.value
    loudness = slider_amp.value

    return loops, loudness, ptch, spd, start_time


@app.cell
def _(mo):
    # start time
    slider_t = mo.ui.slider(0, 30.0, label='Time in Song (s)')
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


@app.cell
def _(mo):
    # should be loops slider
    editor_loop = mo.ui.checkbox(label="TODO use or delete this")
    editor_loop
    return


@app.cell
def _(mo):
    # a button that when clicked will have its value set to True;
    # any cells referencing that button will automatically run.
    button_addclip = mo.ui.run_button(label='Update')
    button_addclip
    return (button_addclip,)


@app.cell
def _(
    audio_selected,
    button_addclip,
    clips_to_add,
    ipd,
    loops,
    loudness,
    np,
    process_one_clip_to_add,
    ptch,
    spd,
    start_time,
    wavfile,
):
    if button_addclip.value:
        print('ADDING A CLIP!!!')
        clips_to_add.loc[len(clips_to_add)] = [audio_selected, start_time, loops, loudness, ptch, spd]
        temp_sr, temp_d = process_one_clip_to_add(audio_selected, start_time, loops, loudness, ptch, spd)
        wavfile.write('temp_clip.wav', temp_sr, np.array(temp_d, dtype=np.float32))
        ipd.Audio('temp_clip.wav')

    return


@app.cell
def _(mo):
    mo.md(
        r"""
    Here’s where the fun begins. Each clip is yours to play with:

    * Speed it up to make it race like a storm or slow it down to let it drift like a lazy current.

    * Shift the frequency to soar into the skies or rumble in the deep.

    * Adjust the amplitude to make it whisper or roar.

    Experiment freely—the ocean has endless voices, and now they’re in your hands. When you’ve crafted the sound just the way you like, click “Add to Song” to weave it into your grand ocean symphony.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""### Acoustic Modifiers""")
    return


@app.cell
def _():
    return


@app.cell(column=4)
def _(mo):
    mo.md(r"""## MIXER""")
    return


@app.cell
def _(mo):
    mo.md(r"""Here’s where your ocean melody comes together. Watch your creation take shape through the waveform (the rolling tides of your song) and the spectrogram (a colorful map of its hidden patterns). Layer, blend, and fine-tune until your composition feels just right. When your symphony is complete, click “Export” to set it free.""")
    return


@app.cell
def _(mo):
    mo.md(r"""### Waveform:""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### Spectrogram:""")
    return


@app.cell
def _(mo):
    button_mixerplay = mo.ui.run_button(label='Play')
    button_mixerplay
    return


@app.cell
def _(mo):
    mixer_loop = mo.ui.checkbox(label="Loop audio")
    mixer_loop
    return


@app.cell
def _(mo):
    # a button that when clicked will have its value set to True;
    # any cells referencing that button will automatically run.
    button_export = mo.ui.run_button(label='Export file')
    button_export
    return


@app.cell
def _(boxes, plot_time_freq_boxes):
    fig3 = plot_time_freq_boxes(boxes)
    fig3
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


@app.cell
def _():
    import pandas as pd
    import ffmpeg

    import glob
    import os
    import shutil
    import librosa

    import IPython.display as ipd
    from scipy.io import wavfile
    from scipy import signal

    from pydub import AudioSegment
    from scipy.signal import resample
    from pydub.effects import speedup
    return ipd, librosa, os, pd, signal, wavfile


@app.cell
def _(librosa, np, signal, wavfile):
    def process_one_clip_to_add(clip, start_time, loop_val, loud_val, ptch_val, spd_val, gen_sr=44100, max_len=60):
        max_len = gen_sr * max_len
        print("NEXT FILE____________________________")
        sr, d = wavfile.read(clip)
        if len(d.shape) > 1:
            d = d.mean(axis=1)
        if np.max(np.abs(d)) != 0: d = d / np.max(np.abs(d))  # Normalize the amplitudes

        print("The raw sampling rate and length are: ", sr, len(d))

        # Modify sampling rate to match the file we are building on
        if sr != 44100:
            ratio = 44100 / sr
            d = signal.resample(d, int(len(d) * ratio))        # Use Fourier method for better quality
            sr = 44100

        # Loop
        sr_looped, d_looped = loop(sr, d, loop_val)
        print("Length of looped file: ", len(d_looped))

        # Loudness
        sr_loop_amp, d_loop_amp = loud(sr_looped, d_looped, loud_val)

        # Pitch
        sr_loop_amp_p, d_loop_amp_p = pitch(sr_loop_amp, d_loop_amp, ptch_val)

        # Speed
        sr_loop_amp_p_s, d_loop_amp_p_s = speed(sr_loop_amp_p, d_loop_amp_p, spd_val)

        sr = sr_loop_amp_p_s
        d = d_loop_amp_p_s

        # Length and start time adjustment
        start_chunk_len = start_time * sr
        strt_zero_chunk = np.zeros(start_chunk_len)
        padded_d = np.concatenate((strt_zero_chunk, d))

        if len(padded_d) > 2646000: d = padded_d[:2646000]
        elif len(padded_d) < 2646000: d = np.append(padded_d, np.zeros(2646000 - len(padded_d)))
        else: d = padded_d

        return sr, d


    def loop(sr, d, num_loops):
        d_looped = np.tile(d, num_loops)
        sr_looped = sr
        return sr_looped, d_looped


    def loud(sr, d, loud_val):
        d_amp = d * loud_val
        sr_amp = sr
        return sr_amp, d_amp

    def pitch(sr, d, factor):
        d_pitched = librosa.effects.pitch_shift(y=d, sr=sr, n_steps=factor)
        sr_pitched = sr
        return sr_pitched, d_pitched

    def speed(sr, d, factor):
        d_sped = librosa.effects.time_stretch(d, rate=factor)
        sr_sped = sr
        return sr_sped, d_sped
    return (process_one_clip_to_add,)


@app.cell
def _(np, plt, process_one_clip_to_add, wavfile):
    # REMIX
    def combine_clips(base_song, clips_to_add):
        sr_base, d_base = wavfile.read(base_song)
        plt.figure(figsize=(10, 4))
        plt.plot(np.arange(0, len(d_base)) / sr_base, d_base, 'b')
        srs, ds, combined_sounds = ([], [], d_base)
        for index, row in clips_to_add.iterrows():
            sr, d = process_one_clip_to_add(row['clip'], row['start_time'], row['loops'], row['loudness'], row['pitch_speed'])
            srs.append(sr)
            ds.append(d)
            plt.plot(np.arange(0, len(d)) / sr, d - 1.5 * index, 'r')
            combined_sounds += d
        (plt.xlabel('Time (s)'), plt.ylabel('Amplitude'))
        plt.title('My Song!')
        plt.grid(True, alpha=0.3)
        wavfile.write('my_final_song.wav', sr_base, np.array(combined_sounds, dtype=np.float32))
        return
    return


@app.cell
def _(clip_list):
    avail_wavs = clip_list
    return


@app.cell
def _(np, pd, wavfile):
    # clear audio
    sample_rate = 44100
    duration = 10
    empty_audio = np.zeros(int(sample_rate * duration), dtype=np.float32)
    clips_to_add = pd.DataFrame(columns=['clip', 'start_time', 'loops', 'loudness', 'pitch', 'speed'])

    wavfile.write('my_song.wav', sample_rate, empty_audio)
    print("The original empty song file is length: ", len(empty_audio))
    print(clips_to_add)
    return (clips_to_add,)


@app.cell
def _(clip_dropdown, clips_path, os):
    os.path.join(clips_path, clip_dropdown.selected_key)
    return


@app.cell
def _(clip_dropdown, clips_path, np, os, wavfile):
    ## SELECT YOUR CLIP:
    audio_selected = os.path.join(clips_path, clip_dropdown.selected_key)
    sr_selected, d_selected = wavfile.read(audio_selected)
    d_selected = d_selected / np.max(np.abs(d_selected))
    return audio_selected, d_selected, sr_selected


@app.cell
def _(audio_selected, clips_to_add, loops, loudness, ptch, spd, start_time):
    clips_to_add.loc[len(clips_to_add)] = [audio_selected, start_time, loops, loudness, ptch, spd]

    for index, clip in enumerate(clips_to_add['clip']):
        print(clip.split("temp", 1)[-1])
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
