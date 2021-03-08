
#import plotly.express as px
import plotly.graph_objects as go
import numpy as np
from numpy import random

N = 400
x = np.arange(3,N,8)
y = [num+10*random.rand() for num in x]

random.shuffle(y)
colors = ["black",]*len(x)



def SelectSort(pole):
    k=1
    for i in range(0, len(pole)):
        k=i
        
        for j in range(i+1, len(pole)):
            colors = ["rgb(192,192,192)",]*len(pole)
            colors[j] = "crimson"
            yield pole,colors
            if pole[j]<pole[k]:
                k=j
        pole[i],pole[k]=pole[k],pole[i]
        colors = ["rgb(192,192,192)",]*len(pole)
        colors[i] = "purple"
        yield pole,colors
    # sorted state    
    colors = ["white",]*len(pole)
    yield pole,colors    


def frame_args(duration):
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
                #"currentvalue" : False, #{"prefix": "speed: "},
                #"visible"
                "steps": [
                    {   
                        "args": [None, frame_args(speed)],
                        "label":  " ", #! Cant you just scratch
                        "method": "animate",
                    }
                    for speed in np.arange(500, 0, -20)
                ],
            }
        ]


# Create figure
fig = go.Figure(
    data=[go.Bar(x=x, y=y,marker_color=colors,
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
                                        args=[None, frame_args(200)] ), 
                                   dict(label="&#9724;", # stop button
                                        method="animate",
                                        args=[[None], frame_args(0)] ),
                                   
                                   ],
                                   ), ],
        sliders=sliders),
    
    frames=[go.Frame(
        data=[dict(type="bar",
            x=x,
            y=output[0], #!
            marker_color=output[1],
            marker_line_color="rgb(0,0,0)",
            marker_line_width=1.5,
            

            ), ],) #! Dont use it purposly or scrape it.

        for output in SelectSort(y)
        ],

        
)
#print(fig)
fig.show()


#print(colors)