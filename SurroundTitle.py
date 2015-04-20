import sublime_plugin


default_char = "#"
caption = "Surround line(s) with:"


class SurroundTitle(sublime_plugin.TextCommand):
	def run(self, edit, char=default_char):
		sel = self.view.sel()

		for region in sel:
			lines = self.view.lines(region)
			max_size = max(line.size() for line in lines)
			chars = char * (max_size + 4)
			self.view.insert(edit, lines[-1].end(), "\n" + chars)
			for line in lines[::-1]:
				self.view.insert(edit, line.end(), (max_size - line.size() + 1) * " " + char)
				self.view.insert(edit, line.begin(), char + " ")
			self.view.insert(edit, lines[0].begin(), chars + "\n")


class SurroundTitlePanel(sublime_plugin.TextCommand):
	def run(self, _):
		self.view.window().show_input_panel(caption, default_char,
			on_done=self.on_done,
			on_change=None,
			on_cancel=None
		)

	def on_done(self, char):
		self.view.run_command("surround_title", {"char": char})
