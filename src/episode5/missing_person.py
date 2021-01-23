# -*- coding: utf-8 -*-
'''
Episode 5-2
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


# DEFINE
TITLE = "失踪者"


# NOTE: outlines
ABSTRACT = """
元刑事$hugarが現場を保存し、警察を呼ぼうとする。だが外は大荒れで更に船が何者かに壊されていた。連絡手段がなく、警察が呼べないとなり、$hugarは自分が現場責任を取ると言い出す。
$sherlockを手下として使い、それぞれのアリバイを聞き出す。
$maryと$lime、$wilsonはそれぞれ$hugarに事情聴取された。彼の聴取は前時代的なもので、最初から「やったこと」にして聴取された。$maryは泣き出すし、$limeはしゃべれなくなる。$wilsonだけがひょうひょうと答えていた。
一方$sherlockは$reui、$karl、$doldらを担当する。それぞれパーティ後からのアリバイを調べた。
双方の情報を集め、$hugarはずっと部屋にこもっていた$karlが怪しいと言い出し、彼の部屋を調べる。$karlの部屋には古文書があり、そこには色々な闇の技法に関する記述があった。中には人を呪い殺す方法などもあり、$hugarは呪い殺したのではないかと疑う。
$sherlockは現場を調べ、人ではないものが殺したように見せかけたのではないかと推理する。ただそこに獣の毛を発見した。
城主の$cherryは体調を崩して部屋にこもってしまい、イベントも開催できず、そんな中、$mochが姿を消した。
"""


# Episode
def main(w: World):
    return w.episode(TITLE,
            # NOTE
            w.plot_setup("$reuiが殺されたことで元刑事$hugarが主導権を取り、殺人事件の捜査が行われることになった"),
            w.plot_turnpoint("警察を呼ぼうと船を見ると、船が壊されていた"),
            w.plot_develop("$hugarが$maryたちを助手に使い、全員の取り調べを行うが心霊学者$karlは魔獣の仕業と騒ぎ立てたり、城主$cherryは部屋にこもってしまったりとうまくいかない"),
            w.plot_turnpoint("$sherlockに通信機で連絡を取るが応答がなかった"),
            w.plot_resolve("$hugarは容疑者として地元学者$jamosを部屋に監禁するが、$maryたちにはどうも犯人とは思えなかった"),
            w.plot_turnpoint("その夜、観光課の$mochが失踪した"),
            w.plot_note("翌朝、ドアが叩かれた音で目覚める$mary"),
            w.plot_note("ベッドではない床で寝ていた"),
            w.plot_note("呼びに来たのは$wilsonで、みんな一階に集まっていると言われる"),
            w.plot_note("訳もわからず着替えて向かう$mary"),
            #
            w.plot_note("一階のホールに入れられ、そこで元刑事の$hugarから発表があった"),
            w.plot_note("「$reuiが殺された」と"),
            w.plot_note("驚く$mary"),
            w.plot_note("こんな状態でイベントどころではないと$moch"),
            w.plot_note("とりあえず警察を呼ぶために船を見に行かせる"),
            w.plot_note("しかし戻ってきた観光課職員$mochは船が破壊されていると言う"),
            w.plot_note("一応イベント終了後、今日の夕方に船がくる手はずになっていたが、それまで連絡を取れないという"),
            w.plot_note("みんながざわつく中で元刑事$hugarが主導権を取る"),
            w.plot_note("明らかに殺人事件と言い、それぞれのアリバイを調べると言い出す"),
            w.plot_note("だがそこに、城主$cherryが現れた"),
            #
            w.plot_note("$cherryは$hugarや$bettyたちから状況を聞いて疲れた表情"),
            w.plot_note("$hugarが$cherryから許可をもらい、城内を調べる権限を得る"),
            w.plot_note("$wilsonは$maryたちと話し合い、なんとか$sherlockに連絡を取ろうということに"),
            w.plot_note("しかし$maryは$hugarにより助手にされてしまう"),
            w.plot_note("$hugarと$maryで手分けして事情聴取することになる"),
            w.plot_note("$maryを手伝う$wilson"),
            #
            w.plot_note("事情聴取は部屋を分けて行われた"),
            w.plot_note("$maryの担当は地元学者$jamosと料理番$dold、新聞記者の$milkだった"),
            w.plot_note("$maryたちはあとで$hugarから事情聴取されることになると言われた"),
            w.plot_note("$jamosは「また起きてしまった」という"),
            w.plot_note("彼は歴史を研究してきただけあって、何か知っているようだった"),
            w.plot_note("$jamosは前日、遅刻して、あとから船で一人でやってきている"),
            w.plot_note("船着き場に到着したあと、船が出ていくのを見送ったかどうか覚えていない"),
            w.plot_note("慌てて城にやってきて、跳ね橋は既に降りていた"),
            w.plot_note("掘りがあり、跳ね橋を降ろさないと渡れない（出入りできない）"),
            w.plot_note("部屋に案内され、それから夜の立食パーティで話す資料を読み込んでいた"),
            w.plot_note("パーティ後はシャワーを浴びて、軽く酒をひっかけてから寝た"),
            w.plot_note("翌朝は使用人$bettyに事件があったことで起こされるまで寝ていた"),
            #
            w.plot_note("続いて料理番$dold"),
            w.plot_note("今回のイベントのために呼ばれただけで、普段は地元で食堂をやっている"),
            w.plot_note("もともと大きなホテルで働いていたが、こちらに戻ってきた帰省組"),
            w.plot_note("両親のこともあり、心配で戻ってきたという"),
            w.plot_note("夜まで本日分の仕込みをしていて、それから軽く水を浴びて寝た"),
            w.plot_note("朝は目が覚めていたが、使用人$bettyの悲鳴で外に出て、彼女を探して歩いた"),
            w.plot_note("合流後、$doldが$bettyにみんなを起こすよう指示し、談話室を見張っていた"),
            #
            w.plot_note("最後は新聞記者$milk"),
            w.plot_note("彼女は昔$maryの住んでいた街の新聞社にいたが、$Londonの本社に栄転していた"),
            w.plot_note("今回は$sherlockを紹介したツテで記事を書かせてもらえることになり、やってきた"),
            w.plot_note("前日は資料を夜遅くまで確かめていた"),
            w.plot_note("寝付きが悪く、何か食べるものが欲しいと$doldを訪ねている"),
            w.plot_note("軽いアルコール入りのミルク粥をもらい、それで眠る"),
            w.plot_note("朝は$maryたちと同じく$bettyにより起こされた"),
            #
            w.plot_note("三人の聴取が終わり、$hugarに連絡する"),
            w.plot_note("早く終わったので$cherryにも聞いてきて欲しいと頼まれる"),
            w.plot_note("$cherryの部屋を訪ねる$mary"),
            w.plot_note("$cherryは不思議な雰囲気の女性だった。年齢もよく分からない"),
            w.plot_note("彼女は夜は早めに寝て（これは$bettyにより証言されているらしい）、朝も$bettyに起こされるまで寝ていたと"),
            w.plot_note("$maryは一つだけ質問する"),
            w.plot_note("この城の中で何か動物を飼っていないか、ということだ"),
            w.plot_note("「飼っていない」と答えた$cherry"),
            #
            w.plot_note("全てが終わると$hugarに$maryたちが事情聴取される"),
            w.plot_note("しかし三人ともそれぞれ同じで、互いに証明できる関係上、あまり重要視されなかった"),
            w.plot_note("全てが終わったところで、改めてホールに集まる"),
            w.plot_note("しかしそこで、$mochの姿が消えていることに気づく"),
            w.plot_note("外に他の船を探しにいったんじゃないかということになり、$hugarと$wilsonで探しに向かう"),
            w.plot_note("だがどこにも見つからなかったと、帰ってきた"),
            w.plot_note("そして外は酷い嵐になった"),
            outline=ABSTRACT)

