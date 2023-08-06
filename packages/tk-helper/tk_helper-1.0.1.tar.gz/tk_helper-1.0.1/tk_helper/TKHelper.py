#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#  Copyright (c) 2019.       Mike Herbert
#
#   This program is free software; you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation; either version 2 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program; if not, write to the Free Software
#   Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301  USA


from tkinter import *
from tkinter import ttk, messagebox
from tkinter.ttk import Progressbar
from typing import List


"""
Provide helper functions for tkinter.ttk widgets:
CtreeView - Support even/odd row colors, easier item setting
CLabel -  standardized get and set text
CEntry -  standardized get and set text.  Support for Undo/Redo in Entry widget
Buttons - routines to enable/disable list of buttons and set a button as 'preferred'
Exit routines - Helper routines to display message and exit
"""


class CTreeView(ttk.Treeview):
    """
    Treeview with support for alternate row colors and simplified insert and clear
    """

    def __init__(self, root, styl, mode, odd_background, even_background):
        super().__init__(root, style=styl, selectmode=mode)
        self.tag_configure('odd', background=odd_background)
        self.tag_configure('even', background=even_background)
        self.odd_row = False

    def list_insert(self, text, prefix, rec_id, score, feature):
        # Tags to alternate row colors in lists
        self.odd_row = not self.odd_row
        if self.odd_row:
            tag = ('odd',)
        else:
            tag = ('even',)
        self.insert(parent='', index="end", iid=None, text=text, values=(prefix, rec_id, score, feature), tags=tag)

    def clear_display_list(self):
        self.odd_row = False
        for row in self.get_children():
            self.delete(row)


class CLabel(ttk.Label):
    """
    TTK Label with generic set text and get text
        Usage:
    label = CLabel(parent, **kwargs)
    label.text = 'hello'
    text = label.text
    """

    def __init__(self, parent, **kwargs):
        """

        :param parent:
        :param kwargs:
        """
        ttk.Label.__init__(self, parent, **kwargs)

    @property
    def text(self) -> str:
        """ Get the text of a widget """
        return self.cget("text")

    @text.setter
    def text(self, text: str):
        """ Set the text of a widget """
        self.configure(text=text)


class CEntry(ttk.Entry):
    """
    TTK Entry with support for Undo/Redo for TextEntry using Ctl-Z,  Ctl-Y.
    Generic set text and get text
        Usage:
    entry = CEntry(parent, *args, **kwargs)
    entry.text = 'hello'
    text = entry.text
    """

    def __init__(self, parent, *args, **kwargs):
        """

        :param parent:
        :param args:
        :param kwargs:
        """
        ttk.Entry.__init__(self, parent, *args, **kwargs)
        self.changes = [""]
        self.steps = int()
        self.bind("<Control-z>", self.undo)
        self.bind("<Control-y>", self.redo)
        self.bind("<Key>", self.add_changes)

    @property
    def text(self) -> str:
        """ Get the text of a widget """
        return self.get()

    @text.setter
    def text(self, text: str):
        """ Set the text of a widget """
        self.delete("0", END)
        self.insert(0, text)

    def insert(self, idx, txt):
        self.changes = [""]
        self.steps = int()
        super().insert(idx, txt)

    def undo(self, _):
        if self.steps > 1:
            self.steps -= 1
            self.delete(0, END)
            super().insert(END, self.changes[self.steps])

    def redo(self, _):
        if self.steps < len(self.changes):
            self.delete(0, END)
            super().insert(END, self.changes[self.steps])
            self.steps += 1

    def add_changes(self, _):
        if self.get() != self.changes[-1]:
            self.changes.append(self.get())
            self.steps += 1

class Progress:
    """ Create a progress bar for loading large files or other long operations """

    def __init__(self, window, bar_color, trough_color, length, status):
        """
        Create a progress bar for loading large files or other long operations
        :param window: parent window
        :param bar_color: color for the bar in the progress bar
        :param trough_color: color for the trough (background) of the progress bar
        :param length: length of bar
        :param status: status text to display
        """
        self.window = window
        self.shutdown_requested = False

        style: ttk.Style = ttk.Style()
        style.configure("bar.Horizontal.TProgressbar",
                        troughcolor=trough_color, bordercolor=trough_color,
                        background=bar_color, lightcolor=bar_color, darkcolor=bar_color)

        self.bar: Progressbar = Progressbar(window, length=length, maximum=100, style="bar.Horizontal.TProgressbar")
        self.bar['value'] = 0
        self.lable = status
        self._full_update: bool = True

        # Call appropriate update loop depending on whether we have entered main window loop
        if self._full_update:
            self.window.update()  # Outside of TK mainloop.  Use stronger window.update
        else:
            self.window.update_idletasks()

    @property
    def full_update(self):
        return self._full_update

    @full_update.setter
    def full_update(self, val):
        # Set this to True when outside TK mainloop and False when in TK mainloop
        self._full_update = val

    def update_progress(self, progress: int, stage: str):
        self.bar['value'] = progress
        self.lable.text = stage
        if self._full_update:
            self.window.update()
        else:
            self.window.update_idletasks()

    def destroy(self):
        self.bar.destroy()
        self.window.update_idletasks()


def disable_buttons(button_list: List[ttk.Button]) -> None:
    # Disable a list of buttons
    for button in button_list:
        button.config(state="disabled")


def enable_buttons(button_list: List[ttk.Button]) -> None:
    # Enable a list of buttons
    for button in button_list:
        button.config(state="normal")


def set_preferred_button(target_button, button_list, pref_style):
    """ Highlight a preferred button """
    # Go through list of buttons and set them to normal style, and set preferred button to pref_style
    for button in button_list:
        if button == target_button:
            # Highlight preferred button and ensure it is enabled
            button.configure(style=pref_style)  # Make this button the preferred selection
            button.config(state="normal")
        else:
            button.configure(style="TButton")  # set to Normal style

def fatal_error(msg: str) -> None:
    """
    Fatal error -  Notify user and shutdown
    :param msg: Message to display before shutdown
    :return: Exits
    """
    messagebox.showerror("Error", msg)
    sys.exit()

def exit_dialog(title, msg):
    """
    Display Yes/No Message box and exit
    :param title:
    :param msg:
    :return: Exits
    """
    if messagebox.askyesno(title, msg):
        sys.exit()
