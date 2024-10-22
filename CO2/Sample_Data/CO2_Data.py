# CO2 data class
#
# This class supports specific tutorials published in Medium  
# it is not intended for general use

# Read the data and define dataframes, ploting functions 
# and variables to support those functions 

import pandas as pd 
import plotly.express as px 
from pathlib import Path

class CO2_Data:
    def __init__(self):

        package_path = str(Path(__file__).parent)

        # Get the data
        self.df_cat = pd.read_csv(package_path+"/co2-emissions-by-category.csv") 
        self.df_total = pd.read_csv(package_path+'/co2_total.csv')
        
        # define parameters for map graphic
        self.year_max = 2020
        self.year_min = 1900
        self.col = 'Annual CO₂ emissions'           # the column that contains the emissions data
        self.max = self.df_total[self.col].max()    # maximum emissions value for color range
        self.min = self.df_total[self.col].min()    # minimum emissions value for color range
                
    ##### Functions to plot the charts and return JSON
    def plot_chart(self, y):
        fig = px.bar(self.df_cat, x="Year", y=y, 
                    width=1000, template="plotly_white")
        return fig.to_json()

    def plot_choro(self,y):
        fig = px.choropleth(self.df_total[self.df_total['Year']==y], 
            locations="Code",                       # The ISO code for the Entity (country)
            color=self.col,                         # color is set by self column
            hover_name="Entity",                    # hover name is the name of the Entity (country)
            range_color=(self.min,self.max),        # the range of values as set above
            scope= 'world',                         # a world map - the default
            projection='equirectangular', 
            title=f"CO2 Emissions by country in {y}",
            color_continuous_scale=px.colors.sequential.Reds,
            template = "plotly_white"   
        )
        # Remove margins
        fig.update_layout(
            margin=dict(l=0, r=0, t=0, b=0)
        )
        return fig.to_json()
