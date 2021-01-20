# -*- coding: utf-8 -*-
'''
Episode 3-4
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


# DEFINE
TITLE = "鎧騎士の正体"


# NOTE: outlines
ABSTRACT = """
$sherlockにより$limeの疑いが晴れた。
しかし$limeは質屋オーナー夫婦に悪いと、家を出る。
孤独になった$limeを、$maryが再び拾って家へと連れてきた。
$maryは自分も働くから何とか置いてもらえないかと頼む。$sherlockは思案するが。
そこで$limeはある告白を始めた。自分が何故こういう状況になっているのか。
$limeは自分が失踪中の第二王女だと告白した。
"""


# Episode
def main(w: World):
    return w.episode(TITLE,
            # NOTE
            w.plot_setup("強盗団が全員死んだことと$sherlockの調査により$limeの疑いが晴れた"),
            w.plot_turnpoint("$limeが釈放されたと連絡を受ける"),
            w.plot_develop("無実となった$limeだったが迷惑をかけたとオーナー夫婦の許を去った。だが路上でどうしようと困っていて、再び$maryに拾われる"),
            w.plot_turnpoint("$maryが$limeを連れてくる"),
            w.plot_resolve("$limeは$sherlockたちに自分がどうしてこうなっているのか、事情を話す"),
            w.plot_turnpoint("$limeは$sherlockたちに自分は失踪中の第二王女だと語った"),
            w.plot_note("翌朝$sherlockは$adelを呼び出した"),
            w.plot_note("王宮の近くにある古い喫茶店で待ち合わせた"),
            w.plot_note("$sherlockは新聞を開いている"),
            w.plot_note("午前の執務の前に店にやってくる$adelは珍しく正装をしている"),
            w.plot_note("王宮内では女性といえど全てがズボンの制服姿になっている"),
            w.plot_note("$sherlockは「急にすまない」と謝りつつも本題に入る"),
            w.plot_note("$adelに聞きたかったのは大金庫にしまってあった王室の大切なものだ"),
            w.plot_note("「教えられると思っているのか？」"),
            w.plot_note("「だから特別にお願いしている」と"),
            w.plot_note("「どうしても必要だというなら」という条件をつける"),
            w.plot_note("$sherlockは手短に今回の事件について説明した"),
            w.plot_note("警察は大金庫にあった沢山の黄金が目的だったとしているが、それは目くらましだと言う"),
            w.plot_note("本題は先日の王子の$royalswordとの関連を睨んでいた"),
            w.plot_note("「その通りだ」と語る$adel"),
            w.plot_note("盗まれたのは$stoneの一つ、$white_stoneだった"),
            w.plot_note("遺跡から発掘されたものを王室が保管していたのだ"),
            w.plot_note("$stoneは四つある、といわれているが$red_stone以外の所在は不明だった"),
            w.plot_note("$sherlockは前日にどうもその一つが見つかった、という情報が半年ほど前に流れて、最近またそれについて情報が買われていると教わった"),
            w.plot_note("$adelが仕事だと出ていくと、$sherlockは考え込んだ"),
            #
            w.plot_note("三日後、$sherlock宅に$restradeがやってくる"),
            w.plot_note("昨日あった火事現場で発見された四人の遺体が、$sherlockの情報から見つけた$jakinsの協力者だと分かったのだ"),
            w.plot_note("$sherlockは指示してすぐに港を封鎖し、駅に検問を張ってもらった"),
            w.plot_note("そうなると陸路で$Londonを脱出するしかなかったが、大量の金を運び出すことは難しい"),
            w.plot_note("となれば盗んだものは置いて、ほとぼりが冷めるまでバラバラに国外に逃げるしかない"),
            w.plot_note("倉庫を探してもらうと、港の一つに不審な荷物の運び込みがあり、それが大金庫に眠っていた金塊だと判明した"),
            w.plot_note("ただそこで見つかったものは全部ではなく、半分程度だったらしい"),
            w.plot_note("主犯こそ火事に見せかけられて殺されたが、本当の犯人はしっかりと目的のものを盗み出したらしい"),
            w.plot_note("また$limeの容疑については、彼の着ていた鎧が特殊な塗料で染められていたために、それと同じものは地下通路内に見つからなかった"),
            w.plot_note("何より被害者$jakinsの爪には肉体の皮膚が残っていたのだ。全身鎧の$limeではありえない"),
            w.plot_note("$patsonは彼の鎧を脱がそうとしたが脱げなかったらしい。あれは呪いの鎧だった"),
            w.plot_note("$restradeから謝罪があり、後で$patsonにも謝りにこさせると言ったがそれは断った"),
            w.plot_note("こうして何も良い収穫のないまま、事件は終わりを迎えてしまった"),
            #
            w.plot_note("$wilsonが家を訪れると$sherlockが不機嫌だった"),
            w.plot_note("「やはり最初に確認しておくべきだったよ。まさかこんなことになるとは思わなかった。そもそも地下から掘っていって抜け道を作れる大金庫とは何だ」"),
            w.plot_note("ただ全てを事前に予測して防ぐなんてことは神様でも難しいと言う"),
            w.plot_note("情報からある程度予測できても、それ以外の予想外は起こるし、何より人の考えることなんてものは推理通りにはならない"),
            w.plot_note("$wilsonは$limeについて尋ねる"),
            w.plot_note("確か今日だろう？"),
            w.plot_note("$sherlockの頼みで彼の鎧にかかった呪いを神官に解いてもらう手はずになっていた"),
            w.plot_note("$maryが付き添いに行くと言っていたが"),
            #
            w.plot_note("$maryは改装中の大聖堂にいた"),
            w.plot_note("その小さな部屋で、大神官により呪いが解かれようとしていた"),
            w.plot_note("$limeの呪いが解かれる"),
            w.plot_note("$patsonや数名の警官も見守る中"),
            w.plot_note("「ありがとうございます」そう言って兜を外すと、そこには女性の素顔があった"),
            outline=ABSTRACT)

