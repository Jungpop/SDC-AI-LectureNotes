from app_window.service.window_service_impl import WindowServiceImpl


class DomainInitializer:

#serviceImpl 들 묶어서 한번에 instance 시
    @staticmethod
    def initRootWindowDomain():
        WindowServiceImpl.getInstance()