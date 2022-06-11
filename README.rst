.. image:: https://raw.githubusercontent.com/abindent/nextwave/master/wave.PNG


.. image:: https://img.shields.io/badge/Python-3.8%20%7C%203.9%20%7C%203.10-blue.svg
    :target: https://www.python.org


.. image:: https://img.shields.io/github/license/EvieePy/Wavelink.svg
    :target: LICENSE



.. image:: https://img.shields.io/pypi/dm/nextwave?color=black
    :target: https://pypi.org/project/nextwave
    :alt: PyPI - Downloads
    
    
.. image:: https://img.shields.io/maintenance/yes/2022?color=pink&style=for-the-badge
    :target: https://github.com/abindent/nextwave/commits/master
    :alt: Maintenance


Nextwave is a fork of the package `Wavelink <https://github.com/PythonistaGuild/Wavelink>`_.
Nextwave is a robust and powerful Lavalink wrapper for `Nextcord.py <https://github.com/nextcord/nextcord>`_.
Nextwave features a fully asynchronous API that's intuitive and easy to use with built in Spotify Support and Node Pool Balancing.

Documentation
---------------------------
`Nextwave Official Documentation <https://docs.nextwave.epizy.com/en/latest/>`_ .


Installation
---------------------------
The following commands are currently the valid ways of installing WaveLink.

**Nextwave requires Python 3.8+**

**Windows**

.. code:: sh

    py -3.9 -m pip install -U nextwave

**Linux**

.. code:: sh

    python3.9 -m pip install -U nextwave

Getting Started
----------------------------

A quick and easy bot example:

.. code:: py
    
    import nextwave
    from nextcord.ext import commands


    class Bot(commands.Bot):

        def __init__(self):
            super().__init__(command_prefix='>?')

        async def on_ready(self):
            print('Bot is ready!')


    class Music(commands.Cog):
        """Music cog to hold Wavelink related commands and listeners."""

        def __init__(self, bot: commands.Bot):
            self.bot = bot

            bot.loop.create_task(self.connect_nodes())

        async def connect_nodes(self):
            """Connect to our Lavalink nodes."""
            await self.bot.wait_until_ready()

            await nextwave.NodePool.create_node(bot=bot,
                                                host='0.0.0.0',
                                                port=2333,
                                                password='YOUR_LAVALINK_PASSWORD')

        @commands.Cog.listener()
        async def on_nextwave_node_ready(self, node: nextwave.Node):
            """Event fired when a node has finished connecting."""
            print(f'Node: <{node.identifier}> is ready!')

        @commands.command()
        async def play(self, ctx: commands.Context, *, search: nextwave.YouTubeTrack):
            """Play a song with the given search query.

            If not connected, connect to our voice channel.
            """
            if not ctx.voice_client:
                vc: nextwave.Player = await ctx.author.voice.channel.connect(cls=wavelink.Player)
            else:
                vc: nextwave.Player = ctx.voice_client

            await vc.play(search)


    bot = Bot()
    bot.add_cog(Music(bot))
    bot.run('YOUR_BOT_TOKEN')


Lavalink Installation
---------------------

Head to the official `Lavalink repo <https://github.com/freyacodes/Lavalink#server-configuration>`_ and give it a star!

- Create a folder for storing Lavalink.jar and related files/folders.
- Copy and paste the example `application.yml <https://github.com/freyacodes/Lavalink#server-configuration>`_ to ``application.yml`` in the folder we created earlier. You can open the yml in Notepad or any simple text editor.
- Change your password in the ``application.yml`` and store it in a config for your bot.
- Set local to true in the ``application.yml`` if you wish to use ``nextwave.LocalTrack`` for local machine search options... Otherwise ignore.
- Save and exit.
- Install `Java 17(Windows) <https://download.oracle.com/java/17/latest/jdk-17_windows-x64_bin.exe>`_ or **Java 13+** on the machine you are running.
- Download `Lavalink.jar <https://ci.fredboat.com/viewLog.html?buildId=lastSuccessful&buildTypeId=Lavalink_Build&tab=artifacts&guest=1>`_ and place it in the folder created earlier.
- Open a cmd prompt or terminal and change directory ``cd`` into the folder we made earlier.
- Run: ``java -jar Lavalink.jar``

If you are having any problems installing Lavalink, please join the official Discord Server listed above for help.
