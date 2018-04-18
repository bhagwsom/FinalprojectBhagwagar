import plotly.plotly as py
import plotly.graph_objs as go


def plot_graph1(trace1, trace2):
    #compare trackcount for 2 Albums

    data= [go.Bar(y=trace1, x=trace2, name='Bar Chart Comparing TrackCount to Beyonce')]
    print(data)


    py.plot(data, filename='Bar Chart Comparing Track Count')

def plot_graph2():
    data= [go.Bar(y=trace1, x=trace2, name='Bar Chart Comparing Popularity to Beyonce')]
    print(data)


    py.plot(data, filename='Bar Chart Comparing Popularity')




def plot_graph3():
    data= [go.Bar(y=trace1, x=trace2, name='Bar Chart Comparing Follower Count to Beyonce')]
    print(data)


    py.plot(data, filename='Bar Chart Comparing FollowerCount')


def plot_graph4():
    #compare popularity for two artists
    pass
