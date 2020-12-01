# -*- coding: utf-8 -*-
'''
Stage: "書斎"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


# NOTE
#   後のウィルソン（本物）が使っている書斎
#   場所は現在のウィルソンの家とは異なり、隠遁生活中のコテージの中


## scenes
def note_for_thisnovel(w: World):
    return w.scene("作品のための注意書き",
            w.change_stage("ReadingRoom"),
            w.change_time("night"),
            w.plot_note("本作品は全て三人称で記述される"),
            w.plot_note("記述者＝私により後から整理され、書かれたもの"),
            w.plot_note("聞いた時が前後しても、読んでいくのにいいように並べ替えてある"),
            w.plot_note("本作は$sherlockという男を中心に巻き起こった事件について書いた、伝記的作品である"),
            )


def allend_and_allstart(w: World):
    wil = w.get("wilson")
    mary = w.get("mary")
    return w.scene("すべての始まりと終わり",
            w.change_camera("wilson"),
            w.change_stage("ReadingRoom"),
            w.change_time("night"),
            w.change_date("future_day"),
            w.plot_note("こうして、$wilsonは探偵小説を書くことになった、と告白する"),
            w.plot_note("またこの作品の記述者は自分だったと告白"),
            w.plot_note("ここまで書いてきたのは全て$wilsonである、と告白"),
            w.plot_note("$wilsonはずっとライターをしてきた"),
            w.plot_note("$sherlockが$heroだということには驚きを隠せないが、その知性は自分が知る「探偵」そのものだ"),
            w.plot_note("この世界で再び$bossが復活し、世界を闇に包み込むようなことがないよう監視する必要もある"),
            w.plot_note("いつか$sherlockが本物の$heroとして冒険の旅に出るなら、それも見届けたいと思うと記述"),
            w.plot_note("そこに再び奇妙な依頼主が現れる"),
            w.plot_note("そこからとんでもない冒険の旅にまきこまれるのだが、それはまた別の物語としよう、と閉める"),
            #
            # TODO
            wil.be("書斎でこの小説の最後を書いている"),
            wil.think("こうして$meは探偵小説を書くことになったことを思い出す"),
            wil.think("と、ここまで書いてくれば$meが誰か分かったことだろう"),
            mary.come("キッチンから声をかけながらやってくる"),
            mary.talk("なあ$wilson、まだそれかかるん？"),
            wil.talk("もう終わるところだが、何かな？"),
            mary.talk("もらったケーキみんなで食べようって"),
            wil.talk("わかった。五分ほどで行くから先に食べてて"),
            mary.talk("ちゃうよー。みんな揃わんとあかんの"),
            wil.talk("ほんの少しだけだよ。すぐに行く"),
            mary.talk("ほんまか？　すぐやで？"),
            mary.go(),
            wil.do("そこには$me以外の四人、$maryと$lime、そしてこの素晴らしく"),
            )
