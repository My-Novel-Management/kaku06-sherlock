# -*- coding: utf-8 -*-
'''
Stage: "シャーロックの家"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


# NOTE
#   物語が展開する中心。事務所
#   シャーロックが借りて住んでいる古い一軒家（二階建て）で、B221という看板が近くにある
#   幽霊が出るといういわくつきの物件で安かった。原因は地場発生の魔石があっただけ
#   ：２F
#   [物置][空き部屋]
#   [寝室１][寝室２]
#   ：１F
#   [キッチン][バス]
#   [ダイニング][トイレ]
#   [研究室]
#   [リビング][書斎]


## scenes
def about_sherlock(w: World):
    return w.scene("$sherlockという男について",
            w.plot_note("知っていたならなぜ忠告してくれなかったんだ、と$wilsonが$sherlockに文句をいい、なんとか家に入れてもらえる"),
            w.plot_note("中に入るとそこら中に本や資料がちらばっていた"),
            w.plot_note("$wilsonはそこで依頼をしようと思ったが、"),
            w.plot_note("そこに何も記載のない手紙が投げ込まれた"),
            )


def read_prince_letter(w: World):
    return w.scene("皇太子の書簡の中身",
            w.plot_note("手紙には独特の紙が使われていて、それが王室のものだと$sherlockは分かった"),
            w.plot_note("中は皇太子からの手紙で、$sherlockに頼みごとが書かれていた"),
            w.plot_note("皇太子は女遊びがひどくてその界隈では有名だが、今回ついに腰を落ち着けて結婚することになった"),
            w.plot_note("相手は近隣の公国の王女で、政治的な意味合いも大きい"),
            w.plot_note("その結婚に際して過去の女性関係をすべて綺麗にした"),
            w.plot_note("ただある一人の女性にプレゼントしてしまった大切なナイフを返してもらいたいが、相手の女性が応じてくれない"),
            w.plot_note("揉め事をおこしたくないので、穏便にすませたいから、$sherlockに彼女を説得して、ナイフを返してもらってくれないか、という依頼"),
            w.plot_note("$sherlockはその依頼内容について、書かれていない部分の推測を述べる"),
            w.plot_note("ナイフと書いているが、実際は王室に伝わる宝剣で、それが王の証の一つで、結婚の際には儀式内で使われる"),
            w.plot_note("酒の勢いで大切な宝剣をあげてしまったのだろうと"),
            w.plot_note("そんなものを取り戻す義理はないが、恩があるので仕方なく依頼を受けると言った"),
            w.plot_note("$sherlockは$wilsonにその女性の家まで送ってほしいと頼んだ"),
            )


def important_than_sword(w: World):
    return w.scene("宝剣より大事なこと",
            w.plot_note("$sherlockは宝剣よりも殺人事件についての調査をしたいと、$wilsonを家に置いて出ていってしまう"),
            w.plot_note("$wilsonは$sherlockの家に戻り、そこで彼を待つことにする"),
            w.plot_note("やってきた若い刑事は$sherlockがいないことに落胆しつつも、状況を教えてくれる"),
            w.plot_note("発見された遺体は一月ほど前に行方不明になった女性だった"),
            w.plot_note("$ailyとは何の関係もなく、そこの接点も見つけられないと嘆く"),
            w.plot_note("殺害方法も不明で、凶器すら見つけられないと"),
            w.plot_note("そこに役所の男から$ailyという女性が住民登録をしたという形跡は見つけられなかったと連絡がきた"),
            )
