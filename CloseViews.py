import sublime_plugin


class CloseViewsInGroup(sublime_plugin.WindowCommand):
    def run(self, close_active=True):
        active_view = self.window.active_view()
        active_group = self.window.active_group()
        for view in self.window.views_in_group(active_group):
            if close_active is True or view.id() != active_view.id():
                self.window.focus_view(view)
                self.window.run_command('close_file')


class CloseViewsInWindow(sublime_plugin.WindowCommand):
    def run(self, close_active=True):
        active_view = self.window.active_view()
        for view in self.window.views():
            if close_active is True or view.id() != active_view.id():
                self.window.focus_view(view)
                self.window.run_command('close_file')
        self.window.focus_group(0)
