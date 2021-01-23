# -*- coding: utf-8 -*-
'''
Episode 5-1
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


# DEFINE
TITLE = "第一の殺人"


# NOTE: outlines
ABSTRACT = """
船で島に渡る$sherlockたち。ガイド役として観光課職員の$mochが同行した。今回のイベントが観光目的だからだそうだ。
島では伝説の殺人があった雑木林に記念碑を建てていたが、その後も猟奇的な殺人事件が何度か起こり、かつて暮らしていた島民は全員外に逃げ出していた。
城では現在の城主$cherryが迎えてくれる。
既にパーティ参加者は集まっていて、それぞれ元刑事$hugar、社会学者$reui、心霊学者$karl、地元の歴史学者$jamos、新聞記者の$milkと癖のある人間が揃っていた。
他にパーティ用に臨時で雇った料理人$doldと使用人$bettyがいた。
イベントは明日行われるからと、前日はささやかな立食パーティが開かれた。
各自部屋があてがわれたが$sherlockたちは人数が多かったため、二人でひと部屋となった。
$maryと$limeはパーティ会場で食べながらそれぞれの参加者の話を苦笑しつつ聞いた。
一方$sherlockは城を興味深く歩いて見て回っていた。
しかし翌早朝、社会学者の$reuiが無残な姿で殺されているのが発見された。
"""


# Episode
def main(w: World):
    return w.episode(TITLE,
            # NOTE
            w.plot_setup("$sherlockの代役として$maryと$lime、$wilsonが行くことになり、島に向かう"),
            w.plot_turnpoint("案内の観光課職員$mochは$wilsonを$sherlockだと勘違いする"),
            w.plot_develop("城に到着するとそこでは元刑事$hugarや社会学者$reui、心霊学者$karlなどの癖の強い面々が待ち構えていて、やってきた$wilsonたちに持論を語る"),
            w.plot_turnpoint("$maryが犬の鳴き声を聞いた、と言った"),
            w.plot_resolve("翌日のパーティの余興として地元の歴史学者$jamosより魔獣伝説の講義があった"),
            w.plot_turnpoint("しかし翌朝、社会学者$reuiが遺体で発見された"),
            w.plot_note("城に到着した$maryたちは使用人$bettyにより、まずは個室に案内される"),
            w.plot_note("$wilsonだけ別室になり、$maryと$limeは同室となった"),
            w.plot_note("部屋はかなり古いもので、ベッドや家具だけ新しく入れたもの"),
            w.plot_note("荷物を置いて、$maryたちは$mochに案内されて談話室に向かう"),
            #
            w.plot_note("談話室では先に到着した面々が待っていた"),
            w.plot_note("まずは元刑事の$hugar。強面で$maryはびくびく"),
            w.plot_note("次に社会学者の$reui。最近よく雑誌に取り上げられている人気の女性学者"),
            w.plot_note("更に心霊学者$karl。やや病的だがその知識は他に追随を許さない"),
            w.plot_note("新聞記者の$milkもいて、新聞社ともタイアップしているという"),
            w.plot_note("$mochからは他にもいるが遅れていると"),
            w.plot_note("そこに部屋に遅れて入ってくる、地元の歴史学者$jamos。人の良さそうなおじさん"),
            w.plot_note("$bettyが案内に入ってくる"),
            w.plot_note("$betty以外にも料理人$doldがいると紹介された"),
            #
            w.plot_note("イベント前に歓談の席がもたれ、立食形式でホールに集まる"),
            w.plot_note("プレイベントとして心霊学者$karlによる魔獣についての講義、地元学者$jamosの伝説と島の歴史講義があった"),
            w.plot_note("$karlの講義を聞きながらも、$maryは$reuiと話す"),
            w.plot_note("彼女は社会学的立場から都市伝説について研究していた"),
            w.plot_note("$sherlockと似たようなことを言っていて、原型となった事件や事故があり、そこに人の様々な思いが歪んで集まることで都市伝説の形を取ると"),
            w.plot_note("$maryは自分の将来について考えたことがなかったが、$reuiを見て、こんなかっこいい女性になりたいと考える"),
            w.plot_note("一方$limeは$hugarに怪しまれていた"),
            w.plot_note("$wilsonが間に割って入り、なんとかごまかす"),
            w.plot_note("$wilsonを$sherlockとして勘違いしていて、そのまま$sherlockになりきらねばならず"),
            w.plot_note("$wilsonにも事件についての感想をイベントで求められると、$mochは説明した"),
            w.plot_note("$karlによる心霊講義が終わり、続いて$jamosの歴史学が始まった"),
            w.plot_note("それは記事に書かれてあったことも話したが、ほとんどは新鮮な話だった"),
            w.plot_note("かつてこの島は無人島だった"),
            w.plot_note("$bossがいた時代"),
            w.plot_note("ある魔族の者の住処となっていて、人間はそこで奴隷としてこき使われていた"),
            w.plot_note("$bossが討伐された後、その奴隷として扱われていた中でも幹部クラスだった男が領主となり"),
            w.plot_note("人間ではなく魔族や$ajinたちを奴隷として使い始めた"),
            w.plot_note("それが島の基本を形成していく"),
            w.plot_note("その圧政の構図が四百年続き、最初こそ人間に対しての扱いは奴隷とは異なっていたが、時折現れる暴君により、人間も奴隷化が進んだ"),
            w.plot_note("いくつかの集落に分け、仕事を割り振った"),
            w.plot_note("その仕事の種類により身分差が生まれた"),
            w.plot_note("第三十三代の領主が生まれた"),
            w.plot_note("領主は奴隷と称して集落から女、特に$ajinの娘を奪い、楽しむのが趣味だった"),
            w.plot_note("ある集落の娘は難攻不落と言われたこの砦を何とか逃げ出し、集落に戻ろうとした"),
            w.plot_note("だが領主は自分が飼っていた猟犬、それも魔獣と交配させて生み出したキメラを使い、娘を追わせた"),
            w.plot_note("娘はキメラに食い殺されたという"),
            w.plot_note("それから領主は娘をさらってきては逃げさせ、キメラに追わせるという遊びをやるようになった"),
            w.plot_note("ある娘の時だった"),
            w.plot_note("娘は領主に条件を出す。もし自分が逃げられたら二度と村の娘に手を出さないと"),
            w.plot_note("約束し、娘は夜、逃げ出す"),
            w.plot_note("娘には策があった"),
            w.plot_note("毎日猟犬の世話をし、少しずつ餌に島特有の花の粉を混ぜていたのだ"),
            w.plot_note("領主はいつもとおりに猟犬をけしかけた"),
            w.plot_note("だがこの日に着ていた領主のマントにはその花の臭いがつけられていた"),
            w.plot_note("猟犬は娘ではなく領主に襲いかかり、領主はキメラに食い殺されてしまった"),
            w.plot_note("そして、今度は娘が領主となり、そのキメラたちを買い始めた"),
            w.plot_note("娘により奴隷が解放された"),
            w.plot_note("だが娘は魔女と呼ばれ、忌避され、やがて島から人々は逃げ出してしまう"),
            w.plot_note("島に残された娘は、猟犬に食べさせることもできず、やがて自分も死んでしまい、その死体が猟犬に食われたという噂も"),
            w.plot_note("それ以降、島ではときおり犬の遠吠えが聴こえることがあるという"),
            w.plot_note("つい一月前にも殺人事件があった"),
            w.plot_note("そんな有様だから人は島には残っていない、現在の城主$cherry以外は"),
            #
            w.plot_note("話を聞いてしまい、眠れなくなる$mary"),
            w.plot_note("$limeがミルクをもらってきてあげると出ていく"),
            w.plot_note("部屋の外で待っていると$reuiが一人で夢遊病のように歩いていくのを見かけた"),
            w.plot_note("声をかけられず、黙って見過ごしてしまう"),
            w.plot_note("$limeが帰ってきてミルクを飲んで、なんとか眠ろうとする"),
            w.plot_note("どこかで犬の遠吠えが聞こえた、と言ったが$limeには聞こえなかった"),
            #
            w.plot_note("翌朝、$reuiが遺体となって発見された"),
            outline=ABSTRACT)

