import sublime_plugin


class ChangeViewInGroup(sublime_plugin.WindowCommand):
    def run(self, step=1):
        views = self.window.views_in_group(self.window.active_group())
        index = views.index(self.window.active_view())
        self.window.focus_view(views[(index + step) % len(views)])
