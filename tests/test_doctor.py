from forge.services.doctor import DoctorService


def test_doctor_service_can_be_created():
    service = DoctorService()

    assert isinstance(service, DoctorService)