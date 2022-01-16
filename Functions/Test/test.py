# import discord
# from discord import slash_command
import discord
from discord.ext import commands

from methods.my_methods import is_me


# from discord_slash import cog_ext, SlashContext

class test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command()
    @is_me()
    async def length(self, ctx, sent):
        sentence = ctx.message.content[7:]
        length = len(sentence)
        i = 0
        count: int = 0
        while i < length - 1:
            i += 1
            if sentence[i] == " ":
                count += 1
        word = count + 1
        letter = i + 1
        await ctx.send(f"World count : {word}, letter count : {letter}")

    @commands.command()
    @is_me()
    async def t(self, ctx, sent):
        embed = discord.Embed(title="HORNY",
                              description="AHOY",
                              color=0xff0000, type='image')
        embed.add_field(name="Horny", value="AHOY")
        await ctx.send(embed=embed)
    #
    # @slash_command(guild_ids=[255440256638255105],
    #                description="AHOY")
    # async def test(self, ctx):
    #     embed = discord.Embed(title="HORNY",
    #                           description="AHOY",
    #                           color=0xff0000)
    #     embed.add_field(name="Horny", value="AHOY", inline=False)
    #     await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(test(bot))

#
# from PIL import Image
# import io
# import numpy as np
#
#
# def fibonacci(n):
#     a = 0
#     b = 1
#     if n < 0:
#         print("Incorrect input")
#     elif n == 0:
#         return 0
#     elif n == 1:
#         return b
#     else:
#         for i in range(1, n):
#             c = a + b
#             a = b
#             b = c
#         return b
#
#
# def pos(before, after=None):
#     if after is None:
#         after = [0, 0, 0, 0]
#     final = [0,0,0,0]
#     l = len(before)
#     for i, val in enumerate(before.copy()):
#         # if before[i] == after[i]:
#         if i == l:
#             final[i]=val
#         elif len(after)>i and before[i] < after[i]:
#             final[i]=fibonacci(after[i]) % 254
#         # final.append(random.randint(fibonacci(after[i])%255, 255))
#         # elif len(after) > i:
#         #     final[i]=fibonacci(after[i]) % 255
#         else:
#             final[i]=fibonacci(before[i]) % 255
#             # final.append(random.randint(fibonacci(before[i])%255, 255))
#     # print(final)
#     return final
#
#
# img = Image.open("4.png")
# output = io.BytesIO()
# img_np = np.array(img)
# for i in range(len(img_np.copy())):
#     for j in range(l := len(img_np[i].copy())):
#         # print(img_np[i][j])
#         if j > 0 and j < l - 1:
#             before = img_np[i][j - 1]
#             after = img_np[i][j + 1]
#             img_np[i][j] = pos(before,after)
#         else:
#             img_np[i][j] = pos(img_np[i][j])
#         # # print("b",img_np[i][j])
#         # if j > 0 and j < l - 1:
#         #     before = img_np[i][j - 1]
#         #     after = img_np[i][j + 1]
#         #     img_np[i][j] = pos(before, after)
#         # else:
#         #     before = after = img_np[i][j]
#         #     img_np[i][j] = pos(before, after)
#         # print("a",img_np[i][j])
# img = Image.fromarray(img_np)
# img.show()
# img.save("output.png", format='Png')
# # hex_val = output.getvalue()
#
# # l = len(hex_val)
# # new_hex = [0 for i in list(hex_val)]
# #
# #
# # def pos(before, after):
# #     if before < after:
# #         return random.randint(before, after)
# #     else:
# #         return random.randint(after, before)
# #
# #
# # for i, val in enumerate(hex_val):
# #     # print(val,type(val))
# #     if i > 0 and i < l - 1:
# #         before = hex_val[i - 1]
# #         after = hex_val[i + 1]
# #         new_hex[i] = pos(before, after)
# #     else:
# #         before = after = hex_val[i]
# #         new_hex[i] = pos(before, after)
# # # img.save(bytearray(new_hex), format='Png')
# # Image.open(bytearray(new_hex))
# # img.show()
# # img.save(output, format='Png')
# # img.show()
