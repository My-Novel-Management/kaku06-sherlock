# -*- coding: utf-8 -*-
'''
Episode 6-3
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


# DEFINE
TITLE = "$maryの乱心"


# NOTE: outlines
ABSTRACT = """
$maryがいなくなり、$limeはどこにいったのか探さないといけないと主張するが、$sherlockは放っておけばいいと聞かない。
$limeは$ignesたちに協力してもらい、$maryの行方を探す。
一方$sherlockは$steinの家の再調査に訪れていた。$morianoが関与した証拠を探すためだ。しかし痕跡が綺麗に消されている。だが$steinの日記のページの間に一本の毛髪を見つけた。毛髪を証拠にできないかと考える$sherlock。
$limeは$morianoの研究所に入るのを見たという情報を得て、単身研究所に向かう。研究所では助手の$muranだけがいて、$morianoがどんな人物なのか、何をしようとしているのか、その本当の姿を語った。
そこに$maryを連れて$morianoが戻ってくる。彼女は誘拐された訳でも監禁された訳でも何か弱みを握られている訳でもなく、自分の考えでここにいると言った。
$maryは戻らないと$limeに言った。
"""


# Episode
def main(w: World):
    return w.episode(TITLE,
            # NOTE
            w.plot_setup("いなくなった$maryを$limeは探そうとするが$sherlockは放っておけばいいと言って取り合わない"),
            w.plot_turnpoint("$limeはしばらく別のところで暮らすと出ていく"),
            w.plot_develop("$limeは市場の人間や今までの知人、また王室関係の力を使って$maryを探す。すると$maryが$moriano犯罪研究所に入るのを見たという情報が入った"),
            w.plot_turnpoint("$moriano犯罪研究所で$maryと出会う"),
            w.plot_resolve("$limeは$maryに戻ってくるよう説得を試みたが$maryの決意は固く、$morianoの手伝いをすると言って、帰された"),
            w.plot_turnpoint("$sherlockの火の不始末により自宅が燃えてしまう"),
            w.plot_note("$sherlockの家が燃えてしまい、なんとか助け出されたものの、大家の$lisaから説教をくらっていた"),
            w.plot_note("やってきた$limeと$wilsonは、どうするのかと尋ねる"),
            w.plot_note("$sherlockは野宿でもして暮らすと言う"),
            w.plot_note("以前はホームレスだった頃もあり、慣れていて平気だと"),
            w.plot_note("$wilsonはそれなら修繕が済むまで自分の家で寝泊まりすればいいと提案する"),
            w.plot_note("$lisaは修理費用も請求すると言い残した"),
            #
            w.plot_note("$carで$wilsonの家に向かう"),
            w.plot_note("道中、$maryの姿を$limeが見つける"),
            w.plot_note("$maryは新興宗教団体$cultXの手伝いをしていた"),
            w.plot_note("$cultXは代表は違うが、もともとは$morianoが立ち上げた宗教団体だという。特にマイノリティに人気があり、現在勢力を伸ばしていると聞いた"),
            w.plot_note("$maryが$morianoの手伝いをしていると知り、$sherlockは不機嫌になる"),
            w.plot_note("$limeは心配していた"),
            #
            w.plot_note("三人は$wilsonの家に到着する"),
            w.plot_note("$wilsonは鉢植えの下から鍵を拾ってそれで開ける"),
            w.plot_note("中はちらかっていた"),
            w.plot_note("適当に部屋は使っていいと言う"),
            w.plot_note("あまり家に戻っていないために、掃除もままならないと$wilson"),
            w.plot_note("$sherlockは適当に部屋を決めて、そこを研究室兼寝室にしてしまう"),
            w.plot_note("$limeはとりあえず掃除と片付けを始めた"),
            w.plot_note("$wilsonは何か食べ物を買ってくると出ていく"),
            w.plot_note("二人になり、$limeは掃除しつつ$sherlockに話す"),
            w.plot_note("$maryについて、どうするつもりかと"),
            w.plot_note("$sherlockは他人の人生に対して責任を取るつもりはずっとなかった、と告白する"),
            w.plot_note("自分一人だけで生きてきたし、今後もそうだろうと"),
            w.plot_note("$limeの件についてもいつかは出ていくし、特に考えはないと"),
            w.plot_note("$maryは$sherlockの生活にとってイレギュラーだった"),
            w.plot_note("普段事件について調べているのも、自分とは関係がないことだからだ"),
            w.plot_note("そこを$morianoに指摘され、どうしていいか余計にわからなくなった"),
            w.plot_note("珍しく$limeに意見を求める$sherlock"),
            w.plot_note("$limeはまず$morianoが$sherlockがいうように本当に危険なら、彼女を説得して、離れさせる必要があると"),
            w.plot_note("しかし$sherlockは$morianoに勝てる自信がなさそうだ"),
            w.plot_note("勝ち負けじゃない、と$limeは言う"),
            w.plot_note("買い出しを終えた$wilsonが戻ってくると、$sherlockが$carを出してくれ、と言った"),
            w.plot_note("行き先は犯罪研究所だった"),
            #
            w.plot_note("犯罪研究所を訪れる$sherlock"),
            w.plot_note("$wilsonたちは待っていてくれと、一人で突入する"),
            w.plot_note("出迎えたのは助手の$muranだった"),
            w.plot_note("$sherlockは$morianoが帰ってくるまで待つという"),
            w.plot_note("$muranは$morianoから伝言を預かっていると言った"),
            w.plot_note("伝言は暗号になっていて、それを解く"),
            w.plot_note("内容は$maryを取り戻したいなら、ある場所に一人で来い、というものだった"),
            w.plot_note("$morianoの狙いは何か分からない"),
            w.plot_note("ただ以前は近づくな、追いかけるなと警告していたので、何か変化があったのだと推理する"),
            w.plot_note("$sherlockは$muranが何も隠さないというので、最近の$morianoの研究内容について尋ねた"),
            w.plot_note("最近の命題は「種の共存」だと語る"),
            w.plot_note("そもそも$bossという存在がかつて生まれたのは、世界の平衡状態を保つためだった可能性に言及していたと"),
            w.plot_note("自然界には浄化作用があり、ある程度バランスを保つようになっている"),
            w.plot_note("$bossの力により生存していた種も多くいた"),
            w.plot_note("今は偏った世界になりつつあると"),
            w.plot_note("$sherlockはその場所に向かうことにしたが、$wilsonたちには別の話を伝えておく"),
            #
            w.plot_note("一方$maryは$morianoの別荘にいた"),
            w.plot_note("すっかり馴染んだように見えたが、どこか怯えてもいる"),
            w.plot_note("$morianoは$maryに質問をする"),
            w.plot_note("$sherlockが来るという連絡があったが、彼に会いたいかと"),
            w.plot_note("$maryは自分の本当の姿を受け入れてもらいたい、と言った"),
            w.plot_note("$morianoは$maryを洗脳しつつあった"),
            w.plot_note("$maryの心は$sherlockに受け入れられるかどうかだけに傾いていた"),
            w.plot_note("もし受入れられなかったらその時は"),
            w.plot_note("$maryは飛んでいた虫を殺す"),
            outline=ABSTRACT)

