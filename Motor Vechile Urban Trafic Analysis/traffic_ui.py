import ipywidgets as widgets
from IPython.display import display

def build_ui(predict_fn):
    junction_in = widgets.Dropdown(options=[1,2,3,4], value=1, description='Junction:')
    year_in     = widgets.BoundedIntText(value=2017, min=2015, max=2020, description='Year:')
    month_in    = widgets.BoundedIntText(value=6, min=1, max=12, description='Month:')
    day_in      = widgets.BoundedIntText(value=15, min=1, max=31, description='Day:')
    hour_in     = widgets.BoundedIntText(value=8, min=0, max=23, description='Hour:')
    predict_btn = widgets.Button(description='Predict', button_style='success', icon='check')
    output_area = widgets.Output()
    def _run(b):
        output_area.clear_output()
        with output_area:
            try:
                val = predict_fn(junction_in.value, year_in.value, month_in.value, day_in.value, hour_in.value)
                print('Predicted vehicles at Junction', junction_in.value, 'on', f'{year_in.value}-{month_in.value:02d}-{day_in.value:02d}', f'{hour_in.value:02d}:00  ->  {val:.1f} vehicles')
            except Exception as e:
                print('Error:', e)
    predict_btn.on_click(_run)
    return widgets.VBox([junction_in, year_in, month_in, day_in, hour_in, predict_btn, output_area])
