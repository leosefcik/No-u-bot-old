# coding=utf-8

import os
import discord
import random
import ffmpeg
import asyncio


spam=0


TOKEN=""
client=discord.Client()
noubotid=["<@!745219622965346315>","<@745219622965346315>"]
chat=["ok","cool","cool beans","bruh","damn","probably","probably not","that sucks","yes","funny","no","maybe","lmao","lol","absolutely not",":flushed:",":moyai:",":postbox:","cool story bro","brb","k",":joy:","ok but do you know Peter Griffin?","bruh moment","bullshit","xD","whatever",":rofl:","seriously","absolutely","not really",":thumbsup:",":thumbsdown:","wow","wdym","same","true","I agree","gg","nah","anything is possible","idk","what","i can't hear you",":sunglasses:",":yum:",":joy_cat:",":orangutan:",":cheese:",":eyes:",":hankey:","interesting","hmmm","good","nice","really",":pig2:","i have to pee","i love you","fr","ong","oh","lemme check","that is fascinating","golly-gee!","I will have to ponder that one","congrats"]
questionchat=["yes","no","maybe","absolutely yes","probably","anything is possible","probably not","idk","absolutely not"]
langlist=["Italian by Vittorio","French by Antoine","Czech by Eliska","German by Klaus","Danish by Rasmus","Swedish by Erik","Dutch by Max","Russian by Alyona","Finnish by Sanna","Turkish by Ipek","Greek by Happy Dimitris","Polish by Ania","Arabic by Nizar","Norwegian by Olav","Korean by Minji"]
allemojis="😀😃😄😁😆😅😂🤣☺️😇🙂🙃😉😍😘😗😙😋😛😝😜🤪🤨🧐🤓😎🤩😏😒😞😔😟😕🙁☹️😣😖😫😩😢😭😤😠😡🤬🤯😳😱😨😰😥😓🤗🤔🤭🤫🤥😶😐😑😬🙄😯😦😧😮😲😴🤤😪😵🤐🤢🤮🤧😷🤒🤕🤑🤠😈👿👹👺🤡💩👻💀☠️👽👾🤖🎃😺😸😹😻😼😽🙀😿😾🤲🤲🏻🤲🏼🤲🏽👐🏾🤲🏿👐👐🏻👐🏼👐🏽👐🏾👐🏿🙌🙌🏻🙌🏼🙌🏽🙌🏾🙌🏿👏👏🏻👏🏼👏🏽👏🏾👏🏿🤝👍👍🏻👍🏼👍🏽👍🏾👍🏿👎👎🏻👎🏼👎🏽👎🏾👎🏿👊👊🏻👊🏼👊🏽👊🏾👊🏿✊✊🏻✊🏼✊🏽✊🏾✊🏿🤛🤛🏻🤛🏼🤛🏽🤛🏾🤛🏿🤜🤜🏻🤜🏼🤜🏽🤜🏾🤜🏿🤞🤞🏻🤞🏼🤞🏽🤞🏾🤞🏿✌️✌🏻✌🏼✌🏽✌🏾✌🏿🤟🤟🏻🤟🏼🤟🏽🤟🏾🤟🏿🤘🤘🏻🤘🏼🤘🏽🤘🏾🤘🏿👌👌🏻👌🏼👌🏽👌🏾👌🏿👈👈🏻👈🏼👈🏽👈🏾👈🏿👉👉🏻👉🏼👉🏽👉🏾👉🏿👆👆🏻👆🏼👆🏽👆🏾👆🏿👇👇🏻👇🏼👇🏽👇🏾👇🏿☝️☝🏻☝🏼☝🏽☝🏾☝🏿✋✋🏻✋🏼✋🏽✋🏾✋🏿🤚🤚🏻🤚🏼🤚🏽🤚🏾🤚🏿🖐🖐🏻🖐🏼🖐🏽🖐🏾🖐🏿🖖🖖🏻🖖🏼🖖🏽🖖🏾🖖🏿👋👋🏻👋🏼👋🏽👋🏾👋🏿🤙🤙🏻🤙🏼🤙🏽🤙🏾🤙🏿💪💪🏻💪🏼💪🏽💪🏾💪🏿🖕🖕🏻🖕🏼🖕🏽🖕🏾🖕🏿✍️✍🏻✍🏼✍🏽✍🏾✍🏿🙏🙏🏻🙏🏼🙏🏽🙏🏾🙏🏿💍💄💋👄👅👂👂🏻👂🏼👂🏽👂🏾👂🏿👃👃🏻👃🏼👃🏽👃🏾👃🏿👣👁👀🧠🗣👤👥👶👶🏻👶🏼👶🏽👶🏾👶🏿👧👧🏻👧🏼👧🏽👧🏾👧🏿🧒🧒🏻🧒🏼🧒🏽🧒🏾🧒🏿👦👦🏻👦🏼👦🏽👦🏾👦🏿👩👩🏻👩🏼👩🏽👩🏾👩🏿🧑🧑🏻🧑🏼🧑🏽🧑🏾🧑🏿👨👨🏻👨🏼👨🏽👨🏾👨🏿👱‍♀️👱🏻‍♀️👱🏼‍♀️👱🏽‍♀️👱🏾‍♀️👱🏿‍♀️👱‍♂️👱🏻‍♂️👱🏼‍♂️👱🏽‍♂️👱🏾‍♂️👱🏿‍♂️🧔🧔🏻🧔🏼🧔🏽🧔🏾🧔🏿👵👵🏻👵🏼👵🏽👵🏾👵🏿🧓🧓🏻🧓🏼🧓🏽🧓🏾🧓🏿👴👴🏻👴🏼👴🏽👴🏾👴🏿👲👲🏻👲🏼👲🏽👲🏾👲🏿👳‍♀️👳🏻‍♀️👳🏼‍♀️👳🏽‍♀️👳🏾‍♀️👳🏿‍♀️👳‍♂️👳🏻‍♂️👳🏼‍♂️👳🏽‍♂️👳🏾‍♂️👳🏿‍♂️🧕🧕🏻🧕🏼🧕🏽🧕🏾🧕🏿👮‍♀️👮🏻‍♀️👮🏼‍♀️👮🏽‍♀️👮🏾‍♀️👮🏿‍♀️👮‍♂️👮🏻‍♂️👮🏼‍♂️👮🏽‍♂️👮🏾‍♂️👮🏿‍♂️👷‍♀️👷🏻‍♀️👷🏼‍♀️👷🏽‍♀️👷🏾‍♀️👷🏿‍♀️👷‍♂️👷🏻‍♂️👷🏼‍♂️👷🏽‍♂️👷🏾‍♂️👷🏿‍♂️💂‍♀️💂🏻‍♀️💂🏼‍♀️💂🏽‍♀️💂🏾‍♀️💂🏿‍♀️💂‍♂️💂🏻‍♂️💂🏼‍♂️💂🏽‍♂️💂🏾‍♂️💂🏿‍♂️🕵️‍♀️🕵🏻‍♀️🕵🏼‍♀️🕵🏽‍♀️🕵🏾‍♀️🕵🏿‍♀️🕵️‍♂️🕵🏻‍♂️🕵🏼‍♂️🕵🏽‍♂️🕵🏾‍♂️🕵🏿‍♂️👩‍⚕️👩🏻‍⚕️👩🏼‍⚕️👩🏽‍⚕️👩🏾‍⚕️👩🏿‍⚕️👨‍⚕️👨🏻‍⚕️👨🏼‍⚕️👨🏽‍⚕️👨🏾‍⚕️👨🏿‍⚕️👩‍🌾👩🏻‍🌾👩🏼‍🌾👩🏽‍🌾👩🏾‍🌾👩🏿‍🌾👨‍🌾👨🏻‍🌾👨🏼‍🌾👨🏽‍🌾👨🏾‍🌾👨🏿‍🌾👩‍🍳👩🏻‍🍳👩🏼‍🍳👩🏽‍🍳👩🏾‍🍳👩🏿‍🍳👨‍🍳👨🏻‍🍳👨🏼‍🍳👨🏽‍🍳👨🏾‍🍳👨🏿‍🍳👩‍🎓👩🏻‍🎓👩🏼‍🎓👩🏽‍🎓👩🏾‍🎓👩🏿‍🎓👨‍🎓👨🏻‍🎓👨🏼‍🎓👨🏽‍🎓👨🏾‍🎓👨🏿‍🎓👩‍🎤👩🏻‍🎤👩🏼‍🎤👩🏽‍🎤👩🏾‍🎤👩🏿‍🎤👨‍🎤👨🏻‍🎤👨🏼‍🎤👨🏽‍🎤👨🏾‍🎤👨🏿‍🎤👩‍🏫👩🏻‍🏫👩🏼‍🏫👩🏽‍🏫👩🏾‍🏫👩🏿‍🏫👨‍🏫👨🏻‍🏫👨🏼‍🏫👨🏽‍🏫👨🏾‍🏫👨🏿‍🏫👩‍🏭👩🏻‍🏭👩🏼‍🏭👩🏽‍🏭👩🏾‍🏭👩🏿‍🏭👨‍🏭👨🏻‍🏭👨🏼‍🏭👨🏽‍🏭👨🏾‍🏭👨🏿‍🏭👩‍💻👩🏻‍💻👩🏼‍💻👩🏽‍💻👩🏾‍💻👩🏿‍💻👨‍💻👨🏻‍💻👨🏼‍💻👨🏽‍💻👨🏾‍💻👨🏿‍💻👩‍💼👩🏻‍💼👩🏼‍💼👩🏽‍💼👩🏾‍💼👩🏿‍💼👨‍💼👨🏻‍💼👨🏼‍💼👨🏽‍💼👨🏾‍💼👨🏿‍💼👩‍🔧👩🏻‍🔧👩🏼‍🔧👩🏽‍🔧👩🏾‍🔧👩🏿‍🔧👨‍🔧👨🏻‍🔧👨🏼‍🔧👨🏽‍🔧👨🏾‍🔧👨🏿‍🔧👩‍🔬👩🏻‍🔬👩🏼‍🔬👩🏽‍🔬👩🏾‍🔬👩🏿‍🔬👨‍🔬👨🏻‍🔬👨🏼‍🔬👨🏽‍🔬👨🏾‍🔬👨🏿‍🔬👩‍🎨👩🏻‍🎨👩🏼‍🎨👩🏽‍🎨👩🏾‍🎨👩🏿‍🎨👨‍🎨👨🏻‍🎨👨🏼‍🎨👨🏽‍🎨👨🏾‍🎨👨🏿‍🎨👩‍🚒👩🏻‍🚒👩🏼‍🚒👩🏽‍🚒👩🏾‍🚒👩🏿‍🚒👨‍🚒👨🏻‍🚒👨🏼‍🚒👨🏽‍🚒👨🏾‍🚒👨🏿‍🚒👩‍✈️👩🏻‍✈️👩🏼‍✈️👩🏽‍✈️👩🏾‍✈️👩🏿‍✈️👨‍✈️👨🏻‍✈️👨🏼‍✈️👨🏽‍✈️👨🏾‍✈️👨🏿‍✈️👩‍🚀👩🏻‍🚀👩🏼‍🚀👩🏽‍🚀👩🏾‍🚀👩🏿‍🚀👨‍🚀👨🏻‍🚀👨🏼‍🚀👨🏽‍🚀👨🏾‍🚀👨🏿‍🚀👩‍⚖️👩🏻‍⚖️👩🏼‍⚖️👩🏽‍⚖️👩🏾‍⚖️👩🏿‍⚖️👨‍⚖️👨🏻‍⚖️👨🏼‍⚖️👨🏽‍⚖️👨🏾‍⚖️👨🏿‍⚖️👰👰🏻👰🏼👰🏽👰🏾👰🏿🤵🤵🏻🤵🏼🤵🏽🤵🏾🤵🏿👸👸🏻👸🏼👸🏽👸🏾👸🏿🤴🤴🏻🤴🏼🤴🏽🤴🏾🤴🏿🤶🤶🏻🤶🏼🤶🏽🤶🏾🤶🏿🎅🎅🏻🎅🏼🎅🏽🎅🏾🎅🏿🧙‍♀️🧙🏻‍♀️🧙🏼‍♀️🧙🏽‍♀️🧙🏾‍♀️🧙🏿‍♀️🧙‍♂️🧙🏻‍♂️🧙🏼‍♂️🧙🏽‍♂️🧙🏾‍♂️🧙🏿‍♂️🧝‍♀️🧝🏻‍♀️🧝🏼‍♀️🧝🏽‍♀️🧝🏾‍♀️🧝🏿‍♀️🧝‍♂️🧝🏻‍♂️🧝🏼‍♂️🧝🏽‍♂️🧝🏾‍♂️🧝🏿‍♂️🧛‍♀️🧛🏻‍♀️🧛🏼‍♀️🧛🏽‍♀️🧛🏾‍♀️🧛🏿‍♀️🧛‍♂️🧛🏻‍♂️🧛🏼‍♂️🧛🏽‍♂️🧛🏾‍♂️🧛🏿‍♂️🧟‍♀️🧟‍♂️🧞‍♀️🧞‍♂️🧜‍♀️🧜🏻‍♀️🧜🏼‍♀️🧜🏽‍♀️🧜🏾‍♀️🧜🏿‍♀️🧜‍♂️🧜🏻‍♂️🧜🏼‍♂️🧜🏽‍♂️🧜🏾‍♂️🧜🏿‍♂️🧚‍♀️🧚🏻‍♀️🧚🏼‍♀️🧚🏽‍♀️🧚🏾‍♀️🧚🏿‍♀️🧚‍♂️🧚🏻‍♂️🧚🏼‍♂️🧚🏽‍♂️🧚🏾‍♂️🧚🏿‍♂️👼👼🏻👼🏼👼🏽👼🏾👼🏿🤰🤰🏻🤰🏼🤰🏽🤰🏾🤰🏿🤱🤱🏻🤱🏼🤱🏽🤱🏾🤱🏿🙇‍♀️🙇🏻‍♀️🙇🏼‍♀️🙇🏽‍♀️🙇🏾‍♀️🙇🏿‍♀️🙇‍♂️🙇🏻‍♂️🙇🏼‍♂️🙇🏽‍♂️🙇🏾‍♂️🙇🏿‍♂️💁‍♀️💁🏻‍♀️💁🏼‍♀️💁🏽‍♀️💁🏾‍♀️💁🏿‍♀️💁‍♂️💁🏻‍♂️💁🏼‍♂️💁🏽‍♂️💁🏾‍♂️💁🏿‍♂️🙅‍♀️🙅🏻‍♀️🙅🏼‍♀️🙅🏽‍♀️🙅🏾‍♀️🙅🏿‍♀️🙅‍♂️🙅🏻‍♂️🙅🏼‍♂️🙅🏽‍♂️🙅🏾‍♂️🙅🏿‍♂️🙆‍♀️🙆🏻‍♀️🙆🏼‍♀️🙆🏽‍♀️🙆🏾‍♀️🙆🏿‍♀️🙆‍♂️🙆🏻‍♂️🙆🏼‍♂️🙆🏽‍♂️🙆🏾‍♂️🙆🏿‍♂️🙋‍♀️🙋🏻‍♀️🙋🏼‍♀️🙋🏽‍♀️🙋🏾‍♀️🙋🏿‍♀️🙋‍♂️🙋🏻‍♂️🙋🏼‍♂️🙋🏽‍♂️🙋🏾‍♂️🙋🏿‍♂️🤦‍♀️🤦🏻‍♀️🤦🏼‍♀️🤦🏽‍♀️🤦🏾‍♀️🤦🏿‍♀️🤦‍♂️🤦🏻‍♂️🤦🏼‍♂️🤦🏽‍♂️🤦🏾‍♂️🤦🏿‍♂️🤷‍♀️🤷🏻‍♀️🤷🏼‍♀️🤷🏽‍♀️🤷🏾‍♀️🤷🏿‍♀️🤷‍♂️🤷🏻‍♂️🤷🏼‍♂️🤷🏽‍♂️🤷🏾‍♂️🤷🏿‍♂️🙎‍♀️🙎🏻‍♀️🙎🏼‍♀️🙎🏽‍♀️🙎🏾‍♀️🙎🏿‍♀️🙎‍♂️🙎🏻‍♂️🙎🏼‍♂️🙎🏽‍♂️🙎🏾‍♂️🙎🏿‍♂️🙍‍♀️🙍🏻‍♀️🙍🏼‍♀️🙍🏽‍♀️🙍🏾‍♀️🙍🏿‍♀️🙍‍♂️🙍🏻‍♂️🙍🏼‍♂️🙍🏽‍♂️🙍🏾‍♂️🙍🏿‍♂️💇‍♀️💇🏻‍♀️💇🏼‍♀️💇🏽‍♀️💇🏾‍♀️💇🏿‍♀️💇‍♂️💇🏻‍♂️💇🏼‍♂️💇🏽‍♂️💇🏾‍♂️💇🏿‍♂️💆‍♀️💆🏻‍♀️💆🏼‍♀️💆🏽‍♀️💆🏾‍♀️💆🏿‍♀️💆‍♂️💆🏻‍♂️💆🏼‍♂️💆🏽‍♂️💆🏾‍♂️💆🏿‍♂️🧖‍♀️🧖🏻‍♀️🧖🏼‍♀️🧖🏽‍♀️🧖🏾‍♀️🧖🏿‍♀️🧖‍♂️🧖🏻‍♂️🧖🏼‍♂️🧖🏽‍♂️🧖🏾‍♂️🧖🏿‍♂️💅💅🏻💅🏼💅🏽💅🏾💅🏿🤳🤳🏻🤳🏼🤳🏽🤳🏾🤳🏿💃💃🏻💃🏼💃🏽💃🏾💃🏿🕺🕺🏻🕺🏼🕺🏽🕺🏾🕺🏿👯‍♀️👯‍♂️🕴🕴🏻🕴🏼🕴🏽🕴🏾🕴🏿🚶‍♀️🚶🏻‍♀️🚶🏼‍♀️🚶🏽‍♀️🚶🏾‍♀️🚶🏿‍♀️🚶‍♂️🚶🏻‍♂️🚶🏼‍♂️🚶🏽‍♂️🚶🏾‍♂️🚶🏿‍♂️🏃‍♀️🏃🏻‍♀️🏃🏼‍♀️🏃🏽‍♀️🏃🏾‍♀️🏃🏿‍♀️🏃‍♂️🏃🏻‍♂️🏃🏼‍♂️🏃🏽‍♂️🏃🏾‍♂️🏃🏿‍♂️👫👭👬💑👩‍❤️‍👩👨‍❤️‍👨💏👩‍❤️‍💋‍👩👨‍❤️‍💋‍👨👪👨‍👩‍👧👨‍👩‍👧‍👦👨‍👩‍👦‍👦👨‍👩‍👧‍👧👩‍👩‍👦👩‍👩‍👧👩‍👩‍👧‍👦👩‍👩‍👦‍👦👩‍👩‍👧‍👧👨‍👨‍👦👨‍👨‍👧👨‍👨‍👧‍👦👨‍👨‍👦‍👦👨‍👨‍👧‍👧👩‍👦👩‍👧👩‍👧‍👦👩‍👦‍👦👩‍👧‍👧👨‍👦👨‍👧👨‍👧‍👦👨‍👦‍👦👨‍👧‍👧🧥👚👕👖👔👗👙👘👠👡👢👞👟🧦🧤🧣🎩🧢👒🎓⛑👑👝👛👜💼🎒👓🕶🌂🐶🐱🐭🐹🐰🦊🐻🐼🐨🐯🦁🐮🐷🐽🐸🐵🙈🙉🙊🐒🐔🐧🐦🐤🐣🐥🦆🦅🦉🦇🐺🐗🐴🦄🐝🐛🦋🐌🐚🐞🐜🦗🕷🕸🦂🐢🐍🦎🦖🦕🐙🦑🦐🦀🐡🐠🐟🐬🐳🐋🦈🐊🐅🐆🦓🦍🐘🦏🐪🐫🦒🐃🐂🐄🐎🐖🐏🐑🐐🦌🐕🐩🐈🐓🦃🕊🐇🐁🐀🐿🦔🐾🐉🐲🌵🎄🌲🌳🌴🌱🌿☘️🍀🎍🎋🍃🍂🍁🍄🌾💐🌷🌹🥀🌺🌸🌼🌻🌞🌝🌛🌜🌚🌕🌖🌗🌘🌑🌒🌓🌔🌙🌎🌍🌏💫⭐️🌟✨⚡️☄️💥🔥🌪🌈☀️🌤⛅️🌥☁️🌦🌧⛈🌩🌨❄️☃️⛄️🌬💨💧💦☔️☂️🌊🌫🍏🍎🍐🍊🍋🍌🍉🍇🍓🍈🍒🍑🍍🥥🥝🍅🍆🥑🥦🥒🌶🌽🥕🥔🍠🥐🍞🥖🥨🧀🥚🍳🥞🥓🥩🍗🍖🌭🍔🍟🍕🥪🥙🌮🌯🥗🥘🥫🍝🍜🍲🍛🍣🍱🥟🍤🍙🍚🍘🍥🥠🍢🍡🍧🍨🍦🥧🍰🎂🍮🍭🍬🍫🍿🍩🍪🌰🥜🍯🥛🍼☕️🍵🥤🍶🍺🍻🥂🍷🥃🍸🍹🍾🥄🥄🍴🍽🥣🥡🥢⚽️🏀🏈⚾️🎾🏐🏉🎱🏓🏸🥅🏒🏑🏏⛳️🏹🎣🥊🥋🎽⛸🥌🛷🎿⛷🏂🏋️‍♀️🏋️‍♂️🤼‍♀️🤼‍♂️🤸‍♀️🤸‍♂️⛹️‍♀️⛹️‍♂️🤺🤾‍♀️🤾‍♂️🏌️‍♀️🏌️‍♂️🏇🧘‍♀️🧘‍♂️🏄‍♀️🏄‍♂️🏊‍♀️🏊‍♂️🤽‍♀️🤽‍♂️🚣‍♀️🚣‍♂️🧗‍♀️🧗‍♂️🚵‍♀️🚵‍♂️🚴‍♀️🚴‍♂️🏆🥇🥈🥉🏅🎖🏵🎗🎫🎟🎪🤹‍♀️🤹‍♂️🎭🎨🎬🎤🎧🎼🎹🥁🎷🎺🎸🎻🎲🎯🎳🎮🎰🚗🚕🚙🚌🚎🏎🚓🚑🚒🚐🚚🚛🚜🛴🚲🛵🏍🚨🚔🚍🚘🚖🚡🚠🚟🚃🚋🚞🚝🚄🚅🚈🚂🚆🚇🚊🚉✈️🛫🛬🛩💺🛰🚀🛸🚁🛶⛵️🚤🛥🛳⛴🚢⚓️⛽️🚧🚦🚥🚏🗺🗿🗽🗼🏰🏯🏟🎡🎢🎠⛲️⛱🏖🏝🏜🌋⛰🏔🗻🏕⛺️🏠🏡🏘🏚🏗🏭🏢🏬🏣🏤🏥🏦🏨🏪🏫🏩💒🏛⛪️🕌🕍🕋⛩🛤🛣🗾🎑🏞🌅🌄🌠🎇🎆🌇🌆🏙🌃🌌🌉🌁⌚️📱📲💻⌨️🖥🖨🖱🖲🕹🗜💽💾💿📀📼📷📸📹📽🎞📞☎️📟📠📺📻🎙🎚🎛⏱⏲⏰🕰⌛️⏳📡🔋🔌💡🔦🕯🗑🛢💸💵💴💶💷💰💳💎⚖️🔧🔨⚒🛠⛏🔩⚙️⛓🔫💣🔪🗡⚔️🛡🚬⚰️⚱️🏺🔮📿💈⚗️🔭🔬🕳💊💉🌡🚽🚰🚿🛁🔑🗝🚪🛋🛏🛌🖼🛍🛒🎁🎈🎏🎀🎊🎉🎎🏮🎐✉️📩📨📧💌📥📤📦🏷📪📫📬📭📮📯📜📃📄📑📊📈📉🗒🗓📆📅📇🗃🗳🗄📋📁📂🗂🗞📰📓📔📒📕📗📘📙📚📖🔖🔗📎🖇📐📏📌📍✂️📝✏️🔍🔎🔏🔐🔒🔓❤️🧡💛💚💙💜🖤💔❣️💕💞💓💗💖💘💝💟☮️✝️☪️🕉☸️✡️🔯🕎☯️☦️🛐⛎♈️♉️♊️♋️♌️♍️♎️♏️♐️♑️♒️♓️🆔⚛️🉑☢️☣️📴📳🈶🈚️🈸🈺🈷️✴️🆚💮🉐㊙️㊗️🈴🈵🈹🈲🅰️🅱️🆎🆑🅾️🆘❌⭕️🛑⛔️📛🚫💯💢♨️🚷🚯🚳🚱🔞📵🚭❗️❕❓❔‼️⁉️🔅🔆〽️⚠️🚸🔱⚜️🔰♻️✅🈯️💹❇️✳️❎🌐💠Ⓜ️🌀💤🏧🚾♿️🅿️🈳🈂️🛂🛃🛄🛅🚹🚺🚼🚻🚮🎦📶🈁🔣ℹ️🔤🔡🔠🆖🆗🆙🆒🆕🆓0️⃣1️⃣2️⃣3️⃣4️⃣5️⃣6️⃣7️⃣8️⃣9️⃣🔟🔢#️⃣*️⃣⏏️▶️⏸⏯⏹⏺⏭⏮⏩⏪⏫⏬◀️🔼🔽➡️⬅️⬆️⬇️↗️↘️↙️↖️↕️↔️↪️↩️⤴️⤵️🔀🔁🔂🔄🔃🎵🎶➕➖➗✖️💲💱™️©️®️〰️➰➿🔚🔙🔛🔝🔜✔️☑️🔘⚪️⚫️🔴🔵🔺🔻🔸🔹🔶🔷🔳🔲▪️▫️◾️◽️◼️◻️⬛️⬜️🔈🔇🔉🔊🔔🔕📣📢👁‍🗨💬💭🗯♠️♣️♥️♦️🃏🎴🀄️🕐🕑🕒🕓🕔🕕🕖🕗🕘🕙🕚🕛🕜🕝🕞🕟🕠🕡🕢🕣🕤🕥🕦🕧🏳️🏴🏁🚩🏳️‍🌈🇦🇫🇦🇽🇦🇱🇩🇿🇦🇸🇦🇩🇦🇴🇦🇮🇦🇶🇦🇬🇦🇷🇦🇲🇦🇼🇦🇺🇦🇹🇦🇿🇧🇸🇧🇭🇧🇩🇧🇧🇧🇾🇧🇪🇧🇿🇧🇯🇧🇲🇧🇹🇧🇴🇧🇦🇧🇼🇧🇷🇮🇴🇻🇬🇧🇳🇧🇬🇧🇫🇧🇮🇰🇭🇨🇲🇨🇦🇮🇨🇨🇻🇧🇶🇰🇾🇨🇫🇹🇩🇨🇱🇨🇳🇨🇽🇨🇨🇨🇴🇰🇲🇨🇬🇨🇩🇨🇰🇨🇷🇨🇮🇭🇷🇨🇺🇨🇼🇨🇾🇨🇿🇩🇰🇩🇯🇩🇲🇩🇴🇪🇨🇪🇬🇸🇻🇬🇶🇪🇷🇪🇪🇪🇹🇪🇺🇫🇰🇫🇴🇫🇯🇫🇮🇫🇷🇬🇫🇵🇫🇹🇫🇬🇦🇬🇲🇬🇪🇬🇭🇬🇮🇬🇷🇬🇱🇬🇩🇬🇵🇬🇺🇬🇹🇬🇬🇬🇳🇬🇾🇬🇾🇭🇹🇭🇳🇭🇰🇭🇺🇮🇸🇮🇳🇮🇩🇮🇷🇮🇶🇮🇪🇮🇲🇮🇱🇮🇹🇯🇲🇯🇵🎌🇯🇪🇯🇴🇰🇿🇰🇪🇰🇮🇽🇰🇰🇼🇰🇬🇱🇦🇱🇻🇱🇧🇱🇸🇱🇷🇱🇾🇱🇮🇱🇹🇱🇺🇲🇴🇲🇰🇲🇬🇲🇼🇲🇾🇲🇻🇲🇱🇲🇹🇲🇭🇲🇶🇲🇷🇲🇺🇾🇹🇲🇽🇫🇲🇲🇩🇲🇨🇲🇳🇲🇪🇲🇸🇲🇦🇲🇿🇲🇲🇳🇦🇳🇷🇳🇵🇳🇱🇳🇨🇳🇿🇳🇮🇳🇪🇳🇬🇳🇺🇳🇫🇰🇵🇲🇵🇳🇴🇴🇲🇵🇰🇵🇼🇵🇸🇵🇦🇵🇬🇵🇾🇵🇪🇵🇭🇵🇳🇵🇱🇵🇹🇵🇷🇶🇦🇷🇪🇷🇴🇷🇺🇷🇼🇼🇸🇸🇲🇸🇹🇸🇦🇸🇳🇷🇸🇸🇨🇸🇱🇸🇬🇸🇽🇸🇰🇸🇮🇬🇸🇸🇧🇸🇴🇿🇦🇰🇷🇸🇸🇪🇸🇱🇰🇧🇱🇸🇭🇰🇳🇱🇨🇵🇲🇻🇨🇸🇩🇸🇷🇸🇿🇸🇪🇨🇭🇸🇾🇹🇼🇹🇯🇹🇿🇹🇭🇹🇱🇹🇬🇹🇰🇹🇴🇹🇹🇹🇳🇹🇷🇹🇲🇹🇨🇹🇻🇻🇮🇺🇬🇺🇦🇦🇪🇬🇧🏴󠁧󠁢󠁥󠁮󠁧󠁿🏴󠁧󠁢󠁳󠁣󠁴󠁿🏴󠁧󠁢󠁷󠁬󠁳󠁿🇺🇸🇺🇾🇺🇿🇻🇺🇻🇦🇻🇪🇻🇳🇼🇫🇪🇭🇾🇪🇿🇲🇿🇼"
@client.event
async def on_ready():
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="xx xten tacions"))
  print(f'{client.user} has connected to Discord!')
  spamchannel=client.get_channel(789507982642774026)
  lbbq = client.get_guild(743449026833416283)
  chicktron = await lbbq.fetch_member(295980196727619584)
  print(chicktron)
  zoochannel=client.get_channel(792434578240438313)
  print(chicktron.status)
  if chicktron.status=="online":
    print("ADfasdfasfsdafdsfafadsfds")
    while True:
      time.sleep(6)
      await zoochannel.send(random.choice(chat))
