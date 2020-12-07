# -*- coding: utf-8 -*-
'''
Stage: "警察署"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


# NOTE
#   交番規模のものから、警察署本部までこちらで


# alias
STATION = "PoliceStation"
OFFICE = "PoliceOffice"
INTERROGATION = "PoliceInterrogationRoom"


# Scenes
## in Empty House
def interrogation(w: World):
    mary, wil, lime = w.get("mary"), w.get("wilson"), w.get("lime")
    pat = w.get("patson")
    rest = w.get("restrade")
    return w.scene("事情聴取",
            w.change_camera("mary"),
            w.change_stage(INTERROGATION),
            w.plot_note("警察の事情聴取を受けた$maryたち"),
            mary.be("事情聴取を受けている$S"),
            pat.be(),
            pat.talk("もう一度聞くけど、いいかい？"),
            mary.talk("何度聞かれても同じことやもん", "一度聞いたら覚えられへんのん、$k_pat"),
            pat.talk("事務手続きだから我慢してよ", "$meだって何もやりたくてやってるんじゃなくて、人が一人亡くなったれっきとした事件だからね"),
            mary.do("$Sは再度、自分たちの状況を話す"),
            mary.do("まず$sherlockが$morianoの居場所を探し出して、追い詰めたところから話し始める"),
            mary.do("そこで$sherlockは$morianoを道連れにして滝壺に落下し、亡くなったこと、そのことを予見して手紙を$maryたちに送っていたこと"),
            mary.do("その後$maryたちは$sherlockを探したが、何も情報は得られなかった"),
            mary.do("そこにホームレスが$EastEndの空き家に$sherlockらしい人物を見かけたというので、やってきて一晩見張っていた"),
            mary.do("$maryは寝てしまっていたが$wilsonにより異変が察知され、見てみると明かりのついた部屋で二人の人間のシルエットが争っている風に見えた"),
            mary.do("その明かりが消えて、しばらく待っていたが何も起こらないので、調べてみることにした"),
            mary.do("部屋に入ったら知らない男の人が倒れていて、急いで$maryが警察を呼んできた"),
            mary.talk("これでええか？"),
            pat.talk("ありがとう。調書は無事に終わったから、外で待っているといいよ。すぐ他の方の調書も終わる"),
            mary.talk("なあ、$k_pat", "$sherlockはどこにいったんやろ"),
            pat.talk("実はね$maryちゃん",
                "君たちの話から我々は$sherlockを重要参考人として手配している"),
            mary.talk("何言うてんの！"),
            pat.talk("二人いて、片方の人間が死んだ。つまり残った$sherlockが殺した疑いが強くなるのは当然だよね"),
            pat.talk("我々もそんな可能性は薄いと思っているけれど、常々思い込みを排除して並べた情報から論理を組み立てるようにと言っていたのは、彼、$sherlockの方だからね"),
            )


def shal_is_suspect(w: World):
    mary, wil, lime = w.get("mary"), w.get("wilson"), w.get("lime")
    pat = w.get("patson")
    rest = w.get("restrade")
    return w.scene("容疑者は$sherlock",
            w.change_stage(OFFICE),
            mary.come("取調室を出る$S"),
            lime.be("廊下で立って待っていた$S"),
            mary.talk("あ、$lime"),
            mary.talk("どうしよ。$sherlockが容疑者にされちゃった"),
            wil.come("取り調べを終えて出てくる$S"),
            wil.talk("聞いたよ", "状況からいえば仕方ない", "ただ我々が見たのが本当に$sherlockかどうか分からないから"),
            mary.do("それならあそこにいたのが$sherlockじゃなかった証拠を見つければいいと考えて、$Sは行く"),
            wil.talk("どうするつもりだ？"),
            mary.talk("もっかいあそこに行って、証拠見つける", "それで$shalが犯人やないことを証明する"),
            mary.go("一人で先走っていってしまう"),
            lime.do("$Sはうなずき、$maryを追いかけていく"),
            pat.come(),
            wil.do("出てきた$patsonと小声で会話する$S"),
            wil.talk("ところで見つかった遺体の身元は？"),
            pat.talk("$sherlockの仲間にはさすがに教えられませんよ",
                "それよりどうです", "これ、美味しいですよ"),
            pat.do("最近よく見る青い瓶の飲み物を勧める"),
            wil.talk("いや、生憎とそれは苦手でね"),
            pat.talk("それは残念"),
            )
