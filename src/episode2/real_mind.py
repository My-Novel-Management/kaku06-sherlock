# -*- coding: utf-8 -*-
'''
Episode 2-5: "本当の気持ち"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


# DEFINE
TITLE = "本当の気持ち"


# NOTE: outlines
ABSTRACT = """
殺人を計画したのは$kailだった。学校時代から憧れの女性で、ずっと彼女に思いを寄せていた$kailは、彼女の悩みのよき相談相手だった。
彼女が結婚してからも、ここで使用人としていることで彼女の助けになった。
$roydが病気でそう長くないことを知らされ、今回の殺人を思いついた。
$jeanには口裏をあわせてもらっただけで、あとで殺すつもりだったと語る。
だがそれが$jeanをかばっていることは明らかだった。
$kailは剥きになり、$jeanを殺そうとする。
その時$maryが$transformし、$jeanを守った。だが$jeanはそれでも$maryを愛しているとは言えなかった。
こうして事件が終わった。
後日$keanからの手紙で$maryが遺産相続を放棄し、邸宅も地元に寄付することになったと教わる。
$maryは遠くの親戚に預けられるそうだが、$keanは父親と$jeanの戻る場所を守るために邸宅の管理をしつつバラ園を整備するという。
そこに$maryが大きな荷物を持ってやってくる。
$maryは$sherlockの家で暮らすと言った。
"""


# Episode
def main(w: World):
    return w.episode(TITLE,
            # NOTE
            w.plot_setup("$transformした$maryを$kailが$gunで殺そうとする"),
            w.plot_turnpoint("しかし$jeanによりそれが阻止される"),
            w.plot_develop("実行犯は$kailだった。$jeanも加担したが心の底からは賛成していなかった。逃げ出した$kailが逮捕され、事件は解決に向かう"),
            w.plot_turnpoint("$jeanは$maryに対して「愛せなくてごめん」と謝罪した"),
            w.plot_resolve("遺産相続を放棄した$maryは荷物を持って$sherlockの家に押しかけた"),
            w.plot_note("$maryが$patsonにより連れてこられた"),
            w.plot_note("$sherlockが$restrade経由で事情を話して連れてきてもらったものだ"),
            w.plot_note("$patsonは不服そう"),
            w.plot_note("$maryは「今の話、本当なの？」と"),
            w.plot_note("$jeanが何か言う前に$kailにより訂正される。「それはこの男が勝手に作った妄想だ」と"),
            w.plot_note("$maryは「そうじゃない」と言う"),
            w.plot_note("$maryは自分があの日、何を話されたのか、それを語る"),
            w.plot_note("呼び出されて向かったのはバラ園の小屋"),
            w.plot_note("そこで$royd氏からバラ園に明かりを灯して花を育てる研究をしていると教わる"),
            w.plot_note("$roydは自分には子供がいない、と語る"),
            w.plot_note("$maryは$animalであり、更に拾った子供だと語った"),
            w.plot_note("実の娘ではないことは$animalであることから明白だった"),
            w.plot_note("$jeanも$animalではない"),
            w.plot_note("ただ小さい時期は$animalとしての特徴や力が不安定で発現しないことも多い"),
            w.plot_note("その上で$maryを守るために学校に行かせなかったがそれが良かったどうか分からないと"),
            w.plot_note("そして自分の命が長くないことを伝えて、こう告げた"),
            w.plot_note("「自分が亡くなったら$jeanはお前のことを捨てるかも知れない」と"),
            w.plot_note("だからその時のために弁護士に身元引受人を委託しておいた、と"),
            w.plot_note("ただそれでもどういう人生を歩んでいくかは、自分で決めることだと"),
            w.plot_note("できれば自分が死ぬ前に家を出ていって社会勉強をしてきてほしいと"),
            w.plot_note("その為に支援は惜しまないとも"),
            w.plot_note("$maryは最初それを家から追い出したいんだと思ってショックだった"),
            w.plot_note("でも警察で$animalとばれて、初めて人間が$animalに対してどういう見方をしているのか分かった、と"),
            w.plot_note("母親がいつまでも自分を避けていたのもそれが原因だったんだと"),
            w.plot_note("「違う」と$jeanは言う"),
            w.plot_note("$jeanは$maryが$animalだから避けていた訳じゃない。「昔の自分に似てたから嫌いなのよ」と"),
            w.plot_note("引っ込み思案で人を見る時に様子を伺うように見上げる"),
            w.plot_note("自分では何もできないのに、ただ弱者として守られて援護されて、自分は何もしなくても誰かによって助けられて生きてきた"),
            w.plot_note("運がいいだけで、自分で何かを掴もうとしない"),
            w.plot_note("それが嫌で$jeanは学校を出たら家を出て一人で生きていこうとしていた"),
            w.plot_note("でも結局色々な人に助けられ、$royd氏に見初められて結婚した"),
            w.plot_note("玉の輿だと喜んだが、一方ではまた自分は何もしていないことにどこか悔しさがあった"),
            w.plot_note("事業に手を出して失敗したのも、それだ"),
            w.plot_note("結局何もしなくなった"),
            w.plot_note("もともと$royd氏は体調がよくなかった"),
            w.plot_note("食事に混ぜていたのは薬で、$royd氏は薬を飲みたがらなかったから"),
            w.plot_note("確かにあの日、$maryをつけていった"),
            w.plot_note("そこで小屋の外だが話も聞いた"),
            w.plot_note("その後、遺産のことを問い詰めた"),
            w.plot_note("遺産はちゃんと二人に充分残すと言っていたけれど、自分が死んだ後には$maryの面倒を見て欲しいとも頼まれた"),
            w.plot_note("でも聞きたかったのは$maryではなく、自分のことだ"),
            w.plot_note("何故自分を選んだのか。結婚したのか。若くて綺麗な娘だったからか"),
            w.plot_note("$royd氏は「罪を償うためだ」と言った"),
            w.plot_note("実は$jeanたちの暮らしていた集落は、$enagy鉱山を見つけた余波で、川が毒に汚染されてしまった"),
            w.plot_note("けれど街のためだと無視して採掘を続けたのだ"),
            w.plot_note("$royd氏はその罪償いだと"),
            w.plot_note("愛はなかった。それが一番悲しかった"),
            w.plot_note("その歪んだ思いで$gunを打った"),
            w.plot_note("逃げ出した"),
            w.plot_note("その後のことは知らない。$gunは途中で捨てたはずだった"),
            w.plot_note("それが$maryの部屋で見つかり、だったらあの子も一緒に捨ててやろうと"),
            w.plot_note("そこまでの告白を終えた$jeanは逮捕を覚悟していた"),
            w.plot_note("だが「嘘はやめろ」と$kail"),
            w.plot_note("$kailはナイフを手に、$jeanを人質に取る"),
            w.plot_note("その指の模様が出るあれで分かってるんだろう？　その$gunに俺のがついてるって"),
            w.plot_note("真犯人は$kailだった"),
            w.plot_note("「ずっと$jeanさんを守っていたんですね、あなたが」と$sherlock"),
            w.plot_note("「違うさ。ただ遺産がほしかっただけだ。事件のことでこいつを脅して遺産をもらうつもりだった」と"),
            w.plot_note("$kailは$jeanを殺そうとする"),
            w.plot_note("その時$maryが$transformし、襲いかかり、$jeanを助ける"),
            w.plot_note("警察により$kailが捕らえられ、事件は終わった"),
            w.plot_note("$jeanは変身した$maryを見て「やっぱり愛せない」と言った"),
            #
            w.plot_note("後日、$milkから事件についてまとめた記事と感謝の手紙がきた"),
            w.plot_note("それによれば$kailと$jeanが共謀していたことを二人とも認めて、裁判はそっちの方向で行われると"),
            w.plot_note("遺産相続は大部分を$maryに残すよう書かれていたが、$maryは権利を放棄し、ほぼ全額を基金に寄付したと"),
            w.plot_note("後見人の$conery氏の知人のところで暮らすらしい"),
            w.plot_note("$keanは父の帰りを待ちつつ、地元に寄付された邸宅の管理とバラ園の世話をするらしい"),
            w.plot_note("そこに訪問客がある"),
            w.plot_note("ドアを開けると大きな荷物を抱えた小さな少女、$maryの姿があった"),
            w.plot_note("「今日からここでお世話になります」と"),
            w.plot_note("理由を聞くと「社会見学をするため」と"),
            w.plot_note("断ろうとした$sherlockだったが、掃除を始めた$maryに対して出ていけとも言えなくなった"),
            outline=ABSTRACT)