@client.event
async def on_message(message):
  msg=message.content.lower()
  if message.author == client.user:
    return
  elif msg.startswith("no u bot emoji"):
    reply=random.choice(allemojis)
    await message.channel.send(reply)
  elif msg.startswith("no u bot help"):
    await message.channel.send("u can do no u bot give me therapy, ping me to get me to respond or talk with me in dms")
  elif msg=="the no u emoji":
    await message.channel.send("<:nou:790856343556849695>")
  elif msg=="bruh":
    await message.channel.send("moment")
  elif msg=="uwu" or msg=="owo":
    await message.channel.send(":flushed:")
  elif msg.startswith("no u bot stop giving me therapy"):
    voice = discord.utils.get(client.voice_clients, guild=message.guild)
    await voice.disconnect()
  elif msg.startswith("no u bot give me therapy"):
    if msg.endswith("list") or msg.endswith("readme"):
      await message.channel.send(file=discord.File(r'no_u_bot_readme.txt'))
      return
    if msg.endswith("ost") or msg.endswith("zip"):
      await message.channel.send(file=discord.File(r"no_u_bot_ost.zip"))
      return
    if message.author.voice and message.author.voice.channel:
      channel = message.author.voice.channel
      await channel.connect()
    else:
      await message.channel.send("Please, connect to a voice channel before we begin.")
      return
    voice = discord.utils.get(client.voice_clients, guild=message.guild)
    try:
      int(msg[-1])
      try:
        int(msg[-2])
        if int(msg[-2])==1 and int(msg[-1])<=4:
          lang=10+int(msg[-1])
        else:
          await message.channel.send("Out of range! Limit to 0-14.")
          await voice.disconnect()
          return
      except:
        lang=int(msg[-1])
    except:
      lang=random.randrange(15)
    shortfile=str(str(lang)+"short.mp3")
    longfile=str(str(lang)+"long.mp3")
    endfile=str(str(lang)+"end.mp3")
    if msg.count("long")>=1:
      voice.play(discord.FFmpegPCMAudio(longfile))
      repli="```(Narrated in "+str(langlist[lang])+")\n\nHello there.\nThe no you bot is here to help.\nAfter this short therapy session, you wil regain your smile.\nThe no, u, bot is beautiful.\nYou can talk to him any time in his D M s.\nNo you bot is always there for you.\nNo, u, bot loves you.\nNo, u, bot will now stay here listening to your feelings for 30 minutes.```"
    else:
      voice.play(discord.FFmpegPCMAudio(shortfile))
      repli="```(Narrated in "+str(langlist[lang])+")\n\nHello there.\nThe no you bot is here to help.\nAfter this short therapy session, you wil regain your smile.\nThe no, u, bot is beautiful.\nYou can talk to him any time in his D M s.\nNo you bot is always there for you.\nNo, u, bot loves you.\nNo, u, bot will now stay here listening to your feelings for 5 minutes.```"
    await message.channel.send(repli)
    if msg.count("long")>=1:
      await asyncio.sleep(1470)
    await asyncio.sleep(330)
    voice.play(discord.FFmpegPCMAudio(endfile))
    await message.channel.send("```That is all the time we have for now.\nThank you for cooperation.\nRemember, you can always depend on no you bot.\n\nThank you for choosing no, u, bot.\nNo, u, bot loves you.```")
    await asyncio.sleep(20)
    await voice.disconnect()
  elif message.channel.id==789963285893742613 or message.channel.id==789969880543658004 or message.channel.id==789972540126134303 or message.channel.id==790174414062092298 or message.channel.id==790208541121576960 or message.channel.id==792756318779867176 or message.channel.id==863868862910955531 or message.channel.id==800707596477923358 or isinstance(message.channel, discord.channel.DMChannel) or msg.startswith("<@!745219622965346315>") or msg.startswith("<@745219622965346315>") or "<@!745219622965346315>" in msg or "<@745219622965346315>" in msg:
    if msg.startswith("!") or str(message.author)=="Chicktron#7799":
      return
    elif msg.endswith("?"):
      await message.channel.send(random.choice(questionchat))
    elif msg.endswith("what"):
      await message.channel.send("what")
    else:
      cunt=msg.count("<@745219622965346315>")
      cunt=cunt+msg.count("<@!745219622965346315>")
      if random.randint(1,11)==1 and cunt==1:
        dooble=str(str(random.choice(chat))+" "+str(random.choice(chat)))
        await message.channel.send(dooble)
      elif cunt==0:
        if random.randrange(25)==21:
          await message.channel.send(random.choice(allemojis))
        else:
          await message.channel.send(random.choice(chat))
      else:
        repli=str()
        for m in range(0,cunt):
          repli=(repli+random.choice(chat)+" ")
        await message.channel.send(repli)

    

client.run(TOKEN)

#https://discord.gg/adcZzvwKYG

#no u bot languages:
#0 - Italian (Vittorio)
#1 - French (Antoine)
#2 - Czech (Eliska)
#3 - German (Klaus)
#4 - Danish (Rasmus)
#5 - Swedish (Erik)
#6 - Dutch (Max)
#7 - Russian (Alyona)
#8 - Finnish (Sanna)
#9 - Turkish (Ipek)
#10 - Greek (DimitrisHappy)
#11 - Polish (Ania)
#12 - Arabic (Nizar)
#13 - Norwegian (Olav)
#14 - Korean (Minji)