# -*- coding: utf-8 -*-
'''
Episode: 0-0 "厄介事と便利屋"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


# DEFINE
TITLE = "厄介事と便利屋"


# NOTE: outlines
ABSTRACT = """
遥か昔に$bossが倒されて平和になったはずの世界。$science技術により産業革命が起こる変革期だった。$wilsonは王室から第二王女失踪の調査を依頼され、困っていた。
行きつけの酒場で旧知の元軍医$stanと再会し、彼から便利屋$sherlockという男を教わる。翌日、$sherlockに仕事を依頼しようと彼の家を訪れるのだが。
その出会いが、やがて大きな事件に関わることに繋がっていた。
"""


# Scenes



# Episode
def main(w: World):
    return w.episode(TITLE,
            # NOTE
            w.plot_setup("王室の厄介事を片付けるエージェントの$wilsonは第二王女が失踪した件についての調査と捜査をすることになっていた"),
            w.plot_turnpoint("情報を集める為に訪れたパブで旧知の元軍医$stanと再会する"),
            w.plot_develop("$stanとは王立学校時代の同期生で彼は医師を目指し、$wilsonは弁護士を目指した仲だった。互いの近況を語り合う"),
            w.plot_turnpoint("$stanから便利屋$sherlockについて教わる"),
            w.plot_resolve("後日、その便利屋$sherlockに仕事を依頼する為に彼の家を訪れた"),
            w.plot_note("$wilsonは王室の厄介事を片付けるエージェントである"),
            w.plot_note("長旅から戻ってきて自宅に入り、そこに置かれた書簡に目を通してため息"),
            w.plot_note("とりあえずパブで情報収集かと出かける"),
            w.plot_note("町の様子"),
            w.plot_note("$bossが$heroによって倒されてから千年の月日が過ぎて、社会も大きく変容している"),
            w.plot_note("$heroの子孫たちにより統治され、いくつかの王国が生まれた"),
            w.plot_note("その一つがこの国"),
            w.plot_note("夜でも明るくなる。$scienceの技術だ"),
            w.plot_note("馴染みのパブには、明らかに人ではない姿の生き物。$ajinと呼ばれる、かつての闇の種族。あるいはその混血"),
            w.plot_note("そこで声をかけられる。「$wilsonじゃないか？」"),
            w.plot_note("王立大学時代の友人$stanだった"),
            w.plot_note("軍医になったが戦線が落ち着いたので任期が終わり、町で開業医になると聞く"),
            w.plot_note("互いの近況について話しつつ、$beerを飲む"),
            w.plot_note("$wilsonはそれとなく最近身近な人が知らない間にいなくなる事件があると話す"),
            w.plot_note("そういう困り事を押し付けられて、と"),
            w.plot_note("お役所勤めは大変だな、と苦笑"),
            w.plot_note("$stanは「便利屋$sherlockという男を知っているか？」と"),
            w.plot_note("$stanも直接は知らないが、今の家を世話してもらった不動産屋$lisaに、何か困ったことがあると彼に相談するといいと教わったと"),
            w.plot_note("$wilsonは手帳にその男の名前と住所をメモする"),
            w.plot_note("$Baker街か"),
            w.plot_note("翌朝、片付かない部屋を見て苦笑する"),
            w.plot_note("どうにも片付けが下手でな、と"),
            w.plot_note("鍵をかけて、玄関の鉢植えの下に隠して出かける"),
            w.plot_note("近所の駐車場まで歩き、そこで$carに乗る"),
            w.plot_note("$scienceにより動く乗り物"),
            w.plot_note("ガードマンに礼をしつつ、出ていく$car"),
            outline=ABSTRACT)

