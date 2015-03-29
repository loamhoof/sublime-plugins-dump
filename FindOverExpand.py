import sublime_plugin
from sublime import Region

class FindOverExpand(sublime_plugin.TextCommand):
    def run(self, _):
        selected_regions = [region for region in self.view.sel()]
        text_to_find = self.view.substr(selected_regions[0])
        text_to_search_in = self.view.substr(Region(0, selected_regions[0].begin()))

        index = text_to_search_in.rfind(text_to_find)

        if index != -1:
            self.select_region(index, index + len(text_to_find))
        else:
            high_boundary = self.view.size()
            for region in reversed(selected_regions):
                low_boundary = region.end()
                text_to_search_in = self.view.substr(Region(low_boundary, high_boundary))

                index = text_to_search_in.rfind(text_to_find)

                if index == -1:
                    high_boundary = region.begin()
                else:
                    self.select_region(low_boundary + index, low_boundary + index + len(text_to_find))


    def select_region(self, low_boundary, high_boundary):
        region_to_select = Region(low_boundary, high_boundary)
        self.view.sel().add(region_to_select)
        self.view.show(region_to_select)
