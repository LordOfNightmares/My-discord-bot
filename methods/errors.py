async def error_not_owner(ctx):
    '''Handle not being the Bot Owner'''
    errormessage = 'Only the `Bot Owner` can run this command'
    await ctx.respond(errormessage, ephemeral=True)


async def error_permission(ctx, attach=False):
    '''Handle a lack of the Send Messages or Attach Files permission'''
    attach_substring = ' / `Attach Files`' if attach else ''
    errormessage = (f'Failed, I need the `Send Messages`{attach_substring} '
                    'permission in this channel')

    await ctx.respond(errormessage, ephemeral=True)
