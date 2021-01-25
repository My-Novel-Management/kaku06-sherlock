# -*- coding: utf-8 -*-
'''
Episode 6-2
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


# DEFINE
TITLE = "$morianoの警告"


# NOTE: outlines
ABSTRACT = """
$morianoは$sherlockに対して自分は$steinの死とは無関係だと言う。証拠がないだろうと。
$sherlockは$morianoがどんな犯罪も自分で直接手をくださず、故に現在の司法では立件できず罪に問えないと言う。
だがそこを何とか見つけ出し、必ず罪を償わせると豪語する$sherlock。
その$sherlockに対し、$morianoは$maryに毒入りの飴を与えたことで脅し、これ以上は深入りしないようにと警告した。
その上で、$morianoは$sherlockが人の気持ちより謎解きの方を大切にすると指摘し、$maryたちも捨てられると予言する。$morianoは$sherlockに犯罪をなくすことは不可能だと言い、これ以上自分を追うと余計な犠牲者が出ると脅した。
その翌日、全員が出払っていた間に$sherlockの家は放火されてしまう。全焼こそ免れたが、中も荒らされていて、しばらく使えないという判断から、少しの間$wilson宅で暮らすことにした。
後日、$maryが市場に買い出しに出かけたまま帰ってこなかった。彼女は失踪した。
"""


# Episode
def main(w: World):
    return w.episode(TITLE,
            # NOTE
            w.plot_setup("$maryが連れてきた老人は$morianoで、$sherlockはすぐに逮捕すべきだと言う"),
            w.plot_turnpoint("$morianoは$maryに毒を飲ませたと言った"),
            w.plot_develop("$morianoによって$sherlockが今までやってきたことが全て無駄で単なる自己満足だったことが暴露される"),
            w.plot_turnpoint("$morianoは$maryに解毒剤を渡して立ち去った"),
            w.plot_resolve("$sherlockは$morianoによる脅しに屈しないと言うが、$maryの様子は変だった"),
            w.plot_turnpoint("後日、$maryが失踪した"),
            w.plot_note("$sherlockは取り調べから戻ってくる"),
            w.plot_note("$wilsonがいて、$limeは掃除していた"),
            w.plot_note("$sherlockは$maryがどこにいるかを尋ねたが、買い出しにいったままだという"),
            w.plot_note("$stein元教授が殺された事件について話す$sherlock"),
            w.plot_note("$steinは大学時代の$morianoの同期（といっても彼の方が年上）だった"),
            w.plot_note("彼は学生時代、特に古代の技術に注目して研究をしていた"),
            w.plot_note("大学を退官し、個人的に研究を続けていて、論文もときどき発表をしていた"),
            w.plot_note("$sherlockが彼の名前を知ったのも、古代技術に関する論文からだった"),
            w.plot_note("$sherlockは$steinに聞きたいことがあり、何度か訪問している"),
            w.plot_note("それを目撃した人間がいて、最近よく出入りしている者として$sherlockが容疑者に上がっただけだった"),
            w.plot_note("事件は新聞記者（$milk）が気づいた"),
            w.plot_note("彼女は教授にインタビューする予定があり（先日の孤島事件で闇の儀式、古代の儀式の特集を組むのにアポした）、家を訪問し、遺体を発見した"),
            w.plot_note("玄関の鍵はかけられていて、半日待っていたが現れず、近所の人に聞くと数日出てくるのを見ていないと言われた"),
            w.plot_note("外の窓から確かめると部屋に倒れているのを発見し、警察に通報"),
            w.plot_note("鍵師を呼んで解錠し、中に入る"),
            w.plot_note("$steinは$gunにより殺されていた"),
            w.plot_note("何件かある$gunによる一連の殺人だった"),
            w.plot_note("荒らされた様子はなく、物取りの犯行は否定された"),
            w.plot_note("大学をやめてからは人付き合いが少なく、だからこそ$sherlockが怪しまれた"),
            w.plot_note("$sherlockは警察から$steinの家に向かい、そこで調査をしてきたという"),
            w.plot_note("気になるのは一冊だけ、以前確認した雑誌が消えていたということ"),
            w.plot_note("$wilsonが何を調べていたのか、と尋ねた"),
            w.plot_note("$sherlockは「闇の技法の中でももっとも忌まわしいものだよ。$boss復活の儀式だ」と答えた"),
            outline=ABSTRACT)

