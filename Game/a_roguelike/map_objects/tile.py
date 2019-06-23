class Tile:

    def __init__(self, blocked, block_sight=None):
        self.blocked = blocked # 被挡住了就不能走。

        if block_sight is None:
            block_sight = blocked

        self.block_sight = block_sight