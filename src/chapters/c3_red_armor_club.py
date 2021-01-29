# -*- coding: utf-8 -*-
'''
Chapter "赤鎧クラブ"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from config import TITLES
from episode3 import closed_red_armor_club
from episode3 import her_identity
from episode3 import limes_reason
from episode3 import silent_knight
from episode3 import strange_part_time_job
from episode3 import the_end_of_case


# Episodes
# NOTE
#   .沈黙の鎧騎士＞謎の鎧騎士を連れてくる
#   .奇妙なバイト＞$sherlockはバイトを辞めるよう忠告
#   .銀行強盗＞$limeが容疑者となる
#   .事件の結末＞強盗団の死
#   .鎧騎士の正体＞$limeは第二王女
#   .事情あり、にて＞$limeが同居人となる

# NOTE: outlines
ABSTRACT = """
$maryが同居人となり家事全般を担当するようになった$sherlock宅。しかし彼女は致命的に下手だった。何度も失敗し、落ち込んで市場に買い出しに向かった$maryは、そこで自分よりも更に落ち込んでいる謎の鎧騎士を見つける。彼（彼女）は言葉が喋れず、身振り手振りの会話で困っていることが分かり、便利屋$sherlockを紹介する。
$limeと名乗った鎧騎士は拾ってもらった質屋オーナー夫婦の店の守衛を仕事にしているが、店の管理の方を担当している店員の$jakinsから特別な仕事を紹介された。それは赤い鎧を着た者だけに資格があり、赤鎧クラブという名前の古くからある団体の機密文書の写本をするというものだった。
割のいいバイトだが、午後から三時間程度黙って店を離れているので気がかりだと相談する。
$sherlockはすぐにその仕事を辞めるように忠告したが、$limeにも事情があるようだった。
数日後、$limeは再び$sherlock宅にやってくる。突如赤鎧クラブが解散してアルバイトが無くなり、おまけに店員の$jakinsが失踪してしまったというのだ。
$sherlockは$limeたちにあのアルバイトも赤鎧クラブも本当の目的のためのダミーであり、それは$jakinsを含めた集団が仕組んだもので、既に目的が達成された為にいなくなったと説明する。
その目的が改装中の国営銀行の大金庫に質屋の地下から抜け道を掘って宝石を盗み出すことだったと判明するが、その地下道で$jakinsが殺されているのが発見され、$limeは殺人の容疑者になってしまった。
$sherlockは彼の容疑を晴らす為、事件の調査に乗り出す。だが別件で、火災現場から見つかった謎の複数名の焼死体が銀行強盗団だったと分かり、強奪された宝石が見つからないまま事件は解決になった。
後日、世話になったオーナー夫婦の家を出た$limeは、自分が失踪中の第二王女だと告白し、事情があるからしばらく置いて欲しいと$sherlockに依頼した。
"""

# NOTE: charas
#   ・$nowlis（本物の$wilsonだが、色々隠れて世界の動向を伺っている。元勇者の仲間。永遠の生命を持つ、外の世界から来た男
#   ・$lime（初出。実は第二王女だが最後の方まで明かされない
#   ・$jakins（ここのみ。質屋オーナー。$limeを拾ってくれた。孤児院に寄付をしている
#   ・$jeena（ここのみ。質屋オーナーの妻。人を疑うことを知らない

# NOTE: stages
#   ・市場（$maryがよく行く場所になる。ここでしっかり描いておく
#   ・国営銀行（改装中。コレクタ$philoの$bossの遺品が保管されている

# NOTE: items
#   ・$white_stone（銀行にあった

# NOTE: case
#   ・赤い鎧騎士だけ募集していた奇妙な仕事　→$limeを店から遠ざける為で、その間に国営銀行の大金庫へ繋がる抜け穴を掘っていた
#   ・$jakins殺害事件　→仲間割れと口封じで殺された。その強盗団も港の船の事故？爆発によって死去

# NOTE: tech
#   ・


# Chapter
def main(w: World):
    return w.chapter(TITLES[3],
            # NOTE
            #   事件：赤鎧クラブという奇妙な仕事　→銀行強盗／バイトの$bins殺害
            #   被害者：銀行の大金庫の宝石群／$bins
            #   容疑者：オーナー夫婦／$lime
            #   犯人：$binsたち強盗団／強盗団（$bins殺害）
            #   依頼人：$maryと$lime
            #   トリック：奇妙な仕事による偽装（割のいいバイトで遠ざけている間に地下通路を掘り、銀行の大金庫から物を奪う
            #   結果：銀行から大量の宝石が盗まれた、中には国宝の$stoneも含まれていた／$limeが解雇され、住居がなくなった
            #   ポイント：古代の武具（非$science的装備）／第二王女／裏で手を引く何者か／$stone白
            #
            silent_knight.main(w),
            strange_part_time_job.main(w),
            closed_red_armor_club.main(w),
            the_end_of_case.main(w),
            her_identity.main(w),
            limes_reason.main(w),
            outline=ABSTRACT)


