# -*- coding: utf-8 -*-
'''
About: "プロット（トリック面）"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


# world settings
def mystery_note(w: World):
    return w.writer_note('トリック設定',
            w.tag.title("赤鎧組合"),
            "元ネタは「赤毛組合」",
            "赤鎧の人間を募集するという奇妙な内容だが、実はターゲットを守衛場所から遠ざけておくための手段",
            "その間にもぬけの殻となった場所で宝物を奪うための抜け穴を作ったりしていた",
            w.tag.title("$pannaが容疑者に"),
            "容疑者偽装トリック",
            "元ネタは「ボスコム谷の殺人」",
            "$cradesが持ってきた事件を解決したらそこに飛び込んできた新依頼がこれ",
            w.tag.title("元神官の男"),
            "$heroを訪れた時に",
            )

