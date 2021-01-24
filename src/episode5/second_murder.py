# -*- coding: utf-8 -*-
'''
Episode 5-3
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


# DEFINE
TITLE = "第二の殺人"


# NOTE: outlines
ABSTRACT = """
$hugarは$mochを怪しみ、探そうとする。だが$sherlockはまず全員の安全を確保すべきと意見が割れ、$hugarから反感を持たれる。
$hugarに従おうとする$jamosや$doldたちと、反発する$sherlock。心霊学者の$karlは全てが魔獣の仕業だと騒いでいた。
$hugarは城の外を捜索すると出ていく。中に残った$sherlockは$cherryに城内調査の許可を貰おうとしたが、彼女は体調を崩したようで、すぐに自室に引っ込んでしまった。
城内を調べていると、かなり古い道具がいくつも見つかった。また改修されているのも分かった。
$hugarたちが戻ってきて$mochの死体を雑木林で発見したと言う。更に$karlの姿が消えていた。
手分けして探すが見つからない。
心配していた$cherryの寝室に入ったが、彼女の姿も消えていた。
"""


# Episode
def main(w: World):
    return w.episode(TITLE,
            # NOTE
            w.plot_setup("元刑事の$hugarは$mochを容疑者とみて捜索させる"),
            w.plot_turnpoint("心霊学者$karlも姿を消す"),
            w.plot_develop("多くの失踪者が出て$hugarは混乱し、現場は統制が取れなくなっていた。$maryは新聞記者$milkとともに改めて情報を整理する"),
            w.plot_turnpoint("失踪した$mochが雑木林で遺体で発見される"),
            w.plot_resolve("連続殺人事件となり、容疑が一旦晴れた$jamosが出され、みんなで固まっている方が安全だという提案がなされるが、$hugarは汚名挽回とばかりに一人で出ていってしまう"),
            w.plot_turnpoint("$sherlockから島に向かっていると連絡が入った"),
            w.plot_note("$mochが失踪したことで$hugarは$mochを容疑者として見ていた"),
            w.plot_note("一旦各々の部屋に戻り、嵐が静まるのを待って、再び$mochの捜索と島からの脱出手段を探すことになる"),
            w.plot_note("$hugarが全員の出入りを見張れるように、個室からの行き来を談話室前を通る通路に制限する"),
            w.plot_note("談話室にあった$reuiの遺体はキッチンの裏手の地下の物置に移動した（地下の方が温度が低いため）"),
            w.plot_note("$maryたちは改めて$wilsonと事件について相談する"),
            w.plot_note("$wilsonは$sherlockから渡されたと、奇妙な機械を見せる"),
            w.plot_note("$limeがそれは遠方と通信する装置だと言う。王宮で見たことがあるらしい。ただしどう使うのかは不明。古代の技術だと言っていた"),
            w.plot_note("それが光り、何かの合図をする"),
            w.plot_note("どうやら$sherlockからの通信らしい"),
            w.plot_note("そこに来客がある。$jamosだった"),
            w.plot_note("$jamosは$wilson（$sherlock）のことを頼って相談があると言った"),
            w.plot_note("実は$mochは以前から「何か新聞で取り上げられるような事件があればもっと人が来るのに」と言っていたと"),
            w.plot_note("$hugarが言うように本当に$mochがそれを企んで人を集めたなら、自分たちも殺されるんじゃないかと。ここでこのままいていいのか"),
            w.plot_note("$wilsonは自分が$sherlockじゃないことを告白する"),
            w.plot_note("その上で$jamosに$sherlockが助けてくれると言った"),
            w.plot_note("$jamosは通信機を見て、その光り方から合図が分かるという"),
            w.plot_note("$jamosを連絡役にして、$sherlockに現状を伝えてもらった"),
            w.plot_note("向こうで警察と船を手配してくれるということになったらしい"),
            w.plot_note("その話を$hugarたちにもしてきた方がいいか、という提案に対して$wilsonは少し黙っておこうと言う"),
            #
            w.plot_note("夕食後$milkに呼び出され、$maryは彼女の部屋を訪れていた"),
            w.plot_note("$milkは何故$sherlockが来ていないかとずっと聞きたかったらしい"),
            w.plot_note("用事があったこととオカルトに興味がないと言っていたことを教える"),
            w.plot_note("$sherlockを紹介したのは$milkで、今回は一緒に泊まれると意気込んでいたのに残念だと"),
            w.plot_note("$milkは$sherlockに彼女や婚約者がいないか質問する"),
            w.plot_note("$maryは$sherlockをそういう対象に見る人がいるとは考えてなかったので、驚く"),
            w.plot_note("$maryは$wilsonたちから聞いた$sherlockと連絡がついて、明日にも来てくれると教えた"),
            #
            w.plot_note("夜中、部屋のドアがノックされる"),
            w.plot_note("現れたのは$cherryだった"),
            w.plot_note("$maryは彼女に呼ばれて出ていく"),
            w.plot_note("談話室にいたはずの$hugarの姿が消えている"),
            w.plot_note("$maryは$cherryから、久しぶりに人が多くて楽しいのにこんなことになってしまって、と謝られる"),
            w.plot_note("$cherryの寝室に招かれ、そこで食べ物と飲み物をもらう（それには薬が仕込まれていた）"),
            w.plot_note("実は今回のイベントを企画したのは$mochで、彼が$cherryの幼馴染だったことを告白する"),
            w.plot_note("昔からこの島に人を呼び戻したいと語っていた"),
            w.plot_note("$cherryは城の跡継ぎとしてここに残ることが決まっていた"),
            w.plot_note("$hugarから$mochが今回の殺人をしたんじゃないかと疑われていると聞いて悲しんでいると"),
            w.plot_note("一番話しやすそうだったのが$maryだった"),
            w.plot_note("$cherryは一部に$ajinの血が入っていると言う"),
            w.plot_note("$cherryは$maryもそうだろう、と言う"),
            w.plot_note("$maryにもっと一緒にいて欲しいと迫る"),
            w.plot_note("$maryは頭がぼんやりとしてきて、意識が遠のく"),
            #
            w.plot_note("翌朝になり$maryが戻ってこないことを心配して$limeが$cherryの部屋を訪れる"),
            w.plot_note("だが物音がしない"),
            w.plot_note("部屋には鍵がかかっていた"),
            w.plot_note("$limeは$wilsonに相談しに戻るが、その途中で血が床にこぼれているのを目撃する"),
            w.plot_note("談話室では$hugarが死んでいた"),
            #
            w.plot_note("$wilsonと$jamosが談話室にやってくる。$limeが呼んだ"),
            w.plot_note("更に$doldがやってくる。彼はキッチンが荒らされていることと、遺体が消えていることを訴える"),
            w.plot_note("$wilsonの指示で、現在いる人をホールに集めることに"),
            w.plot_note("$limeは$milkを呼び出す"),
            w.plot_note("まだ寝ぼけていた$milkは何事かと寝間着のままで飛び出す"),
            w.plot_note("事情を説明し、$bettyも呼んでもらうことに"),
            w.plot_note("だが$bettyは部屋に不在。鍵は開いていた"),
            w.plot_note("$jamosは$karlもいなくなったと言っている"),
            w.plot_note(""),# TODO
            outline=ABSTRACT)

