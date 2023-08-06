"""Scenario"""

from __future__ import annotations

from concurrent.futures import Future, ThreadPoolExecutor
from dataclasses import dataclass, field
from typing import List, Optional, Union

from .case import Case, CaseListener, CaseResult
from .context import ApplicationContext, ScenarioContext, analyze_context
from .description import Description
from .status import (
    Status, StatusedMixin, StatusedSequence, collect_statused, merge_statuses
)
from .verification import Verification, collect


class ScenarioListener(CaseListener):
    """
    Interface to listen to scenario running.
    """
    pass


@dataclass(frozen=True)
class ScenarioResult(StatusedMixin):
    label: Optional[str] = None
    message: Optional[str] = None
    conditions: Verification = field(default_factory=Verification)
    cases: StatusedSequence[CaseResult] = field(
        default_factory=StatusedSequence,
    )
    subscenarios: StatusedSequence[ScenarioResult] = field(
        default_factory=StatusedSequence,
    )


class RunningScenarioTask:

    def __init__(
        self, label: Optional[str],
        conditions: Verification,
        cases: Future,
        subscenarios: List[ScenarioTask],
    ):
        self._label = label
        self._conditions = conditions
        self._cases = cases
        self._subscenarios = subscenarios

    def result(self) -> ScenarioResult:
        cases = self._cases.result()
        subscenarios = collect_statused(s.result() for s in self._subscenarios)
        status = merge_statuses(cases.status, subscenarios.status)
        return ScenarioResult(
            label=self._label,
            status=status,
            conditions=self._conditions,
            cases=cases,
            subscenarios=subscenarios,
        )


class StaticScenarioTask:

    def __init__(self, result: ScenarioResult):
        self._result = result

    def result(self) -> ScenarioResult:
        return self._result


ScenarioTask = Union[RunningScenarioTask, StaticScenarioTask]


class Scenario:

    def __init__(
        self,
        label: Optional[str] = None,
        conditions: Optional[List[Description]] = None,
        cases: Optional[List[Case]] = None,
        subscenarios: Optional[List[Scenario]] = None,
    ):
        self._label = label
        self._conditions = conditions or []
        self._cases = cases or []
        self._subscenarios = subscenarios or []

    def run(
        self,
        context: ApplicationContext,
        listener: Optional[ScenarioListener] = None,
    ) -> ScenarioResult:
        with ThreadPoolExecutor(1) as executor:
            return self.submit(executor, context, listener).result()

    def submit(
        self,
        executor: ThreadPoolExecutor,
        context: ApplicationContext,
        listener: Optional[ScenarioListener] = None,
    ) -> ScenarioTask:
        current_context = ScenarioContext(app=context.app)
        context_analyzer = analyze_context(current_context)
        conditions = collect(
            condition.verify(context_analyzer)
            for condition in self._conditions
        )
        if conditions.status == Status.FAILURE:
            return StaticScenarioTask(ScenarioResult(
                label=self._label,
                status=Status.FAILURE,
                conditions=conditions,
            ))
        if conditions.status == Status.UNSTABLE:
            return StaticScenarioTask(ScenarioResult(
                label=self._label,
                status=Status.SKIPPED,
                conditions=conditions,
            ))

        listener = listener or ScenarioListener()
        cases = executor.submit(self._run_cases, current_context, listener)
        subscenarios = [
            subscenario.submit(executor, current_context, listener)
            for subscenario in self._subscenarios
        ]
        return RunningScenarioTask(
            label=self._label,
            conditions=conditions,
            cases=cases,
            subscenarios=subscenarios,
        )

    def _run_cases(
        self,
        context: ScenarioContext,
        listener: CaseListener,
    ) -> StatusedSequence[CaseResult]:
        return collect_statused(
            case.run(context, listener) for case in self._cases
        )
