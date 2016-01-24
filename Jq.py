from os import path
import subprocess
from tempfile import TemporaryFile
from contextlib import closing

import sublime_plugin
from sublime import Region


JQ_PATH = path.join(path.dirname(path.realpath(__file__)), 'jq-linux64')
history = []
history_index = None
current_input = None
caption = "Command:"
default_command = "."


class Jq(sublime_plugin.TextCommand):
    def run(self, edit):
        tmp_file = TemporaryFile()
        whole_file = Region(0, self.view.size())
        with closing(tmp_file):
            jq_input = self.view.substr(whole_file).encode('utf-8')
            tmp_file.write(jq_input)
            tmp_file.seek(0)
            jq_output = subprocess.check_output([JQ_PATH, history[-1]], stdin=tmp_file)
        self.view.replace(edit, whole_file, jq_output.decode('utf-8'))


class JqPanel(sublime_plugin.TextCommand):
    def run(self, _):
        global history_index, current_input

        self.panel = self.view.window().show_input_panel(caption, default_command,
            on_done=self.on_done,
            on_change=self.on_change,
            on_cancel=self.on_cancel
        )
        self.panel.settings().set('JqInputPanel', True)
        history_index = 0
        current_input = default_command

    def on_change(self, command):
        global current_input

        if history_index == 0:
            current_input = command

    def on_done(self, command):
        self.panel.settings().set('JqInputPanel', False)
        history.append(command)
        self.view.run_command('jq')

    def on_cancel(self):
        self.panel.settings().set('JqInputPanel', False)


class JqHistory(sublime_plugin.TextCommand):
    def run(self, edit, backwards=False):
        global history_index

        history_index += 1 if backwards else -1
        history_index %= len(history) + 1

        region_to_replace = Region(0, self.view.size())

        self.view.replace(edit, region_to_replace, ([current_input] + history)[-history_index])
