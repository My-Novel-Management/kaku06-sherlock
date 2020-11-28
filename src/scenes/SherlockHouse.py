# -*- coding: utf-8 -*-
'''
Stage: "シャーロックの家"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


# NOTE
#   物語が展開する中心。事務所
#   シャーロックが借りて住んでいる古い一軒家（二階建て）で、B221という看板が近くにある
#   幽霊が出るといういわくつきの物件で安かった。原因は地場発生の魔石があっただけ
#   ：２F
#   [物置][空き部屋]
#   [寝室１][寝室２]
#   ：１F
#   [キッチン][バス]
#   [ダイニング][トイレ]
#   [研究室]
#   [リビング][書斎]


## scenes
def about_sherlock(w: World):
    return w.scene("$sherlockという男について",
            w.plot_note("知っていたならなぜ忠告してくれなかったんだ、と$wilsonが$sherlockに文句をいい、なんとか家に入れてもらえる"),
            w.plot_note("中に入るとそこら中に本や資料がちらばっていた"),
            w.plot_note("$wilsonはそこで依頼をしようと思ったが、"),
            w.plot_note("そこに何も記載のない手紙が投げ込まれた"),
            )


def read_prince_letter(w: World):
    return w.scene("皇太子の書簡の中身",
            w.plot_note("手紙には独特の紙が使われていて、それが王室のものだと$sherlockは分かった"),
            w.plot_note("中は皇太子からの手紙で、$sherlockに頼みごとが書かれていた"),
            w.plot_note("皇太子は女遊びがひどくてその界隈では有名だが、今回ついに腰を落ち着けて結婚することになった"),
            w.plot_note("相手は近隣の公国の王女で、政治的な意味合いも大きい"),
            w.plot_note("その結婚に際して過去の女性関係をすべて綺麗にした"),
            w.plot_note("ただある一人の女性にプレゼントしてしまった大切なナイフを返してもらいたいが、相手の女性が応じてくれない"),
            w.plot_note("揉め事をおこしたくないので、穏便にすませたいから、$sherlockに彼女を説得して、ナイフを返してもらってくれないか、という依頼"),
            w.plot_note("$sherlockはその依頼内容について、書かれていない部分の推測を述べる"),
            w.plot_note("ナイフと書いているが、実際は王室に伝わる宝剣で、それが王の証の一つで、結婚の際には儀式内で使われる"),
            w.plot_note("酒の勢いで大切な宝剣をあげてしまったのだろうと"),
            w.plot_note("そんなものを取り戻す義理はないが、恩があるので仕方なく依頼を受けると言った"),
            w.plot_note("$sherlockは$wilsonにその女性の家まで送ってほしいと頼んだ"),
            )


def important_than_sword(w: World):
    return w.scene("宝剣より大事なこと",
            w.plot_note("$sherlockは宝剣よりも殺人事件についての調査をしたいと、$wilsonを家に置いて出ていってしまう"),
            w.plot_note("$wilsonは$sherlockの家に戻り、そこで彼を待つことにする"),
            w.plot_note("やってきた若い刑事は$sherlockがいないことに落胆しつつも、状況を教えてくれる"),
            w.plot_note("発見された遺体は一月ほど前に行方不明になった女性だった"),
            w.plot_note("$ailyとは何の関係もなく、そこの接点も見つけられないと嘆く"),
            w.plot_note("殺害方法も不明で、凶器すら見つけられないと"),
            w.plot_note("そこに役所の男から$ailyという女性が住民登録をしたという形跡は見つけられなかったと連絡がきた"),
            )


def housemate_mary(w: World):
    return w.scene("同居人$mary",
            w.plot_note("同居するようになった$maryはやたらと$sherlockにまとわりつく"),
            w.plot_note("$sherlockは大好きな読書もできず、困っていた"),
            )


def mary_has_worry(w: World):
    return w.scene("$maryの悩み",
            w.plot_note("$maryは彼の迷惑になりたくなくて、$wilsonに相談する"),
            w.plot_note("女手が不足しているから自分が役立つところをアピールしてみたら、と助言を受ける"),
            w.plot_note("$maryは掃除や買い物を買って出る"),
            )


def about_missings(w: World):
    return w.scene("失踪者について",
            w.plot_note("やっと外に出てくれてほっとした$sherlockは$wilsonに事件について相談する"),
            w.plot_note("最近謎の失踪者が増えていた"),
            w.plot_note("失踪事件として新聞や雑誌も特集を組んでいる"),
            w.plot_note("$wilsonはその調査を$sherlockに依頼していたが、未だに何も情報がなかった"),
            )


def strange_armor_knight(w: World):
    return w.scene("奇妙な鎧騎士",
            w.plot_note("そこに$maryが見知らぬ人を連れて戻ってくる"),
            w.plot_note("道端で困っていたから拾ったけれど言葉がしゃべれないのだと$maryは説明した"),
            )


def strange_work(w: World):
    return w.scene("奇妙な仕事",
            w.plot_note("その鎧騎士は$sherlockに$limeと名乗った（筆談で）"),
            w.plot_note("彼女は今ある老夫婦の家に居候しているが、彼らの知人の質屋の護衛のアルバイトをしていた"),
            w.plot_note("守衛仲間の$binsと交代しながら閉店時刻まで警備をしている"),
            w.plot_note("その$binsから別のバイトを紹介され、今は途中にそちらもやっている"),
            w.plot_note("その別のバイトが相談したいことだった"),
            w.plot_note("最初に$binsからチラシを見せてもらったときには「赤い鎧の者だけがバイト資格がある」と書かれていた"),
            w.plot_note("仕事内容はじっと座ってある本の写しを作る作業を三時間行うだけで、週給で結構な金額がもらえた"),
            w.plot_note("実際に面接に行ってみると確かに赤い鎧を来た人間が集まっていたが、$limeみたいに見事に全身赤という者はいなかった"),
            w.plot_note("主催者である赤鎧クラブは彼女を合格とし、その翌日から守衛を抜け出して三時間、そのアルバイトをしているらしい"),
            w.plot_note("オーナー夫婦には申し訳なく感じているが、そのお金でプレゼントしたいと思っているのだと説明する"),
            w.plot_note("その話をきいて$sherlockは彼女に今すぐそのアルバイトを辞めるようにとだけ言った"),
            )


def reason_for_lime_work(w: World):
    return w.scene("$sherlockの忠告",
            w.plot_note("家に帰った$maryはどうしてあんな風に言ったのか$sherlockに問いただす"),
            w.plot_note("$sherlockはそんなにうまい話は存在しないし、自分が知る限り「赤鎧クラブ」なんてものは存在しないと断言する"),
            w.plot_note("$maryは実際に持ち帰ったチラシを見せながら、彼女を拾ってくれたオーナーさんや同僚の$binsの優しさを力説する"),
            w.plot_note("しかし後日$sherlockの言っていたように問題が発生する"),
            w.plot_note("その近所にあった改装中の銀行が強盗に襲われた"),
            w.plot_note("警備員が気づいて連絡したが、表からも裏からも誰も入ってはおらず、謎の強盗と話題になっていた"),
            w.plot_note("しかし現地を調べたところ、抜け穴が掘ってあり、大量のダイヤと金塊が盗まれたあとだった"),
            w.plot_note("しかもその抜け穴は質屋に繋がっていたのだ"),
            w.plot_note("その質屋のオーナー夫婦も逮捕され、$limeも容疑者の一人として逮捕された"),
            )


def help_lime_please(w: World):
    return w.scene("$limeを助けて",
            w.plot_note("$maryが$limeを助けてやってほしいと$sherlockに言う"),
            w.plot_note("$sherlockは自分の忠告を聞かなかったからだと言うが、それでも話だけは聞くと言う"),
            w.plot_note("質屋につながっていた抜け穴の中で、重要参考人だった$ignesが遺体で発見された"),
            w.plot_note("その容疑者として$limeが逮捕され、オーナー夫婦も事情聴取を受けている最中らしい"),
            w.plot_note("強盗の件についても調査中で、全部彼女に押し付けられるかもしれないと言い出す"),
            w.plot_note("$sherlockはその質屋に案内してもらう"),
            )


def limes_talk_of_strange_case(w: World):
    return w.scene("奇妙な事件についての$limeの話",
            w.plot_note("$maryが$limeを拾い、再び家へと連れてくる"),
            w.plot_note("$sherlockは銀行から盗まれたものがダイヤだけじゃないと睨むが、教えてもらえなかった"),
            w.plot_note("家に戻ってくると$sherlockはそこに$limeがいることに頭を抱える"),
            w.plot_note("$limeがしゃべれないのは呪いの鎧のせいだと言う"),
            w.plot_note("その呪いをといてもらおうと、知人の神官を読んでいた"),
            w.plot_note("呪いを解いたが$limeはしゃべれないままだった"),
            w.plot_note("その$limeは筆談で自分が王室の人間であると告白する"),
            )


def lime_was_royal_family(w: World):
    return w.scene("$limeは王家の人間",
            w.plot_note("$limeは自分が誘拐された訳ではなく、普通に家出をしたのだと告白する"),
            w.plot_note("王室はそんな品の悪い発表をできないから失踪事件にして公表したのだと言った"),
            w.plot_note("もともと妾の子で、周囲から浮いていて、王室にも自分の居場所がなく帰りたくないと泣く"),
            )


def newcommer_lime(w: World):
    return w.scene("新しい同居人$lime",
            w.plot_note("$maryは$sherlockに$limeを一緒に住まわせてほしいとお願いする"),
            w.plot_note("$sherlockは金銭的な問題さえ解決できればと提案する"),
            w.plot_note("$wilsonは金のことなら大丈夫だと、なぜか大金を手にして言う"),
            w.plot_note("$wilsonは$sherlockの秘蔵コレクションを売り払っていた"),
            w.plot_note("こうして新しい住人$limeをここに加えることになった"),
            )


def cooker_lime(w: World):
    return w.scene("料理人$lime",
            w.plot_note("$limeは料理担当になっていて、そのガチョウをもらってさばいてくれる"),
            )


def marys_market_talk(w: World):
    return w.scene("$maryの市場の話",
            w.plot_note("$maryは市場で仕入れた面白い話を$sherlockに話す"),
            w.plot_note("今市場ではガチョウからダイヤが出てくると話題になっていた"),
            w.plot_note("$limeがやってきて、何か出たという"),
            w.plot_note("ガチョウの中から出てきたのは血がついたナイフだった"),
            )


def knife_in_the_goose(w: World):
    return w.scene("ガチョウの中の凶器",
            w.plot_note("$sherlockはそれがなにかの事件の凶器だと分かり、すぐに警察に連絡を取る"),
            w.plot_note("$restradeがやってきて、それは現在彼が追っている事件の重要な証拠品だと言われた"),
            )


def restrade_talk_about_goose_knife(w: World):
    return w.scene("$restradeのガチョウの凶器事件の話",
            w.plot_note("$restradeからその事件についての概要を聞く"),
            w.plot_note("事件はある一軒家で起こった"),
            w.plot_note("引退した学者が謎の死を遂げた"),
            w.plot_note("刺殺だったのだが凶器が発見されず、犯人も特定されないまま現在に至る"),
            w.plot_note("そのナイフを警部に渡して調べてもらう"),
            w.plot_note("その間に興味をもった$sherlockは一人でその現場を調べに出ていってしまう"),
            w.plot_note("後日、そのナイフからずっと失踪中の$jackの指紋が検出された"),
            )


def backhome_mary_with_jack_wanted(w: World):
    return w.scene("$jack容疑者の話を持って返ってきた$mary",
            w.plot_note("戻ってきた$sherlockは$maryからそのことを聞き、"),
            w.plot_note("$sherlockは現場を見てきたことを$maryたちに話す"),
            )


def talk_about_goose_case(w: World):
    return w.scene("ガチョウ凶器事件についての調査",
            w.plot_note("現場は住宅街から少し離れた郊外の一軒家で、男は民間の研究所をやめたあとも個人的に何かを研究していた"),
            w.plot_note("歴史学と民俗学に造形が深く、$sherlockもその所蔵していた資料に関心をしたくらい"),
            w.plot_note("彼が書き残しているものの一つに古代の技法がいくつか紹介されていた"),
            w.plot_note("刺された場所は彼の家だが、凶器は消えている"),
            w.plot_note("ただし$jackとの関係性は全く見えず、彼女ならそんな手段を使わないと$sherlockは考えた"),
            w.plot_note("$sherlockは誰かが$jackを表舞台に引っ張り出したい、その罠だと考える"),
            )


def jacks_letter(w: World):
    return w.scene("$jackからの手紙",
            w.plot_note("と、差出人不明の手紙に$jackからのメッセージがあった"),
            w.plot_note("助けてほしいと"),
            )


def sherlocks_message_for_jack(w: World):
    return w.scene("$sherlockのメッセージ",
            w.plot_note("そこに$sherlockからの伝言を$ignesが持ってくる"),
            w.plot_note("数日留守にすることと、$jackに会いに行ってくると書かれていた"),
            )
