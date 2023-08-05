import re

from parse import parse

from mcdreforged.handler.impl import BukkitHandler

class Del_ANSICodeHandler(BukkitHandler):
    def get_name(self) -> str:
        return 'del_ansicode_handler'

    def pre_parse_server_stdout(self, text: str) -> str:
        text = super().pre_parse_server_stdout(text)
        pattern = r'\x1b(\[.*?[@-~]|\].*?(\x07|\x1b\\))'
        return re.sub(pattern, '', text)