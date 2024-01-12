import abc

class UiFrameController(abc.ABC):

    @abc.abstractmethod
    def requestToCreateUiFrame(self):
        pass

    @abc.abstractmethod
    def requestToStartPrintGamUi(self):
        pass