from typing import Dict, List, Sequence, Tuple, Union

from .._ffi import ffi
from .._state import MuteState, NormalState
from .model import AltModel, Node, NullModel, SpecialNode, Transitions
from .standard import StandardPath


class StandardNode(Node):
    def __init__(self, M: NormalState, I: NormalState, D: MuteState):
        self._M = M
        self._I = I
        self._D = D

    @property
    def M(self) -> NormalState:
        return self._M

    @property
    def I(self) -> NormalState:
        return self._I

    @property
    def D(self) -> MuteState:
        return self._D

    def states(self) -> List[Union[MuteState, NormalState]]:
        return [self._M, self._I, self._D]


class StandardSpecialNode(SpecialNode):
    def __init__(
        self,
        S: MuteState,
        N: NormalState,
        B: MuteState,
        E: MuteState,
        J: NormalState,
        C: NormalState,
        T: MuteState,
    ):
        self._S = S
        self._N = N
        self._B = B
        self._E = E
        self._J = J
        self._C = C
        self._T = T

    @property
    def S(self) -> MuteState:
        return self._S

    @property
    def N(self) -> NormalState:
        return self._N

    @property
    def B(self) -> MuteState:
        return self._B

    @property
    def E(self) -> MuteState:
        return self._E

    @property
    def J(self) -> NormalState:
        return self._J

    @property
    def C(self) -> NormalState:
        return self._C

    @property
    def T(self) -> MuteState:
        return self._T

    def states(self) -> List[Union[MuteState, NormalState]]:
        return [self._S, self._N, self._B, self._E, self._J, self._C, self._T]


class StandardNullModel(NullModel):
    def __init__(self, state: NormalState):
        super().__init__(state)
        self._normal_state = state

    @property
    def state(self) -> NormalState:
        return self._normal_state


class StandardAltModel(AltModel):
    def __init__(
        self,
        special_node: StandardSpecialNode,
        nodes_trans: Sequence[Tuple[StandardNode, Transitions]],
    ):
        self._special_node = special_node
        self._core_nodes = [nt[0] for nt in nodes_trans]
        self._states: Dict[ffi.CData, Union[MuteState, NormalState]] = {}

        for node in self._core_nodes:
            for state in node.states():
                self._states[state.imm_state] = state

        for state in special_node.states():
            self._states[state.imm_state] = state

        super().__init__(special_node, nodes_trans)

    @property
    def length(self):
        return len(self._core_nodes)

    def core_nodes(self) -> Sequence[StandardNode]:
        return self._core_nodes

    @property
    def special_node(self) -> StandardSpecialNode:
        return self._special_node

    def viterbi(self, seq: bytes) -> Tuple[float, StandardPath]:
        score, path = super().viterbi(seq)

        spath = StandardPath()
        for step in path.steps():
            imm_state = step.state.imm_state
            spath.append_standard_step(self._states[imm_state], step.seq_len)

        return (score, spath)
