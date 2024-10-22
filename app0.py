import time

import mesop as me



@me.page(path="/")
def page():

    header_text()

header_style = me.Style(
        font_size=24,
        font_weight="bold",
        color="blue",)

def header_text():
    me.text(
      "Mesop Starter Kit",
      style=header_style
    )




def example_box(example: str, is_mobile: bool):
  with me.box(
    style=me.Style(
      width="100%" if is_mobile else 200,
      height=140,
      background="#F0F4F9",
      padding=me.Padding.all(16),
      font_weight=500,
      line_height="1.5",
      border_radius=16,
      cursor="pointer",
    ),
    key=example,
    on_click=click_example_box,
  ):
    me.text(example)

