# -*- coding: utf-8 -*-
"""
    File Name: replace_command
    Description: ""
    Author: Donny.fang
    Date: 2020/6/4 15:08
"""
from spl_arch.command.base_command import BaseCommand


class ReplaceCommand(BaseCommand):
    def __init__(self, cmd_name, cmd_type, val, replace_val, field):
        super(ReplaceCommand, self).__init__(cmd_name, cmd_type)
        self.val = val
        self.replace_val = replace_val
        self.field = field
        self.in_stream, self.out_stream = None, None

    def set_input_stream(self, in_stream):
        self.in_stream = in_stream

    def set_output_stream(self, out_stream):
        self.out_stream = out_stream

    def stream_in(self):
        return self.in_stream

    def calc(self):
        docs = self.in_stream

        for doc in docs:
            raw = doc["_source"]["_raw"]

            if raw[self.field] == self.val:
                raw[self.field] = self.replace_val

        self.set_output_stream(docs)
