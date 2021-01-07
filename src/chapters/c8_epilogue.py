# -*- coding: utf-8 -*-
'''
Chapter "エピローグ"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from config import TITLES
from scenes import Market
from scenes import ReadingRoom
from scenes import SherlockHouse
from scenes import WilsonHouse


# Episode
# NOTE
#   .全ての顛末＞本物の$wilsonが帰ってくる
#   .探偵の誕生＞探偵社を設立
#   .$wilsonの手記＞新しい仕事が舞い込んでくる

# NOTE: outlines
ABSTRACT = """
偽$wilsonの死去により全ての事件は幕を下ろしたかに思えた。
家を失った$sherlockはひとまず$wilsonの家を借りることにする。
だがそこに$wilsonの家の大家がきて、家賃が半年滞納されていると催促してくる。
お金がなくどうしようもできない$sherlockたちだったが、そこに本物の$wilsonが帰ってきた。
事情を話すと$wilsonは自分が$sherlockの活躍を小説にして、それを新聞小説として掲載してもらおうと提案した。
こうしてこの作品は書かれたのだ、というネタばらしがある。
"""
OUTLINES = [
"""
偽$wilsonである$zeronの自殺により$boss復活の儀式にかかわる一連の事件に一応の決着がついた。
だが$sherlockと$mary、$limeは住む場所を失い、仕方なく$wilsonの家でしばらく暮らすことになる。しかし大家が家賃滞納を理由に家から出ていけと言ってきた。
そこに本物の$wilsonが帰ってきて、$sherlockたちは彼に一連の事件と自分たちがここにいる事情を語った。
$wilsonは$sherlockの活躍を小説として新聞に掲載することで家賃分を何とかしようと提案する。
これを承諾し、ここに$sherlock探偵社が誕生した。
""",
"""
※という訳で、記述者は本物の$wilsonだった。
作品の締めくくりに当たるエピローグを書き終えたところで$maryたちに呼ばれる。$maryが初めて焼いたというケーキなるお菓子を食べようというのだ。
$wilsonはそれを口にして昔暮らしていた世界を懐かしく思うが、そこに新たな問題を抱えた依頼人がやってきた。だがまたそれは次の物語。
""",
        ]

# NOTE: charas
#   ・本物の$wilson（一応ここが初出。だが$nowlisとして市場で出てきた男でもある。勘のいい読者だけ分かるように

# NOTE: stages

# NOTE: items

# NOTE: case
#   ・$wilsonすり替わり事件　→本物の$wilsonに長旅をさせ、その間になりすました


def total_the_end(w: World):
    return w.episode("全ての顛末",
            # NOTE
            #   ・全てが終わり
            w.plot_setup("偽$wilsonの自殺により一連の事件の幕引きがなされ、ひとまず$wilsonの家で生活を送っていた$sherlockたち"),
            w.plot_note("偽$wilsonの自殺により、一連の事件は終わりを告げた"),
            w.plot_note("住む場所を失い、とりあえず$wilsonの家を間借りして暮らすことにした$sherlockたち"),
            w.plot_note("今まで食費などの大半が偽$wilsonが出してくれていたので、仕方なく$maryと$limeはアルバイトを続ける"),
            w.plot_turnpoint("大家がやってきて家賃がずっと滞納していて、今すぐ払えないと出ていってほしいと話す"),
            w.plot_develop("何とか打開策を考えようとする$maryたちに対して、どこでも本が読めればいいとやる気のない$sherlock"),
            w.plot_note("$sherlockはそんな金あるはずがないと答える"),
            w.plot_note("$maryたちは何とか金策をして待ってもらう方法を考える"),
            w.plot_note("$limeは王室からお金を借りようかとすら考えるが、そこに頼るのはできないと思い直す"),
            w.plot_note("$maryは遺産を寄付したことを後悔する"),
            w.plot_turnpoint("本物の$wilsonが帰ってくる"),
            w.plot_develop("$sherlockたちは$wilsonに一連の事件と自分たちがここで暮らしている事情を語る"),
            w.plot_note("本物の$wilsonなのか疑う$sherlock"),
            w.plot_note("$wilsonは自分が本物である証拠として、彼しか知らない家の備品の秘密を話す"),
            w.plot_note("本物の$wilsonだということを認めた上で「残念ながら君はここから出て行かなくてはならない」と告げる$sherlock"),
            w.plot_note("家賃滞納の事情を語り、理解してもらう"),
            w.plot_note("$wilsonによると、どうやら家賃分のお金が全て生活費として引き出されていたことが判明した"),
            w.plot_note("つまり偽$wilsonが支援してくれていた生活費の原資は、本物の$wilsonの家賃だった"),
            w.plot_note("$wilsonは$sherlockたちが家を失うのは困るだろうと対策を考える"),
            w.plot_turnpoint("$wilsonが$sherlockの活躍を小説にすると言い出す"),
            w.plot_resolve("$wilson提案により探偵社$sherlockとして看板を掲げて難事件解決を行うことになった"),
            w.plot_note("$wilsonは偽物が語った通り、王室からの依頼を受けて活動しているエージェントだが、他にもライターをやっていた"),
            w.plot_note("以前から新聞社の知人に小説を書かないかと頼まれていたらしい"),
            w.plot_note("$maryたちは$sherlockにどうせなら事件解決を仕事にすればいいと提案される"),
            w.plot_note("$wilsonは「探偵」という職業が別の国にはあると説明する"),
            w.plot_note("こうして正式に事件解決会社「探偵社$sherlock」として看板を掲げ、商売を始めることになった"),
            outline=OUTLINES[0])


def wilsons_papers(w: World):
    return w.episode("$wilsonの手記",
            # NOTE
            w.plot_setup("作品の記述者は本物の方の$wilsonだった"),
            w.plot_note("※$wilsonの一人称になり、ネタバラシがある"),
            w.plot_note("偽物の$wilsonが本当は何をしていたのかについては$sherlockとは別の見解を持っている"),
            w.plot_note("$sherlockから話を聞いただけでは事件概要と彼らの視点しか分からなかったので、自分で情報を集めて補完した"),
            w.plot_note("小説として書いた以外にももちろん些細な情報を得ているが、その全てを記すには紙面が足りない"),
            w.plot_note("一点だけ書き加えておくと、偽物の$wilsonは$boss復活のために遣わされた訳ではなく、わずかに残っていた資料（数冊の本が増えていた）から、自分で考えて$boss復活が最良の手段だと選んで実行したこと"),
            w.plot_note("謎が多い$zeronについて、今後も調査をしてみることにする"),
            w.plot_turnpoint("$maryが$wilsonを呼びに来る"),
            w.plot_develop("一旦今回の事件の分を書き終えた$wilson"),
            w.plot_note("部屋は余っていたが、二階のそれぞれの部屋を$mary、$lime、$sherlockに当てた"),
            w.plot_note("お陰で書斎兼仕事部屋は物置になっている"),
            w.plot_note("最近料理を覚え始めた$mary"),
            w.plot_note("きっちり測ると同じ味にできるというのでお菓子作りが楽しいらしい"),
            w.plot_note("リビングでは焼き立てのケーキがあった"),
            w.plot_note("甘い物は苦手な$sherlock"),
            w.plot_note("$maryは彼に食べさせたくて仕方ない"),
            w.plot_note("まず$wilsonが味見することになっていた"),
            w.plot_turnpoint("$maryのケーキを食べた時に過去の記憶を思い出す$wilson"),
            w.plot_resolve("かつて$jackとして活動していた頃があるが、いずれそれについても語ることがあるだろうと締める"),
            w.plot_note("$wilsonは表のエージェントとして、あるいはライターとしての顔以外も持っていた"),
            w.plot_note("書斎で$jackから預かった本物の$blue_stoneを見る$wilson"),
            w.plot_note("いずれ役立つ時がくるまで隠しておこうと、隠し棚にしまった"),
            w.plot_note("そこに新たな依頼者が訪れる"),
            w.plot_note("これがまた新しい$sherlockの事件の始まりだった"),
            outline=OUTLINES[-1])


# Chapter
def main(w: World):
    return w.chapter(TITLES[-1],
            total_the_end(w),
            wilsons_papers(w),
            w.symbol("（了）"),
            outline=ABSTRACT)


