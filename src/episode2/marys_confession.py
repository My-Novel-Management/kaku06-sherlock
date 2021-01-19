# -*- coding: utf-8 -*-
'''
Episode 2-4: "$maryの告白"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


# DEFINE
TITLE = "$maryの告白"


# NOTE: outlines
ABSTRACT = """
検出結果を受けて$sherlockは再度$royd邸を訪問する。
$jeanは体調悪いからと使用人$kailに断られたが$maryを連れてきて、彼女と直接話があるというと奥から$jeanが出てきて応じてくれた。
$maryはあの場所で父親になんと言われたかを語った。
それは決して遺産相続の話ではなく、自分の出自にかかわることだった。
拾われた子供だ、というのは既に街の人間の噂から察していたが、それだけでなく$animalだと告白された。それも、自分と別の$animalの子供だ、と。実の娘だった。
それは$royd氏がずっと隠していた事実であり、だからこそ$royd氏は遺書で全財産を娘にやると書いていたのだ。
それにショックを受けて家に戻った$mary。一晩中自分の気持を処理できずに寝られなかった。
その告白に対して$jeanはずっとそうじゃないかと疑っていたと。だから余計に愛せなかったと。
そして前日の夜、$roydから直接、話す決意をしたと聞かされた。それは$maryの十六歳の誕生日を迎えるからだった。
$jeanは遺産を$maryにあげたくなくて、$roydを殺して$maryを犯罪者にしたと告白したが、
その時$kailがナイフを振りかざして人質に取った
"""


# Episode
def main(w: World):
    return w.episode(TITLE,
            #   NOTE
            w.plot_setup("$sherlockは再度$jeanと$kailに話を聞きに邸宅を訪れる"),
            w.plot_turnpoint("$kailから$jeanが体調を崩していて会えないと断られる"),
            w.plot_develop("$jeanは$maryが拾われ子であり$animalだということを知っていたのを隠していたことを告白する"),
            w.plot_turnpoint("そこに警察が$maryを連れてくる"),
            w.plot_resolve("$kailと$jeanは$maryが父親を憎んでいてそれで殺したと罪をなすりつけようとするが、$sherlockにより証言の齟齬が突かれてボロが出る"),
            w.plot_turnpoint("$maryは$kailたちが父親を殺したことに激怒し、$transformした"),
            w.plot_note("翌日$sherlockは$royd邸を訪れた"),
            w.plot_note("$jeanへの面会を求めたがやはり使用人$kailにより体調が悪いからと断られる"),
            #
            w.plot_note("$sherlockは$keanにバラ園を見せてもらう"),
            w.plot_note("遺体発見現場となった小屋は氏のプライベートルームになっていたようで、頼まれた時以外は$keanも入らないようにしていると"),
            w.plot_note("鍵を開けてもらい、中に入る"),
            w.plot_note("$royd氏はかなり貧乏性らしく、部屋は乱雑に物が置かれていた。ゴミに見えるものまである"),
            w.plot_note("$keanから$royd氏について聞く"),
            w.plot_note("$royd氏は外では成り上がりの気前のいいおじさんだったが、家ではかなり神経質で細かい取り決めがあった"),
            w.plot_note("また外食では良いものを食べるようにしていたが、家では古いパンをミルクに浸して食べるようなものが好きだった"),
            w.plot_note("そのことに対して後妻の$jeanはかなり嫌っていた"),
            w.plot_note("夫婦仲は悪いとも良いとも言えなかった"),
            w.plot_note("結婚して十五年ならそんなものだろうと"),
            w.plot_note("また各方面に支援や寄付をするのを$jeanは好まなかった"),
            w.plot_note("$maryについては学校には行かせたがらなかった"),
            w.plot_note("事情は分からないが、$royd氏の意向だと聞いている"),
            #
            w.plot_note("$sherlockは警察に立ち寄る"),
            w.plot_note("$wilsonが$edoを連れてきていた"),
            w.plot_note("$edoは奇妙な機械と薬品を用いて$gunから何か採取する"),
            w.plot_note("また$maryからも採取している"),
            w.plot_note("フィンガープリント、と呼んでいた。指紋といったところだろうか"),
            w.plot_note("人間誰でも固有の指の文様を持っている。それを採取しておいて形の照合を行うことで同一人物かどうか判断できると"),
            w.plot_note("まだ研究段階の技術で、本当にそうかどうか怪しいが、少なくとも$maryのそれと$gunについていたそれは異なると"),
            w.plot_note("$sherlockはその情報を得て、再び屋敷に向かう"),
            #
            w.plot_note("屋敷を訪れた$sherlockを面倒そうに追い返そうとする$kail"),
            w.plot_note("しかし$sherlockが$maryのことについて$jeanに話があるというと、彼女が奥から出てきて応じてくれた"),
            w.plot_note("寝間着姿の$jeanは確かにやつれているが、美人だったと思わせる細身の女性"),
            w.plot_note("何度も「すみません」と謝る"),
            w.plot_note("$sherlockは$maryが$animalだったのを、あなたは知っていましたね？　と"),
            w.plot_note("$jeanは頷く"),
            w.plot_note("$royd氏が呼び出したのはそれについての告白が一つだったこと"),
            w.plot_note("それからもう一点。これは$sherlockの推測だけれども、おそらくは遺産相続に関わることだったと"),
            w.plot_note("遺産相続については通常何もなければ未亡人となった$jeanに相続されることになっている"),
            w.plot_note("だが$royd氏と親交があり、学校の理事長を勤める弁護士$conery氏は遺産についての書類を管理していた"),
            w.plot_note("その内容は事件が終わるまで一旦保留になっている"),
            w.plot_note("それが$maryに全財産を残すというものなら$jeanは非常に困ることになるだろうと"),
            w.plot_note("$sherlockは「既に内容はそうだと伺ってます」とブラフをはる"),
            w.plot_note("「やっぱり」という言葉が$jeanからもれた"),
            w.plot_note("事件前夜に$jeanに話したそうだ、$royd氏は自分の体のこともあり、遺産について悩んでいた。娘の$maryに大半を残そうと思うと"),
            w.plot_note("「だからどうしてあの子が、って思うんですよ」と$jean"),
            w.plot_note("「あなたがご主人を手に掛ける方が自然ですよね？」と$sherlock"),
            w.plot_note("$kailが割って入り「病人に対してなんて口をきくんだ！」と"),
            w.plot_note("$sherlockは「あなたは同じ学校を出ていますね。学校で彼女の肖像画を描いたのはあなただった」と"),
            w.plot_note("$sherlockは$gunを$maryが触っていない証拠を説明し、事件の推理を話す"),
            w.plot_note("遺産相続の話を聞いた$jeanは$royd氏を殺害する計画を考える"),
            w.plot_note("$royd氏が$maryに話があると夜にバラ園に呼び出すのを知り、$maryが出たあとでこっそりあとをつける"),
            w.plot_note("バラ園への道は人通りが少なく、明かりもないために、暗がりの中を歩き慣れた人でないと難しい"),
            w.plot_note("$maryが帰った後で、用意していた$gunで$royd氏を殺害する"),
            w.plot_note("家に戻り、翌日$maryを起こすときに部屋に$gunを戻しておけばいい"),
            w.plot_note("最初に見つけたのが$kailだというから、$kailに手伝わせたのかも知れない"),
            w.plot_note("これで遺書さえなければ遺産は見事夫人のものとなる"),
            w.plot_note("$royd氏が体を壊したのは結婚後だというから、何か食事に混ぜていた可能性があるとも"),
            w.plot_note("「すべてあなたの推測でしょう？不快です」と"),
            w.plot_note("だがそこに、$patsonが$maryを連れてやってきた"),
            outline=ABSTRACT)

