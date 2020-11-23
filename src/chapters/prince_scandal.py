# -*- coding: utf-8 -*-
'''
Chapter "皇太子の醜聞"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from config import TITLES


# Episodes
def visit_sherlock(w: World):
    return w.episode("訪問者",
            w.plot_note("$wilsonは$carで$sherlockの家の前までやってくる"),
            w.plot_note("$wilsonは近くにいた子供（$ignes）に家を尋ねて教えてもらう"),
            w.plot_note("そこで子供たちがもめ始めて、困惑"),
            w.plot_note("なんとか場が収まり、$sherlockの家を訪問する"),
            w.plot_note("$sherlockは何も言っていないのに$wilsonの素性を言い当てる"),
            w.plot_note("その上で王室からの依頼は受けないと言って断る"),
            w.plot_note("最後に「さっきの子供に財布をすられてるよ」と"),
            w.plot_note("$wilsonは振り返ったがもう子供たちの姿は消えていた"),
            w.plot_note("知っていたならなぜ忠告してくれなかったんだ、と$wilsonが$sherlockに文句をいい、なんとか家に入れてもらえる"),
            w.plot_note("中に入るとそこら中に本や資料がちらばっていた"),
            w.plot_note("$wilsonはそこで依頼をしようと思ったが、"),
            w.plot_note("そこに何も記載のない手紙が投げ込まれた"),
            )


def prince_letter(w: World):
    return w.episode("皇太子からの密書",
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


def that_lady(w: World):
    return w.episode("その女",
            w.plot_note("$carに乗せてもらい$wilsonの運転でその女の家に向かう"),
            w.plot_note("手紙に同封されていた地図と情報を見る$sherlock"),
            w.plot_note("女の家は高級住宅街にあった"),
            w.plot_note("女の家を訪れる前に周囲に聞いて回る"),
            w.plot_note("周囲の評判はいい人で人当たりもよく、色々分けてもらっている話しか出なかった"),
            w.plot_note("$sherlockは$wilsonに「何か妙だ」といってから、$ailyの家に向かう"),
            w.plot_note("しかし誰も出てこない"),
            w.plot_note("鍵が空いているのを妙に思い、中に入る"),
            w.plot_note("家の中はがらんとしていて、まるで新居のよう"),
            w.plot_note("一つだけ木箱が置かれていただけで、そこには人が倒れていた"),
            w.plot_note("女の家で謎の女性の遺体が発見された"),
            )


def murder_case(w: World):
    return w.episode("殺人事件",
            w.plot_note("$sherlockは警察に連絡を取る"),
            w.plot_note("現れたのは$restradeで、$sherlockとは旧知の仲のようだった"),
            w.plot_note("$sherlockは$restradeと少し話す"),
            w.plot_note("$sherlockは現場を見て、殺害されていたのは$ailyではないと言う"),
            w.plot_note("そもそも家の中にものがなさすぎて、生活していた証拠がない"),
            w.plot_note("遺体の身元は行方不明になっている人間の誰かだろうと"),
            w.plot_note("自分がここにきたのはある人物に彼女にあずけているものを取り戻してほしいと頼まれたからだ、とだけ"),
            w.plot_note("$sherlockは$wilsonと一緒に外に出て、ある場所に行くように指示する"),
            w.plot_note("行き先はある孤児院だった"),
            )


def she_is_not_exist(w: World):
    return w.episode("彼女は存在しない",
            w.plot_note("$ailyという女性については謎が多い"),
            w.plot_note("市場によって$ignesたちに情報を集めるように指示する"),
            w.plot_note("$wilsonの財布を返してもらったが、中身は減っていた"),
            w.plot_note("孤児院に到着し、そこに入る"),
            w.plot_note("なぜここにきたのか尋ねると、$ailyという女性が寄付をしていた場所だったと"),
            w.plot_note("寄付をするとそこの孤児たちが作った栞がもらえるが、それが落ちていたのだ"),
            w.plot_note("尋ねたが、$ailyという女性に心当たりはないらしい"),
            w.plot_note("応対してくれた教師（実は$aily）は、ここは養子としてもらわれていく子もいるが、大半は自立して働いて暮らしていると"),
            w.plot_note("その場所に支援してくれているその女性も素晴らしい人だろうと、彼女は言った"),
            w.plot_note("$sherlockはそこで子供たちが自分のことをいつもくる女性の知人と思って話しかける"),
            w.plot_note("子供が彼女からあるものを預かっていることを知った"),
            w.plot_note("それは宝剣だった"),
            # TODO
            )


def jack_the_identity(w: World):
    return w.episode("$jackの正体",
            w.plot_note("$jackは名前も戸籍も存在しない、悲しい捨て子だった"),
            )


def prince_wedding(w: World):
    return w.episode("皇太子の結婚式",
            w.plot_note("偽物の$stoneを使い、無事に皇太子の結婚式は行われた"),
            )



# Chapter
def main(w: World):
    return w.chapter(TITLES[1],
            w.plot_setup("$wilsonはある依頼をするために$sherlockを訪れる"),
            w.plot_turnpoint("皇太子からの書簡により$sherlockはそちらの依頼を受けることになる"),
            w.plot_develop("$sherlockは皇太子が贈った宝剣を取り戻すために$ailyの家を訪れる"),
            w.plot_turnpoint("$ailyの家で女の遺体が発見される"),
            w.plot_develop("$ailyの友人という女性に出会い、彼女の話を聞く"),
            w.plot_turnpoint("遺体は$ailyと認められた"),
            w.plot_develop("$sherlockは彼女が実在した証拠をつかみ、調べていく"),
            w.plot_turnpoint("$ailyは存在しない女だった"),
            w.plot_develop("$jackを追い詰めて$sherlockは何とか宝剣を取り戻す"),
            w.plot_turnpoint("しかし取り戻した宝剣には肝心の$stoneが付いていなかった"),
            w.plot_resolve("皇太子は偽物の$stoneをつけた宝剣を使い、婚姻の儀を終わらせた"),
            visit_sherlock(w),
            prince_letter(w),
            that_lady(w),
            she_is_not_exist(w),
            jack_the_identity(w),
            prince_wedding(w),
            )


