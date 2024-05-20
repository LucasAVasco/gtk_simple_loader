#!/bin/env python3


"""Opens the example window in 'examples/interface.ui' file.

Example that shows how to load a '.ui' file and create a window with
'gtk_simple_loader' with type checking.

This example is equivalent to the one in 'examples/simple_window_no_loader.py', but
uses the 'gtk_simple_loader' module to show the difference in the resulted code.
"""


import logging

import gi

gi.require_version("Gtk", "4.0")
from gi.repository import Gtk  # noqa: E402,I001
import gtk_simple_loader.builder  # noqa: E402


logging.getLogger().setLevel(logging.INFO)


@gtk_simple_loader.builder.load_from_files(["examples/interface.ui"])
class App(Gtk.Application):
    """Simple example that shows how to load a '.ui' file and create a window."""

    def on_activate_handler(self, app: Gtk.Application) -> None:  # noqa: ARG002
        """Show the window.

        Called when the application is launched.

        Parameters
        ----------
        app : Gtk.Application
            The application object (equal to *self* in this context).

        """
        self.main_window: Gtk.Window
        self.box_1: Gtk.Box
        self.entry_1: Gtk.Entry
        self.scale_1: Gtk.Scale
        self.button_1: Gtk.Button
        self.switch_1: Gtk.Switch
        self.button_2: Gtk.ToggleButton

        self.main_window.present()

    def on_close_request_handler(self, window: Gtk.Window) -> None:
        """Destroy the window."""
        logging.info("Destroying the window %s", window)

    def on_switch_set_handler(self, switch: Gtk.Switch, on: bool) -> None:  # noqa: ARG002,FBT001
        """Hide/show the entry."""
        if on:
            logging.info("Hiding the entry.")
            self.entry_1.hide()
        else:
            logging.info("Showing the entry.")
            self.entry_1.show()

    def on_btn1_clicked_handler(self, button: Gtk.Button) -> None:  # noqa: ARG002
        """Erase the entry."""
        logging.info("Clearing the entry.")
        self.entry_1.set_text("")

    def on_btn2_toggle_handler(self, toggle_button: Gtk.ToggleButton) -> None:
        """Erase the entry."""
        if toggle_button.get_active():
            logging.info("Disabling the entry.")
            self.entry_1.set_sensitive(False)
        else:
            logging.info("Enabling the entry.")
            self.entry_1.set_sensitive(True)

    def on_scale_changed_handler(
            self, scale: Gtk.Scale, scroll_type: Gtk.ScrollType,  # noqa: ARG002
            value: float) -> None:
        """Fill the entry with the scale value."""
        logging.info("Filling the entry with the scale value.")
        self.entry_1.set_text(str(value))


if __name__ == "__main__":
    app = App(application_id="com.testing.GtkApplication")
    app.run([])
