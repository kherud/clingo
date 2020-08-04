# DO NOT EDIT THIS FILE! It was generated by scratch/mypy.py.

from typing import *
from abc import *

from .types import Comparable, Lookup
from . import ast


Infimum: Symbol
Supremum: Symbol
__version__: str


def Function(name: str, arguments: Iterable[Symbol]=[], positive: bool=True) -> Symbol: ...
def Number(number: int) -> Symbol: ...
def String(string: str) -> Symbol: ...
def Tuple_(arguments: Iterable[Symbol]) -> Symbol: ...
def clingo_main(application: Application, files: Iterable[str]=[]) -> int: ...
def parse_program(program: str, callback: Callable[[ast.AST], None]) -> None: ...
def parse_term(string: str, logger: Callable[[MessageCode,str],None]=None, message_limit: int=20) -> Symbol: ...


class Application(metaclass=ABCMeta):
    @abstractmethod
    def main(self, control: Control, files: Sequence[str]) -> None: ...
    def register_options(self, options: ApplicationOptions) -> None: ...
    def validate_options(self) -> bool: ...
    def logger(self, code: MessageCode, message: str) -> None: ...
    program_name: str = 'clingo'
    message_limit: int = 20

class Propagator(metaclass=ABCMeta):
    def init(self, init: PropagateInit) -> None: ...
    def propagate(self, control: PropagateControl, changes: Sequence[int]) -> None: ...
    def undo(self, thread_id: int, assignment: Assignment, changes: Sequence[int]) -> None: ...
    def check(self, control: PropagateControl) -> None: ...
    def decide(self, thread_id: int, assignment: Assignment, fallback: int) -> int: ...

class Observer(metaclass=ABCMeta):
    def init_program(self, incremental: bool) -> None: ...
    def begin_step(self) -> None: ...
    def rule(self, choice: bool, head: Sequence[int], body: Sequence[int]) -> None: ...
    def weight_rule(self, choice: bool, head: Sequence[int], lower_bound: int, body: Sequence[Tuple[int,int]]) -> None: ...
    def minimize(self, priority: int, literals: Sequence[Tuple[int,int]]) -> None: ...
    def project(self, atoms: Sequence[int]) -> None: ...
    def output_atom(self, symbol: Symbol, atom: int) -> None: ...
    def output_term(self, symbol: Symbol, condition: Sequence[int]) -> None: ...
    def output_csp(self, symbol: Symbol, value: int, condition: Sequence[int]) -> None: ...
    def external(self, atom: int, value: TruthValue) -> None: ...
    def assume(self, literals: Sequence[int]) -> None: ...
    def heuristic(self, atom: int, type: HeuristicType, bias: int, priority: int, condition: Sequence[int]) -> None: ...
    def acyc_edge(self, node_u: int, node_v: int, condition: Sequence[int]) -> None: ...
    def theory_term_number(self, term_id: int, number: int) -> None: ...
    def theory_term_string(self, term_id : int, name : str) -> None: ...
    def theory_term_compound(self, term_id: int, name_id_or_type: int, arguments: Sequence[int]) -> None: ...
    def theory_element(self, element_id: int, terms: Sequence[int], condition: Sequence[int]) -> None: ...
    def theory_atom(self, atom_id_or_zero: int, term_id: int, elements: Sequence[int]) -> None: ...
    def theory_atom_with_guard(self, atom_id_or_zero: int, term_id: int, elements: Sequence[int], operator_id: int, right_hand_side_id: int) -> None: ...
    def end_step(self) -> None: ...

class ApplicationOptions(metaclass=ABCMeta):
    def add(self, group: str, option: str, description: str, parser: Callable[[str], bool], multi: bool=False, argument: str=None) -> None: ...
    def add_flag(self, group: str, option: str, description: str, target: Flag) -> None: ...

class Assignment(Sequence[int], metaclass=ABCMeta):
    def decision(self, level: int) -> int: ...
    def has_literal(self, literal : int) -> bool: ...
    def is_false(self, literal: int) -> bool: ...
    def is_fixed(self, literal: int) -> bool: ...
    def is_true(self, literal: int) -> bool: ...
    def level(self, literal: int) -> int: ...
    def value(self, literal) -> Optional[bool]: ...
    decision_level: int
    has_conflict: bool
    is_total: bool
    root_level: int
    trail: Trail

