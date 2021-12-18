PLUGIN_METADATA = {
    'id': 'dimteleport',
    'version': '1.0.0',
    'name': 'dimTeleport',
    'description': 'A plugin to teleport cross dimension easily',
    'author': 'BlissfulAlloy79',
    'dependencies': {
        'mcdreforged': '>=1.0.0',
    }
}

CMDS = [
    'overworld',
    'nether',
    'end',
    'ow',
    'n',
    'e'
]


def on_info(server, info):
    args = info.content.split(' ')
    command = args[0][2:]
    pos = args[1:4]

    if not args[0].startswith('!!'):
        return
    if command not in CMDS:
        return
    if len(args) != 4:
        server.say('command error!')
        return

    if command == 'overworld' or command == 'ow':
        server.execute(f'execute in minecraft:overworld run teleport {info.player} {pos[0]} {pos[1]} {pos[2]}')
    if command == 'nether' or command == 'n':
        server.execute(f'execute in minecraft:the_nether run teleport {info.player} {pos[0]} {pos[1]} {pos[2]}')
    if command == 'end' or command == 'e':
        server.execute(f'execute in minecraft:the_end run teleport {info.player} {pos[0]} {pos[1]} {pos[2]}')
    return
