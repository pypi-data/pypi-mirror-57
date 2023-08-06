from __future__ import absolute_import, annotations

import logging
from dataclasses import dataclass, field
from typing import Any, Optional, List, Dict, Set

import networkx as nx
import pygraphviz as gv
from spacy.language import Language
import pendulum

from . import utils, dt
from .node import Node
from .analysis import Analysis


@dataclass
class Edge:
    """Edge in AIF format.

    Attributes `from` and `to` are mandatory.
    """

    start: Node
    end: Node
    key: int = field(default_factory=utils.unique_id)
    visible: bool = None
    annotator: str = None
    date: pendulum.DateTime = field(default_factory=pendulum.now)

    @property
    def _uid(self):
        return (self.key, self.start.key, self.end.key)

    def __hash__(self):
        return hash(self._uid)

    @staticmethod
    def from_ova(
        obj: Any, nodes: Dict[int, Node] = None, nlp: Optional[Language] = None
    ) -> Edge:
        if not nodes:
            nodes = {}

        start_key = int(obj.get("from").get("id"))
        end_key = int(obj.get("to").get("id"))

        return Edge(
            start=nodes.get(start_key) or Node.from_ova(obj.get("from"), nlp),
            end=nodes.get(end_key) or Node.from_ova(obj.get("to"), nlp),
            visible=obj.get("visible"),
            annotator=obj.get("annotator"),
            date=dt.from_ova(obj.get("date")),
        )

    def to_ova(self) -> dict:
        return {
            "from": self.start.to_ova(),
            "to": self.end.to_ova(),
            "visible": self.visible,
            "annotator": self.annotator,
            "date": dt.to_ova(self.date),
        }

    @staticmethod
    def from_aif(
        obj: Any, nodes: Dict[int, Node], nlp: Optional[Language] = None
    ) -> Edge:
        start_key = int(obj.get("fromID"))
        end_key = int(obj.get("toID"))

        return Edge(
            start=nodes.get(start_key),
            end=nodes.get(end_key),
            key=int(obj.get("edgeID")),
        )

    def to_aif(self) -> dict:
        return {
            "edgeID": str(self.key),
            "fromID": str(self.start.key),
            "toID": str(self.end.key),
            "formEdgeID": None,
        }

    def to_nx(self, g: nx.DiGraph) -> None:
        g.add_edge(self.start.key, self.end.key)

    def to_gv(
        self, g: gv.AGraph, color="#666666", prefix: str = "", suffix: str = ""
    ) -> None:
        g.add_edge(
            f"{prefix}{self.start.key}{suffix}",
            f"{prefix}{self.end.key}{suffix}",
            color=color,
        )

    def __eq__(self, other: Edge) -> bool:
        return self.start == other.start and self.end == other.end
