# -*- coding: utf-8 -*-
'''
Episode 2-0: "悲しい事件"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from config import TITLES


# Scenes
# NOTE

# NOTE: outlines
ABSTRACT = """
$wilsonは毎日のようにやってきては$sherlockに第二王女失踪事件の調査を依頼しようとする。だが$sherlockはその気はなく、新聞記事を見ては興味のある事件を探している。
記事のある事件。資産家の男が娘に$gunによって殺されるという悲しい事件があった。明け方に新聞配達の男により沼地で倒れている$royd氏が見つかり、死亡が確認された。
警察は状況から娘を容疑者として逮捕し、取り調べを行っていると。
$gunについては詳細は書かれていないが、最近ちょくちょく出回っているものだ。闇社会で資金源になっているのかも知れないと$sherlockは言う。
一方、失踪事件については明確な証拠も関連性もなく、王女のそれについてもよく分からないと$sherlock。
$wilsonの依頼は受けないが、警察や他の依頼者の依頼は色々と抱えていた。
また自分自身で犯罪関連の研究も行っていた。今日は自分の血液を採取して、血の研究をしていた。
と、そこに訪問者がある。
その事件の被害者宅に務める使用人の息子$keanが訪れて、$sherlockに容疑者である娘の容疑を晴らして欲しいと依頼した。
"""


# Episode
def main(w: World):
    return w.episode("悲しい事件",
            # NOTE
            w.plot_setup("$wilsonは毎日のようにやってきて$sherlockに仕事を依頼しようとするが$sherlockは無視して新聞から興味深い事件を探す"),
            w.plot_turnpoint("$sherlockは犯罪解決のための開発に忙しいと外出してしまう"),
            w.plot_develop("翌日も訪れた$wilsonは$sherlockが興味を持ちそうな事件を探す。田舎町の悲しい父親殺しの事件をピックアップし、それについて$sherlockに尋ねる"),
            w.plot_turnpoint("そこに一人の少年（$kean）が仕事を依頼したいと訪れる"),
            "地元の新聞社の仲良い人の紹介",
            w.plot_resolve("父親殺し事件の容疑者となった娘の家に勤める使用人$keanが、娘の無実を証明してほしいと依頼に訪れた"),
            w.plot_turnpoint("なけなしの小遣いで依頼する$keanに、$sherlockは二つ返事で受け付けた"),
            outline=ABSTRACT)

