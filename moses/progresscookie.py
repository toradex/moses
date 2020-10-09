import singleton
import uuid
import threading
import copy
import exceptions

from typing import cast, Dict, Optional


class ProgressCookieData:
    def __init__(self):
        self.id = ""
        self.pending = True
        self.progress = -1
        self.messages: List[str] = []
        self.result = {"code": -1, "message": "", "description": ""}

    def _to_json(self) -> dict:
        return self.__dict__


class ProgressCookie(ProgressCookieData):
    """Class used to store and return progress of a long running operation
    """

    def __init__(self):
        super().__init__()
        self.id = str(uuid.uuid4())
        self.lock = threading.Lock()
        self.event = threading.Event()
        self.min = self.max = self.current = 0

    def set_minmax(self, minv: float, maxv: float):
        self.min = min(minv, maxv)
        self.max = max(minv, maxv)

    def acquire(self):
        self.lock.acquire()

    def release(self):
        self.lock.release()

    def freeze(self, wait_for_update: bool) -> ProgressCookieData:

        if wait_for_update:
            self.event.wait(5)

        self.acquire()

        try:
            clone = ProgressCookieData()

            clone.id = self.id
            clone.pending = self.pending
            clone.progress = self.progress
            clone.messages = self.messages
            clone.result = self.result

            # we can clean messages (we do a new assign)
            self.messages = []
            self.event.clear()
        finally:
            self.release()

        return clone

    def append_message(self, message: str):

        message = message.rstrip()

        if message is None or len(message) == 0:
            return

        self.acquire()
        try:
            self.messages.append(message)
            self.event.set()
        finally:
            self.release()

    def set_progress(self, value: int):
        self.acquire()
        try:
            val = min(value, 100)

            if val != self.progress:
                self.progress = val
                self.event.set()
        finally:
            self.release()

    def set_progress_minmax(self, value: float):
        self.acquire()

        try:
            self.current = value
            progress = min(
                100, int(((self.current - self.min) * 100.0) / (self.max - self.min))
            )

            if progress != self.progress:
                self.progress = progress
                self.event.set()

        finally:
            self.release()

    def update_progress_minmax(self, increase: float):
        self.acquire()

        try:
            self.current += increase
            progress = min(
                100, int(((self.current - self.min) * 100.0) / (self.max - self.min))
            )
            if progress != self.progress:
                self.progress = progress
                self.event.set()
        finally:
            self.release()

    def completed(self):
        self.acquire()
        try:
            self.pending = False
            self.result["code"] = 200
            self.result["message"] = ""
            self.result["description"] = ""
            self.event.set()
        finally:
            self.release()

    def report_error(self, exception: Exception):
        self.acquire()
        try:
            self.pending = False

            if isinstance(exception, exceptions.MosesError):
                moseserror = cast(exceptions.MosesError, exception)
                self.result["code"] = moseserror.code
                self.result["message"] = moseserror.message
                self.result["description"] = moseserror.description
            else:
                self.result["code"] = 500
                self.result["message"] = str(exception)
                self.result["description"] = "Internal Error"

            self.event.set()
        finally:
            self.release()


class ProgressCookies(Dict[str, ProgressCookie], metaclass=singleton.Singleton):
    """Static singleton with all existing cookies

    Args:
        Dict ([type]): cookies
        metaclass ([type], optional): [description]. Defaults to singleton.Singleton.
    """

    def __init__(self):
        pass

    def create_cookie(self) -> ProgressCookie:
        """allocates and returns a new progress cookie

        Returns:
            ProgressCookie: new cookie
        """
        cookie = ProgressCookie()
        self[cookie.id] = cookie
        return cookie

    def delete_cookie(self, cookie_id: str):
        if cookie_id in self:
            cookie = self[cookie_id]
            cookie.acquire()
            del self[cookie_id]
            cookie.release()

    def get_update(
        self, cookie_id: str, wait_for_update: bool
    ) -> Optional[ProgressCookieData]:
        if cookie_id in self:
            clone = self[cookie_id].freeze(wait_for_update)
            return clone
        return None
