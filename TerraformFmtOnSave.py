import sublime_plugin


class TerraformFmtOnSave(sublime_plugin.EventListener):
    @staticmethod
    def on_post_save(view):
        if view.file_name().endswith('.hcl'):
            return

        if not view.syntax().scope.startswith('source.terraform'):
            return

        view.window().run_command(
            'build', {
                'build_system':
                'Packages/sublime-plugins-dump/TerraformFmt.sublime-build'
            })
        view.window().run_command('hide_panel', {'panel': 'output.exec'})
