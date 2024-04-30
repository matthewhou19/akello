from transitions import Machine, EventData

from mbc.domain.model.patient import Patient
from mbc.domain.state_machines.patient_machine.models.state import State
from mbc.domain.ports.patient_query_service import PatientQueryService


class PatientStateMachine:
    patient: Patient
    patient_query_service: PatientQueryService

    def __init__(self, patient: Patient, patient_query_service: PatientQueryService, states: list[State]) -> None:
        self.patient_query_service = patient_query_service
        self.patient = patient
        self.machine = Machine(model=self, states=states, initial=patient.state, send_event=True)
        self.registered_states = {state.name: state for state in states}

    def check_transition(self, event: EventData):
        destination_state = self.registered_states[event.transition.dest]

        print(f"Checking transition to '{destination_state.name}' triggered by event '{event.event.name}'")

        for prerequisite in destination_state.prerequisites:
            if not prerequisite.handler(**prerequisite.params):
                return False
        return True

    def before_transition(self, event: EventData):
        print(f"Before transition to '{event.transition.dest}' triggered by event '{event.event.name}'")
        self.patient.state = event.transition.dest

        for event_fn in event.state.event_functions:
            if event_fn.trigger == event.event.name:
                event_fn.run(self.patient, self.patient_query_service, event)

        return True