class Backend(ContextManager[Backend], metaclass=ABCMeta):
    def add_acyc_edge(self, node_u: int, node_v: int, condition: Iterable[int]) -> None: ...
    def add_assume(self, literals: Iterable[int]) -> None: ...
    def add_atom(self, symbol : Optional[Symbol]=None) -> int: ...
    def add_external(self, atom : int, value : TruthValue=TruthValue.False_) -> None: ...
    def add_heuristic(self, atom: int, type: HeuristicType, bias: int, priority: int, condition: Iterable[int]) -> None: ...
    def add_minimize(self, priority: int, literals: Iterable[Tuple[int,int]]) -> None: ...
    def add_project(self, atoms: Iterable[int]) -> None: ...
    def add_rule(self, head: Iterable[int], body: Iterable[int]=[], choice: bool=False) -> None: ...
    def add_weight_rule(self, head: Iterable[int], lower: int, body: Iterable[Tuple[int,int]], choice: bool=False) -> None: ...

class Configuration(metaclass=ABCMeta):
    def description(self, name: str) -> str: ...
    keys: Optional[List[str]]

class Control:
    def __init__(self, arguments: Iterable[str]=[], logger: Callable[[MessageCode,str],None]=None, message_limit: int=20): ...
    def add(self, name: str, parameters: Iterable[str], program: str) -> None: ...
    def assign_external(self, external: Union[Symbol,int], truth: Optional[bool]) -> None: ...
    def backend(self) -> Backend: ...
    def builder(self) -> ProgramBuilder: ...
    def cleanup(self) -> None: ...
    def get_const(self, name: str) -> Optional[Symbol]: ...
    def ground(self, parts: Iterable[Tuple[str,Iterable[Symbol]]], context: Any=None) -> None: ...
    def interrupt(self) -> None: ...
    def load(self, path: str) -> None: ...
    def register_observer(self, observer: Observer, replace: bool=False) -> None: ...
    def register_propagator(self, propagator: Propagator) -> None: ...
    def release_external(self, symbol: Union[Symbol,int]) -> None: ...
    def solve(self, assumptions: Iterable[Union[Tuple[Symbol,bool],int]]=[], on_model: Callable[[Model],Optional[bool]]=None, on_statistics : Callable[[StatisticsMap,StatisticsMap],None]=None, on_finish: Callable[[SolveResult],None]=None, on_core: Callable[[Sequence[int]],None]=None, yield_: bool=False, async_: bool=False) -> Union[SolveHandle,SolveResult]: ...
    configuration: Configuration
    enable_cleanup: bool
    enable_enumeration_assumption: bool
    is_conflicting: bool
    statistics: dict
    symbolic_atoms: SymbolicAtoms
    theory_atoms: TheoryAtomIter

class Flag:
    def __init__(self, value: bool=False): ...
    flag: bool

class HeuristicType(Hashable, Comparable, metaclass=ABCMeta):
    Factor: HeuristicType
    False_: HeuristicType
    Init: HeuristicType
    Level: HeuristicType
    Sign: HeuristicType
    True_: HeuristicType

class MessageCode(Hashable, Comparable, metaclass=ABCMeta):
    AtomUndefined: MessageCode
    FileIncluded: MessageCode
    GlobalVariable: MessageCode
    OperationUndefined: MessageCode
    Other: MessageCode
    RuntimeError: MessageCode
    VariableUnbounded: MessageCode

class Model(metaclass=ABCMeta):
    def contains(self, atom: Symbol) -> bool: ...
    def extend(self, symbols: Iterable[Symbol]) -> None: ...
    def is_true(self, literal: int) -> bool: ...
    def symbols(self, atoms: bool=False, terms: bool=False, shown: bool=False, csp: bool=False, theory: bool=False, complement: bool=False) -> List[Symbol]: ...
    context: SolveControl
    cost: List[int]
    number: int
    optimality_proven: bool
    thread_id: int
    type: ModelType

class ModelType(Hashable, Comparable, metaclass=ABCMeta):
    BraveConsequences: ModelType
    CautiousConsequences: ModelType
    StableModel: ModelType

class ProgramBuilder(ContextManager[ProgramBuilder], metaclass=ABCMeta):
    def add(self, statement: ast.AST) -> None: ...

class PropagateControl(metaclass=ABCMeta):
    def add_clause(self, clause: Iterable[int], tag: bool=False, lock: bool=False) -> bool: ...
    def add_literal(self) -> int: ...
    def add_nogood(self, clause: Iterable[int], tag: bool=False, lock: bool=False) -> bool: ...
    def add_watch(self, literal: int) -> None: ...
    def has_watch(self, literal: int) -> bool: ...
    def propagate(self) -> bool: ...
    def remove_watch(self, literal: int) -> None: ...
    assignment: Assignment
    thread_id: int

