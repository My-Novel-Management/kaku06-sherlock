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


def mysterious_case(w :World):
    return w.scene("怪奇事件",
            w.plot_note("$sherlockは怪奇事件の特集記事を読みながら「こんなものは実在しない」と言う"),
            w.plot_note("そもそも奇妙な現象、霊的なもの、不思議なものは人間が理解することを放棄していると説明する"),
            w.plot_note("小さい頃、学校内で七不思議というものがあったが、それを全て解明したらみんなから怒られたと"),
            )


def legend_of_dark_dog(w: World):
    return w.scene("魔獣伝説",
            w.plot_note("そこに$wilsonがこんな話がある、と、ある孤島に伝わる魔獣伝説を話した"),
            w.plot_note("そこはこの三年の間に六名もの犠牲者が出ているという"),
            w.plot_note("最初は飼い犬や家畜が殺されているだけだった"),
            w.plot_note("しかし最初に人の犠牲者が出た"),
            w.plot_note("それはどう見ても人の手によるものではなく、何か獣による被害だった"),
            w.plot_note("最初の事件から次の事件まではかなり時間が開いたが、直近はこの三ヶ月の間に二件も殺人事件が起こっている"),
            w.plot_note("$sherlockはそれだけ続くなら必ず人の手が関わっていると断言する"),
            )


def invitation_from_dark_island(w: World):
    return w.scene("孤島からの招待状",
            w.plot_note("そこに招待状が届く"),
            w.plot_note("$wilsonはそれを開封し、噂をしていれば、とその伝説の孤島に暮らす城主からの招待状だと言った"),
            )


def commision_of_murder_case(w: World):
    return w.scene("殺人事件の解決依頼",
            w.plot_note("$sherlockは新聞を読んでいた"),
            w.plot_note("そこに殺人事件の調査依頼が持ち込まれる"),
            w.plot_note("最初は$maryも驚いていたが今では慣れたもので、依頼人を案内して、飲み物を出しながら依頼内容を話すよう促す"),
            w.plot_note("$maryは秘書気取りだった"),
            w.plot_note("だが$sherlockは依頼人が出した名前に驚く"),
            w.plot_note("それは$morianoの大学の後輩だったからだ"),
            w.plot_note("犯罪学の研究をしている人間が殺された"),
            w.plot_note("大学の研究室内での密室殺人。その手口が全く不明だが自殺ではないと警察は断定しているという"),
            w.plot_note("さっそくその調査に向かう$sherlock"),
            )


