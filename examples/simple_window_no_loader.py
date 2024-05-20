#!/bin/env python3


"""Opens the example window in 'examples/interface.ui' file.

Example that shows how to load a '.ui' file and create a window without
'gtk_simple_loader' with type checking.

This example is equivalent to the one in 'examples/simple_window.py', but does not uses
the 'gtk_simple_loader' module to show the difference in the resulted code.
"""


import logging
from typing import TypedDict, cast

import gi
from typing_extensions import Unpack

gi.require_version("Gtk", "4.0")
from gi.repository import Gtk  # noqa: E402

logging.getLogger().setLevel(logging.INFO)


class AppKwargsTypes(TypedDict):
    """Types for the Application keyword arguments."""

    application_id: str


class App(Gtk.Application):
    """Simple example that shows how to load a '.ui' file and create a window."""

    def __init__(self, **kwargs: Unpack[AppKwargsTypes]) -> None:
        """Initialize the application."""
        super().__init__(**kwargs)
        self.connect("activate", self.on_activate_handler)

    def on_activate_handler(self, app: Gtk.Application) -> None:  # noqa: ARG002
        """Show the window.

        Called when the application is launched.

        Parameters
        ----------
        app : Gtk.Application
            The application object (equal to *self* in this context).

        """
        # Configures the bulder to get the objects from the '.ui' file
        self._builder = Gtk.Builder(self)
        self._builder.add_from_file("examples/interface.ui")

        # Gets the objects from the '.ui' file
        self.main_window = cast(Gtk.Window, self._builder.get_object("main_window"))
        self.box_1 = cast(Gtk.Box, self._builder.get_object("box_1"))
        self.entry_1 = cast(Gtk.Entry, self._builder.get_object("entry_1"))
        self.scale_1 = cast(Gtk.Scale, self._builder.get_object("scale_1"))
        self.button_1 = cast(Gtk.Button, self._builder.get_object("button_1"))
        self.switch_1 = cast(Gtk.Switch, self._builder.get_object("switch_1"))
        self.button_2 = cast(Gtk.ToggleButton, self._builder.get_object("button_2"))

        # Configures the main window and the shows it
        self.main_window.set_application(self)
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

