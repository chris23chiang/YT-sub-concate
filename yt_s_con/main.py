from yt_s_con.pipeline.steps.preflight import Preflight
from yt_s_con.pipeline.steps.get_video_list import GetVideoList
from yt_s_con.pipeline.steps.download_captions import DownloadCaptions
from yt_s_con.pipeline.steps.read_caption import ReadCaption
from yt_s_con.pipeline.steps.postflight import Postlight
from yt_s_con.pipeline.steps.step import StepException
from yt_s_con.pipeline.pipeline import Pipeline
from yt_s_con.utils import Utils

CHANNEL_ID = 'UCKSVUHI9rbbkXhvAXK-2uxA'


def main():
    inputs = {
        'channel_id': CHANNEL_ID
    }

    steps = [
        Preflight(),
        GetVideoList(),
        DownloadCaptions(),
        ReadCaption(),
        Postlight(),
        ]

    utils = Utils()
    p = Pipeline(steps) #pipeline design pattern
    p.run(inputs, utils)

if __name__ == '__main__':
    main()
