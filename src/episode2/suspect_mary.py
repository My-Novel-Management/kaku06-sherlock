# -*- coding: utf-8 -*-
'''
Episode 2-2: "容疑者$mary"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


# DEFINE
TITLE = "容疑者$mary"


# NOTE: outlines
ABSTRACT = """
警察にやってきた$sherlockたち。$patsonは$maryとは会わせられないという。
$sherlockは$restradeのツテを利用してなんとか僅かばかりの面会の時間を得る。
面会した$maryは衰弱していたが、$sherlockが$keanの依頼できたことを知ると、全て話すと言った。
$maryは自分が父親に話があるからと呼び出されて事件現場に行った。どうしても家の中で話せないことがあるからと。
そこで自分が拾われた子供だったと告白された。それにショックを受け、そのままその場を立ち去った。途中バラ園で休んでから家に戻った。そのまま部屋から一歩も出ず、翌朝、$kailに起こされて父親が亡くなったことを聞かされた、と。
その時にはまだ誰が殺したか分からず、ただしんだことだけ教わった。
その後、警察が来たり、それぞれ事情聴取された。何故か自分の部屋から凶器の$gunが発見され、容疑者になってしまった。
自分は絶対にやらないし、拾われ子だったことはショックだったが、父親には恩義しか感じていないと。
面会後、$sherlockは全てを語っていないと言う。
$maryは$animalだった。またそれが警察の容疑者候補として強い印象になっていると。
"""


# Episode
def main(w: World):
    return w.episode(TITLE,
            # NOTE
            w.plot_setup("警察にやってきた$sherlockはそこで容疑者の$maryと面会をする"),
            w.plot_turnpoint("$maryは沈黙を守っていたが$keanの名前に安心して話し始めた"),
            w.plot_develop("$maryから事件前後の話を聞く。彼女は父親に呼び出されてある話をされたと語った"),
            w.plot_turnpoint("$maryは家に帰った時に使用人の$kailと顔をあわせたと言った"),
            w.plot_resolve("地元刑事の$patsonは警察は確かな証拠を掴んでいるからこのまま証拠と証言を固めて裁判所に送ると言う"),
            w.plot_turnpoint("$sherlockは$maryが$animalであると言った"),
            w.plot_note("警察にやってきた$sherlock"),
            w.plot_note("応対に出た地元警官は変な人物を見る目"),
            w.plot_note("それでも現場責任者という地元の刑事を連れてきてくれた"),
            w.plot_note("若そうな刑事$patsonがやってくる"),
            w.plot_note("$patonは金髪（染めている）でかっこつけて服を着崩している"),
            w.plot_note("$patsonは$sherlockが事件を調べているというと、怪しむ"),
            w.plot_note("ついてきた新聞記者$milkが$restradeとも親交があると言うと、その名前に驚く$patson"),
            w.plot_note("部下の$shotから「ひょっとしてあの噂になってる方じゃないすか？」"),
            w.plot_note("警察内の業界紙に「事件解決に協力してくれた人物」として名前が出ている"),
            w.plot_note("「話を聞かせてもらえるだけでいいんだ」と$sherlock"),
            w.plot_note("$patsonは渋々といった様子で承諾する"),
            #
            w.plot_note("面会用の個室に入って待っている$sherlock。$wilsonと$milkは部屋の外に追い出された"),
            w.plot_note("見張りの警官$shotがいて、$patsonが手錠をつないだ$maryを連れてくる"),
            w.plot_note("$maryは青白い顔をして、あきらかに憔悴していた"),
            w.plot_note("小柄で栗色の髪。$royd氏の肖像画は黒髪だったから、母親似なのかと考える"),
            w.plot_note("$maryは黙ったまま何もしゃべらず"),
            w.plot_note("$sherlockは自分が$keanに頼まれてここにやってきたことを話すと表情が柔らかくなる"),
            w.plot_note("$sherlockは更に自分は可能性として$maryがやっていない方を強く見ていると発言"),
            w.plot_note("それでも色々な可能性を考えて、本当にやっているとしたらその時は犯人として扱うと"),
            w.plot_note("$maryは決意し、話し始める"),
            w.plot_note("$maryは父親に、事件のあった日の朝、話があるが家の中では話せないから、いつも使っている外の小屋（バラ園の側）で話すと言った"),
            w.plot_note("父親は最近地元の農地開発に精力的で、$keanが管理しているバラ園もその一環だった"),
            w.plot_note("日が沈むと、$maryはこっそりと出かけた。誰にも言っていない"),
            w.plot_note("バラ園までには一人、牛飼いの$roseaと出会った（これは証言取れている）"),
            w.plot_note("父親は待っていて、そこである話を$maryにした"),
            w.plot_note("家庭内のことだから秘密にしたいと、ここは話さなかった"),
            w.plot_note("その話が終わった後、$maryはすぐに家に戻った"),
            w.plot_note("それから疲れてそのまま部屋でずっと寝ていた、と"),
            w.plot_note("朝になって一度起きたが、誰もいなくて、キッチンにあったミルクを飲んでから、また寝たと"),
            w.plot_note("昼前になり、$kailに起こされた"),
            w.plot_note("目覚めたら部屋のテーブルに$gunが置いてあり、$kailはそれを見て「お前がやったんだな？」と言った"),
            w.plot_note("何があったのか分からないままで、布団にくるまって怖がっていた"),
            w.plot_note("続いて部屋に$keanが入り「落ち着いてください」と言われた"),
            w.plot_note("何があったのかすぐには説明してもらえず、待っていると警察が入ってきて、逮捕する、ということになった"),
            w.plot_note("警察にいってから父親が亡くなったことを知った"),
            w.plot_note("事情がよく分からないまま、自分は父親に呼び出されて会いに行っただけで他は何も知らない、の一点張り"),
            w.plot_note("以上が全てだ、と$maryは語った"),
            w.plot_note("$sherlockは事情は理解した、と言った上で、こう付け加える「今後、君が話したくないことを話す場面が出るかもしれない。それだけは少し覚悟しておいてほしい」と"),
            w.plot_note("$maryが連れ出され、面会は終わった"),
            #
            w.plot_note("別れ際、$patsonから「証拠はある。絶対に$maryが犯人だ」と言う"),
            w.plot_note("$sherlockは$wilsonに「何だと思う？」と"),
            w.plot_note("$wilsonは「$gunだろう？　それ以外にない」"),
            w.plot_note("彼女はね、実は$animalなんだ。そう$sherlockは語った"),
            outline=ABSTRACT)

