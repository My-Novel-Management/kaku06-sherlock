# -*- coding: utf-8 -*-
'''
Episode 7-1
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


# DEFINE
TITLE = "空き家の冒険"


# NOTE: outlines
ABSTRACT = """
ホームレスからスラム街の空き家に$sherlockが出没すると言われ、そこを監視する$maryたち。
夜になると外見や風貌が$sherlockに似た男がその空き家に入り、明かりが灯った。男はいつも$sherlockがしていたように本を読んでいた。
そこに来客がある。二人はしばらく何か言い争った後で、突然明かりが消えた。
しばらく待っても動きがなく、$maryたちは調べるために空き家に突入する。
そこで殺された男の遺体を発見し、警察に通報した。
警察の事情聴取を受けた$maryたち。$maryはそこで$patsonから警察は$sherlockを容疑者として疑っている情報を得る。
$maryは単身で、$sherlockの容疑を晴らすために空き家の調査を行う。
すると、そこで抜け道を発見した。
$maryが抜け道を進むと廃工場に出た。そこで今までに失踪した人間たちの遺体を発見する。だがそこで何者かによって意識を失った。
"""


# Episode
def main(w: World):
    return w.episode(TITLE,
            # NOTE
            w.plot_setup("$sherlockが現れるという空き家を監視していた$maryたちは、そこで争いがあるのを目撃して、中を調査する"),
            w.plot_turnpoint("空き家で男の遺体を発見する"),
            w.plot_develop("警察に連絡し、$maryたちは事情聴取を受ける。そこで$sherlock生存情報を得たことなどを話す$mary"),
            w.plot_turnpoint("$maryは$patsonから$sherlockを容疑者に考えていることを教わる"),
            w.plot_resolve("$maryは単独で空き家を調査に向かう"),
            w.plot_turnpoint("$maryは抜け道を見つけた"),
            w.plot_note("監視している空き家に明かりがともり、そこに$sherlockらしき人影が見えた"),
            w.plot_note("人影はいつも$sherlockがしているように本を読んでいるのが分かった"),
            w.plot_note("$maryはすぐに確認に行こうというが、$wilsonが少し待つように言う"),
            w.plot_note("すると、そこに来客があった"),
            w.plot_note("コートの男が入っていき、何やら口論をしている風"),
            w.plot_note("$maryたちはじっとその様子を見ている"),
            w.plot_note("すると突然明かりが消えた。物音がした"),
            w.plot_note("息を潜めて待つ$maryたち"),
            w.plot_note("だが何も起こらない"),
            w.plot_note("$maryは何かを察して飛び出していく"),
            w.plot_note("慌てて後を追う$wilsonたち"),
            #
            w.plot_note("真っ暗な空き家に入る"),
            w.plot_note("誰の声も物音もしない"),
            w.plot_note("夜目がきく$maryが先に行く"),
            w.plot_note("$wilsonは困ってマッチをつけ、明かりを作る"),
            w.plot_note("リビングが照らされ、そこに死体が出現した"),
            w.plot_note("$maryは$sherlockかと勘違いし悲鳴を上げるが、よく見たら違うと言われた"),
            w.plot_note("入っていったコートの男だった"),
            w.plot_note("$maryたちはもうひとりがどこに行ったか探すが、キッチン側はドアが壊れて開かなくなっていた"),
            w.plot_note("他の場所にも人が歩いた形跡がなく、消えてしまった"),
            w.plot_note("とりあえず警察を呼びに$limeが出ていった"),
            #
            w.plot_note("明け方、$maryたちは警察にいた"),
            w.plot_note("個室で事情聴取されている"),
            w.plot_note("$maryの担当は$patsonで、実は最近続いている$gunによる殺人事件との関連性を疑っていると"),
            w.plot_note("$maryは$sherlockがいるという目撃情報を得て、監視していたことを伝えた"),
            w.plot_note("$patsonは状況から$sherlockを容疑者として疑わざるを得ないと言った"),
            w.plot_note("$maryは$sherlockが絶対に殺人をしていないと言い張るが、$patsonに$sherlockのことをどこまで知っているのかと聞かれて沈黙"),
            w.plot_note("人は変わるんだ、という$patsonの言葉に反論できない"),
            w.plot_note("事情聴取が終わり、$maryは一人廊下に立つ"),
            w.plot_note("先に終わったらしく、一人で警察を出る"),
            w.plot_note("$maryはどうしても$sherlockがやったとは信じられず、あそこにいたのが$sherlockかどうかすら分からないのに警察は何故疑うのかと考える"),
            w.plot_note("$sherlockに罪を押し付けようとしているんじゃないかと思い至る"),
            w.plot_note("$maryは一人、現場の調査に向かった"),
            #
            w.plot_note("空き家のあるスラム街にやってきた$mary"),
            w.plot_note("だが事件のあった空き家は警官が見張りで立っている"),
            w.plot_note("鑑識作業は終わったようだ"),
            w.plot_note("刑事たちが去っていくのを見送る"),
            w.plot_note("そこに$ignesが声を掛ける"),
            w.plot_note("$maryは事情を説明し、$ignesに陽動してもらう"),
            w.plot_note("$ignesたちが騒動を起こしている間に、警官がそちらに向かったすきを突いて$maryは空き家に侵入する"),
            #
            w.plot_note("空き家はよく見れば窓も割れているし、人が暮らすにはやはり、という場所"),
            w.plot_note("テーブルの上の本や本棚の資料、ソファの上の新聞は押収されてなくなっていた"),
            w.plot_note("キッチン側のドアはぶちぬかれ、出入りできるようになっている"),
            w.plot_note("色々と調べてまわった後"),
            w.plot_note("$maryは前夜のことを思い出し、二人の男の位置関係を考える"),
            w.plot_note("明かりはランタンでついていたはず"),
            w.plot_note("ランタンが床に落ちて古いカーペットに油のシミができていた"),
            w.plot_note("男はどこから外に出たかを考える"),
            w.plot_note("裏口は警察が既に調べている"),
            w.plot_note("結局探し回って分からず、リビングに戻ってきたが、喉がかわいてキッチンを覗く"),
            w.plot_note("そこに物を動かした後を見つけた"),
            w.plot_note("キッチンの棚が動く"),
            w.plot_note("裏側に隠し入り口があった"),
            w.plot_note("そこから地下に梯子が伸びている。$maryは降りていく"),
            #
            w.plot_note("やっと事情聴取から解放された$wilsonは$limeと合流する"),
            w.plot_note("$maryがいないことに気づいて$burnsに尋ねるが、一人で帰ったと"),
            w.plot_note("とりあえず$wilsonの家に戻ることにする"),
            #
            w.plot_note("一方$maryはずっと地下道を歩いていた"),
            w.plot_note("古い下水用施設がそのまま残されている"),
            w.plot_note("新しくなる街の暗部だった"),
            w.plot_note("そこには動物の遺体もあり、腐臭が漂う"),
            w.plot_note("びくびくしながら進むと、行き止まり"),
            w.plot_note("伸びている梯子を登るとそこはどこかの廃工場の中だった"),
            w.plot_note("薄暗い中、そこに沢山横たわっている人影を見る"),
            w.plot_note("確認するとそれはすべて殺された人間だった"),
            w.plot_note("一人は少し有名な女優で、$sherlockが失踪事件のリストで挙げていた人物だった"),
            w.plot_note("そこに物音がする"),
            w.plot_note("現れたのは痩せてはいたが$sherlock（によく似た男）だった"),
            w.plot_note("$k_shal？　と呼びかけるが彼はうつろで「見てしまったね」と言った"),
            outline=ABSTRACT)

