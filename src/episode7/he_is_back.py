# -*- coding: utf-8 -*-
'''
Episode 7-3
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


# DEFINE
TITLE = "英雄の帰還"


# NOTE: outlines
ABSTRACT = """
変身して$sherlockたちを追い詰める$jake。しかし$sherlockの機転で工場に穴を開け、日光を浴びせかけることで$jakeは皮膚から大量に出血し、爆発した。
その爆音を聞いて$limeたちが駆けつける。$maryが身を挺して$sherlockを守っていたが、$maryは大怪我を負ってしまった。入院することになる$mary。
戻った$sherlockは、一旦$wilsonの家で$limeたちに事情を語る。
$morianoとの対決により滝壺に落下し、死を覚悟した$sherlockだったが、$maryが繕ってくれた服の裾が引っかかり、何とか死だけは免れた。
ただ大怪我をしており、そこを助けてくれたのが、$jackだった。彼女の別荘で回復するまで休養しながら各国の情報を集め、$moriano配下の動向を追いかけていた。
未だに$sherlockを探す動きが見えたので、おびき出すために空き家の件をでっち上げた。だがそれを利用した$jakeにより$maryがおびき出された、というのが今回の一件だった。
$sherlockは$maryに預けておいた$blue_stoneを取り戻す必要があると言う。
しかし$sherlockたちが病院に駆けつけると、$maryの姿が消えていた。
"""


# Episode
def main(w: World):
    return w.episode(TITLE,
            # NOTE
            w.plot_setup("連続殺人犯$jakeは$maryを殺そうとする"),
            w.plot_turnpoint("そこにホームレスが助けに入る"),
            w.plot_develop("$sherlockは$jakeがどんな人生を歩んできたかを全て言い当て$jakeの牙を無力化しようとする"),
            w.plot_turnpoint("$transformした$maryにより$sherlockが守られるが、彼女が負傷する"),
            w.plot_resolve("$sherlockが呼んでおいた警察により$jakeは捕らえられた。$maryは入院し、$sherlockも治療を受ける"),
            w.plot_turnpoint("入院している$maryから$blue_stoneを貰おうと思ったが$patosonにより連れ出された後だった"),
            w.plot_note("$maryは病室で目覚める"),
            w.plot_note("そこには$patsonの姿があった"),
            w.plot_note("$maryは$sherlockは？　と尋ねるが、わからないと言われる"),
            w.plot_note("$patsonは$maryへの事情聴取を行う"),
            w.plot_note("一体あそこで何を見たのか"),
            w.plot_note("$maryはその黒焦げの遺体が、連続猟奇殺人事件の犯人だと証言した"),
            w.plot_note("$patsonは$jakeがそう告白したのか？　と尋ねた"),
            #
            w.plot_note("$limeは$ignesたちから$maryが爆発現場で発見されたと聞く"),
            w.plot_note("その$ignesはホームレスと仲良さそうに話している"),
            w.plot_note("その男こそ$sherlockだった"),
            w.plot_note("$limeは驚き、事情を聞く"),
            w.plot_note("$sherlockは実はずいぶん前に国内に戻ってきていて、$ignesは事情を知らされていた"),
            w.plot_note("$sherlockを狙う連中をごまかすために、色々と嘘の情報をばらまいていた"),
            w.plot_note("空き家情報も嘘のものだったが、それを使って猟奇殺人犯の$jakeが細工をし、$maryをおびき出した"),
            w.plot_note("それを先導した人間が誰かいる、と$sherlockは言う"),
            w.plot_note("滝壺から落ちたあと、$jackに助けられ、彼女の隠れ家で治療をしてもらっていた"),
            w.plot_note("今回殺害されていた$ronaldが所有していた最後の$black_stoneが盗まれたことがわかり、戻ってきた"),
            w.plot_note("四つ$stoneを揃えられるとまずい、と$shserlockは言う"),
            w.plot_note("ひとまず$maryの様子を見に行くことにし、タクシーを拾う（これが$jack）"),
            #
            w.plot_note("病院にやってくると先に様子をみにきていた$refiがいる"),
            w.plot_note("$refiは泣きそうになって、$maryを$patsonが連れ出したという"),
            w.plot_note("$sherlockはそれで理解し、すぐに大聖堂に向かうと"),
            w.plot_note("しかし$wilsonがいない。タクシー運転手に頼んで向かってもらう"),
            #
            w.plot_note("車内で説明する$sherlock"),
            w.plot_note("四つの$stoneは$boss復活の儀式に必要な祭具だった"),
            w.plot_note("かつて$bossを倒した$heroたちの神器にはまっていたものだが、$bossの力を吸収し、封じ込めたもの"),
            w.plot_note("それが時代を経て、売られたり、盗まれたりし、行方不明になった"),
            w.plot_note("今ある多くはレプリカだという"),
            w.plot_note("実際に四つ揃え、かつての$boss城があった場所で儀式を行う"),
            w.plot_note("それが大聖堂だという"),
            w.plot_note("$boss城を封じる目的であの場所に建っていたのだ"),
            w.plot_note("昨年春にあった地震は儀式の失敗だという"),
            w.plot_note("その頃はまだ何が必要なのか、すべて判明していなかった。だが$stein教授により解明された"),
            w.plot_note("その資料は$morianoにより盗まれ、紛失している"),
            w.plot_note("実際にどういうものなのかは$sherlockも知らない"),
            #
            "$wilsonは最後に登場",
            w.plot_note("大聖堂にやってくると、何があったのか警官（$parkerたち）が警備していた"),
            w.plot_note("巨大な爆弾が見つかったというのでみんなを避難させるように言われたと"),
            w.plot_note("そこに$restradeもやってきて、困惑している"),
            w.plot_note("一体何をやってるんだ、$patsonはと"),
            w.plot_note("$sherlockはすぐ$patsonの家を調べるように言う。彼が$cultXの手先だった"),
            w.plot_note("$sherlockは中に入る"),
            #
            w.plot_note("大聖堂の中は人がいなくなり、静まり返っていた"),
            w.plot_note("聖堂を進む"),
            w.plot_note("偉人たちの墓が並ぶ聖廟でもあった"),
            w.plot_note("その一つが開けられている。中身はない"),
            w.plot_note("扉があり、奥にいくと地下への階段"),
            w.plot_note("地下に降りていく$sherlockたち"),
            w.plot_note("そこには巨大なホールが広がっていた"),
            w.plot_note("祭壇には四つの$stoneが供えられ、$patsonが儀式を始めようとしている"),
            w.plot_note("誰も入れるなと言ったのに、と不敵な顔の$patson"),
            w.plot_note("$maryは倒れていた。服が少し破れている。中に$stoneを身に着けていたからだ"),
            w.plot_note("$sherlockがすぐにやめるように忠告する"),
            w.plot_note("儀式は失敗すると言った"),
            w.plot_note("しかし$patsonは儀式を行うべく、祝詞をとなえる"),
            w.plot_note("その$patsonを現れた$wilsonが$gunで撃ち抜いた"),
            w.plot_note("「間に合ってよかったよ」という$wilson"),
            outline=ABSTRACT)

