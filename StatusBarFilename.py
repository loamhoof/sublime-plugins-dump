import os.path

import sublime_plugin


class StatusBarFilename(sublime_plugin.TextCommand):
    def __init__(self, view):
        super().__init__(view)

        filepath = view.file_name()

        if filepath is None:
            return

        dirpath, filename = os.path.split(filepath)
        dirname = os.path.basename(dirpath)

        view.set_status('filename', os.path.join(dirname, filename))
