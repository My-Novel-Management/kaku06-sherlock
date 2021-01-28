# -*- coding: utf-8 -*-
'''
Episode 8-0
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


# DEFINE
TITLE = "全ての顛末"


# NOTE: outlines
ABSTRACT = """
偽$wilsonである$zeronの自殺により$boss復活の儀式にかかわる一連の事件に一応の決着がついた。
だが$sherlockと$mary、$limeは住む場所を失い、仕方なく$wilsonの家でしばらく暮らすことになる。しかし大家が家賃滞納を理由に家から出ていけと言ってきた。
そこに本物の$wilsonが帰ってきて、$sherlockたちは彼に一連の事件と自分たちがここにいる事情を語った。
$wilsonは$sherlockの活躍を小説として新聞に掲載することで家賃分を何とかしようと提案する。
これを承諾し、ここに$sherlock探偵社が誕生した。
"""


def main(w: World):
    return w.episode(TITLE,
            # NOTE
            w.plot_setup("偽$wilsonである$zeronの死により一連の事件に決着がついた"),
            w.plot_turnpoint("$sherlockは$wilsonが偽物だと気づいていた、と告白する"),
            w.plot_develop("$sherlockは最初の時点でおかしいと思い、更に$wilsonの家に行って気づいたと語る。全ての事件に巧妙に$zeronが関わり、更に$boss復活の儀式の祭具を揃える動きを行っていたと語る"),
            w.plot_turnpoint("本物の$wilsonが帰ってくる"),
            w.plot_resolve("$sherlockたちは$wilsonに全ての事情を説明する"),
            w.plot_turnpoint("$wilsonは$sherlockの活躍を小説にして稼ぐことを提案した"),
            w.plot_note("十日ほどで退院し、$sherlockが家に戻ってくる"),
            w.plot_note("$sherlockはなぜか$adelに送られてやってきた"),
            w.plot_note("出迎える$maryと$lime"),
            w.plot_note("$ignesたちもいて、退院パーティを開く"),
            w.plot_note("しかし途中で$maryが$wilsonの家をこのまま使っていていいものか、と尋ねる"),
            w.plot_note("$sherlockは家賃を支払う必要がなければハウスキーピングするという名目でしばらく使わせてもらおうと提案する"),
            w.plot_note("みんなでここに住めばいいと言い出す$ignes"),
            w.plot_note("そこに$lisaが顔を出す"),
            w.plot_note("どうやらここのオーナーが$lisaに管理を委託したらしい"),
            w.plot_note("気まずい$sherlock"),
            w.plot_note("$lisaは家賃が一年ほど滞納したままだといって、すぐに払わないと出ていってもらいたいと言い出す"),
            w.plot_note("$sherlockは金の目処があるから、数日待ってほしいと頼む"),
            w.plot_note("$lisaは信じない、というから、仕方なくあの場からくすねてきた$red_stoneを渡す"),
            w.plot_note("$lisaはそれを担保にして、とりあえず待つということになった"),
            w.plot_note("どうするか相談する"),
            w.plot_note("$sherlockはとりあえず出ていくしかないだろうと"),
            w.plot_note("$wilsonのことも分からないし、そもそもいつも家賃をどうしていたのかと"),
            w.plot_note("$limeに王室に出してもらえば、と$ignesが言い出すが、$limeはそっちは頼れないと"),
            w.plot_note("$maryが少し働いたお金はほぼ生活費に消えていた"),
            w.plot_note("基本的に偽物の$wilsonにもらっていたが、どうやらそれが家賃分だったと通帳を見て判明する"),
            w.plot_note("ほぼ金がなく、$sherlockは野宿でもするか、適当な空き家を使うか、と言い出す始末"),
            w.plot_note("そこに訪問客がくる"),
            w.plot_note("見たことのない男性は$wilsonと名乗った。彼は本物の$wilsonだった"),
            #
            w.plot_note("事情を説明し、一応の理解をえる"),
            w.plot_note("$wilsonはよく仕事や個人的な事情で家を開けることが多いから、使ってもらって構わないと言う"),
            w.plot_note("また家賃に関してはいつも王立銀行のシステムを利用して先払い分をそこにチャージしておいて、引き出してもらっていると"),
            w.plot_note("だがそれがなくなっていることも伝える"),
            w.plot_note("別の口座にある分で当座の金は払っておいて、生活費と家賃を稼ぐ必要があると言い出す"),
            w.plot_note("$maryは仕事をしていたが、$sherlockは何もない。そもそも普段も依頼を受けて、それで稼げたり稼げなかったりするが気にしていない"),
            w.plot_note("$wilsonは「探偵」をやることを提案する"),
            w.plot_note("またその活躍を$wilsonが小説にして知人の新聞に掲載して、掲載料をもらおうと"),
            w.plot_note("しばらく外に出て戻ってくると、その話をまとめていた"),
            w.plot_note("偽物とは違い、かなりてきぱきと仕事をしてくれる"),
            w.plot_note("こうしてまたしばらく$sherlockたちは四人で謎解きの仕事ができるようになった"),
            outline=ABSTRACT)