class PropagateInit(metaclass=ABCMeta):
    def add_clause(self, clause: Iterable[int]) -> bool: ...
    def add_literal(self, freeze: bool=True) -> int: ...
    def add_minimize(self, literal: int, weight: int, priority: int=0) -> None: ...
    def add_watch(self, literal: int, thread_id: Optional[int]=None) -> None: ...
    def add_weight_constraint(self, literal: int, literals: Iterable[Tuple[int,int]], bound: int, type: int=0, compare_equal: bool=False) -> bool: ...
    def propagate(self) -> bool: ...
    def solver_literal(self, literal: int) -> int: ...
    assignment: Assignment
    check_mode: PropagatorCheckMode
    number_of_threads: int
    symbolic_atoms: SymbolicAtoms
    theory_atom: TheoryAtomIter

class PropagatorCheckMode(Hashable, Comparable, metaclass=ABCMeta):
    Both: PropagatorCheckMode
    Fixpoint: PropagatorCheckMode
    Off: PropagatorCheckMode
    Total: PropagatorCheckMode

class SolveControl(metaclass=ABCMeta):
    def add_clause(self, literals: Iterable[Union[Tuple[Symbol,bool],int]]) -> None: ...
    def add_nogood(self, literals: Iterable[Union[Tuple[Symbol,bool],int]]) -> None: ...
    symbolic_atoms: SymbolicAtoms

class SolveHandle(ContextManager[SolveHandle], metaclass=ABCMeta):
    def cancel(self) -> None: ...
    def core(self) -> List[int]: ...
    def get(self) -> SolveResult: ...
    def model(self) -> Optional[Model]: ...
    def resume(self) -> None: ...
    def wait(self, timeout: Optional[float]=None) -> bool: ...

class SolveResult(metaclass=ABCMeta):
    exhausted: bool
    interruped: bool
    satisfiable: Optional[bool]
    unknown: bool
    unsatisfiable: Optional[bool]

class StatisticsArray(MutableSequence[Union[StatisticsArray,StatisticsMap,float]], metaclass=ABCMeta):
    def append(self, value: Any) -> None: ...
    def extend(self, values: Iterable[Any]) -> None: ...
    def update(self, values: Sequence[Any]) -> None: ...

class StatisticsMap(Mapping[str,Union[StatisticsArray,StatisticsMap,float]], metaclass=ABCMeta):
    def items(self) -> AbstractSet[Tuple[str, Union[StatisticsArray,StatisticsMap,float]]]: ...
    def keys(self) -> AbstractSet[str]: ...
    def update(self, values: Mapping[str,Any]) -> None: ...
    def values(self) -> ValuesView[Union[StatisticsArray,StatisticsMap,float]]: ...

class Symbol(Hashable, Comparable, metaclass=ABCMeta):
    def match(self, name: str, arity: int) -> bool: ...
    arguments: List[Symbol]
    name: str
    negative: bool
    number: int
    positive: bool
    string: str
    type: SymbolType

class SymbolType(Hashable, Comparable, metaclass=ABCMeta):
    Function: SymbolType
    Infimum: SymbolType
    Number: SymbolType
    String: SymbolType
    Supremum: SymbolType

class SymbolicAtom(metaclass=ABCMeta):
    def match(self, name: str, arity: int) -> bool: ...
    is_external: bool
    is_fact: bool
    literal: int
    symbol: Symbol

class SymbolicAtomIter(Iterator[SymbolicAtom], metaclass=ABCMeta):
    pass

class SymbolicAtoms(Lookup[Union[Symbol,int],SymbolicAtom], metaclass=ABCMeta):
    def by_signature(self, name: str, arity: int, positive: bool=True) -> Iterator[SymbolicAtom]: ...
    signatures: List[Tuple[str,int,bool]]

class TheoryAtom(metaclass=ABCMeta):
    elements: List[TheoryElement]
    guard: Tuple[str, TheoryTerm]
    literal: int
    term: TheoryTerm

class TheoryAtomIter(Iterator[TheoryAtom], metaclass=ABCMeta):
    pass

class TheoryElement(Hashable, Comparable, metaclass=ABCMeta):
    condition: List[TheoryTerm]
    condition_id: int
    terms: List[TheoryTerm]

class TheoryTerm(Hashable, Comparable, metaclass=ABCMeta):
    arguments: List[TheoryTerm]
    name: str
    number: int
    type: TheoryTermType

class TheoryTermType(Hashable, Comparable, metaclass=ABCMeta):
    Function: TheoryTermType
    List: TheoryTermType
    Number: TheoryTermType
    Set: TheoryTermType
    Symbol: TheoryTermType
    Tuple: TheoryTermType

class Trail(Sequence[int], metaclass=ABCMeta):
    def begin(self, level: int) -> int: ...
    def end(self, level: int) -> int: ...

class TruthValue(Hashable, Comparable, metaclass=ABCMeta):
    False_: TruthValue
    Free: TruthValue
    Release: TruthValue
    True_: TruthValue
