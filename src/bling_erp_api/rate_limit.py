"""Local rate limiting helpers."""

from __future__ import annotations

import threading
import time
from collections import deque


class RateLimiter:
    """Thread-safe sliding-window rate limiter for local SDK calls."""

    def __init__(self, *, max_requests: int = 3, period_seconds: float = 1.0) -> None:
        """Create a limiter that allows ``max_requests`` per period."""
        if max_requests <= 0:
            msg = "max_requests must be greater than zero"
            raise ValueError(msg)
        if period_seconds <= 0:
            msg = "period_seconds must be greater than zero"
            raise ValueError(msg)

        self._max_requests = max_requests
        self._period_seconds = period_seconds
        self._timestamps: deque[float] = deque()
        self._lock = threading.Lock()

    def wait(self) -> None:
        """Block until the next request can be sent."""
        while True:
            with self._lock:
                now = time.monotonic()
                self._drop_expired(now)
                if len(self._timestamps) < self._max_requests:
                    self._timestamps.append(now)
                    return

                wait_seconds = self._period_seconds - (now - self._timestamps[0])

            if wait_seconds > 0:
                time.sleep(wait_seconds)

    def _drop_expired(self, now: float) -> None:
        while self._timestamps and now - self._timestamps[0] >= self._period_seconds:
            self._timestamps.popleft()
