# -*- coding: utf-8 -*-
'''
Stage: "地下室（古城内）"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


# NOTE
#   拷問部屋と儀式部屋はここで扱う。地下への通路や階段も


## scenes
def goto_basement_stairs(w: World):
    return w.scene("地下室への階段",
            )


def torture_room(w: World):
    return w.scene("拷問部屋",
            w.plot_note("地下にはかつての拷問部屋が存在していた"),
            w.plot_note("そこで新しい血の跡を発見する"),
            w.plot_note("振り返ると$cherryがいた"),
            w.plot_note("彼女は近代まで使われていたと語る"),
            w.plot_note("実際事故死した彼女の夫もそれを使い、使用人を何人も病院送りにしているらしい"),
            w.plot_note("そこに犬用のトレイを見つけた"),
            w.plot_note("$sherlockはここで犬を買っていることを示唆するが、$cherryは強く否定する"),
            w.plot_note("だがそこに大きな黒い犬が出現する"),
            w.plot_note("殺そうとしたところに、$cherryは体を張って立ちふさがった"),
            )


def confession_criminal(w: World):
    return w.scene("犯人の告白",
            w.plot_note("$sherlockは全ての犯行が彼女によるものだと断言する"),
            w.plot_note("全ての犯行が獣にやられるように見せかけられていたが、この拷問室にある道具には獣の歯型をした拷問具があった"),
            w.plot_note("それに新しい血がついているので、これが使われたと"),
            w.plot_note("この場所を知っていた人間は$cherry以外に誰かいるのか尋ねると、$mockもだと語った"),
            w.plot_note("彼女は全ての計画は彼がねって実行したものだと言う"),
            w.plot_note("しかし$sherlockは彼がここに赴任して三年目だということを知っていた"),
            w.plot_note("犯人だと論破された$cherryは部屋を真っ暗にして逃げ出す"),
            )


def runaway_cherry(w: World):
    return w.scene("逃亡",
            w.plot_note("$sherlockは彼女を助けないと危ないという"),
            w.plot_note("しかし彼女が出ていった出口は閉ざされ、別の出入り口を探すしかなくなった"),
            w.plot_note("そうこうしているうちに島に到着した警察が、助けに入ってくる"),
            w.plot_note("やってきた$restradeに事情を説明し、$cherryを捜索してもらう"),
            )


def ritual_room(w: World):
    return w.scene("儀式の部屋",
            w.plot_note("女主人$cherryの死去により事件は全てに幕を下ろした"),
            w.plot_note("死後に見つかった手記により今までの大半の事件の陰に彼女の存在があったことが判明する"),
            w.plot_note("$sherlockは死後に秘密の地下室を発見し、そこで儀式の跡を見た"),
            )
