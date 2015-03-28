import sublime_plugin


class RenameFileCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		self.view.window().run_command("rename_path", {"paths": [self.view.file_name()]})
