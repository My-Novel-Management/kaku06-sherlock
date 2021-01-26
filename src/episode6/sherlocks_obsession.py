# -*- coding: utf-8 -*-
'''
Episode 6-4
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


# DEFINE
TITLE = "$sherlockの執念"


# NOTE: outlines
ABSTRACT = """
$maryが$morianoと一緒にいると知り、どうにかしないといけないと$sherlockに言う$limeだったが、$sherlockは何もしない。彼女の考えに任せればいいと言う。
$wilsonたちにも相談したが、$mary自身の考えはどうしようもないとだけ。
$sherlockは何かに夢中になり、頻繁に外出を繰り返し、頼りない状態だった。
そんな$limeに王室の執務官$mikelがやってきて、王室に戻るように言う。王の病気が悪化したというのだ。$limeは$maryを放っておいたままではいけないと悩む。
一方$sherlockは頼んでおいた毛髪鑑定により、人毛で$morianoと同一の血液型ということまで判明した。しかし決定的証拠にはならない。そこを騙ることでボロを出させようと、研究所に向かう。
だがそこで待ち構えていたのは$transformした$maryだった。$morianoは逃げ出したのだ。
$sherlockの説得むなしく、彼女により$sherlockは酷い傷を追う。それで正気に戻り、$maryは気絶した。
"""


# Episode
def main(w: World):
    return w.episode(TITLE,
            # NOTE
            w.plot_setup("家が燃えた$sherlockは$wilsonの家で世話になることにした"),
            w.plot_turnpoint("戻ってきた$limeから$maryが$morianoの助手になったと聞いた"),
            w.plot_develop("$sherlockは$morianoが危険だと語り、今まで以上に彼の証拠集めに必死になる。一方$limeは王室に戻るかどうかの決断を迫られていた"),
            w.plot_turnpoint("$sherlockは$morianoを追い詰める証拠を見つける"),
            w.plot_resolve("$moriano研究所を訪れる$sherlock。そこで彼を追い詰めようと手を打つが、$maryによって阻止される"),
            w.plot_turnpoint("$transformした$maryにより$sherlockは負傷し、$morianoを取り逃がしてしまう"),
            w.plot_note("$limeは目覚めるとここが知らない場所だと錯覚しそうになる"),
            w.plot_note("$wilsonの家だが、誰もいない"),
            w.plot_note("昨日戻ってから$sherlockはずっと自室に閉じこもり、$wilsonは用事があると出かけてしまった"),
            w.plot_note("$limeは$sherlockに買い物に行くとメッセージを書き残して、出かける"),
            w.plot_note("街の雰囲気が冬のフェスタで盛り上がっていた"),
            w.plot_note("$limeは王室にいた頃を思い出す"),
            w.plot_note("王室では父親がいつも盛大なイベントを行っていた"),
            w.plot_note("派手好きで、それは兄もそうで、結婚した後も女性関係の噂は絶えない"),
            w.plot_note("姉（第一王女）は病弱で、それでも政略結婚の道具として許嫁が決まっていた"),
            w.plot_note("なぜか父親は娘ではなく、$limeの方をより可愛がっていたふしがある"),
            w.plot_note("側室ですらない女に産ませた子なのに、と周囲で言われた"),
            w.plot_note("市場にやってくると、$adelがいた"),
            w.plot_note("$mikelの秘書をやっているということだけしか知らない。謎の多い女性"),
            w.plot_note("$adelは緊急に王室に戻るように言う。王が危篤状態だと"),
            w.plot_note("新聞にも掲載されていない"),
            w.plot_note("いろいろ試したが駄目で、死ぬ前に$limeと話したいという"),
            w.plot_note("$limeは迷ったが、行くことを決断する"),
            w.plot_note("$adelの$carに乗り込み、向かう"),
            #
            w.plot_note("$wilsonが家に戻ると、誰もいなくなっていた"),
            w.plot_note("そこに$sherlockの書き置きがあった"),
            w.plot_note("これから$morianoの別荘に向かう、と書かれていた"),
            w.plot_note("$sherlockは自分の死を覚悟していて、$morianoが何らかの方法で自分の命を奪うか、拘束するだろうと書かれていた"),
            w.plot_note("$morianoの別荘の場所も書かれ、帰らなかったら警察に届けてほしいとある"),
            w.plot_note("そこには$stein教授の殺害に$morianoが関与したという証拠がいくつか書かれていた"),
            w.plot_note("ただし現在の技術では$moriano本人であると確定するだけの強い証拠はなく、あくまで保険だと"),
            w.plot_note("そして、$sherlockはこれから起こるだろうことを予測し、そこに書いていた"),
            w.plot_note("$wilsonはその短い物語を読み始めた"),
            #
            w.plot_note("$sherlockはしっかり準備をし、駅に向かう"),
            w.plot_note("道中で$ignesたちに$maryのことを頼むと伝える"),
            w.plot_note("いつまでも$wilsonの家に世話にはなれないからと、$lisaにも家を世話してやってほしいと手紙を残しておいた"),
            w.plot_note("$trainで向かう"),
            w.plot_note("隣国だけに$sherlockの知人は全く使えない"),
            w.plot_note("山近くにある別荘は空気が綺麗だろう"),
            w.plot_note("小川も流れ、少し歩くと有名な滝もある"),
            w.plot_note("一人で別荘に到着した$sherlockを、助手$muranが出迎える"),
            w.plot_note("$morianoは全てを見抜いていたかのように、$sherlockを喜んで迎える"),
            w.plot_note("通された部屋にお茶を運んできたのは$maryだった"),
            w.plot_note("$maryは何も言わず、$sherlockのことを見ず、ただ人形のように立ち振る舞う"),
            w.plot_note("そこに$morianoがやってくる"),
            w.plot_note("$morianoは「ようこそ$sherlock君。お待ちしていたよ」と言うだろう"),
            w.plot_note("$morianoはいつか自分の考えが分かる時がくると言っていた"),
            w.plot_note("$sherlockを見て、すべて理解したことに喜びを覚えている"),
            w.plot_note("$morianoは問いかける。「私を手伝う気はないか」と"),
            w.plot_note("最初から$sherlockという才能を手に入れるのが狙いだった。自分の思想を具体化する手足が欲しいのだ"),
            w.plot_note("それは$morianoの唯一の欠点が肉体だからだ。彼は若い頃からすばらしかった。頭脳において"),
            w.plot_note("だがその頭脳を収めておく器が駄目だったのだ"),
            w.plot_note("いくつもの医者にかかっているが、そう長く生きられないという診断ばかりだった"),
            w.plot_note("見た目よりずっと若い"),
            w.plot_note("そういう病なのだと言われた"),
            w.plot_note("だからこそ、自分の思想を早く具体化したかった"),
            w.plot_note("その一番の肉体として$sherlockが選ばれた"),
            w.plot_note("頭脳だけを移す闇の技法もあったが、それについては$steinの研究は不足していた"),
            w.plot_note("$sherlockは$morianoに引導を渡すために現れたから、彼の申し出を当然断った"),
            w.plot_note("そのときの反応の候補は二つ"),
            w.plot_note("一つはその場で殺害してしまう"),
            w.plot_note("もう一つは$maryを人質として使う"),
            w.plot_note("だが現場では更に別の手段が準備されている"),
            w.plot_note("読めない第三の選択肢が何かは分からない"),
            w.plot_note("だがそれによって不覚を取り、傷つくだろうと推測されている"),
            w.plot_note("後日、この部分については補足があり、実際に何があったかは分かった"),
            w.plot_note("$maryを差し向けたのだ"),
            w.plot_note("$morianoの下で$maryはその能力をいかしてボディーガードならぬ暗殺者のスキルを手に入れていた"),
            w.plot_note("もともと$animalであり$transformした彼女は戦闘に長けていたのだ"),
            w.plot_note("$maryは$sherlockと対決する"),
            w.plot_note("これはずっと後に$maryから聞いた話だ"),
            w.plot_note("このときの$maryは常時薬物を使っていてただ$sherlockの気持ちを自分に向けることしか考えていなかった"),
            w.plot_note("$sherlockは「すまない」とだけ言った"),
            w.plot_note("$morianoのやることを阻止する必要があり、$maryののぞみは叶えられないと"),
            w.plot_note("$maryは$sherlockを殺して、自分の望む彼に生まれ変わらせようとする"),
            w.plot_note("だが$sherlockを追い詰め、傷つけてしまったところで$maryは我に返った"),
            w.plot_note("$sherlockはそのすきに$maryを気絶させ、逃げ出した$morianoを追う"),
            outline=ABSTRACT)

