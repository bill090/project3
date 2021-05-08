from django.shortcuts import render
from bokeh.plotting import figure, output_file, show
from bokeh.embed import components
from bokeh.models import HoverTool
import pandas as pd
from math import pi
import datetime
from .dataservice import get_crypto_data, convert_to_df_crypto

# Create your views here.

def homepage(request):

    if request.method == 'POST':
        crypto = request.POST['crypto']
    else:
        crypto = 'BTC'
    
    market = 'USD'
    
    result = get_crypto_data(crypto, market, "FXW2F1NQB7AEGIU6")

    source = convert_to_df_crypto(result)

    TOOLS = "pan, box_zoom, reset, save"

    title = f"{crypto} to {market} chart."

    p = figure(x_axis_type="datetime", tools=TOOLS, plot_width = 700, plot_height = 500, title = title)
    p.xaxis.major_label_orientation = pi / 4
    p.line(x='date', y='high', line_width=2, source=source)


    line = p.line(x='date', y='high', line_width = 2, line_color = "#ed0505", source = source)

    hover_tool = HoverTool(
        tooltips = [
            ('Price', '$y{0, 0.00}'),
            ('Date', '$x{%F}'),
        ],
        formatters = {'$x': 'datetime'},
    )
    p.tools.append(hover_tool)


    script, div = components(p)

    return render(request, 'crypto/base.html', {'script' : script, 'div' : div})
