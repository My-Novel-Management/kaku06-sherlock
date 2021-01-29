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
            #
            w.plot_note("$maryは$moriano犯罪研究所にいた"),
            w.plot_note("助手の$muranに色々と教授のことを教わる"),
            w.plot_note("$morianoは広い目で物事を見ることの大切さを説く"),
            w.plot_note("この世界は人間だけのものではなく、他の生き物、人型にしても$ajinなども同居している"),
            w.plot_note("$muranも実際$ajinで、外見ではわからないが魔女の血を引いていて、多少心得があるという"),
            w.plot_note("小さい頃から魔女というだけでいじめられ、酷い目に何度もあった。死にそうになったこともある"),
            w.plot_note("$morianoの知人によって助けられ、$morianoを紹介された"),
            w.plot_note("$morianoの違うところは、自分自身では何もしないということ"),
            w.plot_note("人を駒のように動かして、自分のやりたいことを達成する"),
            w.plot_note("一人では力がなくても、何人か合わせればいいし、適材適所でやれる人がやればいいという"),
            w.plot_note("それは逆に誰にでも仕事がある、やるべきことがある世界観だった"),
            w.plot_note("また$morianoは今後、より人間の力が強まり、色々なものが迫害される世界が近づいていると予見している"),
            w.plot_note("そこで$ajinたちを中心に、彼らを救うべく組織を作っているという"),
            w.plot_note("「こんなわたしでも力になれますか？」"),
            w.plot_note("$maryに対して、戻ってきた$morianoが「君の本当のすばらしさに気づけないのが、あの男の弱さだ」と言う"),
            #
            w.plot_note("$maryが帰ってこないまま、すでに五日が過ぎていた"),
            w.plot_note("$ignesたちに探させているが情報がない"),
            w.plot_note("$limeも心配で探しに出ていたが、戻ってきて「駄目」と"),
            w.plot_note("$sherlockは子供じゃないんだし放っておけばいいと言うが、$limeはまだ子供だ、と反論する"),
            w.plot_note("$sherlockは研究室に閉じこもり、何かを調べていた"),
            w.plot_note("$wilsonも忙しいと出ていってしまう"),
            w.plot_note("$limeは自分の悩みも相談できないまま、キッチンに立ち、考え事をする"),
            #
            w.plot_note("翌日$limeもしばらく一人になりたいからと外に出ていってしまう"),
            w.plot_note("$sherlockはまた一人に戻っていた"),
            w.plot_note("お茶を頼んでも誰もいない"),
            w.plot_note("かつての自分の暮らしに戻っただけだ、と"),
            w.plot_note("そこに大家の$lisaがやってきて、家賃の支払いが滞っているという"),
            w.plot_note("あと、最近放火犯が出ていて気をつけてくださいとも"),
            w.plot_note("邪険に追い払い、研究室にこもる"),
            w.plot_note("今取り組んでいるのは体液や毛髪から個人を特定できないか、というものだった"),
            w.plot_note("しかし成分検出しても、それがその個人特有のものかまでは特定できず、証拠としては全く使えない代物だった"),
            w.plot_note("明け方、焦げ臭い臭いで目覚める"),
            w.plot_note("家が燃えていた"),
            w.plot_note("$sherlockの火の不始末だった"),
            outline=ABSTRACT)

