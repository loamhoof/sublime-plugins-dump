import sublime
import sublime_plugin


class GoToPointer(sublime_plugin.TextCommand):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.viewport_position = (0, 0)
        self.selected_regions = [sublime.Region(0, 0)]

    def run(self, _):
        selected_regions = self.selected_regions
        self.selected_regions = list(self.view.sel())
        viewport_position = self.view.viewport_position()
        self.view.set_viewport_position(self.viewport_position)
        self.view.sel().clear()
        for selected_region in selected_regions:
            self.view.sel().add(selected_region)
        self.viewport_position = viewport_position
