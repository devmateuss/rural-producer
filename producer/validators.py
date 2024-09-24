import re

from django.core.exceptions import ValidationError


def validate_document(value):
    cpf_pattern = r"^\d{11}$"
    cnpj_pattern = r"^\d{14}$"

    if not (re.match(cpf_pattern, value) or re.match(cnpj_pattern, value)):
        raise ValidationError(
            "O documento deve ser um CPF (11 dígitos) ou CNPJ (14 dígitos)."
        )
