# -*- coding: utf-8 -*-
'''
Episode 7-0
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


# DEFINE
TITLE = "$sherlockを探して"


# NOTE: outlines
ABSTRACT = """
シャーロックが消えてから半年、メアリーは市場の手伝いをし、ライムは護衛のアルバイトしながら、彼を探し続けていた。しかし未だに何も情報がなくパットソンたちは諦めた方がいいと言っていた。
だがある日、シャーロックの家が強盗に荒らされていて、まだシャーロックを探している人物がいることが分かる。
メアリーたちは安全のために一旦ウィルソンの家に移り、地道にシャーロックに関する情報を収集した。
そして遂にウィルソンがシャーロックを見たというホームレスの情報を持ってくる。
"""


# Episode
def main(w: World):
    return w.episode(TITLE,
            # NOTE
            w.plot_setup("$sherlockが滝壺に落ちてから三ヶ月が経つが何も生存情報が見つからず、$maryたちは新しい生活に馴染み始めていた"),
            w.plot_turnpoint("$wilsonが$sherlockに似た男を目撃したという情報を持ってくる"),
            w.plot_develop("ホームレスから情報を得て、$maryたちは$sherlockに似た男が現れるという空き家を監視する"),
            w.plot_turnpoint("夜になり$sherlockに似た男が空き家に入っていく"),
            w.plot_resolve("シルエットは$sherlockを思わせたが、その空き家に別の男性が入っていくのを目撃する"),
            w.plot_turnpoint("争う音がして、明かりが消えた"),
            w.plot_note("$sherlockが滝壺に落ちていなくなってから三ヶ月が過ぎていた"),
            w.plot_note("$wilsonが帰ってくると$maryがぼんやりと座っていた"),
            w.plot_note("一瞬見間違えて「$sherlock？」と声をかける"),
            w.plot_note("すぐ$wilsonと気づいてため息"),
            w.plot_note("$wilsonも$sherlockの情報は今日も何もないと言う"),
            w.plot_note("$limeも王室に戻ってしまい、二人になっていた"),
            w.plot_note("$wilsonは$ignesたちが心配していたと伝える"),
            w.plot_note("退院してきてからずっとこの調子で$wilsonも参っていた"),
            w.plot_note("$maryは買い物に行くという"),
            w.plot_note("ちょうどそこに$adelがやってきて、入れ替わりで$maryが出ていく"),
            #
            w.plot_note("$maryは街の様子が変化しているのを感じていた"),
            w.plot_note("$sherlockも$morianoも消えた"),
            w.plot_note("今まで解決していた事件が軒並み放置され、未解決事件が増えた"),
            w.plot_note("また冤罪や$ajinの違法逮捕も増えていた"),
            w.plot_note("治安が悪くなり、街角には警官が立つ（$parkerがいた）"),
            w.plot_note("$maryは$sherlockの姿を探してしまう"),
            w.plot_note("そこに肉屋の$nowlisが声をかける"),
            w.plot_note("元気を出せと肉をくれた"),
            w.plot_note("懐かしい感じを思い出したが、それでまた涙が滲む"),
            w.plot_note("$refiが花屋で立っている"),
            w.plot_note("$maryは自分も彼女みたいに働いてみたいと思って、声をかけた"),
            w.plot_note("$refiは最近二号店を出した店主にかわって、市場の花屋を任されていた"),
            w.plot_note("それでも一人ではいろいろ不安で手伝いが欲しいと思っていて、$maryに手伝ってみないかと"),
            w.plot_note("$maryは手伝うことにする"),
            #
            w.plot_note("$wilsonのいるところに$limeが訪ねてくる"),
            w.plot_note("鎧騎士の姿だ。また城を抜け出してきたという"),
            w.plot_note("ときおり様子を見に来ていた"),
            w.plot_note("どうやら守衛のアルバイトを見つけて、一人暮らしをさせてもらっているらしい"),
            w.plot_note("不安視されていた王様の具合も落ち着いていて、いつでも戻れるようにしていると"),
            w.plot_note("また$adelの部下が様子見しているとも"),
            w.plot_note("$maryが花屋で働き始めたときき、喜ぶ$lime"),
            w.plot_note("一方で王室の方でも何人かやとって$sherlockの生存調査を行っているが音沙汰なしだった"),
            #
            w.plot_note("一週間ほど花屋で働いて、$maryも少し元気になりはじめた"),
            w.plot_note("$refiにお礼をいって、店を出る"),
            w.plot_note("街角で$cultXの信者が立って世界平和を訴えていた"),
            w.plot_note("$morianoが消えても彼の作ったものは消えていない"),
            w.plot_note("また最近女性を狙う猟奇殺人が頻繁に起こっていた。過去の$jack事件との関連性を疑っているとも"),
            w.plot_note("$patsonと出会う"),
            w.plot_note("今また$gunによる殺人事件を追っていると言っていた"),
            w.plot_note("以前のような軽薄さはなくなり、徐々に刑事が身についてきていた"),
            w.plot_note("みんな変わっていくのを感じていた"),
            #
            w.plot_note("$maryが花屋の仕事もだいぶ慣れて、やっと元通りの生活になってきたころ"),
            w.plot_note("$wilsonが興奮気味に戻ってくる"),
            w.plot_note("「聞いてくれ。$sherlockに似た男の目撃情報があった」と"),
            w.plot_note("ちょうどお茶を飲みに来ていた$limeと$maryは揃って驚きつつも「どこで？」と"),
            w.plot_note("$wilsonはある空き家に出没する、と言った"),
            w.plot_note("すぐにそこを見に行こうという話になり、出かける"),
            #
            w.plot_note("$wilsonの案内でスラム街の空き家にやってくる"),
            w.plot_note("空き家の中に誰かいる気配はなく、中に入って調べてみる"),
            w.plot_note("リビングにはテーブルがあり、本が一冊置かれていた"),
            w.plot_note("破れたソファに拾ってきた新聞が散らばっている"),
            w.plot_note("奥のキッチンのドアは立て付けが悪く、なんとか開けて入るとゴミがいっぱい"),
            w.plot_note("最近のものらしく、誰かがここで暮らしていると"),
            w.plot_note("夜に戻ってくるという話だったので、少し離れた空き家を使い、監視することにする"),
            w.plot_note("二階の部屋に陣取り、そこから監視する$maryたち"),
            w.plot_note("$wilsonは買い出しに行く"),
            w.plot_note("$maryと$limeは少し話す"),
            w.plot_note("$maryは$sherlockに会ったら謝りたいと言っていた。自分が迷わなかったら、もっとちゃんとしていたらこんなことにならなかったと"),
            w.plot_note("いつも迷惑をかけてばかりでごめんなさいと"),
            w.plot_note("$wilsonが戻ってきて、少し食べると仮眠を取った"),
            #
            w.plot_note("夜になり、人影が家に入る"),
            w.plot_note("そこに明かりが灯る"),
            w.plot_note("浮かび上がったシルエットはまぎれもなく$sherlockのそれだった"),
            outline=ABSTRACT)