def moriano_is_here(w: World):
    return w.scene("$moriano見参",
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


def marys_strange(w: World):
    return w.scene("奇妙な$mary",
            w.plot_note("$morianoがきてから$maryの様子がおかしい"),
            w.plot_note("$sherlockは$morianoを何とか見つけ出そうと躍起になっている"),
            w.plot_note("$maryは$limeに相談することもできず、市場の$nowlisに愚痴る。自分だけが違う気がすると"),
            )


def where_is_mary(w: World):
    return w.scene("$maryはどこへ？",
            w.plot_note("すぐに$sherlockたちは$morianoの邸宅に向かう"),
            )


def alive_moriano(w: World):
    return w.scene("$morianoは生きている",
            w.plot_note("しかし後日、$morianoのメッセージが新聞に掲載される"),
            w.plot_note("$maryは無事で丁重に監禁していると。場所は$sherlockなら推理できると書かれて、ヒントが残されていた"),
            )


def morianos_whereabouts(w: World):
    return w.scene("$morianoの居場所",
            w.plot_note("$sherlockはヒントから$maryの居場所は$morianoと関係ない場所にいると推測する"),
            w.plot_note("$mary救出隊として少年探偵団の協力を仰ぐ"),
            w.plot_note("その間に$sherlockはその新聞記事からたどり、$morianoがどこからメッセージを出しているのかを調べる"),
            )


def vanished_sherlock(w: World):
    return w.scene("消えた$sherlock",
            w.plot_note("$maryたちが戻ると、そこには$sherlockの姿がなかった"),
            )


def sherlocks_information(w: World):
    return w.scene("$sherlockに関する情報",
            w.plot_note("$maryが目覚めるとそこに$sherlockの姿がいなかった"),
            w.plot_note("戻ってきた$wilsonは$sherlockの手がかりを追ったが見失ったと言う"),
            w.plot_note("$maryは$sherlockが戻ってくると信じて待っていたが、連絡も戻ってくることもなかった"),
            )


def no_sherlock_life(w: World):
    return w.scene("$sherlock不在の生活",
            "同・寝室",
            w.plot_note("一月が経ち、$maryたちは$sherlockのいない生活に馴染み始めていた"),
            )


def serching_sherlock(w: World):
    return w.scene("$sherlockの捜索隊",
            w.plot_note("町では$morianoも$sherlockも消えたというのに犯罪は起こっていた"),
            w.plot_note("$wilsonは手を尽くして$sherlockを探す"),
            w.plot_note("$limeが王室のツテを使い、何とか情報を集めると言い出す"),
            w.plot_note("少年探偵団も手を尽くした"),
            w.plot_note("今まで世話になった人たちも$sherlockのことを探してくれた"),
            w.plot_note("それでも情報すら見つからない"),
            )


def arrived_his_message(w: World):
    return w.scene("$sherlockからのメッセージ",
            w.plot_note("雨の酷いある日、一通の郵便が届く"),
            w.plot_note("届いた手紙には宛名がなかったが$sherlock特有の署名が入っていた"),
            )


def sadness_report(w: World):
    return w.scene("悲しいお知らせ",
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


def believed_his_alive(w: World):
    return w.scene("$sherlockの生存を信じて",
            w.plot_note("$maryたちは$sherlockが生きていると思って捜索を続けていた"),
            w.plot_note("しかし何の情報もなく、ただ時間だけが過ぎていく"),
            w.plot_note("家を失い、$wilsonの住まいに居候していた$maryたち"),
            w.plot_note("$wilsonは忙しそうに外に出ていることが増えた"),
            w.plot_note("$maryは$sherlockの手紙にヒントはないかと考えるが、何も見つからない"),
            )


def news_of_sherlock_alive(w: World):
    return w.scene("$sherlock生存情報",
            w.plot_note("だが$limeはそこに$sherlockが生きているという証拠を見つけた"),
            w.plot_note("そこに$wilsonが戻ってくる"),
            w.plot_note("$wilsonは「$sherlockに似た人間を見かけた」という情報を聞いたと話した"),
            )


def consideration_of_sherlock(w: World):
    return w.scene("容疑者$sherlockについての考察",
            w.plot_note("一旦家に戻り、犯人にされてしまった$sherlockについて考える"),
            w.plot_note("$wilsonは$sherlockが$moriano一味に騙されたというのだが"),
            w.plot_note("もう一度あの空き家を訪れる"),
            )


def injured_wilson(w: World):
    return w.scene("負傷した$wilson",
            w.plot_note("家に戻ると$wilsonがいて、ひどい怪我を負っていたが、無事に逃げ出したと言う"),
            w.plot_note("$maryは自分たちを助けた男が$sherlockの生存を言っていたと伝える"),
            w.plot_note("$wilsonはそのホームレスのことを教えてくれと頼む"),
            w.plot_note("$maryたちにここで休むようにいい、$wilsonは$sherlockを探しに出ていった"),
            w.plot_note("そこに$wilsonが指名手配されたと$restradeがやってくる"),
            )


def last_scene(w: World):
    wil = w.get("wilson")
    shal, mary, lime = w.get("sherlock"), w.get("mary"), w.get("lime")
    return w.scene("ラストシーン",
            w.change_camera("wilson"),
            w.change_stage("SherlockHouseLiving"),
            wil.come(),
            shal.be(),
            mary.be(),
            lime.be(),
            wil.do("リビングに出ていくと、そこには$maryと$lime、そして生涯に渡って$meに多大な影響を与えてくれた人生の最高の友人にして、$heroである$sherlockがいた"),
            shal.talk("早くそこに座ってくれないか", "でないと始められない"),
            wil.talk("一体何なんだ？"),
            mary.talk("これやよ。見てわからん？"),
            wil.do("テーブルの上のケーキには歪んだ文字で（おそらく$maryの手によるものだろう）『$wilson誕生日おめでとう』とあった"),
            wil.think("すっかり忘れていたが、あの日、長旅から戻ってきて彼らから色々聞いた日は$meの誕生日だった"),
            wil.talk("ありがとう"),
            wil.do("こうして楽しげなパーティが始まったが"),
            shal.talk("そもそも誕生日を祝うという風習はね"),
            wil.think("また始まった", "$sherlockはいつもと変わらない調子で自分の広大な知識を披露し始める"),
            wil.do("こうして$meたちの夜は更けていった"),
            )
