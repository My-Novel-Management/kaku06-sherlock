# -*- coding: utf-8 -*-
'''
Episode 4-2
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


# DEFINE
TITLE = "ガチョウクラブ"


# NOTE: outlines
ABSTRACT = """
$wilsonから$jackが容疑者として浮上していることを知らされ、$sherlockは$jackについての情報を探ってもらっている情報屋に確認を取る。
特に彼女が国内に戻ってきた情報はなく、最近は$jackによるものと見られる盗難事件もない為に$sherlockは何者かが彼女を利用していると考える。
一方、$maryは$ignesとともにガチョウクラブに潜入する。
会員制でガチョウを安く手に入れられるという表向きだったが、そこには$ignesも知るアンダーグラウンドの大物が出入りしていた。
目をつけられる$maryたちだったが、謎の女性により助けられる。
その女性からもうガチョウクラブには出入りしないように注意される。
一旦家に戻った$maryだったが、$sherlockが調べている事件の被害者がガチョウクラブの会員だと分かり、再度ガチョウクラブへの潜入を決意。
ガチョウクラブの男たちが$drag取引をしている現場を目撃した$maryは、逃げ出そうとして気づかれ、捕まってしまう。
"""


# Episode
def main(w: World):
    return w.episode(TITLE,
            # NOTE
            w.plot_setup("$maryはガチョウクラブの情報を仕入れて$sherlockに相談しようとする"),
            w.plot_turnpoint("$sherlockは$jackが国内に入っているという情報を得て、出ていってしまう"),
            w.plot_develop("$maryは$limeと$ignesに頼んでガチョウクラブについて潜入捜査を試みる"),
            w.plot_turnpoint("会員名簿の中に殺された$moura夫人の夫の名前を見つける"),
            w.plot_resolve("もらったガチョウから$dragを発見する"),
            w.plot_turnpoint("$maryは$dragと$gunの取引現場を目撃してしまう"),
            w.plot_note("$maryは肉の卸問屋$hornetにガチョウクラブが何か尋ねる"),
            w.plot_note("ガチョウクラブは会員制のガチョウ投資団体で、決まった月額でガチョウを飼育し、それを安く購入できるようにするもの"),
            w.plot_note("また販売した利益から何割かは戻ってきて、会員が増えるほど儲けも大きくなるという"),
            w.plot_note("最近よく取り扱っていると言われた"),
            w.plot_note("$maryはガチョウクラブの本部を教えてもらう"),
            w.plot_note("ただ当日仕入れたガチョウがどのガチョウだったのかはよく分からないと"),
            w.plot_note("ガチョウクラブからのものもあったが、他にもいくつかの農家から分けてもらったので"),
            w.plot_note("$maryはお礼を言ってガチョウクラブに向かうことにする"),
            #
            w.plot_note("$sherlockは単身、$moura夫人の家にやってきていた"),
            w.plot_note(""),# TODO
            outline=ABSTRACT)

