.. currentmodule:: nextwave


Event Reference
---------------

WaveLink Events are events dispatched when certain events happen in Lavalink and Nextwave.
All events must be coroutines.

Events are dispatched via nextcord and as such can be used with listener syntax.

**For example:**

An event listener in a cog...

.. code-block:: python3

    @commands.Cog.listener()
    async def on_nextwave_node_ready(node: Node):
        print(f"Node {node.id} is ready!")


.. function:: on_nextwave_node_ready(node: Node)

    Called when the Node you are connecting to has initialised and successfully connected to Lavalink.

.. function:: on_nextwave_websocket_closed(player: Player, reason, code)

    Called when the Node websocket has been closed by Lavalink.

.. function:: on_nextwave_track_start(player: Player, track: Track)

    Called when a track starts playing.

.. function:: on_nextwave_track_end(player: player, track: Track, reason)

    Called when the current track has finished playing.

.. function:: on_nextwave_track_exception(player: Player, track: Track, error)

    Called when a TrackException occurs in Lavalink.

.. function:: on_nextwave_track_stuck(player: Player, track: Track, threshold)

    Called when a TrackStuck occurs in Lavalink.


Abstract Base Classes
---------------------

.. autoclass:: nextwave.abc.Playable
    :members:

.. autoclass:: nextwave.abc.Searchable
    :members:

.. autoclass:: nextwave.abc.Playlist
    :members:

NodePool
--------
.. attributetable:: NodePool

.. autoclass:: NodePool
    :members:

Node
----

.. attributetable:: Node

.. autoclass:: Node
    :members:

Tracks
------

Track
~~~~~

.. attributetable:: Track

.. autoclass:: Track
    :members:

SearchableTrack
~~~~~~~~~~~~~~~

.. attributetable:: SearchableTrack

.. autoclass:: SearchableTrack
    :members:

YouTubeTrack
~~~~~~~~~~~~

.. attributetable:: YouTubeTrack

.. autoclass:: YouTubeTrack
    :members:

YouTubeMusicTrack
~~~~~~~~~~~~~~~~~

.. attributetable:: YouTubeMusicTrack

.. autoclass:: YouTubeMusicTrack
    :members:

SoundCloudTrack
~~~~~~~~~~~~~~~

.. attributetable:: SoundCloudTrack

.. autoclass:: SoundCloudTrack
    :members:

YouTubePlaylist
~~~~~~~~~~~~~~~

.. attributetable:: YouTubePlaylist

.. autoclass:: YouTubePlaylist
    :members:

PartialTrack
~~~~~~~~~~~~

.. attributetable:: PartialTrack

.. autoclass:: PartialTrack

LocalTrack
~~~~~~~~~~

.. attributetable:: LocalTrack

.. autoclass:: LocalTrack
    :members:

Player
------

.. attributetable:: Player

.. autoclass:: Player
    :members:

Queues
------

.. attributetable:: Queue

.. autoclass:: Queue
    :members:

.. attributetable:: WaitQueue

.. autoclass:: WaitQueue
    :members:


Filters
-------

.. attributeable:: Filter

.. autoclass:: Filter
    :members:

.. attributeable:: Equalizer

.. autoclass:: Equalizer
    :members:

.. attributeable:: Karaoke

.. autoclass:: Karaoke
    :members:

.. attributeable:: Timescale

.. autoclass:: Timescale
    :members:

.. attributeable:: Tremolo

.. autoclass:: Tremolo
    :members:

.. attributeable:: Vibrato

.. autoclass:: Vibrato
    :members:

.. attributeable:: Rotation

.. autoclass:: Rotation
    :members:

.. attributeable:: Distortion

.. autoclass:: Distortion
    :members:

.. attributeable:: ChannelMix

.. autoclass:: ChannelMix
    :members:

.. attributeable:: LowPass

.. autoclass:: LowPass
    :members:


Exceptions
----------

.. py:exception:: NextwaveError
.. py:exception:: AuthorizationFailure
.. py:exception:: LavalinkException
.. py:exception:: LoadTrackError
.. py:exception:: BuildTrackError
.. py:exception:: NodeOccupied
.. py:exception:: InvalidIDProvided
.. py:exception:: ZeroConnectedNodes
.. py:exception:: NoMatchingNode
.. py:exception:: QueueException
.. py:exception:: QueueFull
.. py:exception:: QueueEmpty