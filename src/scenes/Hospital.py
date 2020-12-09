# -*- coding: utf-8 -*-
'''
Stage: "病院"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


# NOTE: 病院（王立病院、個人のクリニック、等）


# alias
HOSPITAL = "Hospital"
ROOM = "SickRoom"


# Scenes

## in Empty House
def shal_comes_back(w: World):
    mary, lime = w.get("mary"), w.get("lime")
    shal = w.get("sherlock")
    wil = w.get("wilson")
    return w.scene("$sherlockが戻ってきた",
            w.change_camera("lime"),
            w.change_stage(ROOM),
            w.change_time("morning"),
            "翌朝",
            mary.be("病室で眠っている$S"),
            lime.come("入ってきて、汗を拭っている$S"),
            mary.do("目覚めて"),
            mary.talk("え、ここは？"),
            mary.talk("そっか。$me、火事にあって"),
            shal.come("そこに見慣れた帽子とガウン姿の男性が入ってくる"),
            mary.talk("$shal！"),
            shal.do("ベッドから動いて飛びつこうとする$maryを制して、$Sは苦笑"),
            shal.talk("よくがんばったね", "間に合わないかと思ったよ"),
            mary.talk("なんですぐ来てくれへんかったん！"),
            shal.talk("色々と事情があって"),
            mary.talk("ほんまに死ぬところやったんよ！"),
            mary.talk("バカ！アホ！　……でも、ありがとう"),
            shal.talk("ああ"),
            lime.do("気を利かせてそっと廊下に出る$S"),
            wil.come("そこに$Sがやってくる"),
            wil.talk("いやあ、探したよ", "$sherlockは中かい？"),
            lime.do("頷く"),
            wil.do("入っていこうとするが、それを$limeが引き止める"),
            wil.talk("どうかしたのか？"),
            lime.do("理由は説明しないが、しばらくそっとしておいてあげて、と"),
            wil.talk("こちらも$sherlockに急用ができたんだ。すまないね"),
            wil.do("強引に入る$S"),
            wil.talk("お取り込み中だったら悪かったが、$sherlock、君がいない間に色々問題があった"),
            shal.talk("$wilson、どうしたんだ？"),
            wil.talk("悪いニュースと少し悪いニュース、どちらから聞きたい？"),
            shal.talk("どちらも悪いニュースか。まいったね"),
            wil.talk("まずはあの連続誘拐犯だが、警察の取調中に脱走して、自殺したのが発見されたよ"),
            shal.talk("自殺？"),
            wil.talk("一連の謎の殺害方法と同じらしい"),
            wil.talk("それからもう一つの悪いニュースだが、君の家が燃やされたよ"),
            shal.talk("何だって？"),
            )

