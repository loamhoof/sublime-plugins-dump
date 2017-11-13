import operator
import sublime
import sublime_plugin


class SelectGist(sublime_plugin.TextCommand):
    def run(self, _):
        self.view.window().show_quick_panel(
            list(map(operator.itemgetter('label'), GISTS)),
            self.on_done,
        )

    def on_done(self, gist_index):
        if gist_index == -1:
            return

        self.view.run_command('insert', {'characters': GISTS[gist_index]['code']})


GISTS = [
{
    'label': 'Shebang - bash',
    'code': '#!/bin/bash',
},
{
    'label': 'Golang - recover',
    'code': """defer func() {
        if r := recover(); r != nil {
        }
    }()"""
}
]
