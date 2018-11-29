import os.path

import sublime_plugin


class ShowFolder(sublime_plugin.TextCommand):
    def run(self, _):
        self.view.window().show_input_panel("Folder path", os.path.dirname(self.view.file_name()),
            on_done=None, on_change=None, on_cancel=None)
