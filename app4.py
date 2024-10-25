import mesop as me
import plotly.express as px

BLOCK_STYLE = me.Style(
            padding=me.Padding.all(12),
            background="white",
            width="100%",
            )

def chart_html(chart):
        return f"""
        <div id='figure'></div>
        <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
        <script>
        Plotly.react('figure', {chart});
        </script>
        <div id='figure'></div>
        """



@me.page(path="/")
def main():
  with me.box(style=BLOCK_STYLE):
    me.markdown("# A Plotly chart")
    data_canada = px.data.gapminder().query("country == 'Canada'")
    fig = px.bar(data_canada, x='year', y='pop')
    chart = chart_html(fig.to_json())
    me.html(
        chart_html(chart),
        mode="sandboxed",
        style=me.Style(width="100%", height="500px")
    )