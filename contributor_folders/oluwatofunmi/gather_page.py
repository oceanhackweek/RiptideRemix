import marimo

__generated_with = "0.14.17"
app = marimo.App(
    width="columns",
    app_title="RiptideRemix_mixer",
    layout_file="layouts/gather_page.grid.json",
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


@app.cell
def _(mo):
    mo.md(""" """)
    return


@app.cell
def _():
    import obspy as os
    import obspy.signal
    from obspy.clients.fdsn import Client
    from obspy import UTCDateTime
    from obspy import clients

    import numpy as np
    import matplotlib.pyplot as plt
    from obspy.taup import TauPyModel
    from obspy.geodetics import locations2degrees
    from obspy.geodetics.base import gps2dist_azimuth
    return Client, TauPyModel, UTCDateTime, locations2degrees


@app.cell
def _(UTCDateTime):
    big_events = { "Japan_2011": { "start_time": UTCDateTime("2011-03-11T05:46:23"), 
                                  "latitude": 38.297, "longitude": 142.372, "depth_km": 29
                                 },
                   "Alaska_2021": { "start_time": UTCDateTime("2021-07-29T06:15:49"),
                                    "latitude": 55.325,"longitude": -157.972, "depth_km": 32
                                  },
                   "Russia_2025": {"start_time": UTCDateTime("2025-07-25T00:15:30"),
                                   "latitude": 54.000, "longitude": 160.0000, "depth_km": 25
                                  }
                }
    return (big_events,)


@app.cell
def _():
    # This shows a network and station pairing 
    # so AF is the network while ["AAUS", "ANKE", "DESE", "EKNA", "IFE", "KAD", "NSU"] is the station. 
    # This applies to the rest for clarity

    network_stations = {
                            "AF": ["AAUS", "ANKE", "DESE", "EKNA", "IFE", "KAD", "NSU"],
                            "AU": ["MCQ"],
                            "G": ["ATD", "TAM"],
                            "IM": ["TOA1", "TOA2", "TOA3", "TOB1", "TOB2", "TOB3", "TOB4", "TOB5", "TORD"],
                            "IP": ["MTOR"],
                            "IU": ["FURI", "MACI"],
                            "NJ": ["AWK", "IFE", "KAD", "NSU", "TORO"],
                            "NZ": ["CTZ"]
    }
    return


@app.cell
def _(Client, TauPyModel, big_events):
    client = Client('IRIS')
    model = TauPyModel(model = "ak135")         
                                        # In the dropdown menu we can have models using either models "iasp91", "ak135", "ak135f", "prem"


    selected_event = "Japan_2011"  #There should be a dropdown for selected events: Japan_2011, Alaska_2021 and Russia_2025
    selected_network = "IU"        #I don't know how this will be connected to networ_stations, i don't know how 
    selected_station = "PAYG"
    selected_channel = "BHZ"       # We can have a drop down for three channels(BH1, BH2, BHZ), for now maybe just focu
    selected_location = "*"        # Thwill serve as a wildcat (*), you can use various wildcat tho in the drop down, 
                                   # eg BH?, LH?

    event = big_events[selected_event]
    start_time = event["start_time"]
    trace_length = 4000             # If possible we can have drop downs for trace length 
    end_time = start_time + trace_length
    event_lat = event["latitude"]
    event_lon = event["longitude"]
    event_depth_km = event["depth_km"]
    return (
        client,
        end_time,
        event_lat,
        event_lon,
        selected_channel,
        selected_location,
        selected_network,
        selected_station,
        start_time,
    )


@app.cell
def _(
    client,
    end_time,
    selected_channel,
    selected_location,
    selected_network,
    selected_station,
    start_time,
):
    try:
        st = client.get_waveforms(selected_network, selected_station, selected_location,
                                  selected_channel, start_time, end_time, attach_response=True
                                 )
        st_rem = st.copy()
        st_rem.remove_response(output="VEL")
        st_rem.detrend('linear')
        st_rem.detrend('demean')
        tr = st_rem[0]
    except Exception as e:
        print(f"There was a download error, please check inputs Maybe incorrect channel, station and network name Ensure your input is correct and well written: {e}")
    return


@app.cell
def _(
    client,
    end_time,
    event_lat,
    event_lon,
    locations2degrees,
    selected_network,
    selected_station,
    start_time,
):
    inv = client.get_stations( network=selected_network, station=selected_station,
                               level="station", starttime=start_time, endtime=end_time
                             )
    sta = inv[0][0]
    station_lat = sta.latitude
    station_lon = sta.longitude
    distance_deg = locations2degrees(event_lat, event_lon, station_lat, station_lon)
    return


@app.cell
def _():
                                                        # I neeed a drop down for the the filter ranges
    filter_ranges = [(0.01, 0.10), 
                     (0.05, 0.2), 
                     (0.01, 0.5), 
                     (0.03, 0.1), 
                     (0.03, 0.15)]      

    nrows = len(filter_ranges) + 1 
    
    phase_types = ["P", "S", "SKS", "SKKS"]   
                                                        #This part shows the TauP phases we wanna overlay on the plots
                                                        # What this does that is shows the body waves(P&S) arrival amongst others
    arrival_colors = {'P': 'r', 
                      'S': 'g', 
                      'SKS': 'b', 
                      'SKKS': 'm'}

    colors = [
                'k', 'r', 'b', 'g',                   
                'orange','purple',         
                'cyan','magenta',     
                'brown','olive',
                'teal','pink','gold'
                'darkred', 'navy',  
            ]
    return


app._unparsable_cell(
    r"""
    try:
        # Get waveform
        st = client.get_waveforms(
            selected_network, selected_station, selected_location,
            selected_channel, start_time, end_time, attach_response=True
        )

        # Preprocess
        st_rem = st.copy()
        st_rem.remove_response(output=\"VEL\")
        st_rem.detrend('linear')
        st_rem.detrend('demean')
        tr = st_rem[0]  # Trace extracted here
    """,
    name="_"
)


app._unparsable_cell(
    r"""
        # Get station metadata
        inv = client.get_stations(
            network=selected_network, station=selected_station,
            level=\"station\", starttime=start_time, endtime=end_time
        )
        sta = inv[0][0]
        station_lat = sta.latitude
        station_lon = sta.longitude
        distance_deg = locations2degrees(event_lat, event_lon, station_lat, station_lon)
    """,
    name="_"
)


app._unparsable_cell(
    r"""
        for i, (fmin, fmax) in enumerate(filter_ranges):
            tr_filt = tr.copy()
            tr_filt.filter(\"bandpass\", freqmin=fmin, freqmax=fmax, corners=4, zerophase=True)
            print(\"The range of frequencies is from:, freqmin, freqmax,  Hz\")
            tr_filt.data = tr_filt.data / max(abs(tr_filt.data))
            t = tr_filt.times(\"relative\")

            arrivals = model.get_travel_times(
                source_depth_in_km=event_depth_km,
                distance_in_degree=distance_deg,
                phase_list=phase_types
            )
            color = colors[i % len(colors)]  

            plt.figure(figsize=(15, 4))
            plt.plot(t, tr_filt.data, label=f'{fmin}–{fmax} Hz', color=color)
            plt.xlabel(\"Time after(s)\")
            plt.ylabel(\"Amplitude\")
            plt.title(f\"{selected_network}.{selected_station}.{selected_channel} | {selected_event} | {fmin}-{fmax} Hz\")

            for arr in arrivals:
                if arr.name in arrival_colors:
                    plt.axvline(arr.time, color=arrival_colors[arr.name], linestyle='--', label=arr.name)

            plt.grid(True)
            if i == 0:
                plt.legend(loc='upper right')
            plt.tight_layout()
            plt.show()

    except Exception as e:
        print(f\" Error occurred: {e}\nCheck network/station/channel values or time window.\")
    """,
    name="_"
)


@app.cell
def _():
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
