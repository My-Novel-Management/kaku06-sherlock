# -*- coding: utf-8 -*-
'''
Chapter "最後の事件"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from config import TITLES


# Episode
def the_fixer(w: World):
    return w.episode("事件の黒幕",
            w.plot_note("$sherlockは新聞を読んでいた"),
            w.plot_note("そこに殺人事件の調査依頼が持ち込まれる"),
            w.plot_note("最初は$maryも驚いていたが今では慣れたもので、依頼人を案内して、飲み物を出しながら依頼内容を話すよう促す"),
            w.plot_note("$maryは秘書気取りだった"),
            w.plot_note("だが$sherlockは依頼人が出した名前に驚く"),
            w.plot_note("それは$morianoの大学の後輩だったからだ"),
            w.plot_note("犯罪学の研究をしている人間が殺された"),
            w.plot_note("大学の研究室内での密室殺人。その手口が全く不明だが自殺ではないと警察は断定しているという"),
            w.plot_note("さっそくその調査に向かう$sherlock"),
            w.plot_note("$restradeと合流し、事件についての情報をもらう"),
            w.plot_note("現場にはＭの文字が書き残されていた"),
            )


def about_moriano(w: World):
    return w.episode("$morianoについて",
            w.plot_note("$sherlockは$morianoだと語る"),
            w.plot_note("$restradeですら耳にしたことがなかったその男のことを、$sherlockは友人のように仔細に話してみせる"),
            w.plot_note("$morianoは教育者の家庭に生まれた"),
            w.plot_note("幼い頃に神童とよばれ、あらゆる学問について素晴らしい成績を収めたが、彼が大学で興味を持ったのは人間そのものだった"),
            w.plot_note("大学時代に書いた論文は一本で、それは「人間と犯罪について」というものだ"),
            w.plot_note("統計手法を用いて実際にあった事件から犯人や被害者の心理、行動が細かく観察されている"),
            w.plot_note("今でも警察が犯罪心理学の基礎として流用しているものの多くがここから派生したもので、犯罪学の父と呼ばれる存在だと"),
            w.plot_note("しかしある時、急に大学をやめ、世間から遠ざかってしまった"),
            w.plot_note("個人の研究所を立ち上げて個人的な研究をしているという噂はあるが、研究成果を発表したりはしていない"),
            w.plot_note("その$morianoと連絡を取り合っていた形跡がある男が殺されたのだ、それも密室で、怪死した"),
            w.plot_note("$sherlockは全ての事件は$morianoにつながると言い切った"),
            )


def his_warning(w: World):
    return w.episode("$morianoの警告",
            w.plot_note("$sherlockが家に戻ってくるとそこには老人の姿があった", "$morianoだ"),
            w.plot_note("$morianoは「はじめまして」と挨拶をし、それから今$sherlockたちがどういう経路で戻ってきたかを言い当てる"),
            w.plot_note("$morianoは$sherlockに自分に関するすべてのことから手を引くようにと警告する"),
            w.plot_note("$sherlockは$morianoがここに来ることも推測して既に逮捕する準備を整えているとブラフを張るが、彼には通用しなかった"),
            w.plot_note("警察は別のところで起こった事件に駆けつけている"),
            w.plot_note("$morianoは言う。すべての人間は自分の意志ではなく、環境要因によって動かされると。つまり誰でもが犯罪者になりうると"),
            w.plot_note("$morianoは$maryに問いかける。彼女は$sherlockを好きだろうと"),
            w.plot_note("$morianoは$limeに本心では王室に帰りたいだろうと"),
            w.plot_note("$wilsonについての言及はとくないが、ここの人間には言えない本音を隠しているだろうと"),
            w.plot_note("$morianoは逃げないからいつでも自分の屋敷に来るがいいと言い残して、去っていく"),
            )


def lookfor_mary(w: World):
    return w.episode("$maryの捜索",
            w.plot_note("$morianoがきてから$maryの様子がおかしい"),
            w.plot_note("$sherlockは$morianoを何とか見つけ出そうと躍起になっている"),
            w.plot_note("$maryは$limeに相談することもできず、市場の$nowlisに愚痴る。自分だけが違う気がすると"),
            w.plot_note("$maryは市場からの帰り道、知らない男から手紙を渡される"),
            w.plot_note("手紙は$morianoから君の悩みの相談に乗ろうというものだった"),
            w.plot_note("$maryはその日、帰ってこなかった"),
            w.plot_note("すぐに$sherlockたちは$morianoの邸宅に向かう"),
            w.plot_note("$morianoの邸宅は火事になり、全てが消え去った"),
            w.plot_note("しかし後日、$morianoのメッセージが新聞に掲載される"),
            w.plot_note("$maryは無事で丁重に監禁していると。場所は$sherlockなら推理できると書かれて、ヒントが残されていた"),
            )


def rescue_mary(w: World):
    return w.episode("$mary救出劇",
            w.plot_note("$sherlockはヒントから$maryの居場所は$morianoと関係ない場所にいると推測する"),
            w.plot_note("$mary救出隊として少年探偵団の協力を仰ぐ"),
            w.plot_note("その間に$sherlockはその新聞記事からたどり、$morianoがどこからメッセージを出しているのかを調べる"),
            w.plot_note("$maryは爆弾が仕掛けられた部屋に閉じ込められていた"),
            w.plot_note("爆弾はダミーだった"),
            w.plot_note("部屋から出られなくなった$maryと$lime、探偵団たち"),
            w.plot_note("$sherlockの言葉を思い出して、$maryは脱出法を見つける"),
            w.plot_note("ダミーとして用意していた爆弾を使い、扉を爆破して何とか抜け出す$maryたち"),
            w.plot_note("$maryたちが戻ると、そこには$sherlockの姿がなかった"),
            )


def his_letter(w: World):
    return w.episode("$sherlockからの手紙",
            "$sherlockから少し前に書いたと思われる内容の手紙が届く",
            w.plot_note("$maryが目覚めるとそこに$sherlockの姿がいなかった"),
            w.plot_note("戻ってきた$wilsonは$sherlockの手がかりを追ったが見失ったと言う"),
            w.plot_note("$maryは$sherlockが戻ってくると信じて待っていたが、連絡も戻ってくることもなかった"),
            w.plot_note("一月が経ち、$maryたちは$sherlockのいない生活に馴染み始めていた"),
            w.plot_note("町では$morianoも$sherlockも消えたというのに犯罪は起こっていた"),
            w.plot_note("$wilsonは手を尽くして$sherlockを探す"),
            w.plot_note("$limeが王室のツテを使い、何とか情報を集めると言い出す"),
            w.plot_note("少年探偵団も手を尽くした"),
            w.plot_note("今まで世話になった人たちも$sherlockのことを探してくれた"),
            w.plot_note("それでも情報すら見つからない"),
            w.plot_note("雨の酷いある日、一通の郵便が届く"),
            w.plot_note("届いた手紙には宛名がなかったが$sherlock特有の署名が入っていた"),
            )


def sad_news(w: World):
    return w.episode("悲しいお知らせ",
            "$sherlockが穴に落ちてなくなったと知らせが届いた",
            w.plot_note("手紙の冒頭にはこう書かれていた"),
            w.plot_note("この手紙が届いたならば自分はすでにこの世界にいないだろうと$sherlockは書いていた"),
            w.plot_note("手紙は$morianoの隠れ家に向かう直前に書いて出したと書かれている"),
            w.plot_note("$morianoは用意周到で、約束通り一人で待っていたりはしない"),
            w.plot_note("$sherlockは陽動をして、手下たちを遠ざけて、可能ならば$morianoをおびき出す"),
            w.plot_note("どうにか一対一で話せる場所を作る、と書いてある"),
            w.plot_note("$morianoがどこまで語るか、告白するかわからないが、彼がやってきた悪事について書き残しておく"),
            w.plot_note("$morianoのことは以前教えたが、大学を出たあとの彼については今回独自調査を行うまで不明な部分が多かった"),
            w.plot_note("$morianoは$cultXと呼ばれる宗教団体との接触から犯罪者人生が始まる"),
            w.plot_note("彼はその教義である人間の本性である「悪」を反映させようとしていた"),
            w.plot_note("今までに解決した事件の裏側にはこの教団か、その教団の人間、関係者が細い糸で繋がっていた"),
            w.plot_note("その大本である$morianoを何としても打ち取ると宣言されていた"),
            w.plot_note("$maryたちは$sherlockがどうなったのか気になり、手紙を出した場所に向かおうとする"),
            w.plot_note("だが$wilsonによりそれは止められる"),
            w.plot_note("兄の$mikelがやってきて「$sherlockがなくなった」と告げた"),
            )


# Chapter
def main(w: World):
    return w.chapter(TITLES[6],
            w.plot_setup("$sherlockは全ての黒幕として$morianoに辿り着く"),
            w.plot_turnpoint("$morianoのメッセージ（暗号）が新聞に掲載される"),
            w.plot_develop("$sherlockが$morianoについて説明する"),
            w.plot_turnpoint("$morianoが現れる"),
            w.plot_develop("$morianoは$sherlockに全てから手を引くよう警告する"),
            w.plot_turnpoint("$maryが人質として連れ去られる"),
            w.plot_develop("$morianoの手がかりを見つけ出し、$maryの居所を見つける"),
            w.plot_turnpoint("$maryを助け出す"),
            w.plot_develop("$sherlockは$maryたちを騙して単身$morianoの隠れ家に向かった"),
            w.plot_turnpoint("$sherlockから手紙が届く"),
            w.plot_resolve("$sherlockからの最後の手紙で彼が$morianoと共に穴に落ちたことを知る"),
            the_fixer(w),
            about_moriano(w),
            his_warning(w),
            lookfor_mary(w),
            rescue_mary(w),
            his_letter(w),
            sad_news(w),
            )


