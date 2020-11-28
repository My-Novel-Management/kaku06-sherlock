# -*- coding: utf-8 -*-
'''
Chapter "赤鎧クラブ"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from config import TITLES
from scenes import PawnShop
from scenes import SherlockHouse
from scenes import Street


# Episodes
def missing_persons(w: World):
    return w.episode("失踪者たち",
            SherlockHouse.housemate_mary(w),
            SherlockHouse.mary_has_worry(w),
            SherlockHouse.about_missings(w),
            SherlockHouse.strange_armor_knight(w),
            )


def strange_work(w: World):
    return w.episode("不思議な仕事",
            SherlockHouse.strange_work(w),
            )


def bank_robbery(w: World):
    return w.episode("銀行強盗",
            Street.mary_walked_lime(w),
            PawnShop.limes_job_place(w),
            "オーナー夫婦の家",
            w.plot_note("質屋のオーナー夫婦はいい人そうで、$binsとも顔を合わせて帰っていった"),
            "$sherlockの家・居間",
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


def truth_of_club(w: World):
    return w.episode("クラブの真相",
            "$sherlockの家・居間",
            w.plot_note("$maryが$limeを助けてやってほしいと$sherlockに言う"),
            w.plot_note("$sherlockは自分の忠告を聞かなかったからだと言うが、それでも話だけは聞くと言う"),
            w.plot_note("質屋につながっていた抜け穴の中で、重要参考人だった$ignesが遺体で発見された"),
            w.plot_note("その容疑者として$limeが逮捕され、オーナー夫婦も事情聴取を受けている最中らしい"),
            w.plot_note("強盗の件についても調査中で、全部彼女に押し付けられるかもしれないと言い出す"),
            w.plot_note("$sherlockはその質屋に案内してもらう"),
            "外の通り",
            w.plot_note("$sherlockは$maryになぜ自分が忠告したかについて語る"),
            w.plot_note("どう考えても妙なアルバイトは彼女をその場から離れさせるための口実だった"),
            w.plot_note("事実、店番をもう片方にまかせている間に、実際は抜け穴をずっと掘っていた"),
            w.plot_note("$ignesの監視情報から、$limeが店を離れると店を一時閉めていたと"),
            w.plot_note("その間に抜け穴を完成させ、盗み出す計画だったが、最後にその計画を知っていた$binsを殺害した"),
            w.plot_note("$limeもオーナー夫婦も質屋から離れた場所で暮らしている"),
            w.plot_note("そのアリバイを証明するだけでいいと$sherlockは言う"),
            "銀行",
            w.plot_note("銀行へとやってきた$sherlockはそこにいた$restradeにそのアリバイの証拠を教える"),
            w.plot_note("前日に鍵が壊れて、誰も質屋に入れなくなっていたのだった"),
            )


def what_was_stolen(w: World):
    return w.episode("盗まれたもの",
            "$sherlockの家",
            w.plot_note("アリバイ証明から$limeとオーナー夫婦の無実は証明された"),
            w.plot_note("開放された$limeだったがオーナー夫婦からは不審がられ、家を追い出されてしまう"),
            w.plot_note("$maryが$limeを拾い、再び家へと連れてくる"),
            w.plot_note("$sherlockは銀行から盗まれたものがダイヤだけじゃないと睨むが、教えてもらえなかった"),
            w.plot_note("家に戻ってくると$sherlockはそこに$limeがいることに頭を抱える"),
            w.plot_note("$limeがしゃべれないのは呪いの鎧のせいだと言う"),
            w.plot_note("その呪いをといてもらおうと、知人の神官を読んでいた"),
            w.plot_note("呪いを解いたが$limeはしゃべれないままだった"),
            w.plot_note("その$limeは筆談で自分が王室の人間であると告白する"),
            )


def new_living(w: World):
    return w.episode("新しい居候",
            "$sherlockの家",
            w.plot_note("$limeは自分が誘拐された訳ではなく、普通に家出をしたのだと告白する"),
            w.plot_note("王室はそんな品の悪い発表をできないから失踪事件にして公表したのだと言った"),
            w.plot_note("もともと妾の子で、周囲から浮いていて、王室にも自分の居場所がなく帰りたくないと泣く"),
            w.plot_note("$maryは$sherlockに$limeを一緒に住まわせてほしいとお願いする"),
            w.plot_note("$sherlockは金銭的な問題さえ解決できればと提案する"),
            w.plot_note("$wilsonは金のことなら大丈夫だと、なぜか大金を手にして言う"),
            w.plot_note("$wilsonは$sherlockの秘蔵コレクションを売り払っていた"),
            w.plot_note("こうして新しい住人$limeをここに加えることになった"),
            )


# Chapter
def main(w: World):
    return w.chapter(TITLES[3],
            w.plot_setup("失踪者のリストの中に第二王女も含まれている"),
            w.plot_turnpoint("$maryは困っている赤鎧の騎士を連れてくる"),
            w.plot_develop("$limeは赤鎧の人間にだけできる不思議なアルバイトをしていると告白する"),
            w.plot_turnpoint("$sherlockはすぐやめるよう忠告するが$limeは断れず続けてしまう"),
            w.plot_develop("大規模な強盗事件が発生し、$limeの店の主人が逮捕される"),
            w.plot_turnpoint("$limeは仕事をクビになる"),
            w.plot_develop("事情を聞いて、赤鎧クラブの仕組みを$sherlockが解説する"),
            w.plot_turnpoint("$sherlockはそのいなくなった同僚が犯人と指摘する"),
            w.plot_develop("犯人たちは既に逃げたあとで同僚の兵士は殺されて見つかった"),
            w.plot_turnpoint("$limeは事情があって王室に戻れないと告白した"),
            w.plot_resolve("$limeが$sherlockの家に居候することになった"),
            missing_persons(w),
            strange_work(w),
            bank_robbery(w),
            truth_of_club(w),
            what_was_stolen(w),
            new_living(w),
            )


