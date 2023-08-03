import functools
import os.path

import sublime
import sublime_plugin

PLUGIN_DIR = os.path.dirname(os.path.realpath(__file__))
GISTS_DIR = os.path.join(PLUGIN_DIR, 'gists')


class SelectGist(sublime_plugin.TextCommand):
    def run(self, _):
        gists = sorted(os.listdir(GISTS_DIR))

        self.view.window().show_quick_panel(
            gists,
            functools.partial(self.on_done, gists),
        )

    def on_done(self, gists, gist_index):
        if gist_index == -1:
            return

        settings = self.view.settings()
        auto_indent = settings.get('auto_indent')
        settings.set('auto_indent', False)

        with open(os.path.join(GISTS_DIR, gists[gist_index])) as f:
            self.view.run_command('insert', {'characters': f.read()})

        settings.set('auto_indent', auto_indent)


try:
    os.mkdir(GISTS_DIR)
except FileExistsError:
    pass
