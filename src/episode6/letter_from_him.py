# -*- coding: utf-8 -*-
'''
Episode 6-5
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


# DEFINE
TITLE = "$sherlockからの手紙"


# NOTE: outlines
ABSTRACT = """
$maryが病院で目覚めると$limeから$sherlockが国外逃亡した$morianoを追っていることを聞かされる。
$maryが自分が$sherlockを傷つけてしまったことを後悔していた。
後日、$sherlockから手紙が届く。そこには$morianoを道連れにしてでも滅ぼす決意と、彼の犯罪関与の証拠とそれについて書いた書類が既に警察に発送されていると記されていた。
最後に$maryについての謝罪が書かれていた。
警察の捜査で$sherlockと$morianoが滝から落下したことが判明。現場に残されていた彼の帽子と血液から、二人は死亡したものと見られた。
"""


# Episode
def main(w: World):
    return w.episode(TITLE,
            # NOTE
            w.plot_setup("負傷した$sherlockは入院し、精神的ショックを受けた$maryも入院する"),
            w.plot_turnpoint("見舞いに訪れた$limeの前から$sherlockは姿を消してしまう"),
            w.plot_develop("$maryたちは$sherlockの行方を探したが見つからない。$moriano犯罪研究所も閉じられ、手がかりが完全に失われた"),
            w.plot_turnpoint("後日$sherlockから手紙がくる"),
            w.plot_resolve("警察の捜索により滝壺から$morianoと$sherlock両名の遺品と思われるものが見つかった"),
            outline=ABSTRACT)

