import sublime, sublime_plugin
import os
from functools import partial


caption = "Module Name:"


class NewPythonModule(sublime_plugin.ApplicationCommand):
    def run(self, paths):
        sublime.active_window().show_input_panel(caption, "",
            on_done=partial(self.init_module, path=paths[0]),
            on_change=None,
            on_cancel=None,
        )

    def init_module(self, name, path):
        new_dir = os.path.join(path, name)
        if os.path.exists(new_dir):
            return
        os.makedirs(new_dir)

        self.create_file(new_dir, "__init__.py")
        # self.create_file(new_dir, "abc.py")

    @staticmethod
    def create_file(folder_path, file_name):
        file_path = os.path.join(folder_path, file_name)
        open(file_path, "w").close()
        sublime.active_window().open_file(file_path)

    @staticmethod
    def is_visible(paths):
        return os.path.isdir(paths[0])
