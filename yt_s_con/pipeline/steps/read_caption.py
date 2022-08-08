import os
from .step import Step
from yt_s_con.settings import CAPTIONS_DIR
from pprint import pprint

class ReadCaption(Step):
    def process(self, data, inputs, utils):
        data = {} #檔名就是key, 字幕就是value
        for caption_file in os.listdir(CAPTIONS_DIR):
            captions = {}
            with open(os.path.join(CAPTIONS_DIR, caption_file), 'r', encoding='utf-8') as f:
                time_line = False #flag
                time = None
                caption = None
                for line in f:
                    line = line.strip()
                    if '-->' in line:
                        time_line = True
                        time = line
                        continue
                    if time_line:
                        caption = line
                        captions[caption] = time #lterate是抓key
                        time_line = False #reset flag
            data[caption_file] = captions

        pprint(data)
        return data