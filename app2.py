import mesop as me

@me.stateclass
class State:
  clicks: int


def button_click(event: me.ClickEvent):
  state = me.state(State)
  state.clicks += 1


@me.page(path="/counter")
def main():
  state = me.state(State)
  me.markdown("# Click counter")
  me.markdown(f"Clicks: {state.clicks}")
  me.button("Increment counter", type="flat", 
            on_click=button_click)