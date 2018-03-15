import tkinter as tk
from capyle.guicomponents import _ConfigUIComponent
from capyle.utils import is_valid_integer


class _WindDirectionUI(tk.Frame, _ConfigUIComponent):
    DEFAULT = 'N'

    def __init__(self, parent):
        """Create and populate the wind direction ui"""
        tk.Frame.__init__(self, parent)
        _ConfigUIComponent.__init__(self)
        gen_label = tk.Label(self, text="Wind direction (1 = N, 2 = E, 3 = S, 4 = W):")
        gen_label.pack(side=tk.LEFT)
        is_valid_int = (self.register(is_valid_integer), '%P')
        self.gen_entry = tk.Entry(self, validate='key',
                                  validatecommand=is_valid_int, width=4)
        self.set_default()
        self.gen_entry.pack(side=tk.LEFT)

    def get_value(self):
        x = self.gen_entry.get()
        if x == '':
            x = 'N'
        elif x == '1':
            x = 'N'
        elif x == '2':
            x = 'E'
        elif x == '3':
            x = 'S'
        elif x == '4':
            x = 'W'
        return str(x)

    def set_default(self):
        self.set(self.DEFAULT)

    def set(self, value):
        super(_WindDirectionUI, self).set(entry=self.gen_entry, value=value)
