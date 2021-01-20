# -*- coding: utf-8 -*-
'''
Episode 3-2
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


# DEFINE
TITLE = "閉じた赤鎧クラブ"


# NOTE: outlines
ABSTRACT = """
$sherlockはまず赤鎧クラブの場所を調べる。$limeが見たという張り紙すら消え、完全に何もなかったことになっていた。
不動産屋にその件を調べてもらうよう、大家の$lisaに頼む。
次は質屋を調べる。旧市街地にあり、すぐに大通りに繋がる場所。近所には改装中の王立銀行もあった。
質屋の店舗は小さいもので、前の店舗部分と奥の控室、更に倉庫となっている。$limeとオーナー夫婦は近所の別の家で暮らしているという。
$sherlockは普段の$limeと$jakinsの仕事内容を聞き、$jakinsに何か起こって失踪した可能性を考える。だが高額なものは置かれておらず、盗まれた形跡もない。
調べてみると、奥の部屋から地下入り口があり、そこからどこかに抜け穴が掘られていた。また近隣の聞き込みから日中頻繁に複数の男が出入りしては大きな袋を運び出していたとも。
その通路を進んでいくと、途中で失踪していた$jakinsの遺体を発見する。更にそれが改装中の銀行の大金庫へと繋がっていたことが分かった。
警察により殺人事件の容疑者として$limeが浮上した。
"""


# Episode
def main(w: World):
    return w.episode(TITLE,
            # NOTE
            w.plot_setup("$limeから赤鎧クラブが閉会したことと同僚$jakinsが失踪したことを聞く$sherlock"),
            w.plot_turnpoint("$sherlockは赤鎧クラブの調査に向かう"),
            w.plot_develop("$limeの言う通り赤鎧クラブは存在そのものが消え去っていた。続いて質屋を調べると奥に地下道を発見する"),
            w.plot_turnpoint("地下道の途中で$jakinsが殺されていた"),
            w.plot_resolve("地下道は改装中の国営銀行の大金庫まで繋がっていて、中から大量の宝石が盗まれていた"),
            w.plot_turnpoint("$jakins殺害容疑で$limeが逮捕された"),
            w.plot_note("$maryによって再び拾われた$lime"),
            w.plot_note("困ったことになったという彼の話を聞く"),
            w.plot_note("以前相談して、その時にすぐ辞めた方がいいと忠告されたにもかかわらず、バイトは続けていた"),
            w.plot_note("$jakinsに相談したら、新しい仕事もそうそう見つけられない中で、せめてなくなるまでは続けたらと言われたからだ"),
            w.plot_note("しかし、今日バイトに行ったら、赤鎧クラブがあった建物は閉鎖され、張り紙一枚してあっただけだった"),
            w.plot_note("赤鎧クラブは本日をもちまして閉会となりました。長年のご愛顧ありがとうございました、という小さな文字のそれがあっただけ"),
            w.plot_note("他の連絡先を知らず、どうしたものかと途方にくれていたのだ"),
            w.plot_note("$sherlockは質屋に戻ったかどうか尋ねる"),
            w.plot_note("意味が分からないらしい"),
            w.plot_note("$sherlockは一緒に行こうという"),
            w.plot_note("ちょうどやってきた$wilsonに$carを出してもらうことになった"),
            #
            w.plot_note("一度赤鎧クラブを確かめる。道順的にそちらの方が近かった"),
            w.plot_note("古い建物で小さな窓のついた平屋建て"),
            w.plot_note("ドアにあった張り紙は綺麗に剥がされていた"),
            w.plot_note("$sherlockは虫眼鏡で観察し、確かにそこに張り紙があったノリの跡を見つける"),
            w.plot_note("施錠され、中には入れず、中から物音もしない"),
            #
            w.plot_note("続いて質屋にやってくる"),
            w.plot_note("大通りから一本入った路地にある"),
            w.plot_note("近所には王立銀行があり、一部改装中で工事の看板が出ている。警備員も出ている"),
            w.plot_note("店は目立たない、質素なものだった。看板も小さく、ショーケースもない"),
            w.plot_note("ただ$limeによると営業中は表に立て看板を出しているという。今は出ていなかった"),
            w.plot_note("ドアを開けて中に入る"),
            w.plot_note("店の中に$jankinsはいない"),
            w.plot_note("$limeは奥に呼びに行く"),
            w.plot_note("と、何か様子がおかしいと戻ってきて、身振り手振り"),
            w.plot_note("控室にも人の姿はなかった。だがそこに$jakins"),
            outline=ABSTRACT)

