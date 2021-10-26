import plotly.express as px


def draw_sunburst(data_frame, path, color, save=False, filename= None):
    fig = px.sunburst(
    data_frame = data_frame,
    path = path,
    color = color,
    color_discrete_sequence = ["red","green","blue","orange"],
    maxdepth = -1,
    )
    fig.update_traces(textinfo='label+percent entry')
    fig.update_layout(margin=dict(t=0, l=0, r=0, b=0))

    fig.show()
    if save:
       fig.write_html(r'C:\Users\Master\Documents\Contenido_Bootcamp\carpeta_alumno\EDA\Graphics\\' + filename + '.html')
