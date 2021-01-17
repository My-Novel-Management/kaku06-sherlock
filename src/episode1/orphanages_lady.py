# -*- coding: utf-8 -*-
'''
Episode 1-4: "孤児院の女"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


# DEFINE
TITLE = "孤児院の女"


# NOTE: outlines
ABSTRACT = """
警察はそのことにより$ailyが何者かにより他殺されたのではないかという話になった。
$sherlockは再度孤児院を訪れる。そこで$ailyと当時仲良かった女性の存在を知る。
彼女は孤児院を抜けてから何をしているか分からない。
事件は容疑者が見つからないまま迷宮入りになりそうだった。
$sherlockは彼女にプレゼントしたという$royalswordの所在について考えていた。
$adel経由で王子と出会い、そこで再度$ailyについての情報を聞く。完全に別人だと判断した$sherlock。
再度孤児院を訪れ、教師に尋ねる。「あなたがオペラ歌手の$ailyですね」と。
"""


# Episode
def main(w: World):
    return w.episode(TITLE,
            # NOTE
            w.plot_setup("$sherlockは$ailyについて聞く為に王子と出会う"),
            w.plot_turnpoint("王子は一度だけ$ailyの自宅を訪ねたが、その時は無視されたと語る"),
            w.plot_develop("一旦$sherlockは$ailyについての情報を整理し、知人の鑑識からも情報を得る"),
            w.plot_turnpoint("$ailyが二人いたことが判明する"),
            w.plot_resolve("$sherlockは再度孤児院を訪ねて女教師に「あなたが$ailyですね」と言った"),
            w.plot_turnpoint("更に$ailyが巷で噂になっている怪盗$jackだと言った"),
            w.plot_note("$sherlockは$ailyが殺されていたということが分かり、考えを修正する"),
            w.plot_note("そこに$adelが訪問してくる"),
            w.plot_note("$adelは昨日渡した手紙により$sherlockに王子と会う機会を作ると言った"),
            w.plot_note("午前中の執務のわずかな間を縫って五分だけだと"),
            w.plot_note("$sherlockはそれまでにもう一度$ailyの自宅を見たいと$wilsonに頼む"),
            #
            w.plot_note("$ailyの自宅には警備の警官$pakerが立っていた"),
            w.plot_note("$sherlockが$restradeの知人だというと通してくれる"),
            w.plot_note("寝室ではなく、他の部屋を調べる$sherlock"),
            w.plot_note("そこに鑑識の$burnsがやってきて「どうしてそんな無駄なことをしている」と"),
            w.plot_note("$sherlockは本当に調べるべきはここだと"),
            w.plot_note("あまり使っていない形跡がある"),
            w.plot_note("特に水回りは、ほとんど家に帰らない人間でも誰もが使う"),
            w.plot_note("こういった高級住宅には水道設備がしっかりしている"),
            w.plot_note("貧しい地域では水は貴重で、川から汲んできたものをバケツに溜めておいたりして使うと"),
            w.plot_note("本当に彼女がこんな家に住んでいたのかと疑問符"),
            w.plot_note("$sherlockはドアについていた白い粉を見つける。これは化粧の粉だった"),
            #
            w.plot_note("$sherlockは$wilsonの$carで移動する"),
            w.plot_note("指定されたのは王立図書館だった"),
            w.plot_note("古文書まで収められた国随一の図書館は$sherlockもよく利用している"),
            w.plot_note("学会誌の棚を見ている$sherlock"),
            w.plot_note("棚の中には古代$magic史なども"),
            w.plot_note("王子$gramが現れる"),
            w.plot_note("王子はすらりと長身で美男子。独特の香りが漂う"),
            w.plot_note("$sherlockは王子に$ailyについて尋ねる。どこが性悪なのか。最初はどんな出会いだったのか"),
            w.plot_note("一番最初は知人の紹介だった"),
            w.plot_note("特別な印象はなく美人だな、という程度。その後オペラハウスで歌っているのを見て、気に入った"),
            w.plot_note("何度か酒をともに飲んだ"),
            w.plot_note("彼女は話も上手く、また王子のこと、悩みなどもよく聞いてくれた"),
            w.plot_note("他の女とは違うと感じて、色々と貢いだ。彼女はそんなものいらないといってくれたが"),
            w.plot_note("何度目だったか。記憶が曖昧だが、一度見せてほしいと言われていた$royalswordをホテルに持っていき、その時にどうやらあげてしまったらしい"),
            w.plot_note("王子にとってはいくつもある宝石等の一つだった"),
            w.plot_note("$sherlockは王子に一つ質問する"),
            w.plot_note("「王子が出会った$ailyは常に化粧をしていましたね？」"),
            w.plot_note("女性だから化粧するのは当たり前だろう、という王子"),
            w.plot_note("しかし舞台女優は舞台化粧があり、舞台のある前後には化粧をしないことが多い。肌を休めるためだ。肌を酷く痛めるのが舞台化粧だった"),
            w.plot_note("「そうだろう、$adelさん」と"),
            w.plot_note("$adelは遠巻きに監視していたが、出てきて「ええ」と"),
            w.plot_note("王子はとにかく$royalswordを取り戻してくれたら$ailyのことはどうでもいいと"),
            #
            w.plot_note("$carに戻った$sherlockは$wilsonに「$ailyは二人いた」と"),
            w.plot_note("そして孤児院に向かってもらう"),
            #
            w.plot_note("孤児院で$yilaを探す"),
            w.plot_note("ちょうど庭に出て子供たちの相手をしていた"),
            w.plot_note("$sherlockは彼女に声をかける「あなたが$ailyさんですね」と"),
            outline=ABSTRACT)

