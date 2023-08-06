from math import log

from .._log import LOG0, LOG1
from .model import AltModel, NullModel
from .result import SearchResult


class Profile:
    def __init__(self):
        self._multiple_hits: bool = True

    @property
    def null_model(self) -> NullModel:
        raise NotImplementedError()

    @property
    def alt_model(self) -> AltModel:
        raise NotImplementedError()

    @property
    def multiple_hits(self) -> bool:
        return self._multiple_hits

    @multiple_hits.setter
    def multiple_hits(self, multiple_hits: bool):
        self._multiple_hits = multiple_hits

    def search(self, seq: bytes) -> SearchResult:
        del seq
        raise NotImplementedError()

    def _set_fragment_length(self):
        if self.alt_model.length == 0:
            return

        B = self.alt_model.special_node.B
        E = self.alt_model.special_node.E

        # Uniform local alignment fragment length distribution
        t = self.alt_model.special_transitions
        t.BM = log(2) - log(self.alt_model.length) - log(self.alt_model.length + 1)
        t.ME = 0.0
        for node in self.alt_model.core_nodes():
            self.alt_model.set_transition(B, node.M, t.BM)
            self.alt_model.set_transition(node.M, E, t.ME)

        for node in self.alt_model.core_nodes()[1:]:
            self.alt_model.set_transition(node.D, E, 0.0)

    def _set_target_length(self, length: int):
        from math import exp

        L = length
        if L == 0:
            return

        if self._multiple_hits:
            l1q = lq = -log(2)
        else:
            lq = LOG0
            l1q = LOG1

        q = exp(lq)
        lp = log(L) - log(L + 2 + q / (1 - q))
        l1p = log(2 + q / (1 - q)) - log(L + 2 + q / (1 - q))
        lr = log(L) - log(L + 1)

        t = self.alt_model.special_transitions

        t.NN = t.CC = t.JJ = lp
        t.NB = t.CT = t.JB = l1p
        t.RR = lr
        t.EJ = lq
        t.EC = l1q

        node = self.alt_model.special_node

        self.alt_model.set_transition(node.S, node.B, t.NB)
        self.alt_model.set_transition(node.S, node.N, t.NN)
        self.alt_model.set_transition(node.N, node.N, t.NN)
        self.alt_model.set_transition(node.N, node.B, t.NB)

        self.alt_model.set_transition(node.E, node.T, t.EC + t.CT)
        self.alt_model.set_transition(node.E, node.C, t.EC + t.CC)
        self.alt_model.set_transition(node.C, node.C, t.CC)
        self.alt_model.set_transition(node.C, node.T, t.CT)

        self.alt_model.set_transition(node.E, node.B, t.EJ + t.JB)
        self.alt_model.set_transition(node.E, node.J, t.EJ + t.JJ)
        self.alt_model.set_transition(node.J, node.J, t.JJ)
        self.alt_model.set_transition(node.J, node.B, t.JB)

        self.null_model.set_transition(t.RR)
