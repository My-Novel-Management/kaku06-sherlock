# -*- coding: utf-8 -*-
'''
Stage: "古城内の談話室"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


# NOTE
#   古城内の談話室はここで扱う


## scenes
def invited_guests(w: World):
    return w.scene("招待客たち",
            w.plot_note("$sherlock以外に招かれたのは怪奇事件の専門家や、動物学者、医師、心霊現象の研究家などだった"),
            w.plot_note("地域の研究者は$bossが生きていた頃から魔獣が存在していて、今もその生き残りがこの島で生き延びているのだと説明する"),
            w.plot_note("$maryは美味しい料理に喜ぶ"),
            )


def isolation_us(w: World):
    return w.scene("孤立する$sherlockたち",
            w.plot_note("$mochが警察を呼ぼうとしたが海が荒れて船が出せない"),
            w.plot_note("地方で最新技術の$telephoneもなく、海が収まるまで連絡できないと言われる"),
            w.plot_note("孤島に閉じ込められた$sherlockたち"),
            w.plot_note("魔獣の存在に怯える招待客たち"),
            w.plot_note("それぞれ部屋に閉じこもったり、外の古くて捨てられた民家に避難したりする"),
            )


def island_history(w: World):
    return w.scene("孤島と古城の歴史",
            w.plot_note("地元の研究者から、$cherryを含めたここの城主の歴史を聞く"),
            w.plot_note("ずっと城主には悲しい運命がつきまとってきた"),
            w.plot_note("地元の人間を奴隷のようにこきつかい、自分が好んだ娘を勝手に奪っては嫁にした"),
            w.plot_note("ある時その娘が決死の脱走を行う"),
            w.plot_note("城主は飼い犬をけしかけ、その匂いを追わせた"),
            w.plot_note("だが発見されたのは城主の遺体で、それは彼の飼い犬たちによって食い殺されていた"),
            w.plot_note("彼女が可愛がっていた飼い犬とともにその新しい城主となった"),
            w.plot_note("だが女が城主になっても圧政は変わらず、その女城主も苦しんだ奴隷によって殺されてしまった"),
            w.plot_note("その話が魔獣を生んだと"),
            w.plot_note("ただ現場で見つけた毛は確かに普通の犬のものではなかった、と$sherlockは言う"),
            w.plot_note("その夜、どこかで犬の吠える声が響いた"),
            )


def find_basement_room(w: World):
    return w.scene("地下への入り口",
            w.plot_note("$sherlockは壁に血の跡を見つけ、そこから地下への入り口を発見する"),
            )


def truth_of_the_case(w: World):
    return w.scene("事件の真相",
            w.plot_note("$sherlockは事件の真実を全て語った"),
            w.plot_note("事件の発端となったのは$cherryの愛犬が彼女の夫によって殺されたことだった"),
            w.plot_note("その恨みを晴らすために夫は事故死させられた"),
            w.plot_note("それに関わった人間が後で殺されている"),
            w.plot_note("彼女は魔獣を手に入れ、それにより殺害を行おうとしたが、魔獣は人殺しをしなかった"),
            w.plot_note("愛犬の代用となった魔獣は人の血が必要で、そのために彼女は自分の手で殺人を侵さざるを得なかった"),
            w.plot_note("彼女に協力していたのが地元の観光協会の男だった"),
            w.plot_note("その男が彼女を愛してしまい、今回の悲劇が訪れた"),
            w.plot_note("やっと到着した地元警察により$cherryが島の一番北側で魔獣に食い殺されている姿で発見された"),
            w.plot_note("魔獣は警察により射殺された"),
            )
