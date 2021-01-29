# -*- coding: utf-8 -*-
'''
Episode 6-1
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


# DEFINE
TITLE = "$morianoについて"


# NOTE: outlines
ABSTRACT = """
$sherlockはすぐにアリバイを語り、自分の容疑を晴らす。
そもそも$stein教授とは王立図書館で出会った。彼の論文は$sherlockもよく目を通していて、教授から古代の知識について色々と教わっていたと話す。
そして$steinは$morianoの友人だと言い出す。
$morianoについて誰も知らなかった。
$sherlockは$morianoについて語る。この都市の多くの犯罪の糸が$morianoに繋がっていた。$sherlockは珍しく自分の命に代えても$morianoを倒すと言う。
そこに$maryが連れてきた老人こそが$morianoだった
"""

# Episode
def main(w: World):
    return w.episode(TITLE,
            # NOTE
            w.plot_setup("$patsonから$stein元教授が自宅で密室状態で殺されていたことを知らされる"),
            w.plot_turnpoint("$sherlockは自分と$stein教授の付き合いについて告白する"),
            w.plot_develop("$sherlockは$stein教授の研究で$boss復活の儀式という闇の技法が存在し、それを実際に行おうという集まりがあると示唆する。その中心的存在が$morianoだった"),
            w.plot_turnpoint("$sherlockは$morianoこそが今までの全ての事件の裏で糸を引いていた存在だと断言する"),
            w.plot_resolve("$sherlockは情報を集めて$morianoを何としても刑務所送りにしなければならないと、いつもにはない雰囲気で言う"),
            w.plot_turnpoint("$maryが連れてきた老紳士こそが$morianoだった"),
            w.plot_note("$maryが連れてきた老人が$morianoだった"),
            w.plot_note("$morianoは$sherlockが何か言う前に自己紹介をして、更に「$sherlock君」と挨拶をする"),
            w.plot_note("「何を驚いているのかね？」"),
            w.plot_note("$morianoは$sherlockのことをよく知っていた"),
            w.plot_note("「そうだね」と、まず$maryの事件解決にかかわったことを話す"),
            w.plot_note("だがその事件解決も、もっと穏便な解決方法があったことを提示する$moriano"),
            w.plot_note("$sherlockのやり方は結果的に使用人$kailを追い詰め、$jeanを危険に晒したと"),
            w.plot_note("続いて赤鎧クラブの事件"),
            w.plot_note("これは$limeが相談にきたところで既に問題は分かっていたのに、関与しようとせず、ただ忠告だけで済ませた"),
            w.plot_note("その結果、銀行強盗が入り、更に$jakinsが殺された。更に強盗団も何者かによって殺されてしまった"),
            w.plot_note("ガチョウクラブ事件では$sherlockがすぐに事件解決に乗り出さなかったことで$maryが売られるところだった"),
            w.plot_note("この前の孤島事件では現場に向かうのが遅れたために多くの犠牲者を出し、更に主犯である$mochも$cherryも殺してしまった"),
            w.plot_note("$sherlockが全く犯罪を防止できていないことをあげつらい「後出しで推理を披露しているだけの自己満足にすぎない」と言ってのける"),
            w.plot_note("$sherlockは何も反論できない"),
            w.plot_note("その$sherlockに、立場が違えば犯罪者側になっていただろうと言う"),
            w.plot_note("犯罪を犯す側とそうでない側の差は何か？　という問いかけ"),
            w.plot_note("$sherlockは黙ったまま"),
            w.plot_note("$morianoは自分の論文を読んだから思い至っただろうと"),
            w.plot_note("$sherlockは言う。「その思考ができるかどうか、だ」と"),
            w.plot_note("つまり事件解決した考えというのは、犯罪者の思考をなぞっているから、その犯罪を犯すに足りるということらしい"),
            w.plot_note("$maryは考えたこともなかった"),
            w.plot_note("$sherlockは$morianoに問いかける。「あなたはそこまで理解していて何故犯罪者に加担するのか」と"),
            w.plot_note("$morianoは「その思考がたどれれば、君も私と同じ立場になれるだろう」と"),
            w.plot_note("$morianoは$sherlockに警告する"),
            w.plot_note("私のやろうとしていることをこれ以上追いかけない方がいいと。戻れなくなる。つまり$sherlockが$morianoになるという警告だった"),
            w.plot_note("$morianoは自分の研究所の冊子を置いて、立ち去る"),
            #
            w.plot_note("$morianoが去ってから$sherlockは考え込む"),
            w.plot_note("$maryは今までの$sherlockとは違う面が見えて困惑していた"),
            w.plot_note("$sherlockは研究室に閉じこもり、出てこなくなった"),
            #
            w.plot_note("数日後、$patsonが$sherlockを訪ねてくる"),
            w.plot_note("ある事件について事情を聞きたいという"),
            w.plot_note("$sherlockを研究室から引っ張り出す"),
            w.plot_note("$patsonは「$stein教授を知っているか」と"),
            w.plot_note("$steinは最近$sherlockが色々と教わりにいっていた人物だった"),
            w.plot_note("その$steinが殺されたらしい。しかも密室殺人だった"),
            w.plot_note("最初の事件を思わせる"),
            w.plot_note("明らかに$morianoからの挑戦と分かったが、$patsonは$sherlockが容疑者と疑っていた"),
            w.plot_note("$sherlockは警察に連れて行かれる"),
            #
            w.plot_note("一方$wilsonは$mikelと出会っていた"),
            w.plot_note("$mikelから$limeのことを頼まれている"),
            w.plot_note("王室としては第二王女である$limeに戻ってきてほしい、ということらしい"),
            w.plot_note("理由は教えてもらえない"),
            w.plot_note("しかしあまり悠長に待てないと言われた"),
            w.plot_note("また別件で$sherlockについての情報を聞く"),
            w.plot_note("$morianoという人物が接触したことを伝える"),
            w.plot_note("$mikelは$morianoという名前に覚えがあり、大司教と面会していた男だと思い出す"),
            w.plot_note("注意を払いつつも、引き続いて$sherlockについて内偵をしてくれと頼む"),
            w.plot_note("また「例の件」を調べておくように、とも"),
            #
            w.plot_note("$maryは冊子を手に、$moriano犯罪研究所の前までやってきていた"),
            w.plot_note("まるで待ち構えていたかのようにドアが開き、知らない女性が出てきた"),
            w.plot_note("彼女は助手の$muranだと言った"),
            w.plot_note("彼女は$morianoから全て聞いていますと言って、$maryを中に入れた"),
            outline=ABSTRACT)

