from insomniac.__version__ import __debug_mode__, __logo__
from insomniac.activation import ActivationController
from insomniac.extra_features.session import ExtendedInsomniacSession
from insomniac.session import InsomniacSession
from insomniac.utils import *


def run(activation_code=""):
    if not __debug_mode__:
        print_timeless(COLOR_OKGREEN + __logo__ + COLOR_ENDC)
        print_version()
    activation_controller = ActivationController()
    activation_controller.validate(activation_code)

    if not activation_controller.is_activated:
        print_timeless("Using insomniac session-manager without extra-features")
        insomniac_session = InsomniacSession()
    else:
        insomniac_session = ExtendedInsomniacSession()

    insomniac_session.run()
