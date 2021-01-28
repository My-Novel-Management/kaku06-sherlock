# -*- coding: utf-8 -*-
'''
Episode 7-5
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


# DEFINE
TITLE = "すべての終わり"


# NOTE: outlines
ABSTRACT = """
$boss復活の儀式が行われ、$stoneに封じられた力が周囲に満ち始める。
だが途中で暴走し、大爆発を引き起こした。$blue_stoneが偽物だったからだ。$jackにより偽物にすりかえられていた。
$patsonの身体は犠牲となり、肉片となって飛び散った。
$sherlockは偽物と知っていて儀式を行わせたのだ。
これで全て終わったかに思えたが、空っぽになった盃を$wilsonが拾い上げる。$wilsonは「また失敗した」と口にする。
意味が理解できない$maryたちだが、$sherlockは予測していた。
$sherlockが全てを行ってきた黒幕が$morianoではなく$wilsonだったと語る。いや、偽物の$wilsonだ。
彼の家を見たときに$wilsonが偽物だと分かった。そこから目的を逆算し、全てを理解した。
$wislonは$zeronと名乗り、正体を現した。
彼は闇の世界から$boss復活のために遣わされた存在だった。
その力は古の魔物のもので、$sherlockたちは太刀打ちできない。$maryが守ろうとしたが負傷していて$transformできない。
追い詰められたかに思えたが、$patsonの使っていた$gunを利用して心臓を打ち抜き、$zeronが利用している体の機能を止めた。
$zeronは闇の力により脱出し、その場から逃げていった
突入した$restradeたちにより助けられ、崩れ去る地下ホールから逃げ出した$sherlockたち。
後日、指名手配で逃走中だった偽$wilson（$zeron）が山小屋で自殺しているのが発見された。
"""


# Episode
def main(w: World):
    return w.episode(TITLE,
            # NOTE
            w.plot_setup("$patsonが$boss復活の儀式を行ったが、偽物の$blue_stoneにより儀式は失敗に終わる"),
            w.plot_turnpoint("$wilsonが$patsonを始末する"),
            w.plot_develop("$wilsonは偽物で、彼こそが$boss復活の主導者だった。偽$wilsonの$zeronは$sherlockに本物の$blue_stoneを持ってくるよう要求する"),
            w.plot_turnpoint("$limeが目の前で$stoneを砕いた"),
            w.plot_resolve("儀式が不可能になり偽$wilsonこと$zeronは逃亡する。後日山中の小屋で自殺しているのが発見された"),
            w.plot_note("$sherlockは病室にいた"),
            w.plot_note("そこに$ignesたちが見舞いにやってくる"),
            w.plot_note("すべての事件が片付き、$restradeたちに事情を説明した"),
            w.plot_note("しかし逃亡した$zeronの行方は知れない"),
            w.plot_note("また本物の$wilsonも行方不明のままらしい"),
            w.plot_note("$sherlockの推理では失踪者事件の被害者になっているだろうと"),
            w.plot_note("$ignesたちはまた来るといって、出ていく"),
            w.plot_note("$sherlockは肉体労働は好きじゃないんだ、とぼやく"),
            w.plot_note("そこに$adelが姿を見せる"),
            w.plot_note("しかし$sherlockは彼女が本物の$adelでないことを見抜く"),
            w.plot_note("「どうして分かったの？」と$jack"),
            w.plot_note("$adelは決して使わないものがある。それが柑橘系の香水だった。彼女は柑橘類が苦手なのだ"),
            w.plot_note("リサーチ不足だったと笑う$jack"),
            w.plot_note("$jackは$sherlockが気づいているとは思わなかったと言う"),
            w.plot_note("タクシー運転手に化けていたのは見破られていたが、まさか$boss復活に関与しているとは思わなかったと"),
            w.plot_note("あの場にいた者だけが$sherlockが$heroの血を引く男だと知っている"),
            w.plot_note("$heroの血はこの現代においてもかなり有力だった"),
            w.plot_note("なぜそれを利用しないのか、と尋ねる"),
            w.plot_note("$sherlockは言う。$heroなんてものはただの象徴でしかなく、本来はもっと多くの人の犠牲の上につかみとった平和というものの本質を見失わせると"),
            w.plot_note("$jackはこれからもしばらく$sherlockを観察対象にすると。おもしろいと言う"),
            #
            w.plot_note("一方$maryは$limeに料理を習っていた"),
            w.plot_note("病院に届けると意気込んで作っているが、あまり見た目はよくない"),
            w.plot_note("それでも真心がこもっていればいいと$limeに言われる"),
            w.plot_note("まだ$wilsonの家に住んでいた"),
            w.plot_note("と、そこを$wilsonの旧友だという医者$stanが訪ねてくる"),
            w.plot_note("$wilsonはずっと不在だと言う"),
            w.plot_note(""),# TODO
            outline=ABSTRACT)

