import sublime_plugin


class TerragruntFmtOnSave(sublime_plugin.EventListener):
    @staticmethod
    def on_post_save(view):
        if not view.file_name().endswith('.hcl'):
            return

        if not view.syntax().scope.startswith('source.terraform'):
            return

        view.window().run_command(
            'build', {
                'build_system':
                'Packages/sublime-plugins-dump/TerragruntFmt.sublime-build'
            })
        view.window().run_command('hide_panel', {'panel': 'output.exec'})
