# -*- coding: utf-8 -*-
'''
Chapter "魔獣"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from config import TITLES


## chapter
def main(w: World):
    return w.chapter(TITLES[5],
            "舞台は荒野ダートムア",
            w.plot_setup("その荒野では魔獣の伝説があった"),
            w.plot_setup("実際に魔獣の仕業と考えられる猟奇殺人が発生する"),
            w.plot_setup("$sherlockのところにその捜査依頼が舞い込む"),
            w.plot_turnpoint("だが別の用事があり$sherlockが行けないと言い出す"),
            w.plot_develop("$maryたちで事件調査に赴く"),
            w.plot_develop("その家は不遇な死が続いていた"),
            w.plot_develop("情報を集めていく中で本物の魔獣に襲われそうになる"),
            w.plot_turnpoint("$maryが魔獣に殺されそうになる"),
            w.plot_resolve("$sherlockがかけつけ、魔獣を追い払う"),
            w.plot_resolve("$maryたちが集めた情報をもとに$sherlockは事件の真相に至る"),
            w.plot_resolve("降霊術で魔獣を呼び出したが、それはただ愛犬を蘇らせたいという女の気持ちだった"),
            w.plot_resolve("魔獣に餌を与える必要があり、仕方なく伝説になぞらえて殺人させたのだ"),
            w.plot_resolve("魔獣は退治され、女は逮捕された"),
            w.plot_resolve("その女に降霊術（偽物）を教えたのはある宗教団体の人間だった"),
            "魔獣の伝説",
            w.plot_note("朝食をとっているところで、幽霊や怪奇現象についての話題が出る"),
            w.plot_note("$sherlockは不可思議な現象を信じない"),
            w.plot_note("かつていたとされている闇の世界の住人も、多くは現実にあったことが歪んで伝えられたのだと言ってのける"),
            w.plot_note("そこにドアがノックされ、男が現れる"),
            "調査依頼",
            w.plot_note("男は$Dartmourから来たといった"),
            w.plot_note("その土地では古くから巨大な犬の伝説があり、住民に恐れられていた"),
            w.plot_note("この半年ほどの間にペットの犬や猟犬が怪死するということが続いていて、半月前にはついに人間の被害者が出たらしい"),
            w.plot_note("現在は三人が被害者になり、引っ越して街を脱出する人間まで現れた"),
            w.plot_note("地元の観光協会は事態を大変重く見て、こうして問題解決のスペシャリストの$sherlockに依頼にきたという訳だ"),
            w.plot_note("$sherlockは魔獣の伝説は信じないが、実際に被害者が出ている事件だから捜査をしようと引き受ける"),
            "$Dartmour",
            w.plot_note("$trainで$Dartmourへと移動する"),
            w.plot_note("$maryたちは軽い旅行気分"),
            w.plot_note("$sherlockはその間に起こっている事件の資料と地域の情報を頭に入れておく"),
            w.plot_note("昔に荘園主が建てた邸宅があり、そこの主が恋をした娘を監禁した"),
            w.plot_note("しかし娘は逃げ出した"),
            w.plot_note("その娘を追わせるために飼っていた犬を放った"),
            w.plot_note("娘を食い殺した犬は、しかし、その飼い主である主をも食い殺してしまったのだ"),
            w.plot_note("猟銃すらきかず、野に放たれた魔獣は今でもこの荒野のどこかをうろついては、家に関わるものを呪い殺そうとしていると言われている"),
            w.plot_note("虫けらのように猟犬を扱っていた主への怨念だとも言われているし、こきつかわれた猟師や小作人、使用人たちが殺したんだとも"),
            "観光協会",
            w.plot_note("駅に到着すると迎えに来ていた観光協会の人間について、まずは事務所に向かう"),
            w.plot_note("観光協会の地図を見ながら、事件のあった場所や、その血筋の生き残りの女性が一人で暮らす家の場所を教わる"),
            w.plot_note("魔獣の伝説のせいで浮いているその女性$cherryの家に向かう$sherlock"),
            "$ln_cherry家の呪い",
            w.plot_note("家は沼地を超えた先にあった"),
            w.plot_note("家を訪れると未亡人となった婦人が出迎えてくれた"),
            w.plot_note("家には彼女以外誰もいないらしい"),
            w.plot_note("魔獣の伝説があるが恐くないのか、と尋ねると生まれる前からずっとそうだったと"),
            w.plot_note("どことなく上の空な雰囲気"),
            w.plot_note("一旦家をあとにする"),
            "宗教団体",
            w.plot_note(""),
            )


