#!/usr/bin/env python3
"""Run HelloWorldActivity locally (GTK4).

Run this from the `hello-world` directory. It ensures the toolkit in
`../src` is on PYTHONPATH and sets minimal SUGAR environment variables
so the activity can find its bundle resources during local testing.

or just do

pip install sugar-toolkit-gtk4
"""

import sys
import os

# sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

import gi

gi.require_version("Gtk", "4.0")
from gi.repository import Gtk

# Provide minimal SUGAR bundle environment for local runs
os.environ.setdefault("SUGAR_BUNDLE_ID", "org.sugarlabs.HelloWorld")
os.environ.setdefault("SUGAR_BUNDLE_NAME", "HelloWorld")
os.environ.setdefault("SUGAR_BUNDLE_PATH", os.getcwd())

from sugar4.activity.activityhandle import ActivityHandle

import activity as hello_activity


def main(argv=None):
    argv = argv or sys.argv

    app = Gtk.Application(application_id="org.sugarlabs.HelloWorld")

    def on_activate(app):
        handle = ActivityHandle("hello-world-local")
        win = hello_activity.HelloWorldActivity(handle, application=app)
        # prefer set_application on GTK4 Window-like Activity
        try:
            win.set_application(app)
        except Exception:
            # fallback: add to application
            try:
                app.add_window(win)
            except Exception:
                pass
        win.present()

    app.connect("activate", on_activate)
    return app.run(argv)


if __name__ == "__main__":
    sys.exit(main())
