# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class DashInteractiveGraphviz(Component):
    """A DashInteractiveGraphviz component.


Keyword arguments:
- id (string; optional): The ID used to identify this component in Dash callbacks.
- selected (string; optional): The ID of the selected node.
- dot_source (string; optional): The dot language source of the graph"""
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, selected=Component.UNDEFINED, dot_source=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'selected', 'dot_source']
        self._type = 'DashInteractiveGraphviz'
        self._namespace = 'dash_interactive_graphviz'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'selected', 'dot_source']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(DashInteractiveGraphviz, self).__init__(**args)
