from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Sequence, Tuple

from .._hmm import HMM
from .._log import LOG0, LOG1
from .._path import CPath
from .._state import CState, MuteState


@dataclass
class Transitions:
    MM: float = LOG0
    MI: float = LOG0
    MD: float = LOG0
    IM: float = LOG0
    II: float = LOG0
    DM: float = LOG0
    DD: float = LOG0

    def normalize(self):
        from numpy import logaddexp

        m_norm: float = logaddexp(logaddexp(self.MM, self.MI), self.MD)
        self.MM -= m_norm
        self.MI -= m_norm
        self.MD -= m_norm

        i_norm: float = logaddexp(self.IM, self.II)
        self.IM -= i_norm
        self.II -= i_norm

        d_norm: float = logaddexp(self.DM, self.DD)
        self.DM -= d_norm
        self.DD -= d_norm


@dataclass
class SpecialTransitions:
    NN: float = 0.0
    NB: float = 0.0
    EC: float = 0.0
    CC: float = 0.0
    CT: float = 0.0
    EJ: float = 0.0
    JJ: float = 0.0
    JB: float = 0.0
    RR: float = 0.0
    BM: float = 0.0
    ME: float = 0.0


class Node(ABC):
    @property
    @abstractmethod
    def M(self) -> CState:
        raise NotImplementedError()

    @property
    @abstractmethod
    def I(self) -> CState:
        raise NotImplementedError()

    @property
    @abstractmethod
    def D(self) -> CState:
        raise NotImplementedError()


class SpecialNode(ABC):
    @property
    @abstractmethod
    def S(self) -> MuteState:
        raise NotImplementedError()

    @property
    @abstractmethod
    def N(self) -> CState:
        raise NotImplementedError()

    @property
    @abstractmethod
    def B(self) -> MuteState:
        raise NotImplementedError()

    @property
    @abstractmethod
    def E(self) -> MuteState:
        raise NotImplementedError()

    @property
    @abstractmethod
    def J(self) -> CState:
        raise NotImplementedError()

    @property
    @abstractmethod
    def C(self) -> CState:
        raise NotImplementedError()

    @property
    @abstractmethod
    def T(self) -> MuteState:
        raise NotImplementedError()


class NullModel(ABC):
    def __init__(self, state: CState):
        self._hmm = HMM(state.alphabet)
        self._hmm.add_state(state, LOG1)

    @property
    @abstractmethod
    def state(self) -> CState:
        raise NotImplementedError()

    def set_transition(self, lprob: float):
        self._hmm.set_transition(self.state, self.state, lprob)

    def likelihood(self, seq: bytes):
        path = CPath.create_cpath()
        for i in range(len(seq)):
            path.append_cstep(self.state, 1)
        return self._hmm.likelihood(seq, path)


class AltModel(ABC):
    def __init__(
        self,
        special_node: SpecialNode,
        core_nodes_trans: Sequence[Tuple[Node, Transitions]],
    ):
        hmm = HMM(special_node.S.alphabet)
        hmm.add_state(special_node.S, LOG1)
        hmm.add_state(special_node.N)
        hmm.add_state(special_node.B)
        hmm.add_state(special_node.E)
        hmm.add_state(special_node.J)
        hmm.add_state(special_node.C)
        hmm.add_state(special_node.T)

        self._special_transitions = SpecialTransitions()

        if len(core_nodes_trans) > 0:
            node, trans = core_nodes_trans[0]
            hmm.add_state(node.M)
            hmm.add_state(node.I)
            hmm.add_state(node.D)
            prev = node

            for node, trans in core_nodes_trans[1:]:
                hmm.add_state(node.M)
                hmm.add_state(node.I)
                hmm.add_state(node.D)

                hmm.set_transition(prev.M, node.M, trans.MM)
                hmm.set_transition(prev.M, prev.I, trans.MI)
                hmm.set_transition(prev.M, node.D, trans.MD)
                hmm.set_transition(prev.I, node.M, trans.IM)
                hmm.set_transition(prev.I, prev.I, trans.II)
                hmm.set_transition(prev.D, node.M, trans.DM)
                hmm.set_transition(prev.D, node.D, trans.DD)
                prev = node

        self._hmm = hmm

    def set_transition(self, a: CState, b: CState, lprob: float):
        self._hmm.set_transition(a, b, lprob)

    @abstractmethod
    def core_nodes(self) -> Sequence[Node]:
        raise NotImplementedError()

    @property
    @abstractmethod
    def special_node(self) -> SpecialNode:
        raise NotImplementedError()

    @property
    def special_transitions(self) -> SpecialTransitions:
        return self._special_transitions

    @property
    @abstractmethod
    def length(self) -> int:
        raise NotImplementedError()

    def viterbi(self, seq: bytes) -> Tuple[float, CPath]:
        return self._hmm.viterbi(seq, self.special_node.T)
