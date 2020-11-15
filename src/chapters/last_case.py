# -*- coding: utf-8 -*-
'''
Chapter "最後の事件"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from config import TITLES


# Episode
def the_fixer(w: World):
    return w.episode("事件の黒幕",
            "$sherlockは黒幕の名前が「$moriano」と語る",
            # TODO
            )


def about_moriano(w: World):
    return w.episode("$morianoについて",
            "しかしいつの間にか$morianoは部屋に姿を見せていた",
            )


def his_warning(w: World):
    return w.episode("$morianoの警告",
            )


def lookfor_mary(w: World):
    return w.episode("$maryの捜索",
            )


def rescue_mary(w: World):
    return w.episode("$mary救出劇",
            "しかし$sherlockは単身で$morianoとの対決に向かった",
            )


def his_letter(w: World):
    return w.episode("$sherlockからの手紙",
            "$sherlockから少し前に書いたと思われる内容の手紙が届く",
            w.plot_note("$maryが目覚めるとそこに$sherlockの姿がいなかった"),
            w.plot_note("戻ってきた$wilsonは$sherlockの手がかりを追ったが見失ったと言う"),
            w.plot_note("$maryは$sherlockが戻ってくると信じて待っていたが、連絡も戻ってくることもなかった"),
            w.plot_note("一月が経ち、$maryたちは$sherlockのいない生活に馴染み始めていた"),
            w.plot_note("町では$morianoも$sherlockも消えたというのに犯罪は起こっていた"),
            w.plot_note("$wilsonは手を尽くして$sherlockを探す"),
            w.plot_note("$limeが王室のツテを使い、何とか情報を集めると言い出す"),
            w.plot_note("少年探偵団も手を尽くした"),
            w.plot_note("今まで世話になった人たちも$sherlockのことを探してくれた"),
            w.plot_note("それでも情報すら見つからない"),
            w.plot_note("雨の酷いある日、一通の郵便が届く"),
            w.plot_note("届いた手紙には宛名がなかったが$sherlock特有の署名が入っていた"),
            )


def sad_news(w: World):
    return w.episode("悲しいお知らせ",
            "$sherlockが穴に落ちてなくなったと知らせが届いた",
            w.plot_note("手紙の冒頭にはこう書かれていた"),
            w.plot_note("この手紙が届いたならば自分はすでにこの世界にいないだろうと$sherlockは書いていた"),
            w.plot_note("手紙は$morianoの隠れ家に向かう直前に書いて出したと書かれている"),
            w.plot_note("$morianoは用意周到で、約束通り一人で待っていたりはしない"),
            w.plot_note("$sherlockは陽動をして、手下たちを遠ざけて、可能ならば$morianoをおびき出す"),
            w.plot_note("どうにか一対一で話せる場所を作る、と書いてある"),
            w.plot_note("$morianoがどこまで語るか、告白するかわからないが、彼がやってきた悪事について書き残しておく"),
            w.plot_note("$morianoのことは以前教えたが、大学を出たあとの彼については今回独自調査を行うまで不明な部分が多かった"),
            w.plot_note("$morianoは$cultXと呼ばれる宗教団体との接触から犯罪者人生が始まる"),
            w.plot_note("彼はその教義である人間の本性である「悪」を反映させようとしていた"),
            w.plot_note("今までに解決した事件の裏側にはこの教団か、その教団の人間、関係者が細い糸で繋がっていた"),
            w.plot_note("その大本である$morianoを何としても打ち取ると宣言されていた"),
            w.plot_note("$maryたちは$sherlockがどうなったのか気になり、手紙を出した場所に向かおうとする"),
            w.plot_note("だが$wilsonによりそれは止められる"),
            w.plot_note("兄の$mikelがやってきて「$sherlockがなくなった」と告げた"),
            )


# Chapter
def main(w: World):
    return w.chapter(TITLES[6],
            w.plot_setup("$sherlockは全ての黒幕として$morianoに辿り着く"),
            w.plot_turnpoint("$morianoのメッセージ（暗号）が新聞に掲載される"),
            w.plot_develop("$sherlockが$morianoについて説明する"),
            w.plot_turnpoint("$morianoが現れる"),
            w.plot_develop("$morianoは$sherlockに全てから手を引くよう警告する"),
            w.plot_turnpoint("$maryが人質として連れ去られる"),
            w.plot_develop("$morianoの手がかりを見つけ出し、$maryの居所を見つける"),
            w.plot_turnpoint("$maryを助け出す"),
            w.plot_develop("$sherlockは$maryたちを騙して単身$morianoの隠れ家に向かった"),
            w.plot_turnpoint("$sherlockから手紙が届く"),
            w.plot_resolve("$sherlockからの最後の手紙で彼が$morianoと共に穴に落ちたことを知る"),
            the_fixer(w),
            about_moriano(w),
            his_warning(w),
            lookfor_mary(w),
            rescue_mary(w),
            his_letter(w),
            sad_news(w),
            )


