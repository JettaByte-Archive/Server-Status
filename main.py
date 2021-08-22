import os

import discord
import socket
from discord.ext import commands
import requests
from discord.ext.commands import bot

client = commands.Bot(command_prefix="!")

@client.event
async def on_ready():
    print("봇의 가동준비 완료")
    activity = discord.Game(name="전세계 모든 서버의 상태를 확인")
    await client.change_presence(status=discord.Status.idle, activity=activity)
    
@client.command()
async def Server(ctx, arg):
    hostname = arg

    response = os.system("ping -n 1 " + hostname)



    if response == 0:


        embed = discord.Embed(title="서버가 정상 상태입니다", description="서버가 정상적으로 응답하는 정상 상태입니다.", color=0x3BF17B)
        embed.set_author(name="서버 상태",
                         icon_url="https://png.pngtree.com/png-vector/20190115/ourlarge/pngtree-vector-server-icon-png-image_316791.jpg")
        embed.set_thumbnail(url="https://icon-library.net/images/v-icon/v-icon-11.jpg")
        embed.add_field(name="", value="", inline=False)
        embed.set_footer(text="귀하의 PING 요청은 SSO ▪ LC GLOBAL SERVER 대한민국 중부에서 처리되었습니다.")
        await ctx.send(embed=embed)


    else:


        embed = discord.Embed(title="서버가 응답하지 않습니다.", description="서버가 응답하지 않습니다.IP를 잘못 입력했거나 서버에서 PING 요청에 응답하지 않는것이 원인일수 있습니다.", color=0xFD3030)
        embed.set_author(name="서버 상태",
                         icon_url="https://png.pngtree.com/png-vector/20190115/ourlarge/pngtree-vector-server-icon-png-image_316791.jpg")
        embed.set_thumbnail(url="https://icon-library.net/images/v-icon/v-icon-11.jpg")
        embed.add_field(name="", value="", inline=False)
        embed.set_footer(text="귀하의 PING 요청은 SSO ▪ LC GLOBAL SERVER 대한민국 중부에서 처리되었습니다.")
        await ctx.send(embed=embed)



@client.command()
async def server(ctx, arg):
    hostname = arg

    response = os.system("ping -n 1 " + hostname)

    if response == 0:


        embed = discord.Embed(title="서버가 정상 상태입니다", description="서버가 정상적으로 응답하는 정상 상태입니다.", color=0x3BF17B)
        embed.set_author(name="서버 상태",
                         icon_url="https://png.pngtree.com/png-vector/20190115/ourlarge/pngtree-vector-server-icon-png-image_316791.jpg")
        embed.set_footer(text="귀하의 PING 요청은 SSO ▪ LC GLOBAL SERVER 대한민국 중부에서 처리되었습니다.")
        embed.set_thumbnail(url="https://icon-library.net/images/v-icon/v-icon-11.jpg")
        await ctx.send(embed=embed)

    else:


        embed = discord.Embed(title="서버가 응답하지 않습니다.", description="서버가 응답하지 않습니다.IP를 잘못 입력했거나 서버에서 PING 요청에 응답하지 않는것이 원인일수 있습니다.", color=0xFD3030)
        embed.set_author(name="서버 상태",
                         icon_url="https://png.pngtree.com/png-vector/20190115/ourlarge/pngtree-vector-server-icon-png-image_316791.jpg")
        embed.set_footer(text="귀하의 PING 요청은 SSO ▪ LC GLOBAL SERVER 대한민국 중부에서 처리되었습니다.")
        embed.set_thumbnail(url="https://uxwing.com/wp-content/themes/uxwing/download/01-user_interface/red-x.png")
        await ctx.send(embed=embed)




client.run('ODE5NDg3NTg0OTQxNjM3NjYz.YEnVSQ.gHVUQhe4agC8mA9S563jgbepd2o')