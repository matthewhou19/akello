from abc import ABC
from datetime import datetime
from typing import List

from mbc.domain.model.patient import Patient
from mbc.domain.ports.patient_query_service import PatientQueryService


class RedisQueryService(PatientQueryService, ABC):

    def get_patient(self, patient_id: str) -> Patient:
        pass

    def get_patients(self) -> List[Patient]:
        pass

    def get_patients_by_name(self, name: str) -> List[Patient]:
        pass

    def get_patients_by_dob(self, dob: datetime) -> List[Patient]:
        pass
