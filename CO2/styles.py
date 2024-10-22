##### Set styles for the pages

import mesop as me

BLOCK_STYLE = me.Style(
            padding=me.Padding.all(12),
            background="white",
            width="100%",
            )

FLEX_STYLE = me.Style(
            display='flex',
            )

BANNER_STYLE = me.Style(background = 'LightSteelBlue', 
                               border_radius=10,
                               margin=me.Margin(bottom=8),
                               padding=me.Padding.all(24))