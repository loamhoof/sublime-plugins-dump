import functools
from pathlib import Path

import sublime
from sublime_plugin import WindowCommand


class PromptOpenRecentProjectOrWorkspace(WindowCommand):

    def run(self):
        project_history = sublime.project_history()

        self.window.show_quick_panel(
            [[
                Path(project).stem,
                project,
            ] for project in project_history],
            functools.partial(self.on_select, project_history),
        )

    def on_select(self, project_history, project_index):
        if project_index == -1:
            return

        self.window.run_command(
            'open_recent_project_or_workspace',
            {'index': project_index},
        )
