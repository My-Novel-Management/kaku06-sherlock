# -*- coding: utf-8 -*-
'''
Episode 2-3: "家族の事情"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


# DEFINE
TITLE = "家族の事情"


# NOTE: outlines
ABSTRACT = """
$sherlockは独自に酒場や街を歩いて情報を集める。
その間に$wilsonは一旦$Londonに戻り、$sherlockに頼まれた仕事をこなしていた。
ある老人を訪ねる。$edoという名の老人は、$sherlockから頼まれてあるものを開発していた。
それは指紋検出器だった。指紋とは指の模様だという。
$sherlockはパブである男性から$jeanが同じ学校だという話を聞く。彼女は後妻で玉の輿に乗れたと喜んでいたと。貧しい家の出で、$royd氏はそういった子供たちに支援もしていた。
そういう人物を拾った娘が殺したのは酷い話だと。どうも街では娘が拾い子だという話は誰もが知っている噂だった。
また$royd氏には莫大な遺産があり、本来ならそれは全てあの娘が相続するはずだったとも。
$sherlockは$jeanが育ったという学校にやってくる。そこで若い頃の$jeanの絵を見つける。卒業生による肖像画だというが、そこに$kailのサインを見つけた。
一晩泊まり、翌日、$sherlockは単身$royd邸を訪ねる。しかし$jeanが体調不良で面会できないと言われた。
警察に行くとちょうど$wilsonが戻ったところで、指紋検出を行う。だがそれは$maryの指紋とは異なっていた。
"""


# Episode
def main(w: World):
    return w.episode(TITLE,
            # NOTE
            w.plot_setup("$sherlockは$wilsonにお使いを頼み、その間に街で$royd氏に関する情報を集める"),
            w.plot_turnpoint("パブで$jeanがかつて通っていた学校の生徒から、彼女が玉の輿に乗れたと喜んでいた話を聞く"),
            w.plot_develop("$sherlockは$jeanの育った学校に行き、彼女の小さい頃の話などを聞く。またそこで$kailに関する話も入手する"),
            w.plot_turnpoint("学校に飾られた$jeanの絵に$kailのサインを発見する"),
            w.plot_resolve("戻ってきた$wilsonから$edoの結果を聞く$sherlock"),
            w.plot_turnpoint("指紋検出と照合の結果、$gunから$maryのものではない指紋が検出されたと$wilsonから聞いた"),
            w.plot_note("警察を後にした$sherlockと$wilson、付添の新聞記者$milkは一度街で聞き込みをする"),
            w.plot_note("それぞれ手分けして$milkはツテの記者や$royd氏関連の会社を、$wilsonは駅前から繁華街を、$sherlockは飲み屋街を担当した"),
            w.plot_note("まだ早い時間だったが開いているパブもあった"),
            w.plot_note("$sherlockはそこで元教師の$mackingerと出会う"),
            w.plot_note("教師は第一発見者として出ていた"),
            w.plot_note("その教師はバラ園が楽しみでよく帰りに寄り道をしていたと語る"),
            w.plot_note("もともと学校も$royd氏が整備してよくなった"),
            w.plot_note("今は後妻$jeanだが、彼女もその学校卒業で、学校の学費は貧しい家の子たちは援助が出ていた"),
            w.plot_note("$sherlockは$jeanについてどんな人物なのか聞くが、老人はあまり知らないと。噂では金遣いが荒くて、そこは若い後妻だから仕方ないと愚痴っていたと"),
            w.plot_note("$sherlockは学校に行ってみることにする"),
            #
            w.plot_note("学校は丘に建てられていた"),
            w.plot_note("学校にやってきた$sherlockは、そこに$royd氏の記念碑が建てられているのを見る"),
            w.plot_note("応対してくれたのは理事長で、弁護士をやっている$coneryだった"),
            w.plot_note("$coneryは$royd氏の後輩らしい"),
            w.plot_note("$royd氏は地元が発展して、貧しい子が一人でも減るようにと常に考えていたという"),
            w.plot_note("自分で孤児院も作っている"),
            w.plot_note("ただ昔はそうではなく野心家だったと。子供が生まれてから変わったんだと言った"),
            w.plot_note("$jeanもここの生徒と聞いたが、その件は古株の教師に教わることに"),
            #
            w.plot_note("老教師$natalyが待っている"),
            w.plot_note("授業の合間に出てきた"),
            w.plot_note("中庭で遊ぶ子供たちを見ながら話す"),
            w.plot_note("$jeanのことはよく覚えているという"),
            w.plot_note("可愛らしい子だったが家が貧しく、着るものも満足になくていつも繕ったツギハギだった"),
            w.plot_note("それをからかわれてよく泣いていた。絶対将来金持ちになると言っていた"),
            w.plot_note("彼女が学校を出てから$royd氏と結婚したと聞いて驚いた"),
            w.plot_note("教室に飾られてた古い肖像画の一つに、$jeanがあった"),
            w.plot_note("そこのサインに$kailとある"),
            w.plot_note("「ああ、これはこの学校の生徒が描いたものですよ。絵が好きだったけど結局諦めたんじゃないかしら」"),
            #
            w.plot_note("その後、ホテルに戻る$sherlock"),
            w.plot_note("$wilsonにはあることを頼んでおいた。早ければ二、三日のうちに結果が分かるだろうと"),
            w.plot_note("一人で寝ながら考えを整理する"),
            #
            w.plot_note("一方$wilsonは一人で$London市内に戻っていた"),
            w.plot_note("ある頼まれ事をしたのだ"),
            w.plot_note("その研究所を訪れ、ドアをノックする"),
            w.plot_note("現れたのは白衣姿の老人$edoだった"),
            w.plot_note("$wilsonの手には袋に包まれた$gunがあった"),
            outline=ABSTRACT)

