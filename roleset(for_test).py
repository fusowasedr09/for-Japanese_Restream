#!/usr/bin/env python
# -*- coding: utf-8 -*-

import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="/")
token = "ここにトークンを記載"

# 起動メッセージ
@bot.event
async def on_ready():
    print("we have logged in as {0}".format(bot.user))

# コマンド本体
# 使用の際にはbotにチャンネル管理、ロール管理、チャンネルの閲覧、メッセージの送信権限を与えてください（面倒なら管理者でも可）
@bot.command()
@commands.has_any_role("Administrator","Sボランティア")
async def create(ctx, arg):
    guild = ctx.guild
    await ctx.send("作成開始！\n完了までしばらくお待ち下さい。")

    # ロール作成
    rolename1 = arg + "スタッフ"
    rolename2 = arg + "解説"
    ## 権限設定
    r1perms = discord.Permissions(read_messages=True, manage_roles=True, change_nickname=True, send_messages=True, embed_links=True,
                                  attach_files=True, add_reactions=True, external_emojis=True, mention_everyone=True, read_message_history=True,
                                  use_slash_commands=True, connect=True, speak=True, stream=True, move_members=True, use_voice_activation=True,
                                  request_to_speak=True, send_tts_messages=True)
    r2perms = discord.Permissions(read_messages=True, manage_roles=False, change_nickname=True, send_messages=True, embed_links=True,
                                  attach_files=True, add_reactions=True, external_emojis=True, mention_everyone=False, read_message_history=True,
                                  use_slash_commands=True, connect=True, speak=True, stream=False, move_members=False, use_voice_activation=True,
                                  request_to_speak=True, send_tts_messages=True)
    ## ロール作成
    role1 = await guild.create_role(name=rolename1, color=discord.Color.orange(), permissions=r1perms)
    role2 = await guild.create_role(name=rolename2, color=discord.Color.green(), permissions=r2perms)
    ## Administrator,Sボランティアを宣言
    Admin = discord.utils.get(guild.roles, name="Administrator")
    Svol = discord.utils.get(guild.roles, name="Sボランティア")

    # スタッフ用カテゴリ・チャンネル作成
    ## スタッフ用カテゴリの作成
    category1 = await guild.create_category(rolename1)
    
    ## 作成したカテゴリをプライベートカテゴリに
    c1overwrites = {
        guild.default_role: discord.PermissionOverwrite(read_messages=False, connect=False),
        role1: discord.PermissionOverwrite(read_messages=True, send_messages=True, connect=True, speak=True),
        Admin: discord.PermissionOverwrite(read_messages=True, send_messages=True, connect=True, speak=True),
        Svol: discord.PermissionOverwrite(read_messages=True, send_messages=True, connect=True, speak=True)
        }
    await category1.edit(overwrites=c1overwrites)

    ## スタッフカテゴリに作成するチャンネル名の格納（案内以外）
    c1TextChannel_Names = [rolename1 + "用", "parsec報告", "解説応募通知", rolename1 + "VC用"]
    c1VoiceChannnel_Names =["控室", "会議室", "作業スタジオ"]

    ## 案内チャンネル作成（専用の権限セットを使用）
    g1overwrites = {
        guild.default_role: discord.PermissionOverwrite(read_messages=False, connect=False),
        role1: discord.PermissionOverwrite(read_messages=True, send_messages=False),
        Admin: discord.PermissionOverwrite(read_messages=True, send_messages=True),
        Svol: discord.PermissionOverwrite(read_messages=True, send_messages=False)
    }
    guidance1 = await category1.create_text_channel(name="\N{Japanese Symbol for Beginner}案内")
    #await guidance1.send("テスト")
    await guidance1.edit(overwrites=g1overwrites)


    ## スタッフ用チャンネルの作成（権限はカテゴリと同期）
    for c1TextChannel_Name in c1TextChannel_Names:
        await category1.create_text_channel(c1TextChannel_Name)

    for c1VoiceChannnel_Name in c1VoiceChannnel_Names:
        await category1.create_voice_channel(c1VoiceChannnel_Name)


    #解説用カテゴリ・チャンネル作成
    ## 解説カテゴリの作成
    category2 = await guild.create_category(rolename2)

    ## 作成したカテゴリをプライベートカテゴリに
    c2overwrites = {
        guild.default_role: discord.PermissionOverwrite(read_messages=False, connect=False),
        role1: discord.PermissionOverwrite(read_messages=True, send_messages=True, connect=True, speak=True),
        role2: discord.PermissionOverwrite(read_messages=True, send_messages=True, connect=True, speak=True),
        Admin: discord.PermissionOverwrite(read_messages=True, send_messages=True, connect=True, speak=True),
        Svol: discord.PermissionOverwrite(read_messages=True, send_messages=True, connect=True, speak=True)
        }
    await category2.edit(overwrites=c2overwrites)


    ## 解説カテゴリに作成するチャンネル名の格納（案内除く）
    c2TextChannel_Names = [rolename2 + "用", rolename2 + "VC用"]
    c2VoiceChannel_Names = ["待機用VC", "テスト用VC", "相談用VC"]

    ## 案内チャンネル作成（専用の権限セットを使用）
    g2overwrites = {
        guild.default_role: discord.PermissionOverwrite(read_messages=False, connect=False),
        role1: discord.PermissionOverwrite(read_messages=True, send_messages=False),
        role2: discord.PermissionOverwrite(read_messages=True, send_messages=False),
        Admin: discord.PermissionOverwrite(read_messages=True, send_messages=True),
        Svol: discord.PermissionOverwrite(read_messages=True, send_messages=False)
    }
    guidance2 = await category2.create_text_channel(name="\N{Japanese Symbol for Beginner}はじめに", overwrites=g2overwrites)
    #await guidance2.send("テスト")
    await guidance2.edit(overwrites=g1overwrites)

    ## 解説用チャンネルの作成（権限はカテゴリと同期）
    for c2TextChannel_Name in c2TextChannel_Names:
        await category2.create_text_channel(c2TextChannel_Name)
    for c2VoiceChannnel_Name in c2VoiceChannel_Names:
        await category2.create_voice_channel(c2VoiceChannnel_Name)


    #終了メッセージ
    await ctx.send("作成完了しました！\nスレッドの権限やロール順位、既存チャンネルへの権限設定の調整を忘れずに行ってください。")

bot.run(token)
