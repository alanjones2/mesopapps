import mesop as me
from styles import BANNER_STYLE

def chart_html(chart):
        return f"""
        <div id='figure'></div>
        <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
        <script>
        Plotly.react('figure', {chart});
        </script>
        <div id='figure'></div>
        """

def banner(head='', subhead=''):
    with me.box(style=BANNER_STYLE):
        me.markdown( f"# {head}", style=me.Style(color="Navy"))
        me.markdown( f"## {subhead}", style=me.Style(color="SteelBlue"))
    return banner