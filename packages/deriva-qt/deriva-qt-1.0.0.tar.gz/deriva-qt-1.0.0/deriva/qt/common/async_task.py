import sys
from PyQt5.QtCore import Qt, QObject, QThreadPool, QRunnable, pyqtSignal


def async_execute(method, args, uid, success_callback, error_callback=None):
    request = Request(method, args, uid, success_callback, error_callback)
    QThreadPool.globalInstance().start(request)
    return request


class Request(QRunnable):

    INSTANCES = []
    FINISHED = []

    def __init__(self, method, args, uid, success_callback, error_callback=None):
        super(Request, self).__init__()
        self.setAutoDelete(True)
        self.cancelled = False

        self.method = method
        self.args = args
        self.uid = uid
        self.success = success_callback
        self.error = error_callback

        Request.INSTANCES.append(self)

        # release all of the finished tasks
        Request.FINISHED = []

    def run(self):
        # this allows us to "cancel" queued tasks if needed, should be done
        # on shutdown to prevent the app from hanging
        if self.cancelled:
            self.cleanup()
            return

        requester = Requester()
        requester.Success.connect(self.success, Qt.QueuedConnection)
        if self.error is not None:
            requester.Error.connect(self.error, Qt.QueuedConnection)

        try:
            result = self.method(*self.args)
            if self.cancelled:
                return
            requester.Success.emit(self.uid, result)
        except:
            (etype, value, traceback) = sys.exc_info()
            # sys.excepthook(etype, value, traceback)
            if self.cancelled:
                return
            requester.Error.emit(self.uid, value)
        finally:
            self.cleanup(requester)

    def cleanup(self, requester=None):
        if requester is not None:
            requester.deleteLater()

        self.remove()

    def remove(self):
        try:
            Request.INSTANCES.remove(self)
            Request.FINISHED.append(self)
        except ValueError:
            return

    @staticmethod
    def shutdown():
        for inst in Request.INSTANCES:
            inst.cancelled = True
        Request.INSTANCES = []
        Request.FINISHED = []


class Requester(QObject):
    
    Error = pyqtSignal(object, object)
    Success = pyqtSignal(object, object)

    def __init__(self, parent=None):
        super(Requester, self).__init__(parent)


class AsyncTask(QObject):
    def __init__(self, parent=None):
        super(AsyncTask, self).__init__(parent)
        self.rid = 0
        self.request = None

    def init_request(self):
        if self.request is not None:
            self.request.cancelled = True
            self.request = None
        self.rid += 1