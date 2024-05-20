"""Tests the 'src/gtk_builder.py' module."""


import unittest

import gi

gi.require_version("Gtk", "4.0")
from gi.repository import GObject, Gtk  # noqa: E402

from src.gtk_simple_loader import builder as builder_loader  # noqa: E402


def test_has_attribute(
        test_case: unittest.TestCase,
        obj: object, attribute_names: list[str]) -> None:
    """Test if the object has the provided attributes.

    Search if the provided object has the provided attributes. If not, it will fail the
    test with a unittest.TestCase object.

    Parameters
    ----------
    test_case : unittest.TestCase
        The test case object to use.

    obj : object
        The object to search by the attributes.

    attribute_names : list[str]
        The list of attributes to search.

    """
    for attribute_name in attribute_names:
        if not hasattr(obj, attribute_name):
            test_case.fail(f"The object '{attribute_name}' was not loaded.")


class TestGtkBuilder(unittest.TestCase):
    """Test case to all utilities related to 'gtk_simple_loader.builder' module."""

    def test_load_from_files(self) -> None:
        """Test the 'load_objects_from_builder()' function."""
        test_object = GObject.GObject()
        builder = Gtk.Builder()
        builder.add_from_file("test/unit/interface.ui")
        builder_loader.load_objects_from_builder(test_object, builder)

        test_has_attribute(self, test_object, ["button", "color_button", "switch"])

    def test_load_builder_from_files(self) -> None:
        """Test the 'load_builder_from_files()' function."""
        test_object = GObject.GObject()
        builder_loader.load_builder_from_files(
            test_object, ["test/unit/interface.ui"])

        test_has_attribute(self, test_object, ["button", "color_button", "switch"])

    def test_load_from_files_wrapper(self) -> None:
        """Test the 'load_from_files()' function."""
        # Need to save before enter the class because the self will be overwritten
        test_gtk_builder = self

        @builder_loader.load_from_files(["test/unit/interface.ui"])
        class MyApp(Gtk.Application):

            def on_activate_handler(self, window: Gtk.Window) -> None:  # noqa: ARG002
                """Test if the objects are loaded."""
                test_has_attribute(
                    test_gtk_builder, self,
                    [
                        "_loader_builder", "_loaded_obj_names",
                        "button", "color_button", "switch",
                    ])

        app = MyApp(application_id="com.testing.GtkApplication")
        app.run([])


if __name__ == "__main__":
    unittest.main()
