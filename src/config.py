# -*- coding: utf-8 -*-
'''
Story Config
============
'''

ASSET = {
        "PERSONS": (
            # (tag / name / full / age (birth) / job / call / info)
            ## main
            ("sherlock", "シャーロック", "ホーマー,シャーロック", 20,(1,1), "male", "勇者", "me:僕"),
            ("mary", "メアリー", "", 16,(1,1), "female", "武闘家", "me:ウチ"),
            ("wilson", "ウィルソン", "ハドル,ウィルソン", 40,(1,1), "元神官", "me:私"),
            ("lime", "ライム", "", 19,(1,1), "female", "騎士（王女）", "me:私"),
            ## sub
            ("mikel", "マイケル", "ホーマー,マイケル", 27,(1,1), "役人", "me:俺"),
            ("aily", "アイリー", "ルドラー,アイリー", 20,(1,1), "female", "王族", "me:私"),
            ("rudy", "ルディ", "ライラ,ルディ", 20,(1,1), "female", "盗賊", "me:私"),
            ("moriano", "モリアーノ", "ジェーンズ,モリアーノ", 50,(1,1), "教授", "me:私"),
            ## kingdom
            ## police
            ("appolo", "アポロ", "リキュール,アポロ", 50,(1,1), "male", "警察（警視）", "me:私"),
            ("restrade", "レストラーデ", "グレイ,レストラーデ", 35,(1,1), "警察（警部）", "me:俺"),
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
            ("boss", "魔王"),
            ("monster", "魔獣"),
            ("k_shal", "シャル"),
            ("enagy", "魔素"),
            ),
        "RUBIS": (
            # (origin / rubi / exclusions / always)
            ),
        }

