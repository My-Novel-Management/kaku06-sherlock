# -*- coding: utf-8 -*-
'''
Episode 4-2
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


# DEFINE
TITLE = "ガチョウクラブ"


# NOTE: outlines
ABSTRACT = """
$wilsonから$jackが容疑者として浮上していることを知らされ、$sherlockは$jackについての情報を探ってもらっている情報屋に確認を取る。
特に彼女が国内に戻ってきた情報はなく、最近は$jackによるものと見られる盗難事件もない為に$sherlockは何者かが彼女を利用していると考える。
一方、$maryは$ignesとともにガチョウクラブに潜入する。
会員制でガチョウを安く手に入れられるという表向きだったが、そこには$ignesも知るアンダーグラウンドの大物が出入りしていた。
目をつけられる$maryたちだったが、謎の女性により助けられる。
その女性からもうガチョウクラブには出入りしないように注意される。
一旦家に戻った$maryだったが、$sherlockが調べている事件の被害者がガチョウクラブの会員だと分かり、再度ガチョウクラブへの潜入を決意。
ガチョウクラブの男たちが$drag取引をしている現場を目撃した$maryは、逃げ出そうとして気づかれ、捕まってしまう。
"""


# Episode
def main(w: World):
    return w.episode(TITLE,
            # NOTE
            w.plot_setup("$maryはガチョウクラブの情報を仕入れて$sherlockに相談しようとする"),
            w.plot_turnpoint("$sherlockは$jackが国内に入っているという情報を得て、出ていってしまう"),
            w.plot_develop("$maryは$limeと$ignesに頼んでガチョウクラブについて潜入捜査を試みる"),
            w.plot_turnpoint("会員名簿の中に殺された$moura夫人の夫の名前を見つける"),
            w.plot_resolve("もらったガチョウから$dragを発見する"),
            w.plot_turnpoint("$maryは$dragと$gunの取引現場を目撃してしまう"),
            w.plot_note("$maryは肉の卸問屋$hornetにガチョウクラブが何か尋ねる"),
            w.plot_note("ガチョウクラブは会員制のガチョウ投資団体で、決まった月額でガチョウを飼育し、それを安く購入できるようにするもの"),
            w.plot_note("また販売した利益から何割かは戻ってきて、会員が増えるほど儲けも大きくなるという"),
            w.plot_note("最近よく取り扱っていると言われた"),
            w.plot_note("$maryはガチョウクラブの本部を教えてもらう"),
            w.plot_note("ただ当日仕入れたガチョウがどのガチョウだったのかはよく分からないと"),
            w.plot_note("ガチョウクラブからのものもあったが、他にもいくつかの農家から分けてもらったので"),
            w.plot_note("$maryはお礼を言ってガチョウクラブに向かうことにする"),
            #
            w.plot_note("$sherlockは単身、$moura夫人の家にやってきていた"),
            w.plot_note("そこには見張りで警官$parkerが立っていた"),
            w.plot_note("また鑑識$burnsが訪れていた"),
            w.plot_note("$sherlockは$burnsに色々言われつつも、彼から現場の状況を聞く"),
            w.plot_note("事件は帰宅した夫によって発見された"),
            w.plot_note("外交官で二週間も家を開けていたからいつ殺害されたかは不明"),
            w.plot_note("死体の状況から発見から三日程度だろうと推測される"),
            w.plot_note("ナイフ状のもので刺殺されていたが凶器は見つからず"),
            w.plot_note("夫人の評判はよく、恨まれていた線は薄いと"),
            w.plot_note("夫への敵対者はそれなりにいるかも知れないが、まだ何も情報がないとも"),
            w.plot_note("「で、どう思うんだ？」と$burns"),
            w.plot_note("$sherlockは部屋を密室にする必要はないし、もしガチョウから出てきたものが凶器だとしてもそこから犯人を特定できる特殊なものじゃない"),
            w.plot_note("衝動的な犯行で、無計画な人間のしたことの可能性が高いと"),
            w.plot_note("出入りの業者も疑っているが、アリバイは誰も灰色だと"),
            w.plot_note("何か新しい情報がわかったら教えて欲しいと言われて、承諾し、$sherlockは家を後にする"),
            w.plot_note("少し気になったのは寝室に血が少なかったこと"),
            w.plot_note("どこかで洗い流したのだろうか、と"),
            #
            w.plot_note("$maryはガチョウクラブにやってきていた"),
            w.plot_note("会員以外はお断り、という張り紙がされていて、中を覗けない"),
            w.plot_note("どうやって会員になればいいかも分からない"),
            w.plot_note("困っていたところに配達途中の$ignesが通りかかる"),
            w.plot_note("$ignesはあまり人が出入りしているのを見たことがないと言う"),
            w.plot_note("どこかから忍びこめないかと探す$ignes"),
            w.plot_note("と、裏口が開いていて、中に入れる"),
            w.plot_note("男たちの声が聞こえて、何か取引をしていた"),
            w.plot_note("こっそり覗くと、どうやら$gunと$dragの密売だった"),
            w.plot_note("$ignesは$maryにさっさと逃げた方がいいと言うが、物音がしてしまう"),
            w.plot_note("なんとか二人とも見つからずに逃げられたが、$ignesはもう近づかない方がいいと忠告する"),
            #
            w.plot_note("帰宅した$maryは$sherlockに相談しようか迷うが、$sherlockはその日は帰りが遅く、また帰ってきてからもすぐ研究室に閉じこもってしまった"),
            w.plot_note("$maryは仕方なく$limeにガチョウクラブのことを相談した"),
            w.plot_note("$limeは危険だからもう警察に任せて手を引いた方がいいと言う"),
            w.plot_note("$maryもその方がいいと思いつつも、もやもやしていた"),
            #
            w.plot_note("三日後、買い物から帰った$maryは家の前に袋がぶら下げてあるのを見つけた"),
            w.plot_note("そこにはガチョウが入っていた"),
            w.plot_note("$nowlisさんが届けてくれたのかと思うが、$limeも不在で、仕方なく自分で捌いてみる"),
            w.plot_note("すると中から$dragが出てきた"),
            w.plot_note("ガチョウクラブの人間に見られていたのだと分かって、$maryはすぐに家を出る"),
            w.plot_note("市場で$ignesを探すが見つからず、配管工の$raiderがいたので、声をかけて付いてきてもらうことに"),
            #
            w.plot_note("ガチョウクラブはちょうど開いていて、何かパーティの最中のようだった"),
            w.plot_note("$maryはあの時見た男を探す"),
            w.plot_note("男は$raiderの知人のようで、幹部だった"),
            w.plot_note("「ガチョウクラブに入りたかったのかい？　なら最初からそういえば紹介してあげたのに」と$raider"),
            w.plot_note("知らない間に入り口が閉められ、囲まれてしまっていた$mary"),
            w.plot_note("「これが欲しかったんじゃないのか？」と$dragを見せられる"),
            outline=ABSTRACT)

