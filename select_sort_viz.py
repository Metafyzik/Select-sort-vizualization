
import plotly.graph_objects as go
import numpy as np
from numpy import random

# This animation is nothing else that bar chart graph that showing a list of the same values differently orderded each moment during the animation. 
# These moments are called frames. Barchart needs x coordinates and y coordinates.

# creating array to be sorted 
N = 400
x = np.arange(3,N,8)
y = x.copy()
random.shuffle(y)

# colors of columns
silver = "rgb(192,192,192)"
colors_init = ["black",]*len(x) 
colors_sorting = [silver,]*len(x) 

def select_sort(array,colors_sorting): 
    # Function does three things: 
    # a) sorting inputed list
    # b) yielding states of process of sorting in form of a list. Each state yielded serves as a frame in animation.
    # c) closely related to b) yielding colors of columns
    k=1
    for i in range(0, len(array)):
        k=i
        for j in range(i+1, len(array)):
         
            colors_sorting[j] = "crimson" # distinguishing selected column
            yield array,colors_sorting 

            colors_sorting[j] = silver # changing color back
            if array[j]<array[k]:
                k=j

        array[i],array[k]=array[k],array[i]

        colors_sorting[i] = "purple" # distinguishing sorted column
        yield array,colors_sorting
        colors_sorting[i] = silver # changing color back

    # sorted (last frame)   
    colors_sorted = ["white",]*len(array)
    yield array,colors_sorted    


def animation_speed(duration):
    return {
            "frame": {"duration": duration,"redraw": False},
            "mode": "immediate",
            "fromcurrent": True,
            "transition": {"duration": 150, "easing": "linear"},
        }

sliders = [
            {
                "pad": {"b": 10, "t": 60},
                "len": 0.5,
                "x": 0.2,
                "y": 0,
                "active" : 10,                
                "steps": [
                    {   
                        "args": [None,  animation_speed(speed)],
                         "label":  " ", 
                        "method": "animate",
                    }
                    for speed in np.arange(500, 0, -20)
                ],
            }
        ]

# Create figure
fig = go.Figure(
    data=[go.Bar(x=x, y=y,marker_color=colors_init, # initial state
        marker_line_color='rgb(0,0,0)',marker_line_width=1.5),
          ],
    layout=go.Layout(
        xaxis=dict(range=[-1, N], autorange=False, zeroline=False, showgrid=False,visible= False),
        yaxis=dict(range=[0, max(y)+1], autorange=False, zeroline=False,showgrid=False,visible= False),
        title_text="Select Sort", hovermode="closest",
        updatemenus=[dict(type="buttons",
                            direction="right",
                            active=0,
                            x=0.5,
                            y=-0.05,
                          buttons=[dict(label="&#9654;", # play button
                                        method="animate",
                                        args=[None, animation_speed(200)] ), 
                                   dict(label="&#9724;", # stop button
                                        method="animate",
                                        args=[[None], animation_speed(0)] ),
                                   
                                   ],
                                   ), ],
        sliders=sliders),
    
    frames=[go.Frame(
        data=[dict(type="bar",
            x=x,
            y=output[0], 
            marker_color=output[1],
            marker_line_color="rgb(0,0,0)",
            marker_line_width=1.5,

            ), ],)
        for output in select_sort(y,colors_sorting)
        ],

)

fig.show()
