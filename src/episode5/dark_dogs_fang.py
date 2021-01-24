# -*- coding: utf-8 -*-
'''
Episode 5-4
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


# DEFINE
TITLE = "魔獣の牙"

# NOTE: outlines
ABSTRACT = """
$sherlockは$jamosに通信機が使えるようにならないか試してもらう。
$hugarは消えた$carlをずっと怪しんでいて単独で捜査してどこかに行ってしまう。
$maryはずっと姿を見ていない$cherryが気になっていたが、部屋には鍵がかかったままだった。
$sherlockは再度、城内を調査する。人の手によるものだとし、最初の談話室の事件が可能だった人物を挙げていく。
そこに$hugarがお手伝いの$bettyも殺されているのを見つけたとやってくる。$hugarと$sherlockは互いを疑い合う。
その時、$limeが談話室で抜け道を見つけた。
地下通路を進むと、その先には拷問器具が置かれた部屋があり、$karlの死体が転がっていた。
更にそこには大きな黒い犬が待ち構えていた。
"""


# Episode
def main(w: World):
    return w.episode(TITLE,
            # NOTE
            w.plot_setup("$maryたちは$sherlockの指示で調べておいてほしいと言われたところを調査する"),
            w.plot_turnpoint("$cherryの寝室に入るが、彼女の姿も消えていた"),
            w.plot_develop("$limeが抜け道に気づいて寝室から談話室に抜けられることを発見する。それが$hugarに見つかり、$limeたちが犯人にされてしまう"),
            w.plot_turnpoint("$sherlockがやってきて$maryたちと合流する"),
            w.plot_resolve("$sherlockは$maryたちから情報を聞き、談話室を調べ始める。そこで地下への階段を見つけた"),
            w.plot_turnpoint("地下に拷問部屋があり、そこで黒い巨大な犬が待ち構えていた"),
            w.plot_note("$jamosは語られなかったもう一つの伝説について話し始める"),
            w.plot_note("$bossが倒され、世界に光が取り戻されてからも、この島は魔族の支配下にあった、という話はした"),
            w.plot_note("その後、$ajinの娘により圧政から解き放たれた、ということまでは話した"),
            w.plot_note("でもその後もときおり村では猟奇的な殺人が起こっていた"),
            w.plot_note("だがそれは表向きの話だ"),
            w.plot_note("ここからは伝聞による資料しかないから、はっきりとしたことではない"),
            w.plot_note("この島はもともと環境がよくなく、作物の出来も悪い"),
            w.plot_note("そんな状況を打破するために、人身御供の儀式がよく行われていたというのだ"),
            w.plot_note("村から魔獣様への供物が選ばれ、その娘が食われていた"),
            w.plot_note("それを魔獣伝説という名の下で、村の男たちが殺していたというのだ"),
            w.plot_note("誰もが口を抑える"),
            w.plot_note("つい先日亡くなった元住民が語ってくれたという"),
            w.plot_note("「それがどうしたんだ」と$doldが怒鳴りつける"),
            w.plot_note("$jamosはその頃やっていたのは人間ではなくて魔族か魔獣で、まだ生き残りがいて、それが自分たちを食い殺しているんだと"),
            w.plot_note("$wilsonはそういうオカルトではなく実際に人が死んでいることを考えようと"),
            w.plot_note("$jamosはびくびくしてしまい、個室に逃げ込む"),
            w.plot_note("$maryは$sherlockから連絡が来ているだろうと思って部屋に戻り、通信機を見ると確かに光っている"),
            w.plot_note("$jamosの部屋に持ち込み、それで連絡してもらおうとする"),
            w.plot_note("$jamosが、実は$mochに弱みを握られていて、いやいやこのイベントに参加しただけで、全然地元の歴史研究家ではないと告白した"),
            #
            w.plot_note("外が晴れていたので$doldが船を探しに行く"),
            w.plot_note("$limeもついていく"),
            w.plot_note("$wilsonは談話室に転がる$hugarについて調べると言っていた"),
            w.plot_note("$doldは自分がこんなちっぽけな田舎町を出て、もっと大舞台で活躍できると思っていたと語る"),
            w.plot_note("でも現実は甘くなく、すぐ壁にぶつかり、結局逃げるようにして地元に帰ってきた"),
            w.plot_note("そんなだから、こんな面倒に巻き込まれて、それも自分のせいじゃないと思っている"),
            w.plot_note("もともと都会で料理人になるのが夢じゃなく、誰かの喜ぶ顔が見たいから料理やってたんだけどな、と"),
            w.plot_note("少なくとも今自分が役に立てそうなのは、これくらいだと。肉体労働をかってでる"),
            w.plot_note("と、雑木林で$mochらしき男の遺体が見つかった"),
            w.plot_note("$mochも殺されていたのだ。しかもあの雨の中で"),
            w.plot_note("と、そこにちょうど船がやってくる"),
            w.plot_note("$sherlockと警官数名が上陸する"),
            w.plot_note("声をかけ、すぐに城へと向かう$sherlockたち"),
            w.plot_note("$doldは警察に事情を説明する"),
            #
            w.plot_note("$maryと$jamosが部屋から出てきて、$sherlockがつくから迎えをよこしてくれと言っていたと"),
            w.plot_note("外に$limeと$doldが出たことを聞く"),
            w.plot_note("と、$maryが妙な臭いがするのに気づいた"),
            w.plot_note("その臭いは暖炉の裏手で、そこに隠し通路を見つけた"),
            w.plot_note("$maryは隠し通路に入っていく"),
            w.plot_note("止めようとするが先に行ってしまい、$wilsonは慌てて追う"),
            w.plot_note("$jamosは途方にくれていた"),
            #
            w.plot_note("$maryと$wilsonは地下に出た"),
            w.plot_note("ずっと進んでいくとそれはいくつかの部屋に繋がっている"),
            w.plot_note("途中で$bettyの遺体が転がっていた"),
            w.plot_note("だが$maryがその臭いがするのは一番奥の部屋だという"),
            w.plot_note("$maryは$cherryの部屋でした臭いで、その場所に$cherryが捕まえられているんじゃないかと思っていた"),
            w.plot_note("一番奥の部屋で、人が倒れていた"),
            w.plot_note("それは$cherryではなく$karlで、既に絶命している"),
            w.plot_note("その部屋は拷問器具が置かれていた"),
            w.plot_note("かつて使われたものだろう、と$wilson"),
            w.plot_note("その部屋の奥で、何かがうごめいた"),
            w.plot_note("飛び出してきたのは真っ黒な大きい獣、魔獣だった"),
            outline=ABSTRACT)

