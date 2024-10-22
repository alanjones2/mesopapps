import mesop as me
import Sample_Data.CO2_Data as CO2
from styles import BLOCK_STYLE, BANNER_STYLE, FLEX_STYLE

def chart_html(chart):
        return f"""
        <div id='figure'></div>
        <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
        <script>
        Plotly.react('figure', {chart});
        </script>
        <div id='figure'></div>
        """

##### State variable
@me.stateclass
class State:
    co2_data = CO2.CO2_Data()
    year = co2_data.year_min



bar_chart = State.co2_data.plot_chart("Total")
CO2_map = State.co2_data.plot_choro(State.co2_data.year_max)

##### Navigation
def navigate(event: me.ClickEvent):
    match event.key:
        case "CO2":
            me.navigate("/CO2")
        case "map":
            me.navigate("/map")
        case _:
            me.navigate("/")


def banner(head='', subhead=''):
    with me.box(style=BANNER_STYLE):
        me.markdown( f"# {head}", style=me.Style(color="Navy"))
        me.markdown( f"## {subhead}", style=me.Style(color="SteelBlue"))
    return banner

##### Home page
@me.page(path="/")
def home():    

    with me.box(style = BLOCK_STYLE):
        
        banner('World CO2 Emissions','Explore the graphs below')
        me.markdown( """The World's CO2 emissions have been increasing at an alarming rate since the time of the Industrial Revolution. 
                    We demonstrate the extend of those emissions using two data sets:  the first tracks overall emissions and we show those
                    onto a World map. We also show the breakdown of the sources of those emissions in a set of bar graphs.""")
        me.markdown("_Click on the buttons below to see the charts._")
        
        with me.box(style = FLEX_STYLE):

            with me.box():
                me.image(src = "https://github.com/alanjones2/mesopapps/blob/main/CO2/images/Co2sources.png?raw=true",
                    alt="",
                    style=me.Style(width="90%")
                )
                me.button("By source", type='flat',on_click=navigate, key='CO2')
            with me.box():
                me.image(src = "https://github.com/alanjones2/mesopapps/blob/main/CO2/images/Co2country.png?raw=true",
                    alt="",
                    style=me.Style(width="90%"),
                )
                me.button("By country", type='flat', on_click=navigate, key='map')

def on_selection_change(select):
   global bar_chart
   bar_chart = State.co2_data.plot_chart(select.values[0])

##### CO2 Source page
@me.page(path="/CO2")
def CO2():
    with me.box(style = BLOCK_STYLE):
        banner( "CO2 Emissions by source since the mid-19th Century")
        me.select(
            label="Select a CO2 Source",
            options=[
            me.SelectOption(label="Total", value="Total"),
            me.SelectOption(label="Coal", value="Coal"),
            me.SelectOption(label="Oil", value="Oil"),
            me.SelectOption(label="Cement", value="Cement"),
            me.SelectOption(label="Flaring", value="Flaring"),
            me.SelectOption(label="Other", value="Other"),      
            ],
            on_selection_change=on_selection_change,
            style=me.Style(width=240, height=70),
        )
        
        me.button("Home page", on_click=navigate, key='home')
        me.html(
            chart_html(bar_chart),
            mode="sandboxed",
            style=me.Style(width="100%", height="500px")
    )

##### Map page
def on_slider_change(event):
   global CO2_map
   State.year=int(event.value)
   CO2_map = State.co2_data.plot_choro(int(event.value))   

@me.page(path="/map")
def map():
    with me.box(style = BLOCK_STYLE):
        banner( f"CO2 Emissions by country for {State.year}")
        me.slider(on_value_change=on_slider_change, value=State.year, max='2020', min='1900', discrete=True)

        me.button("Home page", on_click=navigate, key='home')
        me.html(
            chart_html(CO2_map),
            mode="sandboxed",
            style=me.Style(width="100%", height="500px")
    )