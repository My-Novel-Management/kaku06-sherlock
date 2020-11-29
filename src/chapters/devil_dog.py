# -*- coding: utf-8 -*-
'''
Chapter "魔獣"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from config import TITLES
from scenes import InShip
from scenes import InTrain
from scenes import Port
from scenes import SherlockHouse
from scenes import Station


# Episodes
def legend_of_darkdog(w: World):
    return w.episode("魔獣伝説",
            SherlockHouse.mysterious_case(w),
            SherlockHouse.legend_of_dark_dog(w),
            SherlockHouse.invitation_from_dark_island(w),
            )


def first_murder(w: World):
    return w.episode("最初の犠牲者",
            Station.goto_dark_island(w),
            InTrain.talk_about_dark_island(w),
            Port.goto_dark_island(w),
            InShip.goto_dark_island(w),
            "孤島",
            w.plot_note("観光協会の男に案内され、怪奇事件の謎を解くイベントに連れて行かれる"),
            "孤島の通り",
            "事件のあった雑木林",
            w.plot_note("男からこの島にはかつて五十名ほどの住人がいたが、魔獣の伝説のせいでみんな逃げ出してしまい、今では城主だけが残っていると"),
            "古城",
            w.plot_note("丘の上の古城にたどり着く"),
            w.plot_note("城の案内をただ一人でここに住んでいるという女城主$cherryが行う"),
            "大広間",
            w.plot_note("パーティのために料理人やお手伝いを呼んでいて、彼らが忙しくなく準備をしていた"),
            w.plot_note("$sherlock以外に招かれたのは怪奇事件の専門家や、動物学者、医師、心霊現象の研究家などだった"),
            w.plot_note("地域の研究者は$bossが生きていた頃から魔獣が存在していて、今もその生き残りがこの島で生き延びているのだと説明する"),
            w.plot_note("$maryは美味しい料理に喜ぶ"),
            "個室",
            w.plot_note("食事がお開きになり、$sherlockたちは与えられた部屋に戻る"),
            w.plot_note("寝ようとしていたときに、悲鳴が聞こえた"),
            "大広間",
            w.plot_note("慌てて駆けつけると、心霊専門家が殺されていた"),
            )


def second_murder(w: World):
    return w.episode("第二の犠牲者",
            "談話室",
            w.plot_note("$mockが警察を呼ぼうとしたが海が荒れて船が出せない"),
            w.plot_note("地方で最新技術の$telephoneもなく、海が収まるまで連絡できないと言われる"),
            w.plot_note("孤島に閉じ込められた$sherlockたち"),
            w.plot_note("魔獣の存在に怯える招待客たち"),
            w.plot_note("それぞれ部屋に閉じこもったり、外の古くて捨てられた民家に避難したりする"),
            "城の中",
            w.plot_note("$sherlockは$cherryに申し出て、城内を調べさせてもらう"),
            w.plot_note("一通り案内してもらい、部屋を見て回ったが特に何も見つからない"),
            "台所",
            "大広間",
            "裏庭",
            w.plot_note("$sherlockは最初の事件があった場所に、$mockに案内してもらった"),
            "雑木林",
            w.plot_note("そこは城から離れた雑木林"),
            w.plot_note("看板が建てられ、そこが最初の殺害現場だと示されている"),
            w.plot_note("観光資源にしようとしている$mockたち"),
            "個室",
            w.plot_note("翌朝、$mockの姿が城から消えていた"),
            )


def exist_darkdog(w: World):
    return w.episode("魔獣は存在する",
            "城内",
            w.plot_note("いなくなた$mockが怪しいと招待客たちは探し始める"),
            "雑木林",
            w.plot_note("しかし$mockは最初の殺害現場で同じように猟奇的に殺害されていた"),
            w.plot_note("$sherlockはそこで$mockの遺体に付着しているあるものを拾う"),
            "談話室",
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


def basement_room(w: World):
    return w.episode("地下室",
            "島側の港",
            w.plot_note("天候が回復し、船舶操作に慣れた男が警察を呼んでくると何人か連れて島を離れる"),
            w.plot_note("その間に$sherlockは$cherryにもう一度城を探させてほしいとお願いする"),
            "城",
            w.plot_note("彼女はあまり気が進まないようだが許可を出す"),
            "城内",
            "談話室",
            w.plot_note("$sherlockは壁に血の跡を見つけ、そこから地下への入り口を発見する"),
            "地下への階段",
            "拷問部屋",
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


def real_murder(w: World):
    return w.episode("犯人",
            "城内・拷問部屋",
            w.plot_note("$sherlockは全ての犯行が彼女によるものだと断言する"),
            w.plot_note("全ての犯行が獣にやられるように見せかけられていたが、この拷問室にある道具には獣の歯型をした拷問具があった"),
            w.plot_note("それに新しい血がついているので、これが使われたと"),
            w.plot_note("この場所を知っていた人間は$cherry以外に誰かいるのか尋ねると、$mockもだと語った"),
            w.plot_note("彼女は全ての計画は彼がねって実行したものだと言う"),
            w.plot_note("しかし$sherlockは彼がここに赴任して三年目だということを知っていた"),
            w.plot_note("犯人だと論破された$cherryは部屋を真っ暗にして逃げ出す"),
            )


def sad_end(w: World):
    return w.episode("悲しい結末",
            "城・地下室",
            w.plot_note("$sherlockは彼女を助けないと危ないという"),
            w.plot_note("しかし彼女が出ていった出口は閉ざされ、別の出入り口を探すしかなくなった"),
            w.plot_note("そうこうしているうちに島に到着した警察が、助けに入ってくる"),
            w.plot_note("やってきた$restradeに事情を説明し、$cherryを捜索してもらう"),
            "談話室",
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


def rebirth_ritual(w: World):
    return w.episode("蘇りの技法",
            "地下・儀式の部屋",
            w.plot_note("女主人$cherryの死去により事件は全てに幕を下ろした"),
            w.plot_note("死後に見つかった手記により今までの大半の事件の陰に彼女の存在があったことが判明する"),
            w.plot_note("$sherlockは死後に秘密の地下室を発見し、そこで儀式の跡を見た"),
            "図書館",
            w.plot_note("図書館にやってきて、古文書を調べる"),
            w.plot_note("太古の技法で失われた魂を呼び戻す、闇の技法だった"),
            w.plot_note("本当に蘇らせたのだとわかる"),
            "教会",
            w.plot_note("$sherlockは彼女に接触しその技法を教えた$cultXのことをマークした"),
            w.plot_note("そこに情報がもたらされる"),
            "裏通り",
            "バー",
            w.plot_note("彼女が最後の$stoneの所有者だったという。しかし技法のために売り払い、今手元にはなかった"),
            w.plot_note("$sherlockは何者かが$stoneを四つ手に入れたのだと理解した"),
            )


# Chapter
def main(w: World):
    return w.chapter(TITLES[5],
            w.plot_setup("魔獣伝説のある場所で猟奇殺人事件が起こる"),
            w.plot_turnpoint("$sherlockの許にその孤島のパーティの招待状が届く"),
            w.plot_develop("$restradeの弟から事件解明を頼まれる"),
            w.plot_turnpoint("最初の殺人事件が起こる"),
            w.plot_develop("海は荒れて脱出も不可能になり、招待客は島に閉じ込められる"),
            w.plot_turnpoint("第二の被害者が出る"),
            w.plot_develop("$sherlockは獣による犯行ではないとして調査を開始する"),
            w.plot_turnpoint("本物の魔獣が出現する"),
            w.plot_develop("魔獣を殺そうとするが女主人が体を張って守ろうとする"),
            w.plot_turnpoint("$sherlockは女主人が犯人だと説明する"),
            w.plot_develop("女主人は魔獣とともに脱出を試みる"),
            w.plot_turnpoint("魔獣は女主人を食べてしまった"),
            w.plot_resolve("蘇りの秘法を使って$boss復活を願う宗教団体だったと判明する"),
            legend_of_darkdog(w),
            first_murder(w),
            second_murder(w),
            exist_darkdog(w),
            basement_room(w),
            real_murder(w),
            sad_end(w),
            rebirth_ritual(w),
            )


