from __future__ import absolute_import

from .utils import serialize_palette, get_value, get_popup

from ..layer import Layer


def color_bins_layer(
        source, value, title='', method='quantiles', bins=5,
        breaks=None, palette=None, size=None, opacity=None,
        stroke_color=None, stroke_width=None, description='',
        footer='', legend=True, popup=True, widget=False, animate=None, credentials=None):
    """Helper function for quickly creating a classed color map.

    Args:
        source (:py:class:`Dataset <cartoframes.data.Dataset>` or str): Dataset
          or text representing a table or query associated with user account.
        value (str): Column to symbolize by.
        title (str, optional): Title of legend.
        method (str, optional): Classification method of data: "quantiles", "equal", "stdev".
          Default is "quantiles".
        bins (int, optional): Number of size classes (bins) for map. Default is 5.
        breaks (list<int>, optional): Assign manual class break values.
        palette (str, optional): Palette that can be a named cartocolor palette
          or other valid CARTO VL palette expression. Default is `purpor`.
        size (int, optional): Size of point or line features.
        opacity (int, optional): Opacity value for point color and line features.
          Default is '0.8'.
        stroke_width (int, optional): Size of the stroke on point features.
        stroke_color (str, optional): Color of the stroke on point features.
          Default is '#222'.
        description (str, optional): Description text legend placed under legend title.
        footer (str, optional): Footer text placed under legend items.
        legend (bool, optional): Display map legend: "True" or "False".
          Set to "True" by default.
        popup (bool, optional): Display popups on hover and click: "True" or "False".
          Set to "True" by default.
        widget (bool, optional): Display a widget for mapped data: "True" or "False".
          Set to "False" by default.
        animate (str, optional): Animate features by date/time or other numeric field.
        credentials (:py:class:`Credentials <cartoframes.auth.Credentials>`, optional):
          A Credentials instance. This is only used for the simplified Source API.
          When a :py:class:`Source <cartoframes.viz.Source>` is passed as source,
          these credentials is simply ignored. If not provided the credentials will be
          automatically obtained from the default credentials.

    Returns:
        cartoframes.viz.Layer: Layer styled by `value`.
        Includes a legend, popup and widget on `value`.
    """
    if method not in ('quantiles', 'equal', 'stdev'):
        raise ValueError('Available methods are: "quantiles", "equal", "stdev".')

    if breaks is None:
        func = {
            'quantiles': 'globalQuantiles',
            'equal': 'globalEqIntervals',
            'stdev': 'globalStandardDev'
        }.get(method)
        default_palette = {
            'quantiles': 'purpor',
            'equal': 'purpor',
            'stdev': 'temps'
        }.get(method)
    else:
        func = 'buckets'
        default_palette = 'purpor'
        breaks = list(breaks)

    animation_filter = 'animation(linear(${}), 20, fade(1,1))'.format(animate) if animate else '1'

    return Layer(
        source,
        style={
            'point': {
                'color': 'opacity(ramp({0}(${1}, {2}), {3}),{4})'.format(
                    func, value, breaks or bins,
                    serialize_palette(palette) or default_palette,
                    get_value(opacity, 'point', 'opacity')
                ),
                'width': get_value(size, 'point', 'width'),
                'strokeColor': get_value(stroke_color, 'point', 'strokeColor'),
                'strokeWidth': get_value(stroke_width, 'point', 'strokeWidth'),
                'filter': animation_filter
            },
            'line': {
                'color': 'opacity(ramp({0}(${1}, {2}), {3}),{4})'.format(
                    func, value, breaks or bins,
                    serialize_palette(palette) or default_palette,
                    get_value(opacity, 'line', 'opacity')
                ),
                'width': get_value(size, 'line', 'width'),
                'filter': animation_filter
            },
            'polygon': {
                'color': 'opacity(ramp({0}(${1}, {2}), {3}), {4})'.format(
                    func, value, breaks or bins,
                    serialize_palette(palette) or default_palette,
                    get_value(opacity, 'polygon', 'opacity')
                ),
                'strokeColor': get_value(stroke_color, 'polygon', 'strokeColor'),
                'strokeWidth': get_value(stroke_width, 'polygon', 'strokeWidth'),
                'filter': animation_filter
            }
        },
        popup=popup and not animate and get_popup(
          popup, title, value, value),
        legend=legend and {
            'type': {
                'point': 'color-bins-point',
                'line': 'color-bins-line',
                'polygon': 'color-bins-polygon'
            },
            'title': title or value,
            'description': description,
            'footer': footer
        },
        widgets=[
            animate and {
                'type': 'time-series',
                'value': animate,
                'title': 'Animation'
            },
            widget and {
                'type': 'histogram',
                'value': value,
                'title': 'Distribution'
            }
        ],
        credentials=credentials
    )
