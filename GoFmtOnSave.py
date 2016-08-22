import os.path

import sublime_plugin


class GoFmtOnSave(sublime_plugin.EventListener):
    @staticmethod
    def on_post_save(view):
        if os.path.splitext(view.file_name())[1] == '.go':
            view.window().run_command('build', {'build_system': 'Packages/sublime-plugins-dump/Gofmt.sublime-build'})
            view.window().run_command('hide_panel', {'panel': 'output.exec'})
