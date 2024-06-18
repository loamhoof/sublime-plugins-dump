import sublime_plugin


class JsonnetFmtOnSave(sublime_plugin.EventListener):

    @staticmethod
    def on_post_save(view):
        if not view.syntax().scope.startswith('source.jsonnet'):
            return

        view.window().run_command(
            'build', {
                'build_system':
                'Packages/sublime-plugins-dump/JsonnetFmt.sublime-build'
            })
        view.window().run_command('hide_panel', {'panel': 'output.exec'})
