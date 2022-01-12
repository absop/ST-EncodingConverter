import sublime
import sublime_plugin


class Run:
    def run(self, edit):
        view = self.view
        if view.has_non_empty_selection_region():
            regions = reversed(view.sel())
        else:
            regions = [sublime.Region(0, view.size())]
        for reg in regions:
            src = view.substr(reg)
            try:
                res = self.convert(src)
                view.replace(edit, reg, res)
            except Exception as e:
                sublime.error_message(f"Convert failed:\n{str(e)}")
                return


class ConvertHexToAsciiCommand(Run, sublime_plugin.TextCommand):
    def convert(self, text):
        return str(bytes.fromhex(text), encoding='utf-8')


class ConvertAsciiToHexCommand(Run, sublime_plugin.TextCommand):
    def convert(self, text):
        return bytes(text, encoding='utf-8').hex()
