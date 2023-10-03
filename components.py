from __future__ import annotations

from typing import Sequence, Union, Any, Optional, TypeVar, TYPE_CHECKING
import os
from discord import ApplicationContext, EmbedField, File, AllowedMentions, GuildSticker, Interaction, Message, MessageReference, StickerItem, WebhookMessage
from discord.abc import Messageable
from discord.colour import Colour
from discord.embeds import Embed, _EmptyEmbed, EmptyEmbed
from discord.ui import View
import datetime



if TYPE_CHECKING:
    from discord.types.embed import EmbedType
    T = TypeVar("T")
    MaybeEmpty = Union[T, _EmptyEmbed]

import discord
COLOR = discord.Color.blue()

class ColoredEmbed(Embed):

    def __init__(
        self,
        *,
        color: Union[int, Colour, _EmptyEmbed] = EmptyEmbed,
        title: MaybeEmpty[Any] = EmptyEmbed,
        type: EmbedType = "rich",
        url: MaybeEmpty[Any] = EmptyEmbed,
        description: MaybeEmpty[Any] = EmptyEmbed,
        timestamp: datetime.datetime = None,
        fields: Optional[list[EmbedField]] = None,
    ) -> None:
        super().__init__(
            colour=COLOR if color is EmptyEmbed else color,
            title=title,
            type=type,
            url=url,
            description=description,
            timestamp=timestamp,
            fields=fields
        )


class BotMessage():
    __slots__ = (
        'content',
        'tts',
        'embed',
        'embeds',
        'file',
        'files',
        'delete_after',
        'allowed_mentions',
        'view',
    )

    def __init__(
        self,
        content: Optional[str] = None,
        tts: bool = None,
        embed: Embed = None,
        embeds: list[Embed] = None,
        file: File = None,
        files: list[File] = None,
        delete_after: float = None,
        allowd_mentions: AllowedMentions = None,
        view: View = None,
    ) -> None:
        self.content: Optional[str] = content
        self.tts: bool = tts
        self.embed: Embed = embed
        self.embeds: list[Embed] = embeds
        self.file: File = file
        self.files: list[File] = files
        self.delete_after: float = delete_after
        self.allowed_mentions: AllowedMentions = allowd_mentions
        self.view: View = view

    async def send(
        self,
        msg: Messageable,
        stickers: Sequence[Union[GuildSticker, StickerItem]] = None,
        nonce: int = None,
        reference: Union[Message, MessageReference] = None,
        mention_author: Optional[bool] = None
    ) -> Message:
        return await msg.send(
            content = self.content,
            tts = self.tts,
            embed = self.embed,
            embeds = self.embeds,
            file = self.file,
            files = self.files,
            stickers = stickers,
            delete_after = self.delete_after,
            nonce = nonce,
            allowed_mentions = self.allowed_mentions,
            reference = reference,
            mention_author = mention_author,
            view = self.view
        )

    async def respond(
        self,
        ctx: ApplicationContext,
        ephemeral: bool = False
    ) -> Union[Interaction, WebhookMessage]:
        tts = False
        if self.tts is not None:
            tts = self.tts
        return await ctx.respond(
            content = self.content,
            embed = self.embed,
            embeds = self.embeds,
            view = self.view,
            tts = tts,
            ephemeral = ephemeral,
            allowed_mentions = self.allowed_mentions,
            file = self.file,
            files = self.files,
            delete_after = self.delete_after
        )