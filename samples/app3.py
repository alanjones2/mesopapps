import mesop as me

BLOCK_STYLE = me.Style(
            padding=me.Padding.all(12),
            background="white",
            width="100%",
            )

@me.stateclass
class State:
  clicks: int

def button_click(event: me.ClickEvent):
  state = me.state(State)
  state.clicks += 1

@me.page(path="/counter")
def main():
  state = me.state(State)
  with me.box(style=BLOCK_STYLE):
    me.markdown("# Click counter")
    with me.box(style=me.Style(display="flex", gap=20)):
        me.markdown(f"Clicks: {state.clicks}")
        me.button("Increment counter", type="flat", 
                on_click=button_click)
    
    me.markdown("## An alternative layout")
    # Alternatively fr = fraction and are the proportion of the width used
    with me.box(style=me.Style(display="grid", 
                                grid_template_columns="1fr 1fr")):
        me.markdown(f"Clicks: {state.clicks}")
        me.button("Increment counter", type="flat", 
                on_click=button_click)  



