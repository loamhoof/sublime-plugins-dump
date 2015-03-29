import sublime_plugin

class JumpToTitle(sublime_plugin.TextCommand):
	def run(self, _):
		titles = self.view.find_all("^# .* #$(?=\n#+$)")
		sub_titles = self.view.find_all("^.+$(?=\n-+$)")

		all_titles = titles + sub_titles
		all_titles.sort()

		self.view.add_regions("titles", all_titles, scope="integer")

		self.view.window().show_quick_panel(
			[self.view.substr(title) for title in all_titles],
			self.on_done,
			on_highlight=self.on_highlight,
		)

	def on_highlight(self, title_index):
		self.move_to_title(title_index)

	def on_done(self, title_index):
		if title_index != -1:
			self.move_to_title(title_index)

		self.view.erase_regions("titles")

	def move_to_title(self, title_index):
		self.view.show(self.view.get_regions("titles")[title_index])
