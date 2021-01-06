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
            w.plot_setup("ひとまず$wilsonの家で生活を送っていた$sherlockたちだが、そこに大家がやってきて家賃が滞納されている事実を伝える"),
            w.plot_note("偽$wilsonの自殺により、一連の事件は終わりを告げた"),
            w.plot_note("住む場所を失い、とりあえず$wilsonの家を間借りして暮らすことにした$sherlockたち"),
            w.plot_turnpoint("本物の$wilsonが帰ってくる"),
            w.plot_develop(""),
            w.plot_turnpoint(""),
            w.plot_resolve(""),
            # TODO
            w.plot_setup("偽$wilsonが自殺して、全ての幕が降ろされた"),
            w.plot_setup("$maryは精神的なショック以外に大きな怪我はなく、しばらく入院したのちに退院した"),
            w.plot_turnpoint("退院した$maryが$limeとともに帰ってくる"),
            w.plot_develop("$sherlockは大家の$lisaに詰められていた"),
            w.plot_develop("家賃の支払いが待てないというのだ"),
            w.plot_develop("仕方なく荷物を手に、外に出る$sherlock"),
            w.plot_develop("$sherlockは行く宛があると言う"),
            w.plot_develop("やってきたのは$wilsonの家だった"),
            w.plot_develop("以前に見つけておいたという合鍵の場所を調べて鍵を手に入れ、中に入る"),
            w.plot_develop("しばらく$wilsonの家で厄介になることにした$sherlockたち"),
            w.plot_turnpoint("翌日、そこに知らない男が入ってくる。本物の$wilsonだった"),
            #   ・本物の$wilson
            w.plot_develop("$wilsonは自分がいない間に何があったのかを$sherlockから聞く"),
            w.plot_develop("また何故ここにいるのか、その事情も知る"),
            w.plot_develop("$wilsonは度々出かけるから、留守の間、家を預かってもらえるのは助かるといいつつ"),
            w.plot_develop("それでも四人分をまかなえるほどの蓄えはないから、それぞれに仕事をしてもらう必要があると"),
            w.plot_develop("$maryたちは仕事の宛があった"),
            w.plot_develop("$sherlockは働く気がない"),
            w.plot_turnpoint("そこで$wilsonが$sherlockの活躍を小説にして新聞社に売りつけることになった"),
            )


def wilsons_papers(w: World):
    return w.episode("$wilsonの手記",
            w.plot_setup("本物の$wilsonが作品の記述者だった"),
            w.plot_setup("$sherlockの活躍を小説として書き上げたのだ"),
            w.plot_develop("小説を書き上げ、$wilsonは仲間の待つリビングに向かう"),
            w.plot_develop("リビングでは今日も$maryがうるさくしていた"),
            w.plot_develop("市場で花屋の手伝いをするようになった$maryが、もらったというお菓子を出してお茶会"),
            w.plot_develop("$limeは王室には戻らず、今は剣の道場を手伝いつつ、守衛のバイトをしていた"),
            w.plot_resolve("みんなそれぞれの仕事をし、新しい日々を送っている"),
            w.plot_resolve("$sherlockは$heroなことを隠して今日も新聞記事を眺めては謎を探していた"),
            w.plot_turnpoint("そこに依頼者がやってくる"),
            )


# Chapter
def main(w: World):
    return w.chapter(TITLES[-1],
            total_the_end(w),
            wilsons_papers(w),
            w.symbol("（了）"),
            outline=ABSTRACT)


