# -*- coding: utf-8 -*-
'''
Story Config
============
'''

ASSET = {
        "PERSONS": (
            # (tag / name / full / age (birth) / job / call / info)
            ("shalon", "シャロン", "ホーマーズ,シャロン", 18,(1,1), "male", "勇者", "me:僕"),
            ("panna", "パンナ", "ワーロン,パンナ", 16,(1,1), "female", "武闘家", "me:ウチ"),
            ("emil", "エミール", "ロムダ,ミレイ", 17,(1,1), "female", "騎士", "me:私"),
            ("crades", "クラデス", "", 67,(1,1), "male", "魔道士", "me:儂"),
            ("ail", "アイル", "アルドラ,アイル", 25,(1,1), "female", "王族", "me:私"),
            ("moro", "モロー", "", 50,(1,1), "male", "盗賊", "me:私"),
            ("mike", "マイク", "ホルムズ,マイク", 27,(1,1), "male", "me:私"),
            ("rudy", "ルディ", "イルア,ルディ", 27,(1,1), "female", "盗賊", "me:私"),
            ## kingdom
            ("adams", "アダムス", "ボルゾイ,アダムス", 30,(1,1), "male", "王族", "me:オレ"),
            ## police
            ("restra", "レストラー", "ゴードン,レストラー", 40,(1,1), "male", "警察官", "me:私"),
            ),
        "STAGES": (
            # (tag / name / parent / (geometry) / info)
            ("Lomdas", "ロムダス", "", (1000,1000)),# 国名
            ("Baily", "ベイリー", "Lomdas"),
            ),
        "DAYS": (
            # (tag / name / month / day / year)
            ),
        "TIMES": (
            # (tag / name / hour / minute)
            ),
        "ITEMS": (
            # (tag / name / cate / info)
            ),
        "WORDS": (
            # (tag / name / cate / info)
            ("hero", "勇者"),
            ("k_shal", "シャル"),
            ("full_Emil", "ロムダ・エル・ミレイ"),
            ),
        "RUBIS": (
            # (origin / rubi / exclusions / always)
            ),
        }

