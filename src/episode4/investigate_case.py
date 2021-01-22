# -*- coding: utf-8 -*-
'''
Episode 4-3
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World



# DEFINE
TITLE = "事件捜査"


# NOTE: outlines
ABSTRACT = """
$limeは$maryが戻ってこないことに気づき、市場に探しに出かける。$ignesからの情報でどうやらガチョウクラブに潜入捜査をしていたことが判明する。
一旦$sherlockに話そうとするが外出中で、$wilsonに手伝ってもらってガチョウクラブに向かうことに。
外出中の$sherlockは彼女が育った孤児院にきていた。そこで教師から彼女が$ajinであることを知らされる。ここに暮らす多くが$ajinだった。
今も毎月彼女から仕送りが届いているらしい。
他にもここの卒業生で仕送りをしてくれている子は多いが、最近になって多額の寄付があったのが、今手広く事業を手がけている男だった。その男からこの前ガチョウを貰ったと喜んでいた。
そのガチョウがガチョウクラブ経由と知る$sherlock。
ガチョウクラブの男たちに捕まえられた$maryは、$animalだとバレて、売り飛ばされそうになっていた。
そこにあの女性が現れ、彼女を助けると言う。その女性$jackだった（別名を名乗るが）。
"""


# Episode
def main(w: World):
    return w.episode(TITLE,
            # NOTE
            w.plot_setup("$jackと$blue_stoneの関係があるという情報を得た$sherlockは、一旦家に戻るが$maryがいない"),
            w.plot_turnpoint("$maryが戻ってこないと$limeに言われた"),
            w.plot_develop("$maryの残した書き置きを手がかりに$sherlockと$limeはガチョウクラブに向かう。だが$maryは見ていないと言われた"),
            w.plot_turnpoint("被害者宅を調べていて$mouraの夫がガチョウクラブ会員であると判明した"),
            w.plot_resolve("$sherlockはガチョウクラブと$mouraの夫周辺を改めて調査する一方で$ignesたちに$mary捜索を依頼した"),
            w.plot_turnpoint("売り飛ばされそうになっている$maryの前に謎の女性（$jack）が現れた"),
            w.plot_note("$sherlockは図書館にいた"),
            w.plot_note("資料を探しているとそこに$adelが登場する。今日は司書姿だ"),
            w.plot_note("$adelは$sherlockに頼まれていた$stoneの件を答える"),
            w.plot_note("現在王室で管理しているのは$red_stoneのみで（結婚式に使われた$royalswordのもの）"),
            w.plot_note("$white_stoneは先日の銀行強盗により盗まれて、その後金塊は見つかったものの$stoneは行方不明"),
            w.plot_note("$black_stoneは長らく所在が分かっておらず"),
            w.plot_note("$blue_stoneについては何人かの手を経た後に、今回ガチョウの中から出来た（現在鑑定中）"),
            w.plot_note("幸せを呼ぶ宝石として都市伝説になっていたらしく、今回の被害者である$moura夫人が持っていた可能性もあったと"),
            w.plot_note("ただそれ以上は調査できず、何も分からない"),
            w.plot_note("$sherlockは$adelに、一体何が目的で集めていると思うか尋ねたが、返答はなかった"),
            w.plot_note("権力の象徴として四つ集めた者が正当な$heroの後継者である、というようなことが言われていた時代があるが、それは遠いむかしの話"),
            w.plot_note("今は既に国家という体制ができてしまい、そこに対してそんなもので亀裂を入れられるような時代ではないと"),
            w.plot_note("それでももしその思考に固執している古い体制観の持ち主がいるとすれば、集める理由になるかも知れないとも"),
            w.plot_note("$sherlockは掴んでいた本の表紙を見せる"),
            w.plot_note("そこには『古代$magic全書』と書かれていた"),
            #
            w.plot_note("$limeが戻ってくると$maryがいない"),
            w.plot_note("とりあえず夕食の準備を始めて待つ"),
            w.plot_note("しばらくして$wilsonが尋ねてくる。$sherlockは不在だ"),
            w.plot_note("新聞にはガチョウの話は出ていない"),
            w.plot_note("$sherlockが$blue_stoneの持ち主を探すために偽の新聞広告を出しておいたが、何の反応もないらしい"),
            w.plot_note("また$wilsonが$maryを喜ばせようと思って巷で噂になっていた菓子を買ってきたのだが、$maryは不在"),
            w.plot_note("そこに$sherlockが険しい顔で戻ってくる"),
            w.plot_note("$maryがどこにいったかを尋ねたが知らないと"),
            w.plot_note("夕食の準備をした$limeは、心配になり、$sherlockたちに先に食べるように言って外に出ていく"),
            #
            w.plot_note("市場の片付けが終わり、飲みにいく$nowlisたち"),
            w.plot_note("そこに$limeがやってきて、$maryを知らないか、と"),
            w.plot_note("$maryが配管工$raiderと一緒に歩いているのは見かけたと言うが"),
            w.plot_note("飲み屋にいた$raiderに話を聞く"),
            w.plot_note("$raiderは最近金回りがよくなったと仲間から言われていた"),
            w.plot_note("「ガチョウクラブってのに入ったんだ。お前も入らないか？」"),
            w.plot_note("ガチョウクラブについて聞く。会員制のガチョウ販売を行っていて、儲けた分からいくらか配当金が受け取れるらしい"),
            w.plot_note("$maryについて尋ねると、話が聞きたいからとクラブに紹介してほしいと言われて紹介しただけで、後は知らないと"),
            w.plot_note("$limeはガチョウクラブに向かう"),
            #
            w.plot_note("ガチョウクラブの建物は閉まっていた"),
            w.plot_note("周囲には怪しげな男たちがたむろしていて、$limeを見ると圧をかけて近寄ってくる"),
            w.plot_note("$limeはそれでも$maryのことを尋ねようとするが"),
            w.plot_note("男たちは$limeが女性と分かるとナンパしてくる"),
            w.plot_note("そこに$mikelが現れて、助ける"),
            w.plot_note("$mikelは「ただでさえ危険な状態で放置しているのに、自ら危険に見を突っ込まれては何かと困るのですが、$lime様」と"),
            w.plot_note("既に自分のことがバレていたと知った$lime"),
            #
            w.plot_note("一方$maryは薄暗い部屋にいた"),
            w.plot_note("「ここどこやねん」"),
            w.plot_note("ドアを隔てた外から男たちの声が聞こえてくる"),
            w.plot_note("ただの娘かと思ったら$animalの娘じゃねえか。かなり高額で売れるぞ"),
            w.plot_note("どうやら自分が売られる相談だと分かり、泣きたくなる$mary"),
            outline=ABSTRACT)

